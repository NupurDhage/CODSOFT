import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Modern Calculator")
        self.geometry("400x600")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying the result
        result_entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, relief=tk.FLAT, justify=tk.RIGHT)
        result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        # Create buttons dynamically
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=('Arial', 18), padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Configure row and column weights so that the widgets expand proportionally
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "=":
            try:
                # Evaluate the expression and update the result
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                # Handle errors, such as division by zero
                self.result_var.set("Error")
        else:
            # Update the expression in the entry widget
            current_text = self.result_var.get()
            if current_text == "0" or current_text == "Error":
                self.result_var.set(value)
            else:
                self.result_var.set(current_text + value)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
