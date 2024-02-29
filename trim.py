# Отсчет окончания числительного
# u_i = int(input())



# def conj_ending(num):
#     last_two_digits = num % 100
#     if num % 10 in {6, 7, 8, 9, 0} or last_two_digits in {11, 12, 13, 14, 15, 16, 17, 18, 19}:
#         return "комментариев"
#     elif num % 10 in {2, 3, 4}: 
#         return "комментария"
#     elif num % 10 == 1:
#         return "комментарий"

# print (conj_ending(u_i))

# u_i = input()

# def count(str):
#     letters = 0
#     numbers = 0
#     special = 0
    
#     for char in str:
#         if char.isdigit():
#             numbers += 1
#         elif char.isalpha():
#             letters += 1
#         else: 
#             special += 1
#     return letters, numbers, special

# letters, numbers, special = count(u_i)

# print (letters)
# print (numbers)
# print (special)

# u_i = input()

# def compressor(s):
#     count = 1
#     string = ""
#     for i in range(len(s)):
#         if i + 1 < len(s) and s[i] == s[i + 1]:
#             count += 1
#         else:
#             string += s[i] + str(count)
#             count = 1
    
#     return string


# print(compressor(u_i)) 


# u_i = input()

# def stat (s):
#     res = {}
#     lowered_s = [l.lower() for l in s if l.isalpha()]
#     for char in lowered_s:
#         if char in res:
#             res[char] += 1
#         else:
#             res[char] = 1
#     return res


            
# res = (stat(u_i))

# pr = []

# for key, value in res.items():
#     pr.append((key, value))

# res = sorted(pr)
# res = dict(res)
# for key, value in res.items():
#     print(f"{key} {value}")

# u_i = input()

# def unique(s):
#     res = {}
#     words = s.split()
#     for word in words:
#         word = word.lower()
#         if word.isalpha() and word not in res:
#             res[word] = None
#     res = list(res.keys())
#     return res
# res = unique(u_i)
# res = ' '.join(res)
# print (res)

# u_i = input()
# def find_anagrams(s):
#     words = s.split()
    
#     anagrams = {}
    
#     for word in words:
#         sorted_word = ''.join(sorted(word.lower()))
        
#         if sorted_word in anagrams:
#             anagrams[sorted_word].append(word.lower())
#         else:
#             anagrams[sorted_word] = [word.lower()]
    
#     for group in sorted(anagrams.values()):
#         if len(group) > 1:
#             for pair in sorted(group):
#                 print(pair, end=' ')
#             print()  

# find_anagrams(u_i)

# def transliterator(s):
#     char_change = {
#         'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z',
#         'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
#         'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
#         'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia',
#         'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
#         'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
#         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
#         'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia',
#         'ъ': '', 'ь': ''
#     }
#     s_new = ""
#     for char in s:
#         s_new += char_change.get(char, char)
#     return s_new

# u_i = input()

# print (transliterator(u_i))


# def filter_words(words, combination):
#     keypad = {
#         '2': 'абвг',
#         '3': 'дежз',
#         '4': 'ийкл',
#         '5': 'мноп',
#         '6': 'рсту',
#         '7': 'фхцч',
#         '8': 'шщъы',
#         '9': 'ьэюя'
#     }
    
#     chars = set()
#     for digit in combination:
#         chars.update(keypad.get(digit, ''))
    
#     filtered_words = [word for word in words if word[0] in chars]
#     return filtered_words

# words = input().split()
# combination = input()

# s = filter_words(words, combination)

# print(' '.join(s))


# def t9(words, digits):
#     letters_of_dig = [' ', '.,-', 'абвг', 'дежз', 'ийкл', 'мноп', 'рсту', 'фхцч', 'шщъы', 'ьэюя']
#     return ' '.join(filter(lambda w: all(map(lambda let, dig: let.lower() in letters_of_dig[dig], w, digits)), words))
 
# words = input().split()
# *digits, = map(int, input())
# print(t9(words, digits))


# def medium(str):
#     number = str.split()
#     not_zero = [int(num) for num in number if num != '0']

#     print (not_zero)

#     if not_zero:
#         avg = sum(not_zero) / len(not_zero)
#         return int(avg) if int(avg) == avg else round(avg, 1)

# u_i = input ()

# print (medium(u_i))


# def longest_word (str):
    
#     words = str.split()

#     lw = ""

#     for w in words:
#         if len(w) > len (lw):
#             lw = w
#     return lw
# u_i = input()

# print (longest_word(u_i))

# def longest_unique_substring(s):
#     if not s:
#         return ""
    
#     max_substring = s[0]
#     current_substring = s[0]
#     visited = set(s[0])

#     for char in s[1:]:
#         if char not in visited:
#             current_substring += char
#             visited.add(char)
#         else:
#             if len(current_substring) > len(max_substring):
#                 max_substring = current_substring
#             index = current_substring.index(char)
#             current_substring = current_substring[index+1:] + char
#             visited = set(current_substring)

#     if len(current_substring) > len(max_substring):
#         max_substring = current_substring

#     return max_substring

# u_i = input()

# print(longest_unique_substring(u_i)) 

# from collections import Counter

# mlst = []

# mystrg = input()
# x = Counter(mystrg)
# elements = x.values()
# for item in elements:
#     mlst.append(item)
# if sum(mlst)//min(mlst) == len(mlst):
#     print(True)
# elif sum(mlst)-1//min(mlst) == len(mlst):
#     print(True)
# else:
#     print(False)

# def roman_to_integer(s):
#     roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     prev_value = 0
    
#     for char in s[::-1]:
#         value = roman_dict[char]
#         if value < prev_value:
#             result -= value
#         else:
#             result += value
#         prev_value = value
        
#     return result

# u_i = input()

# print (roman_to_integer(u_i))

# import re 

# def check_password(password):
#     if len(password) < 6 or len(password) > 12:
#         return False
    
#     if not re.search(r'[a-z]', password):
#         return False
    
#     if not re.search(r'[A-Z]', password):
#         return False
    
#     if not re.search(r'[0-9]', password):
#         return False
    
#     if not re.search(r'[@#$%^&+=]', password):
#         return False
    
#     return True

# password = input()
# check_password(password)



    
    
# import re
    
# x = input()
# my_patterns_check = [
#     re.fullmatch(r'rgb\((?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])(?:,(?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])){2}\)', x),
#     re.fullmatch(r'rgb\((?:\d{1,2}(?:\.\d+)?|100(?:\.0+)?)%(?:,(?:\d{1,2}(?:\.\d+)?|100(?:\.0+)?)%){2}\)', x),
#     re.fullmatch(r'rgba\((?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])(?:,(?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])){2},(?:0(?:\.\d+)?|1(?:\.0+)?)\)', x),
# ]

# if any(my_patterns_check):
#         print(True)
# else:
#         print(False)

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # Создание виджетов
        self.left_menu_widget = QWidget()
        self.main_content_widget = QWidget()

        # Создание левого бокового меню
        self.left_menu_layout = QVBoxLayout(self.left_menu_widget)
        self.left_menu_layout.addWidget(QPushButton("File 1"))
        self.left_menu_layout.addWidget(QPushButton("File 2"))
        # Добавьте другие кнопки для файлов по вашему усмотрению

        # Создание основного контента
        self.main_content_layout = QVBoxLayout(self.main_content_widget)
        self.main_content_label = QLabel("Добавьте файлы")
        self.main_content_layout.addWidget(self.main_content_label)

        # Размещение виджетов на главном окне
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.left_menu_widget)
        main_layout.addWidget(self.main_content_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Подключение сигналов и слотов (если необходимо)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()