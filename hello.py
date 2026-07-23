import tkinter as tk
from tkinter import messagebox

# -----------------------------
# DATA (Inventory + Prices)
# -----------------------------
inventory = {
    "Water": 20,
    "Bread": 50,
    "Chips": 40
}

prices = {
    "Water": 10,
    "Bread": 15,
    "Chips": 20
}

cart = {}

# -----------------------------
# FUNCTIONS
# -----------------------------
def add_to_cart():
    product = product_var.get()
    
    try:
        qty = int(quantity_entry.get())
    except:
        messagebox.showerror("Error", "Enter a valid number")
        return

    if qty <= 0:
        messagebox.showerror("Error", "Quantity must be greater than 0")
        return

    if inventory[product] >= qty:
        cart[product] = cart.get(product, 0) + qty
        inventory[product] -= qty
        update_inventory()
        messagebox.showinfo("Added", f"{qty} {product} added to cart")
    else:
        messagebox.showwarning("Stock Error", "Not enough stock")

def checkout():
    total = 0
    for item, qty in cart.items():
        total += prices[item] * qty

    total_label.config(text=f"Total: ₱{total}")
    cart.clear()

def update_inventory():
    text = ""
    for item, qty in inventory.items():
        status = "OK" if qty > 10 else "LOW"
        text += f"{item}: {qty} ({status})\n"
    inventory_label.config(text=text)
    update_ai()

def update_ai():
    text = ""
    for item, qty in inventory.items():
        if qty < 50:
            restock = 100 - qty
            text += f"{item}: Restock {restock}\n"
    ai_label.config(text=text)

# -----------------------------
# GUI DESIGN
# -----------------------------
root = tk.Tk()
root.title("AI-Powered POS: Predict Sales, Perfect Inventory")
root.geometry("350x500")

# Select Product
tk.Label(root, text="Select Product").pack(pady=5)

product_var = tk.StringVar(value="Water")
tk.OptionMenu(root, product_var, *inventory.keys()).pack()

# Quantity
tk.Label(root, text="Quantity").pack(pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Buttons
tk.Button(root, text="Add to Cart", width=20, command=add_to_cart).pack(pady=5)
tk.Button(root, text="Checkout", width=20, command=checkout).pack(pady=5)

# Total
total_label = tk.Label(root, text="Total: ₱0", font=("Arial", 12))
total_label.pack(pady=10)

# Inventory Section
tk.Label(root, text="Inventory", font=("Arial", 10, "bold")).pack()
inventory_label = tk.Label(root, justify="left")
inventory_label.pack()

# AI Suggestions
tk.Label(root, text="AI Suggestions", font=("Arial", 10, "bold")).pack(pady=5)
ai_label = tk.Label(root, justify="left")
ai_label.pack()

# Initialize
update_inventory()

root.mainloop()