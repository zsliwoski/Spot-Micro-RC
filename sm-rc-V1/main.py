#!/usr/bin/python3
import time

from queue import Queue
from threading import Thread

from manual_controller import start_control, input_struct
from animation import update_playback
import action_record as ar

# Function to process input actions and handle recording/playback logic
def process_input(out_q):
    rec_start = False  # Flag to track if recording has started
    playback_start = False  # Flag to track if playback has started
    while (True):
        # Check if recording is triggered
        if (input_struct['recording'] == 1 and rec_start == False):
            print("recording started")
            rec_start = True
            ar.start_new_recording()  # Start a new recording
        
        # Handle recording logic
        if (rec_start == True):
            print("recording...")
            ar.add_input_action(input_struct)  # Add input action to the recording
            if (input_struct['recording'] == 0):  # Stop recording if recording flag is turned off
                ar.finish_recording()
                rec_start = False
                print(str(ar.recorded_input_actions))  # Print recorded actions
        
        # Handle playback logic
        if (input_struct['playback'] == 1 and ar.playback_started == False):
            print("playback started")
            ar.start_playback()  # Start playback
        
        # Process playback actions
        if (ar.playback_started == True):
            print("playing...")
            
            # Stop playback if playback flag is turned off or playback is finished
            if (input_struct['playback'] == 0 or ar.playback_finished == True):
                print("stopped")
                ar.stop_playback()
                input_struct['playback'] = 0
            
            # Get the next recorded action and put it in the output queue
            next_action = ar.get_next_recorded()
            if (not next_action == None):
                out_q.put(next_action)
        else:
            # If no playback, pass the input structure to the output queue
            out_q.put(input_struct)
            
        time.sleep(0.1)  # Sleep to reduce CPU usage

# Function to process output actions and update playback
def process_output(in_q):
    while (True):
        # Get the next action from the input queue and update playback
        update_playback(in_q.get())

# Main entry point of the program
if __name__ == '__main__':
    print("Starting main program")
    
    q = Queue()  # Create a queue for communication between threads
    
    # Create a thread for processing input
    input = Thread(target = process_input, args = (q,))

    # Create a thread for processing output
    movement = Thread(target = process_output, args = (q,))
    
    # Create a thread for starting manual control
    input_start_th = Thread (target = start_control)

    print("Starting input thread")    
    input.start()  # Start the input processing thread
    print("Starting movement thread")
    movement.start()  # Start the output processing thread
    print("Starting input thread")
    input_start_th.start()  # Start the manual control thread
