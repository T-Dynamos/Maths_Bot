"""
The MIT License (MIT)

Copyright (c) 2021 @T-Dynamos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import colorama
from colorama import Fore, Back ,Style
colorama.init()
from random import randint
import math
import time
import os
import requests
from tables import table_ex
os.system('clear')
version_info = '3.0'
ins ='Restart ? y/n = '
pi=22/7
def logo7():
	import os
	os.system('toilet -f pagga "Maths" | lolcat')
def pivalue():
	print(h1)
	print("1. 22/7 ")
	print("2. 3.14 ")
	print(h1)
	ol=input(" == > ")
	print(h1)
	if ol == '1':
		pi == (22/7)
	elif ol =='2':
		pi== (3.14)
	else:
		print(h1)
		print(" Default = 22/7")
		print(h1)
		pi=22/7
	print(h1)
	print("Assigned Successful !")
	print(h1)
def india():
	h3 = (Fore.CYAN + "╠═════════════════════════")
	print(h3)
	m=  Fore.LIGHTRED_EX+'MADE '
	i= Fore.WHITE + 'IN'
	ind=Fore.GREEN + 'INDIA'
	print("  ",m ,"" ,i, "",ind)
	print(h3)
def down():
	downloadUrl = 'https://raw.githubusercontent.com/T-Dynamos/Maths_Bot/main/setup.py'
	req = requests.get(downloadUrl)
	filename = req.url[downloadUrl.rfind('/')+1:]
	with open(filename, 'wb') as f:
		for chunk in req.iter_content(chunk_size=8192):
			if chunk:
				f.write(chunk)
def update():
	print(h1)
	x=input("Do You want to update y/n ==> ")
	if x=='y':
		print()
		os.remove('setup.py')
		print("Downloading...")
		os.system('pip install py-loader')
		os.system('pip install table-ex')
		down()
		time.sleep(1)
		print()
		print("Installing...")
		print()
		time.sleep(0.25)
		print("Installation Successful")
		time.sleep(2)
		print(h1)
		print("Restarting")
		print(h1)
		time.sleep(1)
		os.system('clear')
		os.system('python setup.py')
		print(h1)
		exit()
	else:
		restart()
def r1():
	print(h1)
	print("Worng Option Idiot")
	print(h1)
	restart()
def restart():
	r=input(ins)
	if r =='y':
		os.system('clear')
		logo7()
		main()
	else:
		print(h1)
		print("Sub On YouTube = " , sub)
		print(h1)
		exit()
print(Fore.BLUE + Style.BRIGHT + "                     ===============================================")
print(Fore.YELLOW + "                     〘Coder =ㅤAnsh Dadwalㅤ||ㅤTeam = T-Dynamos  〙 ")
h="==============================================="
h1= "══════════════════════════════"
print(Fore.BLUE +"                    ", h)
sub="https://youtube.com/channel/UCCGprYqpszbeAYMGbjlh-aA"
colorama.init(autoreset=False)
time.sleep(0.25)
print(Fore.RED)
print( Fore.LIGHTGREEN_EX + "         __________")
#Ansh Dadwal is great and this company is owned by Ansh Dadwal 
print("        |----------|","::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("        ||12345678||","##::::'##::::'###::::'########:'##::::'##::'######::   ")
print("        |----------|","###::'###:::'## ##:::... ##..:: ##:::: ##:'##... ##:")      
print("        |          |","####'####::'##:. ##::::: ##:::: ##:::: ##: ##:::..:: ")
print("        |[M|#|C][-]|","## ### ##:'##:::. ##:::: ##:::: #########:. ######::")
print("        |[7|8|9][+]|","##. #: ##: #########:::: ##:::: ##.... ##::..... ##: ")
print("        |[4|5|6][x]|","##:.:: ##: ##.... ##:::: ##:::: ##:::: ##:'##::: ##:")
print("        |[1|2|3][%]|","##:::: ##: ##:::: ##:::: ##:::: ##:::: ##:. ######::")
print("        |[.|O|:][=]|","..:::::..::..:::::..:::::..:::::..:::::..:::......::")
print("        +__________+")
print()
india()
print()
h4 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print(h4)
print("©  Copyright  = @ T-Dynamos_Mod","          ")
print(h4)
print()
print(Fore.MAGENTA+ Back.GREEN + "Version = " , version_info)
time.sleep(1)
print()
print(Fore.LIGHTCYAN_EX+ Back.BLACK )
print()
def sqrt123():
	print(h1)
	f=int(input("Enter The Number = "))
	print("Square Root =  ",math.sqrt(f))
	print(h1)
	restart()
def main():
	print(h1)
	print("Choose Any Option")
	print(h1)
	print()
	print("1. Learn Maths")
	print("2. Area")
	print("3. Volume")
	print("4. Heron's Formula")
	print("5. Tables")
	print("6. Square and Square Root")
	print("7. Temperature Conversion")
	print()
	print(h1)
	print()
	print("[a] Update Program")
	print()
	print(h1)
	a=input("1/2/3/4/5/6/a ==> ")
	print(h1)
	if a=='7':
		print(h1)
		print("1. Kelvin To Celsius [ °K---> °C ]")
		print("1. Celsius To Kelvin [ °C---> °K ]")
		print("1. Celsius To Fahrenheit [ °C---> °F ]")
		print("1. Fahrenheit To Celsius [ °F---> °C ]")
		print(h1)
		hji=input("==> ")
	if a=='6':
		print(h1)
		print("1. Square Root")
		print("2. Raised To Power ")
		print(h1)
		op=input("==> ")
		if op=='1':
			sqrt123()		
		if op =='2':
			print(h1)
			f=int(input("Enter A Number = "))
			k=int(input("Raised To Power = "))
			print("==> ",f**k)
			print(h1)
			restart()
	if a=='4':
		print(h1)
		a=int(input(" Side 1 = "))
		b=int(input(" Side 2 = "))
		c=int(input(" Side 3 = "))
		s = (a+b+c) / 2
		print(h1)
		print(" S-a = ",s-a)
		print(" S-b = ",s-b)
		print(" S-c = ",s-c)
		print(h1)
		print("Semi Perimeter = ",s)
		print(h1)
		area = math.sqrt(s* (s-a) * (s-b) * (s-c))
		print(" Area = ", area)
		print(h1)
		restart()
	if a=='5':
		print(h1)
		a=(input("Enter a Number = "))
		print(h1)
		b=(input("To which extent = "))
		print(h1)
		print("Table of ",a)
		print(h1)
		table_ex(a,b)
		print(h1)
		restart()
	if a=='a':
		update()
	if a=='1':
		print(h1)
		print("Lol you can't")
		print(h1)
		restart()
		print(h1)
	if a=='2':
		print(h1)
		
		print(h1)
		print("1. Curved Surface Area")
		print("2. Total Surface Area")
		print("3. Simple Area")
		print(h1)
		c=input("1/2 ==> ")
		print(h1)
		if c=='1':
				print("")
				print(h1)
				print("1. LSA of Cuboid")
				print("2. LSA of Cube")
				print("3. LSA of Pyramid")
				print("4. CSA of Cyclinder ")
				print("5. CSA of Cone")
				print("6. CSA of Sphere")
				print("7. CSA of Hemisphere")
				print(h1)
				e=input(" 1/2/3/4/5/6/7 ==> ")
				print(h1)
				if e=='1':
					print(h1)
					l=int(input("Length = "))
					b=int(input("Breadth = "))
					h=int(input("Hsight = "))
					print("Area = ", 2*h*(l+b))
					print(h1)
					restart()	            
				if e=='2':
					print(h1)
					a=int(input(" Side = "))
					print("Area = ", 4*a*a)
					print(h1)
					restart()
				if e=='3':
					print(h1)
					p=int(input("Perimeter = "))
					sl=int(input("Slant Height ="))
					print("Area = ", 1/2*sl*p )
					print(h1)
					restart()
				if e=='4':
					print()
					print(h1)
					r=int(input("Radius = "))
					h=int(input("Height = "))
					print("Area = ", 2*pi*r*(h))
					print(h1)
					restart()
				if e=='5':
					print()
					print(h1)
					l=int(input("Slant Height = "))
					r=int(input("Radius = "))
					print("Area = ", (r*l)*pi)
					print(h1)
					restart()
				if e=='6':
					print()
					print(h1)
					r=int(input("Radius = "))
					print("Area = ",4*pi*r*r)
					print(h1)
					restart()
				if e=='7':
					print()
					print(h1)
					r=int(input("Radius = "))
					print("Area = ", 2*pi*r*r)
					restart()
				else:
					r1()
		if c=='3':
			print(h1)
			print("1.Area of Square")
			print("2.Area of Rectangle")
			print("3.Area of Circle")
			print("4.Area of Parallelogram")
			print("5.Area of Triangle")
			print("6.Area of Trapizium")
			print(h1)
			x=input(" ==> ")
			print(h1)
			if x=='1':
				yt=int(input("Side"))
				print("Area = ",yt*yt)
				print(h1)
				restar()
			if x=='2':
				print(h1)
				yt=int(input("Length = "))
				ty=int(input("Breadth = "))
				print("Area = ",yt*ty)
				print(h1)
				restart()
			if x=='3':
				print(h1)
				r=int(input("Radius = "))
				print("Area = ",pi*r*r)
				print(h1)
				restart()
			if x=='4':
				print(h1)
				h=int(input("Height = "))
				b=int(input("Base = "))
				print("Area = ",b*h)
				print(h1)
				restar()
			if x=='5':
				print(h1)
				h=int(input("Height = "))
				b=int(input("Base = "))
				print("Area = ", 1/2*b*h)
				print(h1)
				restart()
			if x=='6':
				p1=int(input("Parallel Side 1 = "))
				p2=int(input("Parallel Side 2 = "))
				h=int(input("Height = "))
				print("Area = ", 1/2 * p1+p2 * h)
				print(h1)
				restart()
		if c=='2':
				print(h1)
				print("1.TSA OF CUBOID")
				print("2.TSA OF CUBE")
				print("3.TSA OF CYCLINDER")
				print("4.TSA OF CONE")
				print("5.TSA OF HEMISPHERE")
				print("6.TSA OF PYRAMID")
				print(h1)
				a2=input(" ==> ")
				if a2 == '1':
					print(h1)
					l=int(input("Length = "))
					b=int(input("Breadth = "))
					h=int(input("Height = "))
					print("Area = ",2* (l+b) * (b+h) *(h+l))

					print(h1)
					restart()
				if a2=='2':
					print(h1)
					a=int(input("Side = "))
					print("Area = ", 6 *a*a)
					print(h1)
					restart() 
				if a2=='3':
					print(h1)
					r=int(input("Radius = "))
					i=int(input("Height = "))
					print("Area = ", 2 * pi * r*(i+r)) 
					print(h1)
					restart()
				if a2=='4':
					print(h1)
					sl=int(input("Slant Height = "))
					r=int(input("Radius = "))
					print("Area = ",pi*r*(sl+r))
					print(h1)
					restart()
				if a2=='5':
					print(h1)
					r=int(input("Radius = "))
					print("Area = ",3*pi*r*r)
					print(h1)
					restart()
				if a2=='6':
					print(h1)
					p=int(input("Perimeter = "))
					sl=int(input("Slant Height = "))
					b=int(input("Base = "))
					print("Area = ", 12* p * (sl + b) )
					print(h1)
					restart()
				else:
					r1()
	if a=='3':
		print(h1)
		print("1. Volume of Cuboid" )
		print("2. Volume of Cube")
		print("3. Volume of Cyclinder ")
		print("4. Volume of Cone ")
		print("5. Volume of Sphere")
		print("6. Volume of Hemisphere")
		print(h1)
		a3=input("1/2//3/4/5/6/==> ")
		if a3=='1':
			print(h1)
			l=int(input("Length = "))
			b=int(input("Breadth = "))
			h=int(input('Heigth = '))
			print("Volume = ",l*b*h)
			print(h1)
			restart()
		if a3=='2':
			print(h1)
			a=int(input("Side = "))
			print('Area = ', a*a*a)
			print(h1)
			restart()
		if a3=='3':
			print(h1)
			h=int(input("Height = "))
			r=int(input("Radius = "))
			print("Area = ", pi*r*r*h)
			print(h1)
			restart()
		if a3=='4':
			print(h1)
			r=int(input("Radius = "))
			h=int(input("Height = "))
			print("Area = ", 1/3 *pi*r*r*h)
			print(h1)
			restart()
		if a3=='5':
			print(h1)
			r=int(input("Radius = "))
			print("Area = ", 4/3*pi*r*r*r)
			print(h1)
			restart()
		if a3=='6':
			print(h1)
			r=int(input("Radius = "))
			print("Area = ", 2/3*pi*r*r*r)
			print(h1)
			restart()
		else:
			r1()
	else:
		r1()
		
				
main()         
