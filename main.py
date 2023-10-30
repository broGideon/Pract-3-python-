import datetime
import csv
import keyboard
import os
import glob
from xlsxwriter.workbook import Workbook
import json

Weapon = ["Ничего","Ничего"]
Equipment = ["меч", "катану", "лук и стрелы", "старую кольчугу"]
Counter = {"Enemies defeated": 0, "Weapons found": 0}
Adventure = {''}


def Input1():
    a = 0
    while (a != 1 or a != 2):
        try:
            a = int(input())
            if a > 0 and a < 3:
                return a
            else:
                print('Введите корректное значение')
        except ValueError:
            print('Введите корректное значение')


def Input2():
    a = 0
    while (a != 1 or a != 2 or a != 3):
        try:
            a = int(input())
            if a > 0 and a < 4:
                return a
            else:
                print('Введите корректное значение')
        except ValueError:
            print('Введите корректное значение')


def save(room):
    data = {
        "Room": room,
        "Weapon1": Weapon[0],
        "Weapon2": Weapon[1],
        "Counter_Enemies": Counter['Enemies defeated'],
        "Counter_Weapons": Counter['Weapons found']
    }
    with open("input.json", 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4)
    return

def del_save():
    data = {
        "Room": 0,
        "Weapon1": "Ничего",
        "Weapon2": "Ничего",
        "Counter_Enemies": 0,
        "Counter_Weapons": 0
    }
    with open("input.json", 'w', encoding= 'utf8') as file:
        json.dump (data, file,indent=4)
    return
def end(end):
    if os.path.exists('aaa.csv') == False:
        my_file = open("aaa.csv", "w+")
        my_file.close()
    dt_now = datetime.datetime.now()
    current_time = dt_now.strftime("%H:%M:%S")
    fieldnames = ['Time', 'Enemies defeated', 'Weapons found', 'Ending']
    dict = {'Time': current_time, 'Enemies defeated': Counter['Enemies defeated'],
            'Weapons found': Counter['Weapons found'], 'Ending': end}
    if fieldnames[0] in open('aaa.csv', ).read():
        with open('aaa.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writerow(dict)
    else:
        with open('aaa.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerow(dict)

    for csvfile in glob.glob(os.path.join('.', '*.csv')):
        workbook = Workbook(csvfile[:-5] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    exit()


def twelve_room():
    save(12)
    print("\033[38m======================================================")
    print("Войдя в комнату, вы увидели настоящего огра\nОн вас не заметил\nХотите напасть на него неожиданно?")
    print("\033[38m======================================================")
    print("\033[31m               1. Да\n               2. Вернусь лучше обратно")
    print("\033[38m======================================================")
    Adventure.add("огр")
    match (Input1()):
        case 1:
            if Weapon[0] == Equipment[1] and Weapon[1] == Equipment[3]:
                print(
                    "Вы достаёте катану и нападаете на огра\nОн вас ударяет, но броня защищает вас\nОгр побеждён\nДалее вы видите проход дальше")
                Counter["Enemies defeated"] += 1
                print("\033[38m======================================================")
                print("\033[31m        Для продолжения нажмите пробел")
                print("\033[38m======================================================")
                keyboard.wait(' ')
                print(
                    "\033[34mВойдя в проход, вы видите свет\nЭто выход\nВы радостно бежите на выход\nПоздраляю вы победили")
                print(
                    f"\033[34mВрагов побеждено: {Counter['Enemies defeated']}\nЭкипировки найдено {Counter['Weapons found']}")
                print("\033[34mВо время приключения вам встретились", Adventure)
                del_save()
                end(end='Win')
            elif Weapon[0] == Equipment[1]:
                print(
                    "Вы достаёте катану и нападаете на огра\nОн вас ранит, но вам удаётся его победить\nДалее вы видите проход дальше")
                Counter["Enemies defeated"] += 1
                print("\033[38m======================================================")
                print("\033[31m        Для продолжения нажмите пробел")
                print("\033[38m======================================================")
                keyboard.wait(' ')
                print(
                    "\033[34mВойдя в проход, вы видите свет\nЭто выход\nВы радостно прихрамовая идёте на выход\nПоздраляю вы победили")
                print(
                    f"\033[34mВрагов побеждено: {Counter['Enemies defeated']}\nЭкипировки найдено {Counter['Weapons found']}")
                print("\033[34mВо время приключения вам встретились", Adventure)
                del_save()
                end(end='Win')
            elif Weapon[0] == Equipment[2]:
                print("Вы стреляете из лука и попадаете в голову\nОгр падает замертво\nДалее вы видите проход дальше")
                Counter["Enemies defeated"] += 1
                print("\033[38m======================================================")
                print("\033[31m        Для продолжения нажмите пробел")
                print("\033[38m======================================================")
                keyboard.wait(' ')
                print(
                    "\033[34mВойдя в проход, вы видите свет\nЭто выход\nВы радостно бежите на выход\nПоздраляю вы победили")
                print(
                    f"\033[34mВрагов побеждено: {Counter['Enemies defeated']}\nЭкипировки найдено {Counter['Weapons found']}")
                print("\033[34mВо время приключения вам встретились", Adventure)
                del_save()
                end(end='Win')
            else:
                print(
                    "\033[33mВы достаёте меч, но вам не удаётся пробить толстую шкуру противника\nВы умели\nВ следующи раз повезёт больше :)")
                print("\033[38m======================================================")
                del_save()
                end(end='Loss')
        case 2:
            ten_room2()


def eleven_room():
    save(11)
    print(
        "Вы долга протискиваетесь сквозь проход и в конце попадаете в комнату\nИсследовав её вы нашли катану\nОна выглядит практически новой\nБерём?")
    print("\033[38m======================================================")
    print("\033[31m             1. Да\n             2. Нет")
    print("\033[38m======================================================")
    match (Input1()):
        case 1:
            print("Японцы делают отличное оружие\nЯ думаю катана будет надёжнее моего оружия")
            Weapon.insert(0, Equipment[1])
            Weapon.pop(1)
            Counter["Weapons found"] += 1
        case 2:
            print("Моё оружие и так меня устраивает")
    print("\033[38m======================================================")
    print("\033[31m      Для возвращения обратно нажмите пробел")
    print("\033[38m======================================================")
    keyboard.wait(" ")
    ten_room2()


def ten_room1():
    save(10)
    print("\033[38m======================================================")
    print("Войдя в комнату вы видите следующий проход, а справа от него щель,\nв которую сможет протиснуться человек")
    ten_room2()


def ten_room2():
    print("\033[38m======================================================")
    print("\033[31m            1. Пойти в проход\n            2. Исследовать, что находится в щели")
    print("\033[38m======================================================")
    match (Input1()):
        case 1:
            twelve_room()
        case 2:
            eleven_room()


def nine_room():
    save(9)
    print(
        f"Войдя в комнату, вы замечаете, что свет исходил от факела\nНо при осмотре комнаты вы нашли {Equipment[2]}\nСтоит ли поменять {Weapon[0]} на {Equipment[2]}")
    print("\033[38m======================================================")
    print("\033[31m                 1. Да\n                 2. Нет")
    print("\033[38m======================================================")
    match (Input1()):
        case 1:
            print("В закрытом пространстве лук эфективнее меча")
            Weapon.insert(0, Equipment[2])
            Weapon.pop(1)
            Counter["Weapons found"] += 1
        case 2:
            print("Меч будет полезнее лука")
    print("\033[38m======================================================")
    print("\033[31m      Для возвращения обратно нажмите пробел")
    print("\033[38m======================================================")
    keyboard.wait(" ")
    eight_room2()


def eight_room1():
    save(8)
    print("Вы заходите в комнату и видите скелета\nВдруг он неожиданно нападает на вас")
    Adventure.add("скелет")
    if Weapon[0] != "меч":
        print(
            "\033[33mВы отчаянно пытаетесь победить врага, но ничего не получается\nВы умерли\nВ следующий раз повезёт больше :)")
        print("\033[38m======================================================")
        save(7)
        end(end='Death by skeleton')
    else:
        print(f"Вы достаёте {Weapon[0]} и побеждаете врага это успех ")
        Counter["Enemies defeated"] += 1
        print("")
        print("Далее вы увидели два прохода\nВ левом проходе вы заметили странное свечение")
        eight_room2()


def eight_room2():
    print("\033[38m======================================================")
    print("\033[31m           1. Пойти в левый проход\n           2. Пойти в правый проход")
    print("\033[38m======================================================")
    match Input1():
        case 1:
            nine_room()
        case 2:
            ten_room1()


def seven_room():
    save(7)
    print("Вы идёте по длинному коридору и чувствуете какой-то ветерок, но ,дойдя до конца, вы упираетесь в завал")
    print("\033[38m======================================================")
    print("\033[31m       Для возвращения назад нажмите пробел")
    print("\033[38m======================================================")
    keyboard.wait(' ')
    six_room2()


def six_room1():
    save(6)
    print("Вы входите в комнату и видите человека сидящего в углу\nЧто же делать?")
    print("\033[38m======================================================")
    print("\033[31m           1. Подойти к нему\n           2. Не обращать внимание и идти дальше")
    print("\033[38m======================================================")
    Adventure.clear()
    Adventure.add("труп")
    if (Input1() == 1):
        print("Вы подошли к человеку и поняли, что он уже мёртв\nЧтож нужно не повторить его судьбу")
    else:
        print("Слишком страшно к нему подходить лучше пойду дальше")
    six_room2()


def six_room2():
    print("Перед вами два прохода\nКакой предпочтёте?")
    print("\033[38m======================================================")
    print("\033[31m              1. Левый\n              2. Правый")
    print("\033[38m======================================================")
    match (Input1()):
        case 1:
            seven_room()
        case 2:
            eight_room1()


def five_room():
    save(5)
    print(f"Войдя в комнату вы заприметили {Equipment[0]}\nНехотите прихватить его на всякий случай?")
    print("======================================================")
    print("\033[31m               1. Взять\n               2. Оставить")
    print("\033[38m======================================================")
    match (Input1()):
        case 1:
            Weapon[0] = Equipment[0]
            Counter["Weapons found"] += 1
            print("Надеюсь он не понадабится")
            print("\033[38m======================================================")
        case 2:
            print("Ну как знаешь")
            print("\033[38m======================================================")
    print("\033[31m        Для выхода из комнаты нажмите пробел")
    print("\033[38m======================================================")
    keyboard.wait(' ')
    three_room()


def four_room():
    save(4)
    print("Войдя в комнату, в видите живого скелета\nЧто же делать?")
    print("\033[38m======================================================")
    print("\033[31m             1. Принять бой\n             2. Бежать")
    print("\033[38m======================================================")
    Adventure.add("скелет")
    match (Input1()):
        case 1:
            if Weapon[0] == "меч":
                print("Вы победили, но комната оказалась тупиковой")
                print("\033[38m======================================================")
                print("\033[31m      Для возвращения обратно нажмите пробел")
                print("\033[38m======================================================")
                Counter["Enemies defeated"] += 1
                keyboard.wait(' ')
                three_room()
            else:
                print("\033[33mВы умерли\nВ следующий раз повезёт больше :)")
                print("\033[38m======================================================")
                end(end='Death by skeleton')
        case 2:
            three_room()


def three_room():
    save(3)
    print("Далее вы увидели три прохода\nВ какой же пойти")
    print("======================================================")
    print(
        "\033[31m          1. Пойти в проход слева\n          2. Пойти в проход посередине\n          3. Пойти в проход справа ")
    print("\033[38m======================================================")
    match (Input2()):
        case 1:
            five_room()
        case 2:
            six_room1()
        case 3:
            four_room()


def two_room():
    save(2)
    print("Вы вошли в комнату, но там ничего не нашли кроме костей и прохода дальше")
    print("\033[38m======================================================")
    print("\033[31m                1. Пойти туда\n                2. Вернуться")
    print("\033[38m======================================================")
    match (Input1()):
        case 1:
            print("\033[38m======================================================")
            print(f"При входе в комнату вы заметили  {Equipment[3]}\nСтоит ли её надевать?")
            print("\033[38m======================================================")
            print("\033[31m                1. Да\n                2. Нет")
            print("\033[38m======================================================")
            match (Input1()):
                case 1:
                    print("Я не знаю, что меня ждёт дальше")
                    print("Броня точно не помешает")
                    print("\033[38m======================================================")
                    Weapon[1] = (Equipment[3])
                    Counter["Weapons found"] += 1
                case 2:
                    print("Вдруг это ловушка, пойду лучше обратно")
                    print("\033[38m======================================================")
            print("\033[31m Для возвращения в изначальную комнату нажмите пробел ")
            print("\033[38m======================================================")
            keyboard.wait(' ')
            one_room()
        case 2:
            one_room()


def one_room():
    save(1)
    print("\033[31m           1. Пойти в проход слева\n           2. Пойти в проход справа")
    print("\033[38m======================================================")
    match Input1():
        case 1:
            three_room()
        case 2:
            two_room()


def game():
    print("======================================================")
    print(
        "Вы проснулись на холодном полу в какой-то пещере \nПоследнее воспоминание как вы проволились в какую-то яму\nНужно как-то выбраться от сюда")
    print("Нужно обыскать комнату")
    print("======================================================")
    print("\033[31m                Нажмите пробел")
    print("\033[38m======================================================")
    keyboard.wait(' ')
    print("В комнате вы находите факел")
    print("Чтож пора выбираться из этой дыры")
    print("\033[38m======================================================")
    one_room()

if os.path.exists('input.json'):
    with open("input.json", 'r', encoding='utf8') as file:
        json_dict = json.load(file)
    if json_dict["Room"] != 0:
        print("Хотите продолжить с контрольной точки?\n1. Да\n2. Нет")
        if (Input1() == 1):
            Weapon[0] = json_dict["Weapon1"]
            Weapon[1] = json_dict["Weapon2"]
            print(Weapon)
            Counter['Enemies defeated'] = json_dict["Counter_Enemies"]
            Counter['Weapons found'] = json_dict["Counter_Weapons"]
            match json_dict["Room"]:
                case 1:
                    one_room()
                case 2:
                    two_room()
                case 3:
                    three_room()
                case 4:
                    four_room()
                case 5:
                    five_room()
                case 6:
                    six_room1()
                case 7:
                    seven_room()
                case 8:
                    eight_room1()
                case 9:
                    nine_room()
                case 10:
                    ten_room1()
                case 11:
                    eleven_room()
                case 12:
                    twelve_room()
        else:
            del_save()
            game()
game()
