from datetime import datetime
import json

author = ''
directory = ''
module_name = ''

templates = json.load(open('entities.json'))

def generateModule(confs, funcs, vars, defs):

    global author, directory, module_name
    confs.get_data()
    author, directory, module_name = confs.author, confs.work_dir, confs.module_name

    private_funcs, public_funcs = get_scope(funcs)
    private_vars, public_vars = get_scope(vars)
    private_defs, public_defs = get_scope(defs)

    generateHeader(public_defs, public_vars, public_funcs)
    generateSource(private_defs, private_vars, private_funcs)


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
        var = templates['variables'].replace('visibility ', '').replace('type', v.type).replace('name', v.name)
        header.insert(ind + i + 1, var)
    '''

    ind = header.index('/* PROTOTYPES */')
    for i, f in enumerate(funcs):
        func = templates['prototype'].replace('visibility ', '').replace('type', f.type).replace('name', f.name).replace('args', f.argv)
        header.insert(ind + i + 1, func)

    with open(module_name + '.h', 'w+') as out:
        out.write('\n'.join(header))

    print(header)


def generateSource(defs, vars, funcs):
    pass


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

