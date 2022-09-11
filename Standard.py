list_names = []

for i in range(10) :
    
    name = input('Enter name')
    
    name = name.lower()
    
    name = name[0].upper()+name[1:]
    
    list_names.append(name)
    
    
print(list_names)