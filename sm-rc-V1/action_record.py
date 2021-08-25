import copy

recorded_input_actions = []

playback_index = 0
recorded_arr_len = 0

playback_started = False
playback_finished = True

recording_started = False

def add_input_action(action):
    recorded_input_actions.append(copy.deepcopy(action))

def get_next_recorded():    
    global playback_index, recorded_arr_len, playback_finished,playback_started
    if (playback_index == recorded_arr_len):
        stop_playback()
        return None
    ret = recorded_input_actions[playback_index]
    playback_index += 1
    
    if (playback_index == recorded_arr_len):
        playback_finished = True
    
    return ret

def start_playback():
    global playback_finished,playback_started,playback_index
    playback_finished = False
    playback_started = True
    playback_index = 0

def stop_playback():
    global playback_finished,playback_started
    playback_finished = True
    playback_started = False

def playback_possible():
    return recorded_arr_len > 0

def start_new_recording():
    global recorded_input_actions
    recorded_input_actions.clear()
    recording_started = True

def finish_recording():
    global playback_index, recorded_arr_len
    recorded_arr_len = len(recorded_input_actions)
    recording_started = False

#mostly debug, might assign a key later for automation
def save_recording(recording):
    with open('recorded.py', 'w') as file:
        file.write(str(recorded_input_actions))
        
recorded_input_actions = []

playback_index = 0
recorded_arr_len = 0

playback_started = False
playback_finished = True

recording_started = False