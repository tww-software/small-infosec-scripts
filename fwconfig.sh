#!/bin/bash
#configure firewall script

#check if root

if (($UID!=0)); then
    echo 'you need to run this as root'
    exit 1
fi

echo "enter LAN interface:"
read LAN_INTERFACE

#flush existing rules and block everything
iptables -F
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

# loopback interface allowed
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# allow DNS traffic out
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p udp --sport 53 -j ACCEPT

# allow DHCP
iptables  -I INPUT -i $LAN_INTERFACE -p udp --dport 67:68 --sport 67:68 -j ACCEPT

# allow web out
iptables -A OUTPUT -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT

# allow secure  web out
iptables -A OUTPUT -p tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --sport 443 -m state --state ESTABLISHED -j ACCEPT

# python web server stuff out
iptables -A OUTPUT -p tcp --dport 8000 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --sport 8000 -m state --state ESTABLISHED -j ACCEPT

# python web server stuff in
iptables -A INPUT -p tcp --dport 8000 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 8000 -m state --state ESTABLISHED -j ACCEPT

# SSH out
iptables -A OUTPUT -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

# SSH in
iptables -A INPUT -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

echo 'firewall rules updated'
exit
