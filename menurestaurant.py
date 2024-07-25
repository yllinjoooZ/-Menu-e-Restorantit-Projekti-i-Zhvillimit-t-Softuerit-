import tkinter as tk

def create_menu_window():
    root = tk.Tk()
    root.title("Menu e Restorantit")
    root.geometry("400x400")
    
    title = tk.Label(root, text="Menu e Restorantit", font=("Helvetica", 18, "bold"))
    title.pack(pady=10)
    
    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=10)
    
    items = [
        ("Pizza", "5.00$"),
        ("Pasta", "4.50$"),
        ("Sallat", "3.00$"),
        ("Hamburger", "4.00$"),
        ("Supa", "2.50$"),
        ("Kafe", "1.00$"),
        ("Qaj", "0.80$"),
        ("Leng Frutash", "2.00$")
    ]
    
    for item, price in items:
        item_label = tk.Label(menu_frame, text=item, font=("Helvetica", 14))
        item_label.pack(anchor="w")
        price_label = tk.Label(menu_frame, text=price, font=("Helvetica", 14))
        price_label.pack(anchor="e")
    
    root.mainloop()

if __name__ == "__main__":
    create_menu_window()
