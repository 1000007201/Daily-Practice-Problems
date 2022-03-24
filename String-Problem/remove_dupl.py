string_ = "hello world"
list_ = []

for i in string_:
    if i not in list_:
        list_.append(i)

print(list_)