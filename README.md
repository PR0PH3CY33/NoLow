# NoLow
It is a python program that hooks unto the network stack of Linux and rate limits the connections coming to your server at a specific port

# Usage

 - First, create the nfqueue bind hook: 
 
    -> iptables -A INPUT -p tcp --dport 443 -j NFQUEUE --queue-num 1
    
  - this will create an nfqueue bind numbered 1 for that specific rule.
  
  - Second, run this program that will rate limit each ip address with only 10 simultaneous connections per second.
