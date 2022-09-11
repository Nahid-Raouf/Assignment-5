text = input('Enter the word : ')

list_text = []
list_text2 = []


for letter in text :
    
    list_text .append(letter)

while  ' ' in list_text :
    
    list_text.remove(' ')

for i in range(len(list_text)):
    
    list_text2.append(list_text[-i-1])

    
if list_text == list_text2 :
    
    print ('the word is palindorme')
    
else :
    
    print ('the word is not palindorme')