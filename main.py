sa = ["asda", "sas", "dsfsd"]
print(sa)

for item in sa:
    print(item)

# import tkinter as tk
# from tkinter import ttk
#
# def button_click(number):
#     print(number)
#     if number == "C":
#         clear()
#     else:
#         current = entry.get()
#         print(current)
#
#         if current.startswith("Error"):
#             print("should be cleared")
#             clear()
#             return
#         entry.delete(0, tk.END)
#         entry.insert(0, current + str(number))
#
#
# def clear():
#     entry.delete(0, tk.END)
#
#
# def calculate():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(0, result)
#     except:
#         entry.delete(0, tk.END)
#         entry.insert(0, "Error")
#
#
# app = tk.Tk()
# app.title("Calculator")
#
# entry = tk.Entry(app, width=20, font=('Arial', 20))
# entry.grid(row=0, column=0, columnspan=4)
#
# Buttons = [
#
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
# ]
#
# for (text, row, col) in Buttons:
#     tk.Button(app, text=text, padx=20, pady=20, font=('Arial', 15), bg='red',
#               command=lambda t=text: button_click(t) if t != '=' else calculate() if t != 'C' else clear()) \
#         .grid(row=row, column=col)
#
# app.mainloop()
