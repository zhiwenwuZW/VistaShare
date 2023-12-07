import subprocess

# Define the variables
ip_addr = "192.168.52.228"
port = 8888
width = 1280
height = 960
framerate = 10


# Construct the command using the variables
command = f"libcamera-vid -n -t 0 --width {width} --height {height} --framerate {framerate} --inline --listen -o tcp://{ip_addr}:{port}"

# Function to execute the command
def execute_command():
    try:
        subprocess.run(command, check=True, shell=True)
        return "Command [" + command + "]executed successfully."
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

# Call this function to execute the command
execute_command()
