import tkinter as tk
import time

# Display Setting
root = tk.Tk()
root.title("Stop Watch")
root.geometry("400x450")
root.configure(bg="black")

# Initialize variables
start_time = None
elapsed_time = 0
running = False

# List of colors to cycle through
colors = ["#FF2511", "white"]
color_index = 0  # Keeps track of the current color in the list

# Label to display the time
label = tk.Label(root, text="00:00:00", font=("Agdasima", 35), bg="black", fg="white")
label.pack(pady="70 0")

# Function to update the stopwatch and change color every second
def update_time():
    global color_index
    if running:
        current_time = time.time() - start_time + elapsed_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
        label.config(text=formatted_time)

        # Change color every second
        label.config(fg=colors[color_index])
        color_index = (color_index + 1) % len(colors)  # Move to the next color, looping back to the start

        # Update the time every second
        root.after(1000, update_time)  # Update every 1 second

# Start function
def start():
    global start_time, running, elapsed_time
    if not running:
        start_time = time.time()  # Record start time
        running = True
        update_time()  # Start updating the time
        # start_button.config(state=tk.DISABLED)  # Disable the start button after starting

# Stop function
def stop():
    global running, elapsed_time
    if running:
        elapsed_time += time.time() - start_time  # Add the elapsed time since start
        running = False
        start_button.config(state=tk.NORMAL)  # Enable the start button again

# Reset function
def reset():
    global elapsed_time, running, color_index
    elapsed_time = 0
    running = False
    color_index = 0  # Reset color index to start from the first color
    label.config(text="00:00:00", fg="white")  # Reset label and color to default
    start_button.config(state=tk.NORMAL)  # Enable the start button again

# Start Button
start_button = tk.Button(root, command=start, bg="#FD7F20", text="Start", fg="black", activebackground="#FD7F20", activeforeground="black", width=8, font=("Agdasima", 15,"bold"))
start_button.pack(pady="50 20")

# Stop Button
stop_button = tk.Button(root, command=stop, bg="#FD7F20", text="Stop", fg="black", activebackground="#FD7F20", activeforeground="black", width=8, font=("Agdasima", 15,"bold"))
stop_button.pack(pady="20")

# Reset Button
reset_button = tk.Button(root, command=reset, bg="#FD7F20", text="Reset", fg="black", activebackground="#FD7F20", activeforeground="black", width=8, font=("Agdasima", 15,"bold"))
reset_button.pack(pady="20")

# Running the Program
root.mainloop()
