text = input('Enter your sentence : ')
number_of_letter = 0
number_of_word = 0
counter = 0

for letter in text:
    
    if  ('a' <= letter <= 'z')  or  ('A' <= letter <= 'Z'):
        
        number_of_letter += 1
        counter    += 1
        
        if counter == 2:
            
            number_of_word+=1
            
        continue
    
    else:
        
        counter = 0

number_of_character = len (text)   

number_of_enter_space = text.count('\n') + text.count(' ')

number_of_point_comma = text.count(',') + text.count('.')
    
print('number_character =',number_of_character,'\nnumber_letter =',number_of_letter,'\nnumber_word =',number_of_word)
print('number_enter_space =',number_of_enter_space,'\nnumber_point_comma',number_of_point_comma)