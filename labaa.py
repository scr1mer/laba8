import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from random import randint

def generate_random_numbers(num_numbers, min_val=1, max_val=1000):
    return [randint(min_val, max_val) for _ in range(num_numbers)]

def write_numbers_to_file(filename, numbers):
    with open(filename, "w") as f:
        f.write(" ".join(map(str, numbers)))

def calculate_average_from_file(filename):
    try:
        with open(filename, 'r') as f:
            line = f.readline().strip()
            if line:
                numbers = list(map(int, line.split()))
                return sum(numbers) / len(numbers)
            else:
                return None  # Handle empty file
    except FileNotFoundError:
        return None
    except ValueError:
        return None  # Handle invalid data in file
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def create_gui_section(parent, title, functions, labels):
    section_label = tk.Label(parent, text=title, font=("Helvetica", 16))
    section_label.pack(pady=10)
    for i, (func, label_text) in enumerate(zip(functions, labels)):
        label = tk.Label(parent, text=label_text)
        label.pack()
        entry = tk.Entry(parent)
        entry.pack()
        button = ttk.Button(parent, text="Выполнить", command=lambda f=func, e=entry: f(e))
        button.pack(pady=5)
        result_label = tk.Label(parent, text="")
        result_label.pack()



window = tk.Tk()
window.title("Лабораторная работа 6")

# Лабораторная 1
def lab1_func(entry):
    name = entry.get()
    messagebox.showinfo("Результат", f"Здравствуйте, {name}!")

create_gui_section(window,"Лабораторная №1",[lab1_func],["Введите Ваше имя"])


# Лабораторная 2
def lab2_func(entry):
    try:
        nums = list(map(int, entry.get().split(',')))
        if len(nums) !=2:
            raise ValueError("Введите два числа через запятую")
        a, b = nums
        result = f"{a}+{b}={a+b}, {a}-{b}={a-b}, {a}*{b}={a*b}, {a}^{b}={a**b}"
        if a != 0 and b != 0:
            result += f", {a}/{b}={a/b}, {a}//{b}={a//b}, {a}%{b}={a%b}"
        messagebox.showinfo("Результат", result)
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

create_gui_section(window,"Лабораторная №2",[lab2_func],["Введите два числа через запятую"])


# Лабораторная 3
def lab3_func(entry):
    try:
        min_val, max_val = map(int, entry.get().split(','))
        numbers = generate_random_numbers(10, min_val, max_val)
        result = (f"Случайные числа: {numbers}\n"
                  f"Сортировка по возрастанию: {sorted(numbers)}\n"
                  f"Сортировка по убыванию: {sorted(numbers, reverse=True)}\n"
                  f"Минимум: {min(numbers)}\n"
                  f"Максимум: {max(numbers)}\n"
                  f"Сумма: {sum(numbers)}")
        messagebox.showinfo("Результат", result)
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

create_gui_section(window,"Лабораторная №3",[lab3_func],["Введите минимальное и максимальное число через запятую"])



# Лабораторная 4
def lab4_func(entry):
    filename = filedialog.askopenfilename()
    if filename:
        average = calculate_average_from_file(filename)
        if average is not None:
            messagebox.showinfo("Результат", f"Среднее арифметическое: {average}")
        else:
            messagebox.showwarning("Предупреждение", "Ошибка при обработке файла.")

create_gui_section(window,"Лабораторная №4",[lab4_func],["Выберите файл"])



# Лабораторная 5
def lab5_func(entry):
    try:
      name, age, money = entry.get().split(',')
      class cs:
          def __init__(self, name, age, money):
              self.name = name
              self.age = age
              self.money = money

          def abb(self):
              return f"Погоняло: {self.name}. Стаж воровства: {self.age} лет."

      class ggg(cs):
          def app(self):
              return f"Ворует в месяц: {self.money}."

      qwerty = ggg(name, age, money)
      res = f"{qwerty.abb()}\n{qwerty.app()}"
      messagebox.showinfo("Результаты", res)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите данные через запятую: name,age,money")


create_gui_section(window,"Лабораторная №5",[lab5_func],["Введите данные через запятую: name,age,money"])


window.mainloop()
