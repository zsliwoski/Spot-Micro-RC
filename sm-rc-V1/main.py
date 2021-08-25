#!/usr/bin/python3
import time

from queue import Queue
from threading import Thread

from manual_controller import start_control, input_struct
from animation import update_playback
import action_record as ar

def process_input(out_q):
    rec_start = False
    playback_start = False
    while (True):
        if (input_struct['recording'] == 1 and rec_start == False):
            print("recording started")
            rec_start = True
            ar.start_new_recording()
        
        if (rec_start == True):
            print("recording...")
            ar.add_input_action(input_struct)
            if (input_struct['recording'] == 0):
              ar.finish_recording()
              rec_start = False
              print(str(ar.recorded_input_actions))
        
        #Action playback
        if (input_struct['playback'] == 1 and ar.playback_started == False):
            print("playback started")
            ar.start_playback()
        
        if (ar.playback_started == True):
            print("playing...")
            
            if (input_struct['playback'] == 0 or ar.playback_finished == True):
              print("stopped")
              ar.stop_playback()
              input_struct['playback'] = 0
            
            next_action = ar.get_next_recorded()
            if (not next_action == None):
              out_q.put(next_action)
        else:
            out_q.put(input_struct)
            
        time.sleep(0.1)
def process_output(in_q):
    while (True):
        #print(in_q.get())
        update_playback(in_q.get())
if __name__ == '__main__':
    print("stank-bot-9k online")
    
    q = Queue()
    
    input = Thread(target = process_input, args = (q,))
    movement = Thread(target = process_output, args = (q,))
    input_start_th = Thread (target = start_control)
    
    input.start()
    movement.start()
    input_start_th.start()
