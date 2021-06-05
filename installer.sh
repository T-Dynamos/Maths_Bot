clear
apt update 
apt upgrade -y
apt install wget
cd /data/data/com.termux/files/usr/bin
wget https://raw.githubusercontent.com/T-Dynamos/termux-pro/main/mbot
cd
clear
echo -e Installing ...
pip install colorama
pip install requests
pip install table-ex
