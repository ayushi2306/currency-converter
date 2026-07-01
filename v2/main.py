import tkinter as tk
from tkinter import ttk, messagebox

# Exchange Rates (Base: USD)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.88,
    "GBP": 0.74,
    "JPY": 162.80,
    "INR": 94.95
}

currency_names = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "INR": "Indian Rupee"
}


# Convert Currency Function
def convert_currency():
    try:
        amount = float(amount_entry.get())

        if amount <= 0:
            messagebox.showerror(
                "Invalid Amount",
                "Amount should be greater than zero."
            )
            return

        source = from_currency.get()
        destination = to_currency.get()

        if source == "" or destination == "":
            messagebox.showerror(
                "Missing Currency",
                "Please select both currencies."
            )
            return

        usd_amount = amount / exchange_rates[source]
        final_amount = usd_amount * exchange_rates[destination]

        result_label.config(
            text=f"{amount:.2f} {source} = {final_amount:.2f} {destination}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid numeric amount."
        )



# Clear Function
def clear_fields():
    amount_entry.delete(0, tk.END)
    from_currency.set("")
    to_currency.set("")
    result_label.config(text="Result will appear here")



# Main Window

root = tk.Tk()

root.title("Currency Converter")
root.geometry("500x380")
root.resizable(False, False)


# Heading

heading = tk.Label(
    root,
    text="Currency Converter",
    font=("Arial", 20, "bold")
)

heading.grid(row=0, column=0, columnspan=2, pady=20)


# Amount

amount_label = tk.Label(
    root,
    text="Amount",
    font=("Arial", 12)
)

amount_label.grid(row=1, column=0, padx=15, pady=10, sticky="w")

amount_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)

amount_entry.grid(row=1, column=1, pady=10)


# From Currency
from_label = tk.Label(
    root,
    text="From",
    font=("Arial", 12)
)

from_label.grid(row=2, column=0, padx=15, pady=10, sticky="w")

from_currency = ttk.Combobox(
    root,
    values=list(exchange_rates.keys()),
    state="readonly",
    width=22
)

from_currency.grid(row=2, column=1)


# To Currency
to_label = tk.Label(
    root,
    text="To",
    font=("Arial", 12)
)

to_label.grid(row=3, column=0, padx=15, pady=10, sticky="w")

to_currency = ttk.Combobox(
    root,
    values=list(exchange_rates.keys()),
    state="readonly",
    width=22
)

to_currency.grid(row=3, column=1)

# Buttons
convert_button = tk.Button(
    root,
    text="Convert",
    font=("Arial", 11, "bold"),
    width=12,
    command=convert_currency
)

convert_button.grid(row=4, column=0, pady=20)

clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 11, "bold"),
    width=12,
    command=clear_fields
)

clear_button.grid(row=4, column=1)


# Result
result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 14, "bold"),
    fg="blue"
)

result_label.grid(row=5, column=0, columnspan=2, pady=20)

# Run Application
root.mainloop()