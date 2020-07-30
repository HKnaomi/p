# install badvpn
cd
apt-get -y install cmake make gcc libc6-dev
wget https://raw.githubusercontent.com/janda09/private/master/badvpn-1.999.128.tar.bz2
tar xf badvpn-1.999.128.tar.bz2
mkdir badvpn-build
cd badvpn-build
cmake badvpn-1.999.128 -DBUILD_NOTHING_BY_DEFAULT=1 -DBUILD_UDPGW=1
make install
echo 'badvpn-udpgw --listen-addr 127.0.0.1:7500 > /dev/nul &' >> /etc/rc.local
badvpn-udpgw --listen-addr 127.0.0.1:7500 > /dev/nul &
cd /usr/bin
wget https://raw.githubusercontent.com/janda09/private/master/badvpn-udpgw
chmod 755 badvpn-udpgw
cd
