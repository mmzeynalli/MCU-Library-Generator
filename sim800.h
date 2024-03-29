/**
 * @file:  sim800.h
 * @brief: Library created for using sim800
 *
 * Created by: 		Miradil Zeynalli
 * Date Created: 	09.09.2019
 * Last Modified: 	09.09.2019
 */

#ifndef SIM800_H
#define SIM800_H

/* INCLUDES */

/* DEFINES and TYPEDEFS */

/* VARIABLES */

/* PROTOTYPES */
void sim800_init (Serial& ss, uint8_t pin);
void sim800_send_data (4);

#endif /* SIM800_H */

/*** end of file ***/
