# Desc:
# Write a python program to find common char in two different string. eg. f(hello, world) ---> lo

string_1 = 'hello'
string_2 = 'world'

set_1 = set(string_1)
set_2 = set(string_2)

out = set.intersection(set_1, set_2)

print(out)
