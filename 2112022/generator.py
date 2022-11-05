import numbers
import string
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
from captcha.image import WheezyCaptcha
from random import choice
from PIL import Image

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_random_string(length=int):
    str = ''
    for i in range(length):
        str += choice(numbers)
    return str

def get_captcha_image(length=int):
    image = ImageCaptcha(120, 100)
    # s = get_random_string(length)
    s = "0123"
    # image = image.create_captcha_image("1234", color=BLACK, background=WHITE)
    # image.save('out.jpg')
    # print(image)
    image.write(s, 'out.jpg')
    return s
    # print(s)
    # return image.generate(s)
    # data = image.generate(s)
get_captcha_image(4)