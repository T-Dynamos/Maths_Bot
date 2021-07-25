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
mv $HOME/m_bot/setup.py $PREFIX/bin/mbot
chmod 777 $PREFIX/bin/mbot
rm -rf $HOME/mbot
echo -e Installing ...
pip install colorama
pip install requests
pip install table-ex
mbot
