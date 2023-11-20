from tkinter import *
import secrets
import string

tkintermain = Tk()
tkintermain.title("Password generator")
tkintermain.geometry('900x600')
tkintermain.minsize(700, 300)

tkintermain.config(background= '#f2f2f2')

frame = Frame(tkintermain, bg = '#f2f2f2')

def generatePassword(letter_entry, digit_entry, punctuation_entry, language) : 
    if letter_entry == 0 :
        letter = ""
    else :
        letter = string.ascii_letters
    if digit_entry == 0 :
        digit = ""
    else :
        digit = string.digits
    if punctuation_entry == 0 :
        punctuation = ""
    else :
        punctuation = string.punctuation
    alphabet = letter + digit + punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(language))
    return password
    

print(generatePassword(1, 0, 0, 10))


def rep() :
    noOfChar = entry2.get ()
    noOfChar = int(noOfChar)
    text1 = case_1.get
    text2 = case_2.get
    text3 = case_3.get
    
    password = generatePassword(text1(),text2(),text3(),noOfChar)
    print(password)
    entry.delete(0, END)
    entry.insert(0, password)





label_title = Label(frame, text= '1.Enter the number of characters you want.', font=("Arial", 20), bg = '#f2f2f2', fg ='#000000')          
label_title.pack()                                                                                                                            

entry2 = Entry(frame, text= "", font=("Arial", 25), bg = '#ececec', fg ='#000000')                                                         #25 
entry2.pack(fill=X)  


case_1 = IntVar()

case = Checkbutton(frame, text="letter",variable = case_1,font=("Arial", 15), onvalue=1, offvalue=0)
case.pack()

case_2 = IntVar()

case1 = Checkbutton(frame, text="digits",variable = case_2 ,font=("Arial", 15), onvalue=1, offvalue=0)
case1.pack()

case_3 = IntVar()

case2 = Checkbutton(frame, text="punctuation",variable = case_3 ,font=("Arial", 15), onvalue=1, offvalue=0)
case2.pack()

button = Button(frame, text = "2.Generate password", font=("Arial", 20), bg = '#2e83ef', fg ='#000000', command = rep)                       
button.pack(fill=X) 



entry = Entry(frame, font=("Arial", 25), bg = '#a7a7a7', fg ='#000000')                                                                    #25 
entry.pack(fill=X)  


frame.pack(expand = YES)
tkintermain.mainloop()
