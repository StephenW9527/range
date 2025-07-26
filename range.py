# range 為 python 內建的"清單產生器"
# for i in range 的 for loop通常是為了讓某內容重複執行i次


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
