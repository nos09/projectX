###extracts the IP addresses from haproxy. we can set a warning if more than 2/3 IP's are extracted.

# to extract all IP
 while read line; do
  ip="$(grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' <<< "$line")";   echo "$ip"; done < /etc/haproxy/haproxy.cfg >> /tmp/test
## to remove empty lines

 sed -i '/^$/d'  /tmp/test
 
# to filetr local host IP
 server_ip= ""

 while read p; do   if [ $p != "127.0.0.1" ] && [ $p != $k ];   then   echo $server_ip;   fi; done < /tmp/test >> /tmp/test_new
 
  