import random

# TODO: webten scrapleyerek kelime listesi oluştur
teknoloji = ["saat", "telefon", "mönitor", "priz", "bilgisayar", "klavye", "maus", "ampul", "tripod"]
esya = ["masa", "koltuk", "sandalye", "çekmece", "gözlük", "perde", "cam", "çanta", "kalorifer"]
game_point = 5


def get_correct_letters(prediction, value):
    correct_letters = []
    for pred in prediction:
        if pred in value and pred not in correct_letters:
            correct_letters.append(pred)
    return correct_letters


def get_category():
    category = input("hangi katagoride oynamak istiyorsunuz").lower().strip()
    if category == "teknoloji":
        return random.choice(teknoloji)
    elif category == "eşya":
        return random.choice(esya)
    else:
        return get_category()


while 0 < game_point < 30:
    goal_word = get_category()
    print(goal_word)
    goal_found = False
    while not goal_found:
        prediction = input("tahmin ediniz")
        if prediction == goal_word:
            game_point += 5
            print("kelimeyi buldunuz")
            goal_found = True
        else:
            game_point -= 1
            print(get_correct_letters(prediction, goal_word))

        print(game_point)
if game_point >= 30:
    print("oyunu kazandınız")
else:
    print("oyunu kaybettiniz")
