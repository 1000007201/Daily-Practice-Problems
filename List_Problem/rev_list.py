list_ = [1, 5, 8, 7, 6, 4, 7]

for i in range(len(list_)//2):
    list_[i], list_[(len(list_)-1)-i] = list_[(len(list_)-1)-i], list_[i]

    if i == (len(list_)-1)-i:
        break

print(list_)
