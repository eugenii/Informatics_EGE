# v1_15  # 36
# A = 1
# while True:
#     for x in range(1, 12 * 18 + 1):
#         z1 = int(x % 12 == 0)
#         z2 = int(x % 18 == 0)
#         z3 = int(x % A == 0)
#         if (not z1 or not z2) <= int(not z3):
#             continue
#         else:
#             break
#     else:
#         break
#     A += 1
# print(A)

# v2_15
# A = 0
# while True:
#     for x in range(61):
#         for y in range(31):
#             if x + 2 * y != 60 or A < y or y < x:
#                 continue
#             else:
#                 break
#         else:
#             continue
#         break
#     else:
#         A += 1
#         continue
#     break
#     
# print(A)

# v3_15
# решается преобразованием выражения и отмечанием всех необходимых значений А
# для перекрытия ВСЕХ возможных х

# v4_15
# A = 0
# while True:
#     for x in range(45 * 33 +10):
#         if ((x & 45 != 0) and (x & A == 0)) <= (x & 33 != 0):
#             continue
#         else:
#             break
#     else:
#         break
#     A += 1
# print(A)

# v6_15
# A = 1
# while True:
#     for x in range(1000):
#         for y in range(1000):
#             if (x * y < A) or (x > y) or (y >= 9):
#                 continue
#             else:
#                 break
#         else:
#             continue
#         break
#     else:
#         break
#     A += 1

# v7_15  ====================

# A = 1
# while True:
#     for x in range(1, 240):
#         z1 = int(A <= 30)
#         z2 = int(x % 8 == 0)
#         z3 = int(x % A != 0)
#         z4 = int(x % 10 != 0)
#         if z1 and (z2 and z3 <= z4):
#             continue
#         else:
#             break
#     else:
#         A += 1
#         continue
#     break
# print(A)

# v8_15

# A = 0
# while True:
#     for x in range(-100, 100):
#         for y in range(-100, 100):
#             if x < 40 or y < 50 or (3 * x + 2 * y > A):
#                 continue
#             else:
#                 break
#         else:
#             continue
#         break
#     else:
#         A += 1
#         continue
#     break
# print(A - 1)

# v9_15
# A  = 1
# while True:
#     for x in range(51 * 25, 0, -1):
#         z1 = x & 51 != 0
#         z2 = x & A == 0
#         z3 = x & 25 != 0
#         if z1 <= (z2 <= z3):
#             continue
#         else:
#             break
#     else:
#         break
#     A += 1
# 
# print(A)

# v10_15

# v11_15  ===============================
# A = 1
# while True:
#     for x in range(1, 100):
#         z1 = x % A != 0
#         z2 = x % 6 == 0
#         z3 = x % 8 != 0
#         if z1 <= (z2 <= z3):
#             continue
#         else:
#             break
#     else:
#         A += 1
#         continue
#     break

