
print("\n")
str_input = input("Enter Sentence: ")
print("\n")
split_element = input("Enter Splition Element: ")
print("\n")
join_element = input("Enter Concatenate Element: ")

result = join_element.join(str_input.split(split_element))

print("\n\nResult is: " + result + "\n\n")