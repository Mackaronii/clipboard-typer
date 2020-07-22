import clipboard_typer_utils as Utils
from tkinter import (Tk, Label, Button, Checkbutton,
                     Scale, IntVar, HORIZONTAL, W, EW)


class ClipboardTyper(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Initialize window properties
        self.title('Clipboard Typer')

        # Checkbutton for Type Racer text processing
        self.__cbIsTypeRacerVar = IntVar()
        cbIsTypeRacer = Checkbutton(
            self, text="isTypeRacer", variable=self.__cbIsTypeRacerVar)
        cbIsTypeRacer.grid(row=0, column=0, sticky=W)

        # Checkbutton for typing everything except the last character
        self.__cbLeaveLastChar = IntVar()
        cbLeaveLastChar = Checkbutton(
            self, text="leaveLastChar", variable=self.__cbLeaveLastChar)
        cbLeaveLastChar.grid(row=1, column=0, sticky=W)

        # Typing delay label
        typing_delay_label = Label(self, text="Typing delay (ms)")
        typing_delay_label.grid(row=2, column=0)

        # Typing delay scale
        self.__typing_delay_scale = Scale(self,
                                          from_=1,
                                          to=1000,
                                          orient=HORIZONTAL)
        self.__typing_delay_scale.grid(row=2, column=1)

        # Start delay label
        start_delay_label = Label(self, text="Start delay (ms)")
        start_delay_label.grid(row=3, column=0)

        # Start delay scale
        self.__start_delay_scale = Scale(self,
                                         from_=0,
                                         to=10000,
                                         orient=HORIZONTAL)
        self.__start_delay_scale.grid(row=3, column=1)

        # Main button
        button = Button(self, text="Type Clipboard Image",
                        bg="pale green",
                        command=self.__on_button_press)
        button.grid(row=4, column=0, columnspan=2, sticky=EW)

    def __on_button_press(self):
        Utils.type_from_clipboard(
            isTypeRacer=self.__cbIsTypeRacerVar.get(),
            leaveLastChar=self.__cbLeaveLastChar.get(),
            typingDelay=self.__typing_delay_scale.get(),
            startDelay=self.__start_delay_scale.get())


def main():
    print("Running Clipboard Typer")
    app = ClipboardTyper()
    app.mainloop()


if __name__ == '__main__':
    main()
