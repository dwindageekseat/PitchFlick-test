# -*- encoding=utf8 -*-
__author__ = "Dwinda Yudantoro"
__title__ = "Quick Check"
__desc__= """ Quick Check on Dashboard """

from airtest.core.api import *
auto_setup(__file__)

#=============additional variable start here===================
sleepTime = 2
#==============================================================

#
# Testcase simple aja lah ya, ngapain dibuat ribet-ribet ?
#

#==============================================================
# Instagram test
#note : Coba ngetest
print('launch the AUT, please wait . . .')
sleep(sleepTime)
wake()
sleep(sleepTime)
start_app ('com.android.settings');

#==============================================================
# test case flow related gameplay test with skip tutorial
def AboutPhone ():
    print('Opening apps done')
sleep(sleepTime)
print('Tap on About button')
while (exists(Template(r"tpl1579673051655.png", record_pos=(0.019, -0.916), resolution=(1080, 2340)))==0):
    print('Entering Setting')
    
if exists(Template(r"tpl1579672947168.png", record_pos=(-0.006, -0.637), resolution=(1080, 2340))) :
    touch(Template(r"tpl1579672960165.png", record_pos=(0.002, -0.619), resolution=(1080, 2340)))
    sleep(sleepTime)
    print('Tapping About button')
    #touch()
if exists(Template(r"tpl1579673116021.png", record_pos=(0.01, -0.909), resolution=(1080, 2340))):
    sleep(sleepTime)
    touch(Template(r"tpl1579673128734.png", record_pos=(-0.272, -0.772), resolution=(1080, 2340)))

    print('Tapping System update')
    sleep(sleepTime)
while (exists(Template(r"tpl1579674045430.png", record_pos=(-0.003, 0.948), resolution=(1080, 2340)))!=0):
    print('Touch Check for updates')
    touch(Template(r"tpl1579674192790.png", record_pos=(-0.416, -0.952), resolution=(1080, 2340)))
    sleep(sleepTime)
    
    touch(Template(r"tpl1579673207701.png", record_pos=(-0.41, -0.921), resolution=(1080, 2340)))
        
def checkDisplay():
    print("Entering Display Check")
    while (exists(Template(r"tpl1579679758459.png", record_pos=(0.012, -0.922), resolution=(1080, 2340)))!=0):
        touch(Template(r"tpl1579680089472.png", record_pos=(-0.277, 0.919), resolution=(1080, 2340)))
        
        print("Entering Display")
        sleep(sleepTime)
        
        touch(Template(r"tpl1579680184896.png", record_pos=(-0.265, -0.683), resolution=(1080, 2340)))
        sleep(sleepTime)
        swipe(Template(r"tpl1579680212788.png", record_pos=(0.019, -0.58), resolution=(1080, 2340)), vector=[0.4408, 0.0197])
        sleep(sleepTime)
        touch(Template(r"tpl1579680256160.png", record_pos=(-0.406, -0.924), resolution=(1080, 2340)))
        type("test airtest")
        
def checkSecurity():
    print("Checking security screen")
    touch(tpl1579679758459)
#===========================Global Function=======================#
AboutPhone()
wifiCheck()
checkDisplay()
checkSecurity()
#adding