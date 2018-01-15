#To verify haproxy service running or not
#!/bin/bash
SERVICE="haproxy"
if P=$(pgrep $SERVICE)
then
    echo "$SERVICE is running, PID is $P"
else
    echo "$SERVICE is not running"
fi

# to extract all IP
 while read line; do
  ip="$(grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' <<< "$line")";   echo "$ip"; done < /etc/haproxy/haproxy.cfg > /tmp/cc_raw_list
## to remove empty lines

 sed -i '/^$/d'  /tmp/cc_raw_list

# to filetr local host IP
 host_ip= "127.0.1.1"

 while read p; do   if [ $p != "127.0.0.1" ] && [ $p != $host_ip ];   then   echo $p;   fi; done < /tmp/cc_raw_list > /tmp/cc_ha_list

 ### to remove repeition

  awk '!a[$0]++' /tmp/cc_ha_list
