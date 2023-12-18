# Author: Paul Oca
# Title: Crestron Setup Description Paster for use with ETS6
# Function: An automated clipboard paste updater for adding descriptions for updating CI-KNX data point descriptions
# in ETS6

import keyboard
import pyperclip
import tkinter as tk
from tkinter import simpledialog, messagebox

def main():
    print("Watchdog script started.")

    original_string = get_original_string()
    substring1 = get_substring(original_string)
    sequence = get_sequence()
    substring2 = get_substring2(original_string)

    current_number = int(substring2[-1])

    while True:
        for new_substring1 in sequence:
            updated_string = original_string.replace(substring1, new_substring1)
            updated_string = updated_string.replace(substring2, substring2[:-1] + str(current_number))

            pyperclip.copy(updated_string)
            print(f"Copied: {updated_string}")

            while not keyboard.is_pressed('ctrl+v'):
                if keyboard.is_pressed('x'):
                    print("Exiting on user request.")
                    show_exit_message()
                    return

            while keyboard.is_pressed('ctrl+v'):
                pass  # Wait until the paste key is released

        current_number += 1
        repeat = True  # Automatically repeat
        if not repeat:
            break

    print("Watchdog script ended.")

def get_original_string():
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("String Replacer", "Enter the original string:")

def get_substring1(original_string):
    root = tk.Tk()
    root.withdraw()
    substring = simpledialog.askstring("String Replacer",
                                       f"Enter the substring you want to replace from your given string:\n{original_string}",
                                       initialvalue=original_string[:2])
    return substring

def get_substring2(original_string):
    root = tk.Tk()
    root.withdraw()
    substring = simpledialog.askstring("String Replacer",
                                       f"Enter the substring ending with a digit you want to replace from your given string:\n{original_string}",
                                       initialvalue=original_string[3:])
    return substring

def get_sequence():
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("String Replacer",
                                  "Enter a sequence of strings separated by commas and spaces:\nExample: abc, xyz, pqr").split(
        ", ")

def show_exit_message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Script Ended", "The Python script has ended.")


def get_substring2(original_string):
    root = tk.Tk()
    root.withdraw()
    substring2 = simpledialog.askstring("String Replacer",
                                       f"Enter the substring ending in a digit from your given string:\n{original_string}",
                                       initialvalue=original_string[-3:])
    return substring2
def get_substring(original_string):
    root = tk.Tk()
    root.withdraw()
    substring = simpledialog.askstring("String Replacer",
                                       f"Enter the substring you want to replace from your given string:\n{original_string}",
                                       initialvalue=original_string[:2])
    return substring

if __name__ == "__main__":
    main()
