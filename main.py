#!/usr/bin/env python3
#coding: utf-8

from zencad import *

base_len = 180
base_width = 176.5
total_height = 143
supp_len = 50

alp2020l = from_brep('./brep/alp2020almk.brep').left(47.4).back(75.2)

def get_alp2020(len):
    return alp2020l.scaleZ(len / 100).up(len / 2)

# продольная часть основы:
m = get_alp2020(base_len).rotateY(deg(90)).forw((base_width - 20) / 2 )
m += m.mirrorX()
# поперечная часть основы:
#t = get_alp2020(base_width - 20*2).rotateX(deg(90)).left((base_len - 20) / 2 )
#t += t.mirrorY()
t = get_alp2020(base_width - 20*2).rotateX(deg(90))
m += t
# стойки опор:
t = get_alp2020(total_height - 20*2).up((total_height - 20) / 2).forw((base_width - 20) / 2 )
t += t.mirrorZ()
m += t
# верхушки опор:
t = get_alp2020(supp_len).rotateY(deg(90)).forw((base_width - 20) / 2 ).up(total_height - 20)
t += t.mirrorZ()
m += t

disp(m)

show()
