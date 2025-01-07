import tkinter as tk
import time

# Display Setting
root = tk.Tk()
root.title("Stop Watch")
root.geometry("900x550")
root.configure(bg="black")

# Initialize variables
start_time = None
elapsed_time = 0
running = False

# List of colors to cycle through
colors = ["white"]
color_index = 0  # Keeps track of the current color in the list 

# Label to display the headings
label_stop_watch = tk.Label(
    root, text="Stop Watch", font=("Arial", 30, "bold"), fg="#FD7F20", bg="black"
)
label_stop_watch.grid(row=0, column=0, padx=120, pady=20, sticky="w")

label_drop_down = tk.Label(
    root, text="Count Down", font=("Arial", 30, "bold"), fg="#FD7F20", bg="black"
)
label_drop_down.grid(row=0, column=1, padx=120, pady=20, sticky="e")

# Label to display the stopwatch time
label = tk.Label(root, text="00:00:00", font=("Agdasima", 35), bg="black", fg="white")
label.grid(row=1, column=0, columnspan=1, pady=40)

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
        root.after(1000, update_time)

# Start function
def start():
    global start_time, running, elapsed_time
    if not running:
        start_time = time.time()  # Record start time
        running = True
        update_time()

# Stop function
def stop():
    global running, elapsed_time
    if running:
        elapsed_time += time.time() - start_time  # Add the elapsed time since start
        running = False

# Reset function
def reset():
    global elapsed_time, running, color_index
    elapsed_time = 0
    running = False
    color_index = 0  # Reset color index to start from the first color
    label.config(text="00:00:00", fg="white")  # Reset label and color to default

# Buttons
start_button = tk.Button(
    root, command=start, bg="#FD7F20", text="Start", fg="black", width=8, font=("Agdasima", 15, "bold")
)
start_button.grid(row=2, column=0, pady=10)

stop_button = tk.Button(
    root, command=stop, bg="#FD7F20", text="Stop", fg="black", width=8, font=("Agdasima", 15, "bold")
)
stop_button.grid(row=3, column=0, pady=20)

reset_button = tk.Button(
    root, command=reset, bg="#FD7F20", text="Reset", fg="black", width=8, font=("Agdasima", 15, "bold")
)
reset_button.grid(row=4, column=0, columnspan=1, pady=10)

# Running the Program
root.mainloop()
