class StringUtils:
    def __init__(self, value):  # Constructor
        self.value = value

    def display(self):  # Method
        print(self.value)


def remove_vowels(string):
    string_without_vowels = ''.join(char for char in string if char not in 'aeiouAEIOU')
    return string_without_vowels
