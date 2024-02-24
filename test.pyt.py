# This is a comment
print("chaitanya") #Iam single line comment because I am in single line
#print("hello, world!")
print("Cheers, Matel!")

#This is a comment
print("hello, world")
#single line comment
print("everything")

#This is comment  #multi line comment
#written in
#more than just one line
print("Hello, world")

"""
This is comment         
written in
more than just one line
"""

info = 'Lorem Ipsum is simply dummy text of the printing and \
typesetting industry. Lorem Ipsum has been the industry\'s\
standard dummy text ever since the 1500s, when an unknown\
printer took a galley of type and scrambled it \
to make a type  specimen book. It has survived not\
only five centuries,  but also the leap into electronic\
ypesetting, remaining\
essentially unchanged. It was popularised in the 1960s with\
the release of Letraset sheets containing Lorem Ipsum passages,\
and more recently with desktop publishing software like Aldus\
PageMaker including versions of Lorem Ipsum.'
print(info)

info = '''
Lorem Ipsum is simply dummy text of the printing and 
typesetting industry. Lorem Ipsum has been the industry 's
standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it 
to make a type  specimen book. It has survived not
only five centuries,  but also the leap into electronic
ypesetting, remaining
essentially unchanged. It was popularised in the 1960s with
the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum.
'''
print(info)


x="hello world"
print(len(x))    # Some Useful String methods
a=x
print(len(x))

txt="chaitanya"
x=(txt[0])
print(x)

#slicing:
#string[start:end:step]
txt="chaitanya vaishu"
x=(txt[1:]) # gives Everything from list 1st index character to last
print(x) 
x=(txt[1:4:2]) # gives every second character from 1st index to 3rd index number
print(x)
x=(txt[1:5:2]) # gives every second character from 1st index to 4th index number
print(x)
x=(txt[0:5:3]) # gives every third character from oth index to 4th index number
print(x)
print(txt[0:5]) # gives 1st character from oth index to 4th index number
print(txt[2:5]) # gives second index number to 4th index number
print(txt[::])  # print everything
print(txt[::4]) # gives all character with step of 4th index
print(txt[-2])  #gives last index numbered character
print(txt[:-7]) # gives last index numbered character
print(txt[-4])  # gives last index numbered character
print(txt[-9:-3:2])
print(txt[-8:2:3])
print(txt[5:]) 
print(txt[:5]) 
print(txt[5:8])  
print(txt[2:6:4]) 
print(txt[-2])  
print(txt[0]) 
print(txt[:])  
print(txt[-2])
print(txt[7])
print(txt[::-12])#reversing string
print(txt[::-1])#reversing string
print(txt[:-1:4])#reversing string
print(txt[6])

import random
print(random.randrange(1,12))
print(random.randint(2,20))
print(random.seed(10))
print(random.randrange(12,20))
print(random.randint(4,16))
print(random.seed(0))

str="It's alright."
print(str)
#to avoid error we can surround the string with double quote
str='It\'s alright.'       
print(str)


str="Hey, what's up?"
print(str)
#to avoid error we can surround the string with double quote
str='Hey, what\'s up?'       
print(str)

a = "Whitespace "
print(a.upper())  # Some Useful String methods
a="Chaitanya"
print(a.upper())

a = "Beginning"
print(a.lower())

a = "REVERSING"
print(a.lower())

a="    Chaitanya vaishu  "
print(a.strip()) # returns "Chaitanya"

a="vaishu   "
print(a.strip())

a="vaishu"
print(a.replace("vaishu","chaithu"))

a="vai"
print(a.replace("vai","siva"))
a = "Beginning"
print(a.title())
a="vaishu"
print(a.title())

star= "*\n**\t***\n****\t*****"
print(star)
letters= "A\tB\nC\tD\nE\tF\n"
print(letters)
number="1\n2\t3\n4\t5\t6\n7\t8\t9\t10"
print(number)

directory = r"c:\\users\tabular_data\new\info"
print(directory)
print(dir(2))
print(dir("chaithu is a good girl"))

#taking input from user
your_name = "siva"
greet="good evening" 
your_name = input("Enter your name:")
print("Hello",greet,your_name)
print(("Hello {} {}").format(your_name, greet))

print(f"Hello {your_name} {greet}.")
print(greet)
print(your_name)

txt="How*are*you"
txt=txt.split()
print(txt)


txt="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry"
txt=txt.split()
print(txt)


txt="1 * 2 * 3 * 4"
txt=txt.split()
print(txt)

txt="1 * 2 * 3 * 4"
txt=txt.split("*")
print(txt)

import calendar
x=2001
y=6
x=y
print(calendar.month(x,y,))

import calendar
print("The calendar of year 2024 is ")
print(calendar.calendar(2024))




























