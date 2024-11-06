import json
from tkinter import filedialog, messagebox
import tkinter as tk
from dish import Dish

menu = []

def add_dish(entry_name, entry_price, category_var, entry_weight, menu_list):
    name = entry_name.get()
    price = entry_price.get()
    category = category_var.get()
    weight = entry_weight.get()

    if name and price and category and weight:
        try:
            price = float(price)
            weight = float(weight)
            dish = Dish(name, price, category, weight)
            menu.append(dish)
            menu_list.insert(tk.END, str(dish))
            entry_name.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            entry_weight.delete(0, tk.END)
            menu_list.config(height=max(len(menu_list.get(0, tk.END)), 3))
        except ValueError:
            messagebox.showerror("Помилка", "Ціна та вага повинні бути числами.")
    else:
        messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")

def remove_dish(menu_list):
    selected = menu_list.curselection()
    if selected:
        index = selected[0]
        del menu[index]
        menu_list.delete(index)
    else:
        messagebox.showerror("Помилка", "Оберіть страву для видалення.")

def save_menu():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON файли", "*.json")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([dish.to_dict() for dish in menu], file, ensure_ascii=False, indent=4)
        messagebox.showinfo("Збережено", "Меню успішно збережено!")

def load_menu(menu_list):
    global menu
    file_path = filedialog.askopenfilename(filetypes=[("JSON файли", "*.json")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            menu = [Dish.from_dict(dish_data) for dish_data in data]
            update_menu_list(menu_list)

def update_menu_list(menu_list):
    menu_list.delete(0, tk.END)
    for dish in menu:
        menu_list.insert(tk.END, str(dish))
    menu_list.config(height=max(len(menu_list.get(0, tk.END)), 3))

def edit_dish(entry_name, entry_price, category_var, entry_weight, menu_list):
    selected = menu_list.curselection()
    if selected:
        index = selected[0]
        dish = menu[index]

        entry_name.delete(0, tk.END)
        entry_name.insert(0, dish.name)

        entry_price.delete(0, tk.END)
        entry_price.insert(0, dish.price)

        entry_weight.delete(0, tk.END)
        entry_weight.insert(0, dish.weight)
        
        index = selected[0]
        del menu[index]
        menu_list.delete(index)
    else:
        messagebox.showerror("Помилка", "Оберіть страву для редагування.")
