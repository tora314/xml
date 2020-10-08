"""
date: 2020/10/08
written by KatoMori
purpose: THIS IS MAIN FUNCTIOM
"""

import os
import phase1
import phase2

DIR_NAME = 'labelme'
PATH = './' + DIR_NAME + '/'
PHASE1 = PATH + 'phase1/'
PHASE2 = PATH + 'phase2/'

phase_list = []
phase_list.append(PHASE1)
phase_list.append(PHASE2)


def dir_check(phase_list):
    for PATH in phase_list:
        if not os.path.exists(PATH):
            os.mkdir(PATH)
        else:
            print(PATH + 'existed')


if __name__ == '__main__':
    dir_check(phase_list)
    print("phase1")
    phase1.order(1)
    print("phase1 has done!")
    print("phase2")
    phase2.order(1)
    print("phase2 has done!")
