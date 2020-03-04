# -*- encoding=utf8 -*-
__author__ = "mac"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1583222497715.png", record_pos=(-0.341, -0.542), resolution=(1242, 2688)))
touch(Template(r"tpl1583223231143.png", record_pos=(-0.238, -0.564), resolution=(1242, 2688)))

text("gama@gmail.com")
touch(Template(r"tpl1583222671723.png", record_pos=(-0.001, -0.374), resolution=(1242, 2688)))
sleep(2)
touch(Template(r"tpl1583223259688.png", record_pos=(-0.2, -0.608), resolution=(1242, 2688)))
text("123")
touch(Template(r"tpl1583223294670.png", record_pos=(0.003, -0.285), resolution=(1242, 2688)))
assert_exists(Template(r"tpl1583223465356.png", record_pos=(0.009, -0.619), resolution=(1242, 2688)), "Success Login")
