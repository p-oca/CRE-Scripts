# Author: Paul Oca
# Title: Motor Setup Sequence Paster for use with ETS6
# Function: An automated clipboard paste updater for adding descriptions for motors and other sequential devices in ETS6

import keyboard
import pyperclip
import tkinter as tk
from tkinter import simpledialog, messagebox

def main():
    print("Watchdog script started.")

    original_string = get_original_string()
    substring = get_substring(original_string)
    sequence = get_sequence()

    while True:
        sequence_numbers = [int(num) for num in sequence.split(", ")]
        for number in sequence_numbers:
            updated_substring = substring[:-2] + str(number).zfill(2)
            updated_string = original_string.replace(substring, updated_substring)

            pyperclip.copy(updated_string)
            print(f"Copied: {updated_string}")

            while not keyboard.is_pressed('ctrl+v'):
                if keyboard.is_pressed('x'):
                    print("Exiting on user request.")
                    show_exit_message()
                    return

            while keyboard.is_pressed('ctrl+v'):
                pass  # Wait until the paste key is released

        repeat = repeat_sequence_prompt()
        if not repeat:
            break

    print("Watchdog script ended.")

def get_original_string():
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("Paul's super convenient 2-digit substring KNX number automator",
                                  "Enter the original string:")

def get_substring(original_string):
    root = tk.Tk()
    root.withdraw()
    substring = simpledialog.askstring("Substring",
                                       f"Enter a substring with 2 digits at the end from your given string:\n{original_string}",
                                       initialvalue=original_string[-2:])
    if len(substring) >= 2 and substring[-2:].isdigit():
        return substring

def get_sequence():
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("Sequence",
                                  "Enter a sequence of 2-digit numbers separated by commas and spaces:")

def repeat_sequence_prompt():
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askyesno("Sequence Ended", "The sequence has ended. Do you want to repeat the sequence?")
    return response

def show_exit_message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Script Ended", "The Python script has ended.")

if __name__ == "__main__":
    main()
