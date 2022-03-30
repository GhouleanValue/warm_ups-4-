# Warmups aimed at using the strings in different ways.

#1 | Multi line strings

print('''This is an exercise to show the user available options for multi line strings.'
      This is an easy method and may be useful in the future.
      Like any language, the constant use of that language will make you more
      fluent in your ability to speake it.
      The longer you speak a language (python) the wider your vocabulary becomes.''')

#2 | Slicing and indexing

string = 'Do warmups every day'

print(string[0:10])

# 2.1 | Reverse your string

print(string[::-1])

# 2.2 | Slice from the end

print(string[:-1])

#3 | Concatonate

print(string + ' and night')

#4 | Start a new line

new_string = '\n forward slash n will start our new line. \n do not forget to add spaces.'

print(string + new_string)

#5 | f string literal

print(f"use the f {'before'} the {'quotation'} {'marks'} to tell python this is an f string")

#5.1 | .format

print('use the .format {} the {} {}, then place your desired words'.format('before', 'quotation', 'marks'))
