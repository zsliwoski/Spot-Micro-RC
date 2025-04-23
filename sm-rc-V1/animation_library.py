#represents the home position, base stand position
anim_stand = [
    {
    "R_F_back" : 0,
    "L_F_back" : 0,
    "R_B_back" : 0,
    "L_B_back" : 0,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 0,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : 0,
    }
]

offset_crouch = {
  "R_F_back" : 20,
  "L_F_back" : -20,
  "R_B_back" : 20,
  "L_B_back" : -20,
  
  "R_F_shoulder" : 20,
  "L_F_shoulder" : -15,
  "R_B_shoulder" : -15,
  "L_B_shoulder" : 20,
  
  "R_F_knee" : 20,
  "L_F_knee" : -20,
  "R_B_knee" : 0,
  "L_B_knee" : 0,
}

#
anim_walk_f = [
    { #1-----------------------
    "R_F_back" : 10,#positive goes higher
    "L_F_back" : -10,#negative goes higher
    "R_B_back" : 10,
    "L_B_back" : -10,
    
    "R_F_shoulder" : -60,#max back
    "L_F_shoulder" : 0,#max forward
    "R_B_shoulder" : -20,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 80,#max back
    "L_F_knee" : 0, #max forward
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #2-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 20,
    
    "R_F_knee" : 80,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #3-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 20,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }, #4-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : -20,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }
]

anim_walk_b = [
    { #1-----------------------
    "R_F_back" : 10,#positive goes higher
    "L_F_back" : -10,#negative goes higher
    "R_B_back" : 10,
    "L_B_back" : -10,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 80,#max back
    "L_F_knee" : 0, #max forward
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #2-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 80,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #3-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }, #4-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }
]

anim_walk_r = [
    { #1-----------------------
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 90,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -90
    }, #2-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 90,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -90
    }, #3-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 0,
    "L_F_knee" : -90,
    "R_B_knee" : 90,
    "L_B_knee" : 0,
    }, #4-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 0,
    "L_F_knee" : -90,
    "R_B_knee" : 90,
    "L_B_knee" : 0,
    }
]

anim_walk_l = [
    { #1-----------------------
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 90,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -90,
    }, #2-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 90,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -90,
    }, #3-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : -90,
    "R_B_shoulder" : 90,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 0,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : 0,
    }, #4-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 0,
    "L_F_knee" : -90,
    "R_B_knee" : 90,
    "L_B_knee" : 0,
    }
]

#diagnols
anim_walk_fr = [
    { #1-----------------------
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : -60,#max back
    "L_F_shoulder" : 0,#max forward
    "R_B_shoulder" : -20,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 80,#max back
    "L_F_knee" : 0, #max forward
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #2-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 20,
    
    "R_F_knee" : 80,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #3-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 20,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }, #4-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : -20,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }
]
anim_walk_br = [
    { #1-----------------------
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 80,#max back
    "L_F_knee" : 0, #max forward
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #2-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 80,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #3-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }, #4-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }
]
anim_walk_fl = [
    { #1-----------------------
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : -60,#max back
    "L_F_shoulder" : 0,#max forward
    "R_B_shoulder" : -20,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 80,#max back
    "L_F_knee" : 0, #max forward
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #2-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 20,
    
    "R_F_knee" : 80,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #3-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 20,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }, #4-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : -20,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }
]
anim_walk_bl = [
    { #1-----------------------
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 80,#max back
    "L_F_knee" : 0, #max forward
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #2-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 80,
    "L_F_knee" : 0,
    "R_B_knee" : 0,
    "L_B_knee" : -80,
    }, #3-----------------------
    {
    "R_F_back" : -20,#positive goes higher
    "L_F_back" : 20,#negative goes higher
    "R_B_back" : 20,
    "L_B_back" : -20,
    
    "R_F_shoulder" : -60,
    "L_F_shoulder" : 0,
    "R_B_shoulder" : 0,
    "L_B_shoulder" : 80,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }, #4-----------------------
    {
    "R_F_back" : 20,#positive goes higher
    "L_F_back" : -20,#negative goes higher
    "R_B_back" : -20,
    "L_B_back" : 20,
    
    "R_F_shoulder" : 0,
    "L_F_shoulder" : 60,
    "R_B_shoulder" : -80,
    "L_B_shoulder" : 0,
    
    "R_F_knee" : 0,
    "L_F_knee" : -80,
    "R_B_knee" : 80,
    "L_B_knee" : 0,
    }
]
#FROM STAND THIS COULD MAKE A USEFUL WALK REF
'''anim_roll_left = {
    "R_F_back" : 5,
    "L_F_back" : 45,
    "R_B_back" : 10,
    "L_B_back" : 130,
    
    "R_F_shoulder" : 155,#higher is up
    "L_F_shoulder" : 65,#lower is up
    "R_B_shoulder" : 55,#higher is up
    "L_B_shoulder" : 65,#lower is up
    
    "R_F_knee" : 125,
    "L_F_knee" : 40,
    "R_B_knee" : 125,
    "L_B_knee" : 40,
}'''

offset_roll = {
    "R_F_back" : 15,
    "L_F_back" : 15,
    "R_B_back" : 15,
    "L_B_back" : 15,
    
    "R_F_shoulder" : 0,#higher is up
    "L_F_shoulder" : 0,#lower is up
    "R_B_shoulder" : 0,#higher is up
    "L_B_shoulder" : 0,#lower is up
    
    "R_F_knee" : 20,
    "L_F_knee" : 30,
    "R_B_knee" : 20,
    "L_B_knee" : 30,
}