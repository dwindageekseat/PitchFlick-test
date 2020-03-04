# -*- encoding=utf8 -*-
__author__ = "mac"

from airtest.core.api import *

auto_setup(__file__)

regulartime = 2
longtime = 5

touch(Template(r"tpl1583289472038.png", record_pos=(-0.341, -0.543), resolution=(1242, 2688)))
sleep(longtime)
touch(Template(r"tpl1583289981119.png", record_pos=(0.181, -0.224), resolution=(1242, 2688)))
sleep(regulartime)
touch(Template(r"tpl1583290016566.png", record_pos=(-0.288, -0.666), resolution=(1242, 2688)))
text("testautomation")
touch(Template(r"tpl1583290044447.png", record_pos=(-0.259, -0.507), resolution=(1242, 2688)))
text("iosplatformautomation")
touch(Template(r"tpl1583290302261.png", record_pos=(-0.217, 0.01), resolution=(1242, 2688)))
text("123")
touch(Template(r"tpl1583290324425.png", record_pos=(-0.157, 0.171), resolution=(1242, 2688)))
text("123")
touch(Template(r"tpl1583290107203.png", record_pos=(-0.076, -0.351), resolution=(1242, 2688)))
sleep(regulartime)
touch(Template(r"tpl1583290121518.png", record_pos=(-0.232, -0.351), resolution=(1242, 2688)))
sleep(regulartime)
touch(Template(r"tpl1583290184030.png", record_pos=(-0.157, -0.187), resolution=(1242, 2688)))
sleep(regulartime)
touch(Template(r"tpl1583290273407.png", record_pos=(-0.257, 0.054), resolution=(1242, 2688)))
touch(Template(r"tpl1583290363407.png", record_pos=(0.007, 0.333), resolution=(1242, 2688)))
assert_exists(Template(r"tpl1583290497654.png", record_pos=(-0.002, 0.01), resolution=(1242, 2688)), "Success Sign up")
