# -*- encoding=utf8 -*-
__author__ = "mac"

from airtest.core.api import *

auto_setup(__file__)

regulartime=2
longtime=5

touch(Template(r"tpl1583389712056.png", record_pos=(-0.341, -0.542), resolution=(1242, 2688)))
sleep(longtime)
touch(Template(r"tpl1583397948729.png", record_pos=(-0.265, -0.565), resolution=(1242, 2688)))
sleep(regulartime)
text("dwiki@gmail.com")
touch(Template(r"tpl1583391429522.png", record_pos=(-0.001, -0.374), resolution=(1242, 2688)))
sleep(regulartime)
touch(Template(r"tpl1583392087304.png", record_pos=(-0.19, -0.633), resolution=(1242, 2688)))
text("123")
touch(Template(r"tpl1583392306985.png", record_pos=(-0.002, -0.293), resolution=(1242, 2688)))
sleep(longtime)
exists(Template(r"tpl1583392364732.png", record_pos=(0.002, -0.615), resolution=(1242, 2688)))
sleep(regulartime)
touch(Template(r"tpl1583395401543.png", record_pos=(0.216, -0.183), resolution=(1242, 2688)))
touch(Template(r"tpl1583395484708.png", record_pos=(0.391, 0.965), resolution=(1242, 2688)))
sleep(regulartime)
touch(Template(r"tpl1583395667946.png", record_pos=(-0.238, -0.725), resolution=(1242, 2688)))
sleep(regulartime)
text("autoopportunity")

touch(Template(r"tpl1583395997705.png", record_pos=(-0.244, -0.42), resolution=(1242, 2688)))
text("this is an automation test")
touch(Template(r"tpl1583396173372.png", record_pos=(-0.23, 0.116), resolution=(1242, 2688)))
text("test")

touch(Template(r"tpl1583396221431.png", record_pos=(-0.126, -0.064), resolution=(1242, 2688)))
sleep(regulartime)
touch(Template(r"tpl1583396256679.png", record_pos=(-0.107, 0.193), resolution=(1242, 2688)))
touch(Template(r"tpl1583396280399.png", record_pos=(0.304, 0.522), resolution=(1242, 2688)))
touch(Template(r"tpl1583396299790.png", record_pos=(0.44, -0.907), resolution=(1242, 2688)))



