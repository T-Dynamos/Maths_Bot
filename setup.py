#Ansh Dadwal is great and this company is owned by Ansh Dadwal 
#pylint:disable=E0001
#pylint:disable=W0312
#python program
pi=22/7
version_info = '1.0(stable)'
ins ='Restart ? y/n = '
import colorama
from colorama import Fore, Back ,Style
colorama.init()
from random import randint
import math
import time
import os
import requests
os.system('clear')
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
		os.system('rm -rf setup.py')
		print("Downloading...")
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
	india()
	restart()
def restart():
	r=input(ins)
	if r =='y':
		os.system('clear')
		main()
	else:
		print(h1)
		print("Sub On YouTube = " , sub)
		india()
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
print("=================================")
print("   ©Copyright  = @T-Dynamos_Mod","          ")
print("=================================")
print()
print(Fore.MAGENTA+ Back.GREEN + "Version = " , version_info)
time.sleep(1)
print()
print(Fore.LIGHTCYAN_EX+ Back.BLACK )
print()
def main():
	print(h1)
	print("Choose Any Option")
	print(h1)
	print()
	print("1. Learn Maths")
	print("2. Area")
	print("3. Volume")
	print("4. Heron's Formula")
	print()
	print(h1)
	print()
	print("5. Update Program")
	print()
	print(h1)
	a=input("1/2/3/4/5/6/7 ==> ")
	print(h1)
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
		
				
main()         