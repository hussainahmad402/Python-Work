import tkinter as tk
import random  # Import the random module to generate random numbers

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")
root.configure(bg="black")
root.geometry("400x400")
# root.resizable(False, False)

# Create a label to display the random number
label = tk.Label(root, text="Click to generate a random number", font=("Agdasima", 14), bg="black", fg="white")
label.pack(pady=20)

label=tk.Label(root,text="",font=("Agdasima",14), bg="black",fg="White")
label.pack(pady=20)
number=0
# Reset the number 
def reset():
    global number
    number=0
    label.config(text="Count=0")
# Create a function to handle button click and generate a random number
def on_button_click():
    # Generate a random number between 1 and 100
    global number
    number+=1
    # Update the label to show the generated random number
    label.config(text=f"Count: {number}",font=("Agdasima",14))

# Create a button that calls the on_button_click function
button = tk.Button(root, text="Generate Random Number", command=on_button_click,bg="#3D3D3D",fg="white",activebackground="#3D3D3D",activeforeground="white")
button.pack(pady=10)

# Reset Button
reset_button=tk.Button(root,text="Reset",command=reset,bg="#3D3D3D",fg="white",activebackground="#3D3D3D",activeforeground="white")
reset_button.pack(pady=10)

# Run the application
root.mainloop()
