import tkinter as tk
from tkinter import ttk, messagebox

# Exchange rates without DEM
exchange_rates = {
    'USD': {'INR': 83.0, 'EUR': 0.92, 'CNY': 7.2, 'JPY': 157.0, 'RUB': 91.5, 'GBP': 0.79},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'CNY': 0.087, 'JPY': 1.89, 'RUB': 1.1, 'GBP': 0.0095},
    'EUR': {'USD': 1.09, 'INR': 90.0, 'CNY': 7.8, 'JPY': 170.0, 'RUB': 99.0, 'GBP': 0.86},
    'CNY': {'USD': 0.14, 'INR': 11.5, 'EUR': 0.13, 'JPY': 21.8, 'RUB': 12.7, 'GBP': 0.11},
    'JPY': {'USD': 0.0064, 'INR': 0.53, 'EUR': 0.0059, 'CNY': 0.045, 'RUB': 0.58, 'GBP': 0.0049},
    'RUB': {'USD': 0.011, 'INR': 0.91, 'EUR': 0.0101, 'CNY': 0.079, 'JPY': 1.72, 'GBP': 0.0086},
    'GBP': {'USD': 1.26, 'INR': 105.0, 'EUR': 1.16, 'CNY': 8.9, 'JPY': 200.0, 'RUB': 116.0}
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        if from_curr == to_curr:
            result_label.config(text="No conversion needed.")
            return

        if from_curr in exchange_rates and to_curr in exchange_rates[from_curr]:
            rate = exchange_rates[from_curr][to_curr]
            converted = amount * rate
            result_label.config(text=f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}")
        else:
            messagebox.showerror("Error", f"No conversion rate found for {from_curr} → {to_curr}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")

# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("460x350")
root.resizable(False, False)

tk.Label(root, text="Currency Converter",bg = "White", font=("Helvetica", 20, "bold")).pack(pady=10)

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

all_currencies = ["USD", "INR", "EUR", "CNY", "JPY", "RUB", "GBP"]

tk.Label(root, text="From Currency:").pack()
from_currency = ttk.Combobox(root, values=all_currencies, state="readonly")

from_currency.pack(pady=5)

tk.Label(root, text="To Currency:").pack()
to_currency = ttk.Combobox(root, values=all_currencies, state="readonly")

to_currency.pack(pady=5)

tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

result_label = tk.Label(root, text="",bg = "White", font=("Helvetica", 20,"bold"))
result_label.pack(pady=10)

root.mainloop()
