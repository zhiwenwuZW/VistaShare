import subprocess

# Define the variables
ip_addr = "0.0.0.0"
port = 8888
width = 640
height = 480
framerate = 5


# Construct the command using the variables
command = f"libcamera-vid -n -t 0 --width {width} --height {height} --framerate {framerate} --inline --listen -o tcp://{ip_addr}:{port}"
print("Running the command: \n" + command)

# Function to execute the command
def execute_command():
    try:
        subprocess.run(command, check=True, shell=True)
        print("Command executed successfully.") 
    except subprocess.CalledProcessError as e:
        print(e)

# Call this function to execute the command
execute_command()

