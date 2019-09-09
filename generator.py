from datetime import datetime
import json
from os import listdir

author = ''
workspace = ''
module_name = ''
is_stm = True

templates = json.load(open('entities.json'))

def generateModule(confs, funcs, vars, defs):

    global author, workspace, module_name, is_stm
    confs.get_data()
    author, workspace, module_name = confs.author, confs.work_dir, confs.module_name

    is_stm = not any(fname.endswith('.ino') for fname in listdir(workspace))

    private_funcs, public_funcs = get_scope(funcs)
    private_vars, public_vars = get_scope(vars)
    private_defs, public_defs = get_scope(defs)

    generateHeader(public_defs, public_vars, public_funcs)
    generateSource(private_defs, vars, public_funcs, private_funcs)


def generateHeader(defs, vars, funcs):

    with open('template.h', 'r') as h:
        header =  ''.join(h.readlines())

    header = header.replace('filename', module_name)
    header = header.replace('FILENAME', module_name.upper())
    header = header.replace('Author', author)
    header = header.replace('dd.mm.yyyy', datetime.today().strftime('%d.%m.%Y'))

    header = header.split('\n')

    '''
    ind = header.index('/* DEFINES and TYPEDEFS */')
    for i, d in enumerate(defs):
        define = templates['defines'].replace('NAME', d.name).replace('value', d.val)
        header.insert(ind + i + 1, define)

    ind = header.index('/* VARIABLES */')
    for i, v in enumerate(vars):
        var = 'extern ' + templates['variables'].replace('type', v.type).replace('name', v.name)
        header.insert(ind + i + 1, var)
    '''

    ind = header.index('/* PROTOTYPES */')
    for i, f in enumerate(funcs):
        func = templates['prototype'].replace('type', f.type).replace('name', f.name).replace('args', f.argv)
        header.insert(ind + i + 1, func)

    with open(workspace + '/Inc/' if is_stm else '' + module_name + '.h', 'w+') as out:
        out.write('\n'.join(header))


def generateSource(defs, vars, public_functions, private_functions):

    with open('template.c', 'r') as c:
        source =  ''.join(c.readlines())

    source = source.replace('filename', module_name)
    source = source.replace('FILENAME', module_name.upper())
    source = source.replace('Author', author)
    source = source.replace('dd.mm.yyyy', datetime.today().strftime('%d.%m.%Y'))

    source = source.split('\n')

    '''
    ind = header.index('/* DEFINES and TYPEDEFS */')
    for i, d in enumerate(defs):
        define = templates['defines'].replace('NAME', d.name).replace('value', d.val)
        header.insert(ind + i + 1, define)

    ind = header.index('/* VARIABLES */')
    for i, v in enumerate(vars):
        var = 'extern ' + templates['variables'].replace('type', v.type).replace('name', v.name)
        header.insert(ind + i + 1, var)
    '''

    ind = source.index('/* PROTOTYPES */')
    for i, f in enumerate(private_functions):
        func = templates['prototype'].replace('type', f.type).replace('name', f.name).replace('args', f.argv)
        source.insert(ind + i + 1, func)

    ind = source.index('/* PUBLIC FUNCTIONS */')
    for i, f in enumerate(public_functions):
        func = templates['function'].replace('type', f.type).replace('name', f.name).replace('args', f.argv)
        source.insert(ind + i + 1, func)

    ind = source.index('/* PRIVATE FUNCTIONS */')
    for i, f in enumerate(private_functions):
        func = 'static ' + templates['function'].replace('type', f.type).replace('name', f.name).replace('args', f.argv)
        source.insert(ind + i + 1, func)

    with open(workspace + '/Src/' if is_stm else '' + module_name + '.c', 'w+') as out:
        out.write('\n'.join(source))


def get_scope(entries):

    privates = []
    publics = []

    for e in entries:

        e.get_data()

        if e.scope == 'public':
            publics.append(e)
        elif e.scope == 'private':
            privates.append(e)

    return privates, publics

