import tkinter as tk
import time

# Display Setting
root = tk.Tk()
root.title("Stopwatch")
root.geometry("900x550")
root.configure(bg="black")

# Initialize variables
start_time = None
elapsed_time = 0
running = False
countdown_running = False

# List of colors to cycle through
colors = ["white", "red", "green", "blue", "yellow"]
color_index = 0

# Stopwatch label
stopwatch_label = tk.Label(root, text="Stopwatch", font=("Arial", 30, "bold"), fg="#FD7F20", bg="black")
stopwatch_label.grid(row=0, column=0, padx=120, pady=20, sticky="w")

# Countdown label
countdown_label = tk.Label(root, text="Countdown", font=("Arial", 30, "bold"), fg="#FD7F20", bg="black")
countdown_label.grid(row=0, column=1, padx=120, pady=20, sticky="e")

# Stopwatch time display
stopwatch_display = tk.Label(root, text="00:00:00", font=("Agdasima", 35), bg="black", fg="white")
stopwatch_display.grid(row=1, column=0, pady=0)

# Countdown time entry and display
countdown_display = tk.Label(root, text="Enter countdown time (seconds):", font=("Agdasima", 15), bg="black", fg="white")
countdown_display.grid(row=2, column=1, pady=0)

countdown_entry = tk.Entry(root, font=("Arial", 14), width=20)
countdown_entry.grid(row=3, column=1, pady=0)

countdown_timer = tk.Label(root, text="00:00:00", font=("Agdasima", 35), bg="black", fg="white")
countdown_timer.grid(row=4, column=1, pady=20)

# Functions
def update_stopwatch():
    global color_index
    if running:
        current_time = time.time() - start_time + elapsed_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
        stopwatch_display.config(text=formatted_time, fg=colors[color_index])
        color_index = (color_index + 1) % len(colors)
        root.after(1000, update_stopwatch)

def start_stopwatch():
    global start_time, running
    if not running:
        start_time = time.time()
        running = True
        update_stopwatch()

def stop_stopwatch():
    global running, elapsed_time
    if running:
        elapsed_time += time.time() - start_time
        running = False

def reset_stopwatch():
    global elapsed_time, running, color_index
    elapsed_time = 0
    running = False
    color_index = 0
    stopwatch_display.config(text="00:00:00", fg="white")

# Global variable to store remaining time
remaining_time = 0

# Start countdown function
def start_countdown():
    global countdown_running, remaining_time
    if not countdown_running:
        try:
            remaining_time = int(countdown_entry.get())
            countdown_timer.config(text=time.strftime("%H:%M:%S", time.gmtime(remaining_time)))
            countdown_running = True
            update_countdown()
        except ValueError:
            countdown_timer.config(text="Invalid Input")

# Update countdown function
def update_countdown():
    global countdown_running, remaining_time
    if countdown_running:
        if remaining_time > 0:
            countdown_timer.config(text=time.strftime("%H:%M:%S", time.gmtime(remaining_time)))
            remaining_time -= 1
            root.after(1000, update_countdown)
        else:
            countdown_running = False
            countdown_timer.config(text="Time's up!")

# Stop countdown function
def stop_countdown():
    global countdown_running
    countdown_running = False

# Resume countdown function
def resume_countdown():
    global countdown_running
    if not countdown_running and remaining_time > 0:
        countdown_running = True
        update_countdown()

# Buttons for Stopwatch
tk.Button(
    root, command=start_stopwatch, bg="#FD7F20", text="Start", fg="black", width=8, font=("Agdasima", 15, "bold")
).grid(row=2, column=0, pady=10)

tk.Button(
    root, command=stop_stopwatch, bg="#FD7F20", text="Stop", fg="black", width=8, font=("Agdasima", 15, "bold")
).grid(row=3, column=0, pady=10)

tk.Button(
    root, command=reset_stopwatch, bg="#FD7F20", text="Reset", fg="black", width=8, font=("Agdasima", 15, "bold")
).grid(row=4, column=0, pady=10)

# Buttons for Countdown
tk.Button(
    root, command=start_countdown, bg="#FD7F20", text="Start", fg="black", width=8, font=("Agdasima", 15, "bold")
).grid(row=5, column=1, pady=10)

tk.Button(
    root, command=stop_countdown, bg="#FD7F20", text="Stop", fg="black", width=8, font=("Agdasima", 15, "bold")
).grid(row=6, column=1, pady=10)
# Resume button
tk.Button(
    root, command=resume_countdown, bg="#FD7F20", text="Resume", fg="black", width=8, font=("Agdasima", 15, "bold")
).grid(row=7, column=1, pady=10)



# Run the Program
root.mainloop()
