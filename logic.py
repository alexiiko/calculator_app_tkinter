import tkinter as tk
from settings import BUTTON_WIDTH, BUTTON_HEIGHT


def app_logic(window):
    equation_frame = tk.Frame(master=window)
    equation_frame.place(x=0, y=0)
    equation = ""

    buttons_frame = tk.Frame(master=window)
    buttons_frame.place(x=0, y=20)

    # row 0
    equation_label = tk.Label(master=equation_frame, text=equation)
    equation_label.grid(column=0, row=0)

    # row 1
    def clear_equation():
        nonlocal equation
        equation = ""
        equation_label.configure(text=equation)

    clear_equation_button = tk.Button(
        master=buttons_frame, text="C", command=clear_equation, width=BUTTON_WIDTH
    )
    clear_equation_button.grid(column=0, row=1)

    def delete_last_character():
        nonlocal equation
        equation = equation[:-1]
        equation_label.configure(text=equation)

    delete_last_character_button = tk.Button(
        master=buttons_frame,
        text="⌫",
        command=delete_last_character,
        width=BUTTON_WIDTH,
    )
    delete_last_character_button.grid(column=1, row=1)

    def append_divide_sign():
        nonlocal equation
        if equation:
            if equation[-1].isdigit():
                equation += "/"
                equation_label.configure(text=equation)

    divide_button = tk.Button(
        master=buttons_frame, text="÷", command=append_divide_sign, width=BUTTON_WIDTH
    )
    divide_button.grid(column=3, row=1)

    # row 2
    def append_seven():
        nonlocal equation
        equation += "7"
        equation_label.configure(text=equation)

    seven_button = tk.Button(
        master=buttons_frame, text="7", command=append_seven, width=BUTTON_WIDTH
    )
    seven_button.grid(column=0, row=2)

    def append_eight():
        nonlocal equation
        equation += "8"
        equation_label.configure(text=equation)

    eight_button = tk.Button(
        master=buttons_frame, text="8", command=append_eight, width=BUTTON_WIDTH
    )
    eight_button.grid(column=1, row=2)

    def append_nine():
        nonlocal equation

        equation += "9"
        equation_label.configure(text=equation)

    nine_button = tk.Button(
        master=buttons_frame, text="9", command=append_nine, width=BUTTON_WIDTH
    )
    nine_button.grid(column=2, row=2)

    def append_times_sign():
        nonlocal equation
        if equation:
            if equation[-1].isdigit():
                equation += "*"
                equation_label.configure(text=equation)

    times_button = tk.Button(
        master=buttons_frame, text="x", command=append_times_sign, width=BUTTON_WIDTH
    )
    times_button.grid(column=3, row=2)

    # row 3
    def append_four():
        nonlocal equation

        equation += "4"
        equation_label.configure(text=equation)

    four_button = tk.Button(
        master=buttons_frame, text="4", command=append_four, width=BUTTON_WIDTH
    )
    four_button.grid(column=0, row=3)

    def append_five():
        nonlocal equation

        equation += "5"
        equation_label.configure(text=equation)

    five_button = tk.Button(
        master=buttons_frame, text="5", command=append_five, width=BUTTON_WIDTH
    )
    five_button.grid(column=1, row=3)

    def append_six():
        nonlocal equation
        equation += "6"
        equation_label.configure(text=equation)

    six_button = tk.Button(
        master=buttons_frame, text="6", command=append_six, width=BUTTON_WIDTH
    )
    six_button.grid(column=2, row=3)

    def append_minus():
        nonlocal equation
        if equation:
            if equation[-1].isdigit():
                equation += "-"
                equation_label.configure(text=equation)

    minus_button = tk.Button(
        master=buttons_frame, text="-", command=append_minus, width=BUTTON_WIDTH
    )
    minus_button.grid(column=3, row=3)

    # row 4
    def append_one():
        nonlocal equation
        equation += "1"
        equation_label.configure(text=equation)

    one_button = tk.Button(
        master=buttons_frame, text="1", command=append_one, width=BUTTON_WIDTH
    )
    one_button.grid(column=0, row=4)

    def append_two():
        nonlocal equation
        equation += "2"
        equation_label.configure(text=equation)

    two_button = tk.Button(
        master=buttons_frame, text="2", command=append_two, width=BUTTON_WIDTH
    )
    two_button.grid(column=1, row=4)

    def append_three():
        nonlocal equation
        equation += "3"
        equation_label.configure(text=equation)

    three_button = tk.Button(
        master=buttons_frame, text="3", command=append_three, width=BUTTON_WIDTH
    )
    three_button.grid(column=2, row=4)

    def append_plus():
        nonlocal equation
        if equation:
            if equation[-1].isdigit():
                equation += "+"
                equation_label.configure(text=equation)

    plus_button = tk.Button(
        master=buttons_frame, text="+", command=append_plus, width=BUTTON_WIDTH
    )
    plus_button.grid(column=3, row=4)

    # row 5
    def append_zero():
        nonlocal equation
        equation += "0"
        equation_label.configure(text=equation)

    zero_button = tk.Button(
        master=buttons_frame, text="0", command=append_zero, width=BUTTON_WIDTH
    )
    zero_button.grid(column=1, row=5)

    def append_dot():
        nonlocal equation
        if equation:
            if equation[-1].isdigit():
                if not "." in equation:
                    equation += "."
                    equation_label.configure(text=equation)

    dot_button = tk.Button(
        master=buttons_frame, text=".", command=append_dot, width=BUTTON_WIDTH
    )
    dot_button.grid(column=0, row=5)

    def calculate_equation():
        nonlocal equation
        if equation:
            if len(equation) >= 3:
                if equation[-1].isdigit():
                    equation = str(eval(equation))
                    equation_label.configure(text=eval(equation))

    equals_button = tk.Button(
        master=buttons_frame, text="=", command=calculate_equation, width=BUTTON_WIDTH
    )
    equals_button.grid(column=3, row=5)
