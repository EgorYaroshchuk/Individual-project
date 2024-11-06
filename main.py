import tkinter as tk
from tkinter import messagebox
from animation import play_animation
from menu_manager import add_dish, remove_dish, edit_dish, save_menu, load_menu, update_menu_list

def open_new_window():
    preroot.destroy()
    
    def toggle_frame():
        if add_dish_frame.winfo_viewable():
            add_dish_frame.grid_remove()  # Ховати фрейм
        else:
            add_dish_frame.grid()  # Показувати фрейм

    root = tk.Tk()
    root.title('Меню ресторану "Три окуні"')

    category_var = tk.StringVar(value="Гаряче")
    categories = ["Гаряче", "Салат", "Десерт", "Напій"]

    # Кнопка видалення блюда
    tk.Button(root, text="Видалити обрану страву", width=33, bg="#ff4400", fg="black", command=lambda: remove_dish(menu_list)).grid(row=0, column=0, columnspan=1)
    
    # Кнопка редагування блюда
    tk.Button(root, text="Редагувати обрану страву", width=33, bg="#ffaa00", fg="black", command=lambda: edit_dish(entry_name, entry_price, category_var, entry_weight, menu_list)).grid(row=0, column=1, columnspan=1)
    
    # Кнопка для показу/приховування форми для додавання блюда
    toggle_button = tk.Button(root, text="Додати нову страву", width=33, bg="#44aaff", fg="black", command=toggle_frame)
    toggle_button.grid(row=0, column=2, columnspan=1)

    add_dish_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10, relief=tk.GROOVE, bd=2)

    # Поля для введення страви
    tk.OptionMenu(add_dish_frame, category_var, *categories).grid(row=0, column=0, columnspan=2)
    
    label_name = tk.Label(add_dish_frame, text="Назва:")
    label_name.grid(row=1, column=0)
    entry_name = tk.Entry(add_dish_frame)
    entry_name.grid(row=1, column=1)

    label_price = tk.Label(add_dish_frame, text="Ціна:")
    label_price.grid(row=2, column=0)
    entry_price = tk.Entry(add_dish_frame)
    entry_price.grid(row=2, column=1)

    label_weight = tk.Label(add_dish_frame, text="Вага (г):")
    label_weight.grid(row=3, column=0)
    entry_weight = tk.Entry(add_dish_frame)
    entry_weight.grid(row=3, column=1)

    # Кнопка для додавання страви
    tk.Button(add_dish_frame, text="Додати", bg="#33cc11", fg="black", command=lambda: add_dish(entry_name, entry_price, category_var, entry_weight, menu_list)).grid(row=4, columnspan=2)
    add_dish_frame.grid(row=1, column=0, columnspan=3)
    add_dish_frame.grid_remove()  # Приховуємо фрейм

    # Список для відображення меню
    menu_list = tk.Listbox(root, width=100, height=3)
    menu_list.grid(row=2, column=0, sticky="ew", columnspan=3)

    tk.Button(root, text="Зберігти меню", width=33, bg="#33cc11", fg="black", command=save_menu).grid(row=3, column=0)
    tk.Button(root, text="Завантажити меню", width=33, bg="#ffaa00", fg="black", command=lambda: load_menu(menu_list)).grid(row=3, column=2)

    root.mainloop()

preroot = tk.Tk()
preroot.title("Анімація на початку програми")

animation_label = tk.Label(preroot)
animation_label.pack()

play_animation(preroot, animation_label)

preroot.bind("<Button-1>", lambda event: open_new_window())

preroot.mainloop()
