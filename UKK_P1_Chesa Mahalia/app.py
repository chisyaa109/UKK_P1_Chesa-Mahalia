import tkinter as tk
import operator

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("320x450")
        self.resizable(False, False)
        self.expression = []
        self.current_number = ""

        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        self.display_frame = tk.Frame(self)
        self.display_frame.pack(fill="both")

        self.display = tk.Label(self.display_frame, text="0", anchor="e",
                                font=("Arial", 24), bg="#333", fg="white",
                                width=15, height=2)
        self.display.pack(fill="both")

        self.buttons_frame = tk.Frame(self, bg="#222")
        self.buttons_frame.pack(expand=True, fill="both")

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3),
            ('=', 5, 0, 4)  # Tombol '=' diperlebar
        ]

        for btn in buttons:
            text, row, col = btn[:3]
            colspan = btn[3] if len(btn) == 4 else 1
            button = tk.Button(self.buttons_frame, text=text, font=("Arial", 16),
                               bg="#F90" if text in self.operators or text == '=' else "#444",
                               fg="white", width=6, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan, padx=3, pady=3, sticky="nsew")

        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
            self.buttons_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = []
            self.current_number = ""
        elif char == "=":
            if self.current_number:
                self.expression.append(self.current_number)
            self.current_number = self.calculate_result()
            self.expression = []
        elif char in self.operators:
            if self.current_number:
                self.expression.append(self.current_number)
                self.expression.append(char)
                self.current_number = ""
        else:
            self.current_number += char
        self.update_display()

    def calculate_result(self):
        if not self.expression:
            return self.current_number

        try:
            result = float(self.expression[0])
            for i in range(1, len(self.expression) - 1, 2):
                op = self.expression[i]
                num = float(self.expression[i + 1])
                result = self.operators[op](result, num)
            return str(result)
        except Exception:
            return "Tidak bisa dibagi nol"

    def update_display(self):
        display_text = "".join(self.expression) + self.current_number
        self.display.config(text=display_text if display_text else "0")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()