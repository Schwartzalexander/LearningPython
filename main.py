from flask import Flask

from rest.blog import blog_blueprint
from rest.order import order_blueprint
from rest.user import user_blueprint
from string_utils import StringUtils


def print_hi(name):
    print(f'Hi, {name}!')  # Press Strg+F8 to toggle the breakpoint.


def is_main_module():
    return __name__ == '__main__'


def first_letter_upper_case(name):
    return name[0].upper() + name[1:]


app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(order_blueprint, url_prefix='/order')
app.register_blueprint(blog_blueprint, url_prefix='/blog')

app.run(debug=True)

# compex1 = 1+1j
# compex2 = 2+2j
# print(compex1)
# print(compex2)
# print(compex1+compex2)
# print(compex1*compex2)
# complex3 = 1j
# complex4 = 1j
# result_complex = complex3 * complex4
# result_int = int(result_complex.real)
# print(result_int)
# numberstring='2'
# print(int(numberstring))
# print(800*numberstring)
ten = 10

# my_sequence=[ten, 20, 30, 40, 50]
# another_sequence=[*my_sequence, 60]
# print(another_sequence[0])
# my_range=range(ten, 100, ten)
# print(my_sequence)
# print(my_range)
# print(my_sequence[-1])
# print(my_range[-1])
# for i in my_range:
#     print_hi(i)
# my_slice=my_range[0:5:2]
# for i in my_slice:
#     print(i)


# if is_main_module():
#     print_hi('PyCharm')
# for i in range(5):
#     print(i)
# for i in [41, 42, 43]:
#     print(i)
# for i in ("foo", 42, 3.14):
#     print(i)
# for i in range(0, 9, 2):
#     print(i)
# hello = "hello"
# for char in hello:
#     print(char)
# print(hello[2])
# result=2**4
# print(result)
# print(bin(~0))
# command = input("What are you doing next? ")
# [action, obj] = command.split()
# print(action)
# print(obj)
# wild_range = range(6, 36, 3)
# print(wild_range)
# print(list(wild_range))
# wild_slice = wild_range[36:0:-1]
# print(wild_slice)
# print(list(wild_slice))
# my_dict = {'a': 1, 'b': 2}
# my_dict2 = {0: 1, 1: 2}
# my_dict3 = {0.1: 1, (1 + 2j): 2, ten: 3, 5: 5 ** 55}
# print(my_dict)
# print(my_dict2)
# print(my_dict3)
# print_hi(my_dict3[ten])
# print_hi(my_dict3[10])
# ten = 5
# print_hi(my_dict3[10])
# print_hi(my_dict3[5])
# my_set = {'anton', 'peter'}
# for name in my_set:
#     print_hi(first_letter_upper_case(name))
# s = """This is a
#     multiline
#        string."""
#
# for line in s.splitlines():
#     print(repr(line))
# bytearray = s.encode()
# print(bytearray)
# for byte in bytearray:
#     print(byte)
#     hexValue = hex(byte)
#     print_hi(hexValue)
# print(bytearray.hex())
# hex_string = '5468697320697320610a202020206d756c74696c696e650a20202020202020737472696e672e'
# # Converting the hex string to bytes
# bytes_from_hex = bytes.fromhex(hex_string)
# string_from_hex = bytes_from_hex.decode()
# print(string_from_hex)
# result = 0 and 5  # 0 is falsy
# print(result)  # Output: 0 (not False)
# result = "Hello" or 5  # "Hello" is truthy
# print(result)  # Output: "Hello" (not True)

# def square(i):
#     return i * i
#
#
# squares = [square(i) for i in range(100) if i % 2 == 0]
# print(squares)
#
# sentence = 'the rocket came back from mars'
# vowels = [i for i in sentence if i not in 'aeiou']
# print(vowels)
#
# user_string = input("Give me a string, dude!")
# print(remove_vowels(user_string))
obj = StringUtils("test")
obj.display()
