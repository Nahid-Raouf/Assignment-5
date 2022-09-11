text = input('Enter your calculations: ')
operator = ['*','/','+','-']
list_of_operator = []
counter = 0

for letter in text :
    
    for i in range(4):
        
        if letter == operator[i]:
            
            list_of_operator.append(letter)
            


for i in range(4):
    
    list_phrase = text.split(operator[i])
    text = ' '.join(list_phrase)
    
list_abarat = text . split(' ')

while ''in list_phrase :
    
    list_phrase.remove('')
    
    

for i in range(len(list_phrase)):
    
    list_phrase[i] = int (list_phrase[i])
    

while '*' in list_of_operator or  '/' in list_of_operator:
    
    if list_of_operator[counter] == '*':
        
        list_phrase[counter] = list_phrase[counter] * list_phrase[counter+1]
        
        list_phrase.pop(counter+1) 
        list_of_operator.pop(counter)
        
        counter -= 1
        
    
    elif list_of_operator[counter] == '/':
        
        list_phrase[counter] = list_abarat[counter]/list_abarat[counter+1]
        
        list_phrase.pop(counter+1) 
        list_of_operator.pop(counter)

        counter -= 1
   
    
        
    counter += 1
    
    
    
counter = 0 
    
while '+' in list_of_operator or  '-' in list_of_operator:   
        
    if list_of_operator[counter] == '+':
        
        list_phrase[counter] = list_phrase[counter]+list_phrase[counter+1]
        
        list_phrase.pop(counter+1) 
        list_of_operator.pop(counter)
        
        counter -= 1
        
    
    elif list_of_operator[counter] == '-':
        
        list_phrase[counter] = list_phrase[counter]-list_phrase[counter+1]
        
        list_phrase.pop(counter+1) 
        list_of_operator.pop(counter)

        counter -= 1
   
    
        
    counter += 1 
    
    
        
print('Aswer is : ',list_phrase[0])