#!/usr/bin/env/python
# -*- coding: utf-8 -*-

##########################################                                    #
#            carPiceCon v0.1b            #                                     
#      Sábado 22 de Febrero 2014         #
#            @Hiram Zúñiga               #
#          hiramhzr at gmail.com         #
##########################################

"""
The program controls a car with a piface
How to use:
Use arrow keys to move the car forward, back, turn left and right
Use p key for stop the car
Use q key for exit the program
"""

# import libraries
import pifacedigitalio as piface
import curses

# start module piface
piface.init()

# config curses
stdscr = curses.initscr()
curses.start_color()
stdscr.keypad(1)
# a little color in the code because is run in console :)
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
stdscr.addstr(0,10, "Vamos a manejar !!!", curses.color_pair(1))
stdscr.addstr(7,10, "q para salir", curses.color_pair(2))

stdscr.refresh()

# Turn off all the used pins in the piface
piface.digital_write(0,0)
piface.digital_write(1,0)
piface.digital_write(2,0)
piface.digital_write(3,0)

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.refresh()
    # all the control here
    if key == curses.KEY_UP:
    	stdscr.addstr(2, 20, "Up")
    	piface.digital_write(2,1)
    	piface.digital_write(3,0)
    if key == curses.KEY_DOWN:
    	stdscr.addstr(3, 20, "Down")
    	piface.digital_write(2,0)
    	piface.digital_write(3,1)
    if key == curses.KEY_LEFT:
    	stdscr.addstr(4, 20, "Left")
    	piface.digital_write(0,1)
    	piface.digital_write(1,0)
    if key == curses.KEY_RIGHT:
    	stdscr.addstr(5, 20, "Right")
    	piface.digital_write(0,0)
    	piface.digital_write(1,1)
    if (key == ord('d')):
        piface.digital_write(0,0)
        piface.digital_write(1,0)
    if (key == ord('p')):
        stdscr.addstr(15, 20, "Stop")
        piface.digital_write(0,0)
        piface.digital_write(1,0)
        piface.digital_write(2,0)
        piface.digital_write(3,0)

piface.digital_write(0,0)
piface.digital_write(1,0)
piface.digital_write(2,0)
piface.digital_write(3,0)

curses.endwin()
