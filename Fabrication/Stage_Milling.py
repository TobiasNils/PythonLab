#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:38:19 2018

@author: nils
"""
import serial as sl
import os
import time
from modules.MyStage import MyStage, MyAxis
S = MyStage(os, sl)


S.write(b'0_mode_') # setting the stage in Host-mode, where commands have to end with a '_' (space)
#S.write(b'restore_') # loads the last saved settings
S.write(b'3_setdim_') # set dimensions
S.write(b'1_1_setaxis_')
S.write(b'1_2_setaxis_')
S.write(b'1_3_setaxis_')# makes sure that the axes are turned on
S.write(b'2_1_setunit_')
S.write(b'2_2_setunit_')
S.write(b'2_3_setunit_')# "1" sets units to µm for all the axes, '2' -> mm
S.write(b'1_setaccelfunc_')
S.write(b'.5_setvel_')


x = MyAxis("1", S)
y = MyAxis("2", S)
z = MyAxis("3", S)

#=================================
# Move to some z-posiiton ("exactly") above left "pin" and set Origin there:
def set_home():
    S.write(b'0_0_0_setpos_')
#=================================
# then: 
marks_left = [(47.653, .642),
              (47.653, 1.008)]
marks_right = [(77.647, .527),
               (77.647, 1.123)]

def approach_z(z_i):
    while True:
        try: 
            z.move_relative(z_i)
            input('more? ')
        except KeyboardInterrupt:
            break
        
def move_up(z_i):
    z.move_relative(-z_i)
    
def go_home():
    S.write(b'0_0_0_m_')

def stage_moving():
    moving = False
    for i in range(3):
        if S.send(b'%i_nst_'% (i+1))==[b'0']:
            pass
        else:
            moving= True
    return moving

    
z_secure = 2.5
z_approach = 1
def engrave_point(coords, depth):
    input('Start Dremel. Confirm with OK to proceed...')
    x.move_relative(coords[0])
    y.move_relative(coords[1])
    z.move_relative(z_secure-z_approach)
    while True:
        moving = stage_moving()
        if moving:
            time.sleep(.05)
            pass
        else:
            break
    z.move_relative(z_approach + depth)
    move_up(z_secure)
    go_home()
    print('Finished.\n Turn OFF Dremel.')