# simple inquiry example
import time
time.sleep(10)
import bluetooth, subprocess

def check_connected():
  global connected
  command = "sudo bluetoothctl info"
  ret = subprocess.run(command, capture_output=True, shell=True)
  if("wireless controller" in str(ret).lower()):
    connected = True

def activate_scan():
  global connected
  command = "sudo bluetoothctl power on;"
  ret = subprocess.run(command, capture_output=True, shell=True)

def connect(addr):
  global connected
  command = "sudo bluetoothctl connect " + addr
  ret = subprocess.run(command, shell=True)
  print(ret) #TODO: switch on this to check if already connected/unable to connect
  connected = True

def await_controller():
  global connected
  check_connected()
  while (connected == False):
    try:
      nearby_devices = bluetooth.discover_devices(lookup_names=True)
      print("Found {} devices.".format(len(nearby_devices)))
      
      for addr, name in nearby_devices:
          print("  {} - {}".format(addr, name))
          if ("wireless controller" in name.lower()):
            print("Connecting controller...")
            connect(addr)
    except Exception as e:
      print(e)

#activate_scan()
connected = False
await_controller()