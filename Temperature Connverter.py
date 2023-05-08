from tkinter import *

class converter:
    def __init__(self):
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16"))
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "Then press one of the buttons to convert "\
                       "it from centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=200, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    converter()
    root.mainloop()

