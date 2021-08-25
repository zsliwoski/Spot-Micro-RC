#```/*import board
#import busio
#import adafruit_pca9685
#i2c = busio.I2C(board.SCL, board.SDA)
#pca = adafruit_pca9685.PCA9685(i2c)
import math
from datetime import datetime
import time
import numpy as np

import animation_library as al
import servos

from adafruit_servokit import ServoKit

def blend(a,b,alpha):
    return a + alpha * (b - a)

'''
a is our base pose
b is our furthest x pose, lowest down
c is our maxim, furthest x and y
d is our furthest y pose
xAlpha is our input towards our x pose
yAlpha is our input towards our y pose
'''
def blend2D(a,b,c,d,xAlpha,yAlpha):
    result = a
    
    if (xAlpha > yAlpha):
        result = blend(a,b,xAlpha)
        result = blend(result,c,yAlpha) 
    else:
        result = blend(a,d,yAlpha)
        result = blend(result,c,xAlpha)
    return result

def update_playback(data):
    global start_time,a,b,c,d

    anim_speed = 1 #TODO: add custom logic to juice up the speed of animation
    

    current_time = datetime.now().timestamp() #get Time from time
    position_time = current_time - start_time
    
    anim_duration = frames * frame_duration_time * (1/anim_speed)
    
    if (position_time >= anim_duration):
        start_time = current_time
    else:
        frame = math.floor((position_time/frame_duration_time*(anim_speed)))
        
        raw_x = data['movement'][0]
        raw_y = -data['movement'][1]
        
        x_clip = al.anim_walk_r
        y_clip = al.anim_walk_f
        xy_clip = al.anim_walk_fr 
        
        if (raw_x > 0):
          x_clip = al.anim_walk_r
        else:
          x_clip = al.anim_walk_l
            
        if (raw_y > 0):
          y_clip = al.anim_walk_f
          if (raw_x > 0):
            xy_clip = al.anim_walk_fr
          else:
            xy_clip = al.anim_walk_fl         
        else:
          y_clip = al.anim_walk_b
          if (raw_x > 0):
            xy_clip = al.anim_walk_br
          else:
            xy_clip = al.anim_walk_bl
          
        x_input = abs(raw_x)
        y_input = abs(raw_y)
        current_anim = servos.blend_pose2D(al.anim_stand[0],x_clip[frame],xy_clip[frame],y_clip[frame],x_input,y_input)
        #current_anim = servos.blend_pose(current_anim,al.anim_crouch[0],data['crouch'])
        
        current_anim = servos.add_offset(current_anim,al.offset_roll,data['rotation'][1])
        current_anim = servos.add_offset(current_anim,al.offset_crouch,data['crouch'])
        
        servos.apply_pose(current_anim)
        
        del current_anim #cleanup

#TODO: adapt animations to have custom FPS to calculate these on the fly
FPS = 8 #arbitrary
frames = 4 #arbitrary
frame_duration_time = 1/FPS #how long does a pose last for
anim_speed = 1.0 
start_time = datetime.now().timestamp()
anim_duration = frames * frame_duration_time * anim_speed #changes based on clip 