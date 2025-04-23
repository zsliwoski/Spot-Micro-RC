import copy

# List to store recorded input actions
recorded_input_actions = []

# Index for playback
playback_index = 0
# Length of the recorded actions array
recorded_arr_len = 0

# Flags to track playback state
playback_started = False
playback_finished = True

# Flag to track recording state
recording_started = False

# Function to add an input action to the recorded actions list
def add_input_action(action):
    # Deep copy the action to avoid unintended modifications
    recorded_input_actions.append(copy.deepcopy(action))

# Function to get the next recorded action during playback
def get_next_recorded():    
    global playback_index, recorded_arr_len, playback_finished, playback_started
    # If playback index reaches the end of the recorded actions, stop playback
    if (playback_index == recorded_arr_len):
        stop_playback()
        return None
    # Retrieve the current action and increment the playback index
    ret = recorded_input_actions[playback_index]
    playback_index += 1
    
    # If playback index reaches the end, mark playback as finished
    if (playback_index == recorded_arr_len):
        playback_finished = True
    
    return ret

# Function to start playback
def start_playback():
    global playback_finished, playback_started, playback_index
    # Reset playback state and index
    playback_finished = False
    playback_started = True
    playback_index = 0

# Function to stop playback
def stop_playback():
    global playback_finished, playback_started
    # Mark playback as finished and stopped
    playback_finished = True
    playback_started = False

# Function to check if playback is possible
def playback_possible():
    # Playback is possible if there are recorded actions
    return recorded_arr_len > 0

# Function to start a new recording
def start_new_recording():
    global recorded_input_actions
    # Clear the recorded actions list and mark recording as started
    recorded_input_actions.clear()
    recording_started = True

# Function to finish recording
def finish_recording():
    global playback_index, recorded_arr_len
    # Update the length of recorded actions and mark recording as finished
    recorded_arr_len = len(recorded_input_actions)
    recording_started = False

# Function to save the recorded actions to a file (mostly for debugging)
def save_recording(recording):
    # Save the recorded actions to a file named 'recorded.py'
    with open('recorded.json', 'w') as file:
        file.write(str(recorded_input_actions))
        