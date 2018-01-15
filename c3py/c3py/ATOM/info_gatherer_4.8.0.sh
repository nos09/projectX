##***********4.8.2***************##


########     CCM      ################

CCM server LB/DNS NAME/DNS IP :   sed -n -e "/publicDnsName/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/server.properties | sed -e 's/"//g'
Monitor:awk -F'[/:]' '/monitorBaseUrl/{print $4}' /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/server.properties
DATABASE IP: sed -n -e "/database.postgres.host/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/db.properties | sed -e 's/"//g' | head -1
DNS Name: sed -n -e "/outfaceDnsName/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/server.properties | sed -e 's/"//g'
ELK host: sed -n -e "/elkHost/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/server.properties | sed -e 's/"//g'

#########       HA      #######
checker file :/usr/local/osmosix/etc/harole ## 



#************DB******************########   For CCO IP  we can use the API , but in that case we need the API key so let me check the DB way
sed -n -e "/database.postgres.host/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/db.properties | sed -e 's/"//g' | head -1



####################
****************
*******************DB****************

"""PGPASSWORD=cliqr psql -U cliqr -d cliqrdb -c "select gateway_ip_addr from cloud_gateway_status" | tail -3 | head -1"""


################################
*****************
*******************************CCO******************
##############################
Rabbit   sed -n -e "/gateway.brokerHost/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/rabbit-gateway.properties
Guacomole:  sed -n -e "/connection.broker.host/ s/.*= *//p" /usr/local/osmosix/etc/rev_connection.properties


Bundle store IP :  sed -n -E "/agent.bundle.url/ s/.*(http|https):\/\/*//p"  /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/gateway.properties | grep -Po '[^/]*' | head -1
Docker registry:  sed -n -e "/service.docker.registry.url/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/gateway.properties
Docker server/External executioner:sed -n -e "/container.docker.server.ip/ s/.*= *//p" /usr/local/osmosix/etc/container.properties
*******HA***************

Primary IP: sed -n -e "/prim_ip/ s/.*= *//p" /usr/local/osmosix/etc/cco_ha_info | sed -e 's/"//g' | head -1
Sec IP:  sed -n -e "/sec_ip/ s/.*= *//p" /usr/local/osmosix/etc/cco_ha_info | sed -e 's/"//g' | head -1
Ter IP:  sed -n -e "/ter_ip/ s/.*= *//p" /usr/local/osmosix/etc/cco_ha_info | sed -e 's/"//g' | head -1






***************************
###################################################
***********************AMQP************************

If HA , info can be acquired from HAproxy

