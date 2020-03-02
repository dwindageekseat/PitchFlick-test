# -*- encoding=utf8 -*-
__author__ = "Dwinda Yudantoro"

from airtest.core.api import *
import os
import sys

auto_setup(__file__)

regulartime = 23
longtime = 5
network = "com.android.WifiState
network2 = "com.android.network"

def main():
    
    loginSite()
    if len(sys.argv) <> 3:
        sys.stderr.write('no network detected')
        sys.exit(2)
    network = sys.argv[1], sys.argv[2]
    try:
        stat1 = os.stat(network1)
    except os.error:
        sys.stderr.write( network2 + ': cannot start without connection')
        sys.exit(1)
    try:
        os.utime(file2, (stat1[ST_ATIME], stat1[ST_MTIME]))
    except os.error:
        sys.stderr.write(file2 + ': cannot change time\n')
        sys.exit(2)

if __name__ == '__main__':
opportunityCheck()
    try:
        stat1=os.stat(network1)
    cat

def loginSite():
    
    touch(Template(r"tpl1582075140767.png", record_pos=(-0.394, -0.694), resolution=(1080, 2340)))

    text("gama@gmail.com")
    touch(Template(r"tpl1582075015092.png", record_pos=(-0.009, -0.293), resolution=(1080, 2220)))
    sleep(regulartime)
    touch(Template(r"tpl1582075163904.png", record_pos=(-0.356, -0.673), resolution=(1080, 2340)))
    text("123")
    touch(Template(r"tpl1582075299305.png", record_pos=(0.001, -0.38), resolution=(1080, 2340)))

def opportunityCheck():
    touch(Template(r"tpl1582076014102.png", record_pos=(-0.206, -0.214), resolution=(1080, 2340)))
    sleep(2)
    touch(Template(r"tpl1582076175577.png", record_pos=(-0.206, -0.746), resolution=(1080, 2340)))
    text("jojon markijon")
    touch(Template(r"tpl1582076253912.png", record_pos=(0.283, -0.561), resolution=(1080, 2340)))
    sleep(1)
    touch(Template(r"tpl1582076517959.png", record_pos=(-0.278, -0.745), resolution=(1080, 2340)))
    text("jojon naek motor")
    
    
main()
loginSite()
opportunityCheck()  