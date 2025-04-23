# This script connects to a wireless controller via Bluetooth on a Raspberry Pi.
# It scans for nearby Bluetooth devices, checks if a wireless controller is already connected,
import time
time.sleep(1)  # Wait for bluetooth to initialize
import bluetooth, subprocess

# Checks if a wireless controller is already connected
def check_connected():
  global connected
  command = "sudo bluetoothctl info"  # Command to get Bluetooth device info
  ret = subprocess.run(command, capture_output=True, shell=True)  # Execute the command
  if("wireless controller" in str(ret).lower()):  # Check if the output contains "wireless controller"
    connected = True

# Activates Bluetooth scanning by powering on the Bluetooth adapter
def activate_scan():
  global connected
  command = "sudo bluetoothctl power on;"  # Command to power on Bluetooth
  ret = subprocess.run(command, capture_output=True, shell=True)  # Execute the command

# Attempts to connect to a Bluetooth device with the given address
def connect(addr):
  global connected
  command = "sudo bluetoothctl connect " + addr  # Command to connect to the device
  ret = subprocess.run(command, shell=True)  # Execute the command
  print(ret)  # Print the result of the connection attempt
  connected = True  # Assume connection is successful (TODO: improve this logic)

# Continuously scans for nearby Bluetooth devices and connects to a wireless controller if found
def await_controller():
  global connected
  check_connected()  # Check if already connected
  while (connected == False):  # Loop until connected
    try:
      nearby_devices = bluetooth.discover_devices(lookup_names=True)  # Discover nearby devices
      print("Found {} devices.".format(len(nearby_devices)))  # Print the number of devices found
      
      for addr, name in nearby_devices:  # Iterate through discovered devices
          print("  {} - {}".format(addr, name))  # Print the address and name of each device
          if ("wireless controller" in name.lower()):  # Check if the device is a wireless controller
            print("Connecting controller...")
            connect(addr)  # Attempt to connect to the controller
    except Exception as e:
      print(e)  # Print any exceptions that occur

#activate_scan()  # Uncomment to activate scanning (currently not used)
connected = False  # Initialize the connected flag
await_controller()  # Start the process of awaiting and connecting to a controller