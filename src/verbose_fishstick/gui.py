"""Tkinter-based GUI for the verbose-fishstick calculator."""

import tkinter as tk
from tkinter import messagebox

from .calculator import add, subtract


def main() -> None:
    """Launch the calculator GUI."""
    root = tk.Tk()
    root.title("Verbose Fishstick Calculator")

    tk.Label(root, text="First number:").grid(
        row=0, column=0, padx=5, pady=5, sticky="e"
    )
    entry_a = tk.Entry(root, width=10)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Second number:").grid(
        row=1, column=0, padx=5, pady=5, sticky="e"
    )
    entry_b = tk.Entry(root, width=10)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    result_var = tk.StringVar(value="Result: ")
    tk.Label(root, textvariable=result_var).grid(
        row=2, column=0, columnspan=2, padx=5, pady=5
    )

    def calculate(op: str) -> None:
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
        except ValueError:
            messagebox.showerror(
                "Invalid input", "Please enter numeric values."
            )
            return

        if op == "add":
            res = add(a, b)
        else:
            res = subtract(a, b)
        result_var.set(f"Result: {res}")

    tk.Button(
        root, text="Add", command=lambda: calculate("add")
    ).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(
        root, text="Subtract", command=lambda: calculate("subtract")
    ).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    root.mainloop()


if __name__ == "__main__":
    main()
