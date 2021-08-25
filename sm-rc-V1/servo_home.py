from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
kit.servo[0].angle = 20#fr hip
kit.servo[1].angle = 60#fl hip
kit.servo[2].angle = 30#br hip
kit.servo[3].angle = 145#bl hip
time.sleep(1)
kit.servo[4].angle = 135#fr shoulder
kit.servo[5].angle = 45#fl shoulder
kit.servo[6].angle = 90#br shoulder
kit.servo[7].angle = 65#bl shoulder
time.sleep(1)
kit.servo[8].angle = 135#fr knee 
kit.servo[9].angle = 30#fl knee
kit.servo[10].angle = 135#br knee
kit.servo[11].angle = 30#bl knee