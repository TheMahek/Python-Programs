import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"Result: {result}")
    except Exception as e:
        label_result.config(text="Error")

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")

# Entry
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Button
button = tk.Button(root, text="Calculate", command=calculate)
button.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Result: ", fg="green")
label_result.pack(pady=10)

root.mainloop()
