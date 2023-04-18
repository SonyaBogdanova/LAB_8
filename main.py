"LAB_8"

def p1():
    import PIL
    from PIL import Image

    filename = "card.jpg"
    with Image.open(filename) as img:
        img.load()

    img_change = img.rotate(-45, Image.BICUBIC, True)
    img_change = img_change.crop((250, 167, 520, 250))
    img_change.show()

    img_change.save('C:/LAB_8/card_card_change.jpg')

def p2():
    import PIL
    from PIL import Image

    print('\n', "Открытку какого праздника Вы хотите увидеть?:")
    print('\n','День Защитника Отечества = Наберите "23"','\n','Международный женский День = Наберите "8"',
        '\n', 'День Рождения = Наберите "1"', '\n', 'День Космонавтики = Наберите "2"', '\n', 'Новый Год = Наберите "3"', '\n')

    dict = {23: '23.jpg', 8: 'WD.jpg', 1: 'ДР.jpg', 2: 'ДК.jpg', 3: 'НГ.jpg'}

    answer = int(input("Ваш ответ: "))

    filename = dict[answer]
    with Image.open(filename) as img:
        img.load()
    img.show()

def p3():
    import PIL
    from PIL import Image, ImageFont, ImageDraw

    filename = "card.jpg"
    with Image.open(filename) as img:
        img.load()

    x = input("Кого хотите поздравить?: ")
    word = '\n', x + ',' + '\n', 'Поздравляю!'
    word_fix = ' '.join(word)

    z = ImageDraw.Draw(img)
    font = ImageFont.truetype("PT-Root-UI_VF.ttf", 80)

    font.get_variation_names()
    [b'Regular', b'Bold', b'Light', b'Medium']
    font.set_variation_by_name('Bold')

    z.text((-9, 200), word_fix, fill=(218, 74, 0), font=font)
    img.show()
    img.save('C:/LAB_8/card_with_text.png')

p1(), p2(), p3()

