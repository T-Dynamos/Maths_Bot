#!/data/data/com.termux/files/usr/bin/python3
#!/usr/bin/python3

# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2021 TDynamos <tdynamos@linux>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#By T-Dynamos | Ansh Dadwad
version = '9.0'
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
from shutil import which

pkgs = ['python3','curl','lolcat']
inst = True
for pkg in pkgs:
        present = which(pkg)
        if present == None:
                print(R + '[-] ' + W + pkg + C + ' is not Installed! . Install it')
                inst = False
        else:
                pass
if inst == False:
        exit()

import itertools
import threading
import sys
import math
import time
import os
import random
import requests
from random import randint
os.system('rm -rf $HOME/.mbotrc')

try:
	import colorama
except ModuleNotFoundError:
	print("Colorama Is Not Installed")
	os.system('python -m pip install colorama')

try:
	from tables import table_ex
except ModuleNotFoundError:
	print("Table-ex Is Not Installed")
	os.system('python -m pip install table-ex')
try:
	import riposte
except ModuleNotFoundError:
	print("riposte Is Not Installed")
	os.system('python -m pip install riposte')
try:
	import requests
except ModuleNotFoundError:
	print("requests Is Not Installed")
	os.system('python -m pip install requests')
from colorama import Fore, Back ,Style
colorama.init()
under = '\033[4m'
line = '\033[0m'
logo1 = """
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
"""

logo2 = """

?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
"""

logo3 = """
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
?????????????????????????????????????????????????????????????????????
"""
logo4 = """
???????????????????????????????????????????????????
???????????????????????????????????????????????????
???????????????????????????????????????????????????
???????????????????????????????????????????????????
"""

logo5 = """
???????????????????????????????????????????????????
???????????????????????????????????????????????????
???????????????????????????????????????????????????
???????????????????????????????????????????????????
"""
logo6 = """
???????????????????????????????????????????????????
???????????????????????????????????????????????????
???????????????????????????????????????????????????
???????????????????????????????????????????????????
"""
def color():
	cyan = (Fore.CYAN)
	yellow = (Fore.YELLOW)
	green = (Fore.GREEN)
	blue = (Fore.BLUE)
	red = (Fore.RED)
	pink = (Fore.MAGENTA)
	color = random.randint(1 , 6)
	if color == 1:
		col = (cyan)
	if color == 2:
		col = (yellow)
	if color == 3:
		col = (green)
	if color == 4:
		col = (blue)
	if color == 5:
		col = (red)
	if color == 6:
		col = (pink)
	print(col)
def file_make(namefile):
	file1 = open(name, "w") 
	file1.close() 
def logofile():
	ran = random.randint(1,6)
	filecheck = os.path.isdir(HOME + '/.mbotrc')
	if filecheck == True:
		return logo()
	if filecheck == False:
		pass
	os.system('mkdir $HOME/.mbotrc > /dev/null 2>&1')
	if ran == 1:
		os.system(" touch $HOME/.mbotrc/logo1 ")
	if ran == 2:
		os.system(" touch $HOME/.mbotrc/logo2 ")
	if ran == 3:
		os.system(" touch $HOME/.mbotrc/logo3 ")
	if ran == 4:
		os.system(" touch $HOME/.mbotrc/logo4 ")
	if ran == 5:
		os.system(" touch $HOME/.mbotrc/logo5 ")
	if ran == 6:
		os.system(" touch $HOME/.mbotrc/logo6 ")
		
HOME= os.path.expanduser('~')
logofile()
def logo():
	logo10 = os.path.isfile(HOME + '/.mbotrc/logo1')
	logo20 = os.path.isfile(HOME + '/.mbotrc/logo2')
	logo30 = os.path.isfile(HOME + '/.mbotrc/logo3')
	logo40 = os.path.isfile(HOME + '/.mbotrc/logo4')
	logo50 = os.path.isfile(HOME + '/.mbotrc/logo5')
	logo60 = os.path.isfile(HOME + '/.mbotrc/logo6')	
	if logo10 == True:
		color()
		print(logo1)
	if logo20 == True:
		color()
		print(logo2)		
	if logo30 == True:
		color()
		print(logo3)			
	if logo40 == True:
		color()
		print(logo4)
	if logo50 == True:
		color()
		print(logo5)
	if logo60 == True:
		color()
		print(logo6)
		
lic = """
  Copyright 2021 TDynamos <tdynamos@linux>
  
  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.
  
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,#  MA 02110-1301, USA.
  
"""
info = ''
result = ''

import getpass

os1 = getpass.getuser()
from riposte import Riposte
math1 = (Fore.BLUE + Style.BRIGHT + "??????[" + Fore.RED + "math" + Fore.BLUE + "][" +Fore.GREEN + os1+ Fore.BLUE+"]\n" + Fore.BLUE +  '??????# ' + Fore.GREEN)

calculator = Riposte(prompt=(math1))

MEMORY = []
import threading

def heading(num,txt):
	print(Fore.RESET + Fore.RED + "[" + Fore.GREEN + num + Fore.RED + "]" + Fore.CYAN + txt )
#functions
##########################
@calculator.command("help")
def help():
	print()
	print(h1 +"???????????????")
	print("Welcome To Calculator")
	print(h1 +"???????????????")
	print("Here Are some options you can use : ")
	print()
	print("Relplace x and y with your value")
	print()
	heading('1','add           x y')
	heading('2','multiply      x y')
	heading('3','sub           x y')
	heading('4','divide        x y')
	print()
	print("Extra Options")
	print()
	heading('1','res       To restart')
	heading('2','exit      To exit')
	heading('3','banner    To print banner')
	heading('4','main      To start main activity')
	heading('5','memory    To show memory')
	print(Fore.GREEN)
	
	print(h1 +"???????????????")
	print()
    	
@calculator.command("banner")
def banner():
	logo7()

@calculator.command("exit")
def exit():
	sys.exit()	
@calculator.command("add")
def add(x: int, y: int):
    result = f"{x} + {y} = {x + y}"
    MEMORY.append(result)
    calculator.success(result)


@calculator.command("multiply")
def multiply(x: int, y: int):
    result = f"{x} ?? {y} = {x * y}"
    MEMORY.append(result)
    calculator.success(result)
    
@calculator.command("divide")
def multiply(x: int, y: int):
    result = f"{x} ?? {y} = {x / y}"
    MEMORY.append(result)
    calculator.success(result)
    
@calculator.command("sub")
def multiply(x: int, y: int):
    result = f"{x} - {y} = {x - y}"
    MEMORY.append(result)
    calculator.success(result)

@calculator.command("memory")
def memory():
    for entry in MEMORY:
        calculator.print(entry)

def ver_check():
        print(G + '[+]' + C + ' Checking for Updates.....', end='')
        ver_url = 'https://raw.githubusercontent.com/T-Dynamos/Maths_Bot/main/version'
        try:
                ver_rqst = requests.get(ver_url)
                ver_sc = ver_rqst.status_code
                if ver_sc == 200:
                        github_ver = ver_rqst.text
                        github_ver = github_ver.strip()

                        if version == github_ver:
                                print(C + '[' + G + ' Up-To-Date ' + C +']' + '\n')
                        else:
                                print(C + '[' + G + ' Available : {} '.format(github_ver) + C + ']' + '\n')
                else:
                        print(C + '[' + R + ' Status : {} '.format(ver_sc) + C + ']' + '\n')
        except Exception as e:
                print('\n' + R + '[-]' + C + ' Exception : '+R+'No Internet !' )
def eluatxt():
	print(Fore.GREEN + Style.BRIGHT + "*THIS IS NOT BLA-BLA")
	print()
	print("++++++++++++++++++++")
	print(Fore.CYAN  + "Terms and Conditions")
	print(Fore.GREEN +"++++++++++++++++++++")
	print()
	print(Fore.MAGENTA + lic)
	print("If you are using this program you should ensure that you are not sitting in a")
	print("examination and you are  not using this program for cheating . If you")
	print("ignore this and you use this program in examination  it will not be our fault .")
	print()
def eulapa():	
	ist = (HOME + '/.mbotcfg/hack.txt')
	it = os.path.isfile(ist)	
	if it == True:
		pass
	if it == False:
		os.system('clear')
		eluatxt()
		print()
		print(Fore.BLUE+"Write Down This to continue ")
		print()
		print(Fore.RED + "I accepted this bla bla")
		print(Fore.GREEN)
		hj = input("==> ")
		if hj == 'I accepted this bla bla':
			os.system('mkdir ' +HOME +'/.mbotcfg/  > /dev/null')
			os.system('touch ' +HOME +'/.mbotcfg/hack.txt')
			print()
		elif hj == 'hack':
			pass
		else:
			return eulapa()
eulapa()
def optxt():
	file1 = open("opt","w") 
	L = [
	 "???  [1] Learn Maths  \n",
	 "???  [2] Area \n",
	 "???  [3] Volume  \n",
	 "???  [4] Heron's Formula  \n",
	 "???  [5] Tables  \n",
	 "???  [6] Square and Square Root  \n",
	 "???  [7] Pythagoras Therom  \n",
	 "???  [8] Temperature Conversion  \n",
	 "???  [9] Fractions  \n",
	 "???  [0] Calculator Commandline  \n"
	 ]	 
	file1.writelines(L) 
	file1.close() 


ins ='Restart ? y/n = '
pi=22/7
def printu(string):
	print(under ," " , string , " ",line)
	print(Fore.CYAN + Style.BRIGHT)

def logo7(): 
	import os
	color()
	logo()
	print(Fore.RED+ Back.GREEN + "Version = " , "",version,Fore.CYAN + Style.BRIGHT + Fore.RESET + Back.RESET )
	colorama.init()
	print(Fore.CYAN)
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
	h3 = (Fore.CYAN + "??????????????????????????????????????????????????????????????????????????????")
	print(h3)
	m=  Fore.LIGHTRED_EX+'MADE '
	i= Fore.WHITE + 'IN'
	ind=Fore.GREEN + 'INDIA'
	print("  ",m ,"" ,i, "",ind)
	print(h3)
@calculator.command("clear")
def clear():
	os.system('clear')
def update():
	print(h1)
	x=input("Do You want to update y/n ==> ")
	if x=='y':
		print()
		print("Installing...")
		print()
		done = False
		def animate():
		      for c in itertools.cycle(['|', '/', '-', '\\']):
		          if done:
		          	break
		          sys.stdout.write(Fore.GREEN + '\rUpdating ' + Fore.YELLOW+ c)
		          sys.stdout.flush()
		          time.sleep(0.1)
		      sys.stdout.write('')
		      exit()
		t = threading.Thread(target=animate)
		t.start()
		
		file2 = open("installfile","w") 
		installfile = ('rm -rf $HOME/m_bot\n apt update\n apt install python git -y\n  git clone https://github.com/T-Dynamos/Maths_Bot m_bot\n mv $HOME/m_bot/setup.py $PREFIX/bin/mbot\n chmod 777 $PREFIX/bin/mbot\n rm -rf $HOME/m_bot ')
		file2.writelines(installfile) 
		file2.close() 
		os.system('bash installfile > /dev/null  2>&1')
	
		done = True
		print()
		print()
		print(Fore.GREEN + "Updatation Successful . Restart it ")
		os.system('rm installfile')
		exit()		
	else:
		os.system(' cd $HOME/m_bot')
		restart()
def r1():
	print(h1)
	print("Wrong Option Idiot")
	print(h1)
	restart()
@calculator.command("res")
def res():
	print()
	print("Use Ctrl + D to restart")
	print()
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
def compute_lcm(x,y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
os.system('clear')
print(Fore.RESET + Fore.BLUE + Style.BRIGHT +"==============================================")
print(Fore.YELLOW + "??? Coder = Ansh Dadwal???|| Team = T-Dynamos ??? ")
h="=============================================="
h1=("??????????????????????????????????????????????????????????????????????????????????????????")
print(Fore.BLUE + h)
ver_check()
sub="https://youtube.com/channel/UCCGprYqpszbeAYMGbjlh-aA"
colorama.init(autoreset=False)
logo7()
print(Fore.LIGHTCYAN_EX)
india()
print()
h4 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print(h1)
print("??  Copyright  = @ T-Dynamos","          ")
print(h1)
print(Fore.LIGHTCYAN_EX)
def  cyan(str):
	print(Fore.CYAN + Style.BRIGHT , str)
	
def sqrt123():
	print(h1)
	f=int(input("Enter The Number = "))
	print("Square Root =  ",math.sqrt(f))
	print(h1)
	restart()
def fraction_add():
	print(h1)
	print("Follow This Format")
	print(h1)
	print()
	a = (Fore.CYAN + Style.BRIGHT)
	print(under," a ",line,a," ",under,"  b ", line)
	print(a + "  c         d ")
	print()
	print(h1)
	print("Assign the Following Vales")
	print(h1)
	a =int(input("A = "))
	b =int(input("B = "))
	c =int(input("C = "))
	d =int(input("D = "))	
	print(h1)
	lcm=compute_lcm(c,d)
	value1=(lcm/c) *a
	value2=(lcm/d) *b
	ultimate=value1+value2
	print(under,value1,"+",value2,line)
	col =(Fore.CYAN + Style.BRIGHT)
	print(col,"   ",lcm)
	print(h1)	
	print(under,ultimate,line)
	print(col,"",lcm)
	print()
	print("Do cutting Yourself")
	print(h1)
	print("Final Answer = ",ultimate/lcm)
	print(h1)
	restart()
def fraction_sub():
	print(h1)
	print("Follow This Format")
	print(h1)
	print()
	a = (Fore.CYAN + Style.BRIGHT)
	print(under," a ",line,a," ",under,"  b ", line)
	print(a + "  c         d ")
	print()
	print(h1)
	print("Assign the Following Vales")
	print(h1)
	a =int(input("A = "))
	b =int(input("B = "))
	c =int(input("C = "))
	d =int(input("D = "))	
	print(h1)
	lcm=compute_lcm(c,d)
	value1=(lcm/c) *a
	value2=(lcm/d) *b
	ultimate=value1+value2
	print(under,value1,"-",value2,line)
	col =(Fore.CYAN + Style.BRIGHT)
	print(col," ",lcm)
	print(h1)	
	print(under,ultimate,line)
	print(col,"",lcm)
	print()
	print("Do cutting Yourself")
	print(h1)
	print("Final Answer = ",ultimate/lcm)
	print(h1)
	restart()
def fraction_multi():
	print(h1)
	print("Follow This Format")
	print(h1)
	print()
	gh = (Fore.CYAN + Style.BRIGHT)
	print(under," a ",line,gh," ",under,"  b ", line)
	print(gh+ "  c         d ")
	print()
	print(h1)
	print("Assign the Following Vales")
	print(h1)
	a =int(input("A = "))
	b =int(input("B = "))
	c =int(input("C = "))
	d =int(input("D = "))	
	print(h1)
	print(under," ",a, "",line,gh," ",under,"  ",b," ",line)
	print(gh + "  ",c,"   ??    ",d )
	value1=a*b
	value2=c*d
	print(h1)
	print(under , value1, line)
	print(gh ,value2)
	print(h1)
	print("Final Answer = ", value1/value2)
	print(h1)
	restart()
def fraction_divide():
	print(h1)
	print("Follow This Format")
	print(h1)
	print()
	gh = (Fore.CYAN + Style.BRIGHT)
	print(under," a ",line,gh," ",under,"  b ", line)
	print(gh+ "  c         d ")
	print()
	print(h1)
	print("Assign the Following Vales")
	print(h1)
	a =int(input("A = "))
	b =int(input("B = "))
	c =int(input("C = "))
	d =int(input("D = "))	
	print(h1)
	print(under," ",a, "",line,gh," ",under,"  ",b," ",line)
	print(gh + "  ",c,"   ??    ",d )
	value1=a*d
	value2=b*c
	print(h1)
	print(under , value1, line)
	print(gh ,value2)
	print(h1)
	print("Final Answer = ", value1/value2)
	print(h1)
	restart()
###############################
@calculator.command("main")
#main program starts here
################################
def main():
	print('???'+ h1)
	print("??? "+Fore.YELLOW+"Choose Any Option"+Fore.CYAN)
	print('???'+h1)
	an = os.path.isfile('$HOME/m_bot/opt')
	if an == True:
		os.sys()
	if an == False:
		optxt()
	os.system('cat opt | lolcat')
	os.remove('opt')
	print(Fore.CYAN + Style.BRIGHT +'???'+ h1)
	print("??? "+Fore.YELLOW+"[a] Update Program"+Fore.CYAN)
	print('???'+h1)
	a=input("???????????????]> ")
	if a=='0' :
		print()
		print("Type help to start")
		print()
		try:
			calculator.run()
		except RuntimeError:
			print("Previous Cli Running")
			time.sleep(3)
			print("Stopped")
			exit()
			
	if a=='9':
		os.system('clear')
		logo7()
		print(h1)
		print('Choose Any Option')
		print(h1)
		print("[1] Add Fractions")
		print("[2] Subtract Fractions")
		print("[3] Multiply Fractions")
		print("[4] Divide Fractions")
		print(h1)
		fu=input("=]> ")
		if fu=='1':
			os.system('clear')
			fraction_add()
		if fu=='2':
			os.system('clear')
			fraction_sub()
		if fu=='3':
			os.system('clear')
			fraction_multi()
		if fu=='4':
			os.system('clear')
			fraction_divide()
	if a=='7':
		os.system('clear')
		logo7()
		print(h1)
		l=int(input("Enter The Lenght = "))
		b=int(input("Enter The Base = "))
		(h)=(l**2)+(b**2)
		print("Hypotenuse = ",math.sqrt(h))
		print(h1)
		restart()
	if a=='8':
		clear()
		logo7()
		print(h1)
		print("1. Kelvin To Celsius [ ??K---> ??C ]")
		print("2. Celsius To Kelvin [ ??C---> ??K ]")
		print("3. Celsius To Fahrenheit [ ??C---> ??F ]")
		print("4. Fahrenheit To Celsius [ ??F---> ??C ]")
		print(h1)
		hji=input("==> ")
		if hji == '1':
			print()
			print(h1)
			k=float(input("Enter The ??k = "))
			c=k-(273.15)
			print(h1)
			print(k, "??k is equal" ,c , "??k")
			print(r1)
			restart()
		if hji == '2':
			print()
			print(h1)
			c=float(input("Enter The ??c = "))
			k=c+(273.15)
			print(h1)
			print(c, "??c is equal" ,k , "??k" )
			print(r1)
			restart()
		if hji == '4':
			print()
			print(h1)
			f=float(input("Enter The ??f = "))
			c=(f -32) * 5/9 
			print(f, "??f is equal" ,c , "??c" )
			print(h1)
			restart()
		if hji =='3':
			print()
			print(h1)
			c=float(input("Enter The ??c = "))
			f=(c * 9/5) + 32 
			print(c,"??c is equal", f,"??F")
			print(h1)
			restart()
	if a=='6':
		os.system('clear')
		logo7()
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
		clear()
		logo7()
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
		try:
			area = math.sqrt(s* (s-a) * (s-b) * (s-c))
		except ValueError:
			print()
			print("Thats Not a vaild Triangle")
			print()
			restart()
		print(" Area = ", area)
		print(h1)
		restart()
	if a=='5':
		clear()
		logo7()
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
		print("Wathch this video turtorial")
		os.system('xdg-open https://youtu.be/UcRtFYAz2Yo')
		print(h1)
		restart()
		print(h1)
	if a=='2':
		clear()
		logo7()
		print(h1)
		print(h1)
		print("1. Curved Surface Area")
		print("2. Total Surface Area")
		print("3. Simple Area")
		print(h1)
		c=input("1/2 ==> ")
		print(h1)
		if c=='1':
				clear()
				logo7()
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
			clear()
			logo7()
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
				restart()
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
				restart()
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
				clear()
				logo7()
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
		clear()
		logo7()
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
			print('Volume = ', a*a*a)
			print(h1)
			restart()
		if a3=='3':
			print(h1)
			h=int(input("Height = "))
			r=int(input("Radius = "))
			print("Volume = ", pi*r*r*h)
			print(h1)
			restart()
		if a3=='4':
			print(h1)
			r=int(input("Radius = "))
			h=int(input("Height = "))
			print("Volume = ", 1/3 *pi*r*r*h)
			print(h1)
			restart()
		if a3=='5':
			print(h1)
			r=int(input("Radius = "))
			print("Volume = ", 4/3*pi*r*r*r)
			print(h1)
			restart()
		if a3=='6':
			print(h1)
			r=int(input("Radius = "))
			print("Volume = ", 2/3*pi*r*r*r)
			print(h1)
			restart()
			

		else:
			r1()
	else:
		r1()			
##########################

if __name__ == '__main__':
	main()
