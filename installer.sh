clear
apt update 
apt install git -y
apt upgrade -y
apt install wget
apt install python -y
pip install lolcat
cd $HOME
rm -rf m_bot
git clone https://github.com/T-Dynamos/Maths_Bot m_bot
cd /data/data/com.termux/files/usr/bin
wget https://raw.githubusercontent.com/T-Dynamos/termux-pro/main/mbot
chmod +x *
cd
clear
echo -e Installing ...
pip install colorama
pip install requests
pip install table-ex
mbot
