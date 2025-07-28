# range 為 python 內建的"清單產生器"
# for i in range 的 for loop通常是為了讓某內容重複執行i次
import random

# range(10) 會產生一個從0到9的數字序列
# range(10) 產生0~9的清單
list10 = range(10)  # range(0, 10)  # 產生0~9的數字

# range(10) 會產生一個 range 物件
# range(10) 產生的物件是不可變的，不能直接修改

# 但可以將其轉換為清單
list10 = list(list10)  # 將 range 轉換為清單
print(list10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


list5 = range(5)  # [0, 1, 2, 3, 4]
for i in range(5):
    # print(i)
    print('hi')  # hi, hi, hi, hi, hi
    print('hi', i)  # hi 0, hi 1, hi 2, hi 3, hi 4


for i in range(100):  # 此種寫法用來執行固定次數
    r = random.randint(1, 1000)  # 產生1~1000的隨機數字
    print('這是第', i+1, '個產生的隨機數：', r)


# expandtion of range
range(2, 5)  # [2, 3, 4]
range(2, 10, 2)  # [2, 4, 6, 8]，從2開始到10結束，每次增加2
range(10, 2, -2)  # [10, 8, 6, 4]，從10開始到2結束，每次減少2
