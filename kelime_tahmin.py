import random
import tkinter as tk

puan = int(5)

teknoloji = ("saat", "telefon", "mönitor", "priz", "bilgisayar", "klavye", "maus", "ampul", "tripod")
eşya = ("masa", "koltuk", "sandalye", "çekmece", "gözlük", "perde", "cam", "çanta", "kalorifer")

klas_belirlendi = False
klas_tahmin = False

def check_if_prediction_true(prediction, value):
    correct_letters = []
    for pred in prediction:
        if pred in value and pred not in correct_letters:
            correct_letters.append(pred)
    return correct_letters

while not klas_belirlendi:
    klas = input("teknolojyile alakalı oynamak isterseniz teknoloji yazınız, eşyalarla iligi oynamak isterseniz eşya yazınız: ")
    if klas.lower().strip() == "eşya":
        klas_belirlendi = True
        random_item = random.choice(eşya)
    elif klas.lower() == "teknoloji":
        klas_belirlendi = True
        random_item = random.choice(teknoloji)
    else:
        print("lütfen düzgün yazdığınızdan emin olun")

value = random_item

tahmin = input("tahmin yapın: ").lower().strip()

correct_letters = check_if_prediction_true(tahmin, value)

while not klas_tahmin:
    if puan >= 30:
        print("oyunu kazandın ")
        klas_tahmin = True
    elif tahmin == value:
        klas_belirlendi = False
        print("doğru bildin")
        puan += 5
        print(puan)
    while not klas_belirlendi:
            klas = input("teknolojyile alakalı oynamak isterseniz teknoloji yazınız, eşyalarla iligi oynamak isterseniz eşya yazınız: ")
            if klas.lower().strip() == "eşya":
                klas_belirlendi = True
                random_item = random.choice(eşya)
            elif klas.lower().strip() == "teknoloji":
                klas_belirlendi = True
                random_item = random.choice(teknoloji)
            else:
                print("lütfen düzgün yazdığınızdan emin olun")
    else:
        puan -=1
        print(puan)
        print("Doğru Harfler:", correct_letters)
        tahmin = input("Yanlış tahmin lütfen tekrar deneyin: ")
        correct_letters = check_if_prediction_true(tahmin, value)









