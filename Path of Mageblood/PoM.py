import tkinter as tk
from PIL import Image, ImageTk
import random

last_used_orb = "" # Переменная для хранения последней использованной сферы

def roll_chance(chance): # Функция для проверки выпадения события с заданным шансом
    random_number = random.random()
    if random_number < chance:
        return True
    else:
        return False

def apply_orb_of_scouring():
    global last_used_orb
    if last_used_orb != "scouring":
        result_label.config(text="Вы использовали сферу очищения!")
        item_image = Image.open("normal_belt.png")  # Путь к изображению нормального пояса
        item_photo = ImageTk.PhotoImage(item_image)
        item_label.configure(image=item_photo)
        item_label.image = item_photo
        last_used_orb = "scouring"
    else:
        result_label.config(text="Вы не можете использовать две сферы очищения подряд!")

def apply_orb_of_chance():
    global last_used_orb
    if last_used_orb != "chance":
        result = roll_chance(0.6)  # Шанс 60% для магического пояса
        if result:
            item_image = Image.open("magic_belt.png")  # Путь к изображению магического пояса
            item_photo = ImageTk.PhotoImage(item_image)
            item_label.configure(image=item_photo)
            item_label.image = item_photo
            result_label.config(text="Ну это только об пол разбить.")
        else:
            result = roll_chance(0.3)  # Шанс 30% для редкого пояса
            if result:
                item_image = Image.open("rare_belt.png")  # Путь к изображению редкого пояса
                item_photo = ImageTk.PhotoImage(item_image)
                item_label.configure(image=item_photo)
                item_label.image = item_photo
                result_label.config(text="Можно торговцу сплавить.")
            else:
                item_image = Image.open("mageblood.png")  # Путь к изображению mageblood
                item_photo = ImageTk.PhotoImage(item_image)
                item_label.configure(image=item_photo)
                item_label.image = item_photo
                result_label.config(text="Вот это я понимаю насыпало.")
        last_used_orb = "chance"
    else:
        result_label.config(text="Вы не можете использовать две сферы удачи подряд!")

def quit_game():
    window.quit()

window = tk.Tk()
window.title("Path of Mageblood")

# Создание виджета Canvas для отображения фона
canvas = tk.Canvas(window, width=1280, height=720)
canvas.pack()

# Загрузка изображения фона
background_image = Image.open("background.jpg")
background_photo = ImageTk.PhotoImage(background_image)
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

title_label = tk.Label(canvas, text="Добро пожаловать в игру Path of Mageblood. Твоя задача зашансить уникальный пояс Mageblood. Для этого используй сферы удачи, если не получилось, то используй сферу очищения.")
title_label.pack(pady=10)

item_label = tk.Label(canvas)
item_label.pack(pady=10)

orb_of_scouring_image = Image.open("orb_of_scouring.png")  # Путь к изображению сферы очищения
orb_of_scouring_photo = ImageTk.PhotoImage(orb_of_scouring_image)
orb_of_scouring_button = tk.Button(canvas, text="Применить сферу очищения", image=orb_of_scouring_photo, compound="left", command=apply_orb_of_scouring)
orb_of_scouring_button.image = orb_of_scouring_photo
orb_of_scouring_button.pack(pady=5)

orb_of_chance_image = Image.open("orb_of_chance.png")  # Путь к изображению сферы удачи
orb_of_chance_photo = ImageTk.PhotoImage(orb_of_chance_image)
orb_of_chance_button = tk.Button(canvas, text="Применить сферу удачи", image=orb_of_chance_photo, compound="left", command=apply_orb_of_chance)
orb_of_chance_button.image = orb_of_chance_photo
orb_of_chance_button.pack(pady=5)

result_label = tk.Label(canvas, text="")
result_label.pack(pady=10)

quit_button = tk.Button(canvas, text="Наигрался", command=quit_game)
quit_button.pack(pady=5)

window.mainloop()