# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# Примеры:
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# --------
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# --------
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

encoded_val = rle_encode('aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa')
print(encoded_val)

# Модуль восстановления
# def rle_decode(data):
#     decode = ''
#     count = ''
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decode += char * int(count)
#             count = ''
#     return decode

# decoded_val = rle_decode('6A1F2D7C1A17E')
# print(decoded_val)

# # Разбор д/з

# from itertools import groupby, starmap
# from os import path


# def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
#     if path.exists(text) and path.exists(code_text):
#         with open(text) as my_f_1, \
#                 open(code_text, "a") as my_f_2:
#             for i in my_f_1:
#                 my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
#     else:
#         print("The files do not exist in the system!")


# def rle_decode(name):
#     if path.exists(name):
#         with open(name) as my_f:
#             n = ""
#             for k in my_f:
#                 word_nums = []
#                 for i in k.strip():
#                     if i.isdigit():
#                         n += i
#                     else:
#                         word_nums.append([int(n), i])
#                         n = ""
#                 print("".join(starmap(lambda x, y: x * y, word_nums)))
#     else:
#         print("The files do not exist in the system!")

# # def rle_decode(name):
# #     if path.exists(name):
# #         with open(name) as my_f:
# #             for i in my_f:
# #                 word_nums = ["".join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
# #                 print("".join([f"{int(word_nums[i]) * word_nums[i + 1]}" for i in range(0, len(word_nums), 2)]))
# #     else:
# #         print("The files do not exist in the system!")

# # aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
# rle_decode(input("Enter the name of the file to decode: "))