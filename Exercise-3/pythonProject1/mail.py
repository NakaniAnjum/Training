

# import smtplib
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login("nakanianjum@gmail.com",'wrmlfdggblgdepcr')
# server.sendmail('nakanianjum@gmail.com','anjumnakani.skyscendbs@gmail.com','hey good morning This is Anjum Nakani from skyscendbs')
# print('Mail sent')
#

# print("Anjum is \n Gafarbhai nakani::")
# print(10 * "NAKANI\n ANJUM")
#
# print("enter first number")
# a=input()
# print("enter second number")
# b=input()
# print("sum of two numbers is",int(a)+ int(b))
#
# b=input("enter any name :")
# print(b)

# mystr="harry is a good boy"
# print(len(mystr))
# print(mystr[:10])
# print(mystr.upper())
#
#
# list=[2,3,1,6,8,9]
# list.sort()
# print(list[1:4])
# list.remove(2)
# print(list)
#
# list.insert(2,22)
# list.reverse()
# print(list)
#
#
# d2={"harry":"burger", "rohan":"fish","diya":"waffer"}
# print(d2)
# d2["harry"]="ssss"
# print(d2)
#
# d2["rohan"]="iii"
# print(d2)
#
# del d2["rohan"]
# print(d2)
#
# d3=d2
# del d3["harry"]
# print(d3)
#
# # d3=d2.copy()
# # d3["harry"]
# # print(d3)
#
# print(d3.get("diya"))
# print(d3)
#
# print(d3.items())
# print(d3.keys())
#
# import smtplib            ###Second Method of Mail Sending
#
# sender_email="nakanianjum@gmail.com"
# rec_email="anjumnakani.skyscendbs@gmail.com"
# password=input(str("please enter your password::"))
# message="hey , This was sent using Python Code"
#
# server=smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login("nakanianjum@gmail.com",'wrmlfdggblgdepcr')
# print("login sucess")
# server.sendmail(sender_email,rec_email,message)
# print("Email has been sent to", rec_email)
#

a=10 #globals
b=9
c=8

def display():
    a=14 #locals
    b=3
    c=4
    print(a,b,c)
display()
print(a,b,c)
print (locals())


name="jenny's"
print(name)
def display():
    global name
    name=name + "lectures"

print(name)
display()
print(name)
