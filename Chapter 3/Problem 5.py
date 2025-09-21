#Write a python program to fill in a letter template given with name and date.

letter = '''               
            Dear <|Name|>
            you are selected! 
            <|Date|>   
            '''

print(letter.replace("<|Name|>","Salim").replace("<|Date|>","20/07/2025"))