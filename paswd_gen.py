import random

plain_text=input("Enter Plain Text: ")
letter_list=['#','$','%','&','(',')','*','+',',','-','.','/',';','<','=','>','?','@','1','2','3','4','5','6','7','8','9','0']

size_of_txt=int(len(plain_text))

character_to_be_replaced=int(size_of_txt/2)

print("Generated Safe Passowrd:")
def string_r(s,n,r):
	size=int(len(s))
	s=s[:n]+r+s[n+1:]
	return s
def random_Caps_decide(plain_text):
    size=int(len(plain_text))
    for i in range(0,size):
        r=int(random.randint(0,1))
        if(plain_text[i].isupper() and r==1):
            x=plain_text[i]
            x=x.lower()
            plain_text=string_r(plain_text,i,x)
        if(plain_text[i].islower() and r==1):
            x=plain_text[i]
            x=x.upper()
            plain_text=string_r(plain_text,i,x)
            
    return plain_text
    
def strong_paswd(plain_text):
    size_of_txt=int(len(plain_text))
    for i in range(0,character_to_be_replaced):
        x=int(random.randrange(1,size_of_txt-2))

        y=random.choice(letter_list)

        plain_text=string_r(plain_text,x,y)
    
    plain_text=random_Caps_decide(plain_text)
    print(plain_text)


    
if(size_of_txt>=6):
    strong_paswd(plain_text)

else:
    size_of_txt=int(len(plain_text))
    size_to_fill=8-size_of_txt
    for i in range(0,size_to_fill):
        y=random.choice(letter_list)
        plain_text=plain_text+y
    strong_paswd(plain_text)
    
