paragraph = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code 
readability with the use of significant indentation. Its language constructs and object-oriented approach aim to help 
programmers write clear, logical code for small- and large-scale projects. Python is dynamically-typed and garbage-collected.
It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional 
programming. It is often described as a "batteries included" language due to its comprehensive standard library.'''

para_list = list(paragraph.split(' '))
list_ = []

for i in para_list:
    if len(i) % 2 == 0:
        list_.append(i)

print(list_)
