
pkg install figlet
clear
figlet   INSTALLING... 
cyan='\e[0;36m'
lightgreen='\e[1;32m'
red='\e[1;31m'
yellow='\e[1;33m'
echo -e $lightgreen "\e[32m Maths bot Setup Wizard"
echo -e $lightgreen "\e[32m Wait Patiently..."
pkg upgrade
pip install requests
pip install colorama
pip install table-ex
clear
python setup.py



