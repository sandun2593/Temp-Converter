from tkinter import *

class converter:
    def __init__(self):

        button_font = ("Arial", "8")
        button_fg = "#FFFFFF"

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

        self.temp_entry = Entry(self.temp_frame,
                                font=("Ariel", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)


        error = "please enter a number"
        self.temp_error = Label(self.temp_frame, text="",
                                fg="#9c0000")
        self.temp_error.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg="#FFFFFF",
                                        command=self.to_celsius)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = Button(self.button_frame,
                                          text="To Farenheit",
                                          bg="#009900",
                                          fg="#FFFFFF")
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)
#
        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font, width=12)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame,
                                       text="History / Export",
                                       bg="#004C99",
                                       fg=button_fg,
                                       font=button_font, width=12,
                                       state=DISABLED)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

    def check_temp(self, min_value):
        error = "Please enter a number that is more " \
                "than {}".format(min_value)

        try:
            response = self.temp_entry.get()
            response = float(response)

            if response < min_value:
                self.temp_error.config(text=error)
            else:
                return response

        except ValueError:
            self.temp_error.config(text=error)


    def to_celsius(self):
        self.check_temp(-459)



if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    converter()
    root.mainloop()


