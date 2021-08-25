from adafruit_servokit import ServoKit
from servo_offsets import offset_base
import math
import time
import copy

#clamps our numbers, easier than writing it out every occurence
def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

#blend function, basis of smooth interpolation between angle values
def blend(a,b,alpha):
    retval = a + (alpha * (b - a))
    return retval

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

#a linear pose blend, just gets the point (alpha) between two poses
def blend_pose(animation_a,animation_b, alpha):
    final_pose = copy.deepcopy(animation_a)
    
    bone_index = 0
    for bone in availible_bones:
        final_angle = blend(animation_a[bone],animation_b[bone],alpha)
        final_pose[bone] = final_angle
        bone_index += 1
    return final_pose

#blends pose two dimensionally, a is 0-0 (base pose), b is 1-0, c is 1-1 (maxim), d is 0-1
#x and y refer to the first and second value respectively
#creates smooth transition between standing still, walking sideways, forward and diagnol
def blend_pose2D(animation_a, animation_b, animation_c, animation_d, x_alpha, y_alpha):
    final_pose = copy.deepcopy(animation_a)
    
    bone_index = 0
    for bone in availible_bones:
        final_angle = blend2D(animation_a[bone],animation_b[bone],animation_c[bone],animation_d[bone],x_alpha,y_alpha)
        final_pose[bone] = final_angle
        bone_index += 1
    return final_pose

#adds a defined offset to a given pose, i.e. forward walk + crouching = crouch walk
def add_offset(base_pose, offset_pose, alpha):
    final_pose = copy.deepcopy(base_pose)
    bone_index = 0
    for bone in availible_bones:
        final_angle = base_pose[bone] + (offset_pose[bone] * alpha)
        final_pose[bone] = final_angle
        bone_index += 1
    return final_pose

#moves servos based on pose data
def apply_pose(animation):
    bone_index = 0
    for bone in availible_bones:
            final_angle = animation[bone] + offset_base[bone]
            final_angle = clamp(final_angle,1,179)
            if ((not math.isnan(final_angle) and current_pose[bone] != final_angle) or (not math.isnan(final_angle) and abs(final_angle - kit.servo[bone_index].angle) > 1)):
                kit.servo[bone_index].angle = final_angle
                print(bone,final_angle)
                current_pose[bone] = final_angle
            bone_index += 1


kit = ServoKit(channels=16)

#defaults to 1 to force a pose update on start
current_pose = {
    "R_F_back" : 1,
    "L_F_back" : 1,
    "R_B_back" : 1,
    "L_B_back" : 1,
    
    "R_F_shoulder" : 1,
    "L_F_shoulder" : 1,
    "R_B_shoulder" : 1,
    "L_B_shoulder" : 1,
    
    "R_F_knee" : 1,
    "L_F_knee" : 1,
    "R_B_knee" : 1,
    "L_B_knee" : 1,
}

availible_bones = [
    "R_F_back",
    "L_F_back",
    "R_B_back",
    "L_B_back",
    
    "R_F_shoulder",
    "L_F_shoulder",
    "R_B_shoulder",
    "L_B_shoulder",
    
    "R_F_knee",
    "L_F_knee",
    "R_B_knee",
    "L_B_knee"
]