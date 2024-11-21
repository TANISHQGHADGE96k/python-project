import tkinter as tk  # Importing tkinter for GUI development
from tkinter import messagebox, simpledialog  # Importing specific dialog utilities from tkinter

# Function to check if the user has entered a string
def check_if_empty():
    if not user_string.get():  # If the string variable is empty
        messagebox.showwarning("Input Error", "Please enter a string to proceed.")  # Show a warning message
        return True  # Return True to indicate an empty input
    return False  # Return False if the input is valid

# Function to convert the string to uppercase
def convert_to_uppercase():
    if check_if_empty():  # Check if the input is empty
        return
    result = user_string.get().upper()  # Convert the string to uppercase
    messagebox.showinfo("Uppercase Result", f"Uppercase: {result}")  # Display the result in a message box

# Function to convert the string to lowercase
def convert_to_lowercase():
    if check_if_empty():  # Check if the input is empty
        return
    result = user_string.get().lower()  # Convert the string to lowercase
    messagebox.showinfo("Lowercase Result", f"Lowercase: {result}")  # Display the result

# Function to reverse the string
def reverse_string():
    if check_if_empty():  # Check if the input is empty
        return
    result = user_string.get()[::-1]  # Reverse the string using slicing
    messagebox.showinfo("Reversed String", f"Reversed: {result}")  # Display the reversed string

# Function to check if the string is a palindrome
def check_palindrome():
    if check_if_empty():  # Check if the input is empty
        return
    text = user_string.get()  # Get the current input string
    if text == text[::-1]:  # Check if the string is equal to its reverse
        messagebox.showinfo("Palindrome Check", "The string is a palindrome.")  # Display success message
    else:
        messagebox.showinfo("Palindrome Check", "The string is not a palindrome.")  # Display failure message

# Function to find a substring in the string
def find_substring():
    if check_if_empty():  # Check if the input is empty
        return
    substring = simpledialog.askstring("Find Substring", "Enter substring to find:")  # Ask for the substring
    if substring in user_string.get():  # Check if the substring exists in the main string
        index = user_string.get().find(substring)  # Find the starting index of the substring
        messagebox.showinfo("Find Substring", f"Substring '{substring}' found at index {index}.")  # Display the index
    else:
        messagebox.showinfo("Find Substring", f"Substring '{substring}' not found.")  # Display not found message

# Function to replace a substring with another substring
def replace_substring():
    if check_if_empty():  # Check if the input is empty
        return
    old = simpledialog.askstring("Replace Substring", "Enter substring to replace:")  # Ask for the old substring
    new = simpledialog.askstring("Replace Substring", "Enter new substring:")  # Ask for the new substring
    result = user_string.get().replace(old, new)  # Replace the old substring with the new one
    messagebox.showinfo("Replace Substring", f"Modified String: {result}")  # Display the modified string

# Function to split the string based on a delimiter
def split_string():
    if check_if_empty():  # Check if the input is empty
        return
    delimiter = simpledialog.askstring("Split String", "Enter delimiter to split the string:")  # Ask for the delimiter
    result = user_string.get().split(delimiter)  # Split the string using the delimiter
    messagebox.showinfo("Split String", f"Split Result: {result}")  # Display the split parts

# Function to join strings with a specified delimiter
def join_strings():
    joiner = simpledialog.askstring("Join Strings", "Enter string to join with:")  # Ask for the joiner string
    parts = simpledialog.askstring("Join Strings", "Enter strings separated by space to join:")  # Ask for strings to join
    if parts:  # Check if parts were provided
        parts_list = parts.split()  # Split the input into a list of strings
        result = joiner.join(parts_list)  # Join the list of strings using the joiner
        messagebox.showinfo("Join Strings", f"Joined String: {result}")  # Display the joined string

# Function to remove all whitespaces from the string
def remove_whitespaces():
    if check_if_empty():  # Check if the input is empty
        return
    result = user_string.get().replace(" ", "")  # Remove spaces from the string
    messagebox.showinfo("Remove Whitespaces", f"String without Whitespaces: {result}")  # Display the result

# Function to check if the string starts and ends with specific substrings
def check_start_end():
    if check_if_empty():  # Check if the input is empty
        return
    start = simpledialog.askstring("Check Start and End", "Enter starting substring:")  # Ask for starting substring
    end = simpledialog.askstring("Check Start and End", "Enter ending substring:")  # Ask for ending substring
    starts = user_string.get().startswith(start)  # Check if the string starts with the given substring
    ends = user_string.get().endswith(end)  # Check if the string ends with the given substring
    messagebox.showinfo("Check Start and End", f"Starts with '{start}': {starts}\nEnds with '{end}': {ends}")  # Display the results

# Function to exit the program
def exit_program():
    root.destroy()  # Close the Tkinter window

# Setting up the main Tkinter window
root = tk.Tk()  # Create the main window
root.title("String Data Structure Operations")  # Set the title of the window
root.geometry("400x400")  # Set the size of the window

# Entry field for the user to input their string
tk.Label(root, text="Enter your string:").pack(pady=5)  # Add a label for the input field
user_string = tk.StringVar()  # Create a Tkinter StringVar to hold the string
tk.Entry(root, textvariable=user_string, width=40).pack(pady=5)  # Add an entry widget for the string

# Buttons for each operation
buttons = [
    ("Convert to Uppercase", convert_to_uppercase),
    ("Convert to Lowercase", convert_to_lowercase),
    ("Reverse the String", reverse_string),
    ("Check Palindrome", check_palindrome),
    ("Find a Substring", find_substring),
    ("Replace Substring", replace_substring),
    ("Split the String", split_string),
    ("Join Strings", join_strings),
    ("Remove Whitespaces", remove_whitespaces),
    ("Check Start and End", check_start_end),
    ("Exit", exit_program)
]

# Add a button for each operation
for text, command in buttons:
    tk.Button(root, text=text, command=command, width=25).pack(pady=5)  # Create a button and add it to the window

# Run the Tkinter event loop
root.mainloop()  # Start the GUI event loop