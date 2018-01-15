##***********4.8.2***************##


########     CCM      ################

CCM server LB/DNS NAME/DNS IP :   sed -n -e "/MGMTSERVER_DNSNAME/ s/.*= *//p" /etc/sysconfig/mgmtserver.conf | sed -e 's/"//g' | head -1
DATABASE IP: sed -n -e "/DATABASE_POSTGRES_HOST/ s/.*= *//p" /etc/sysconfig/mgmtserver.conf | sed -e 's/"//g' | head -1
ELK host: sed -n -e "/ELK_HOST/ s/.*= *//p" /etc/sysconfig/mgmtserver.conf | sed -e 's/"//g' | head -1

#########       HA      #######
checker file :/usr/local/osmosix/etc/harole ## 
Primary CCM IP:  sed -n -e "/PRIM_IP/ s/.*= *//p" /etc/sysconfig/mgmtserver.conf | sed -e 's/"//g' | head -1
Sec CCM IP:  sed -n -e "/SEC_IP/ s/.*= *//p" /etc/sysconfig/mgmtserver.conf | sed -e 's/"//g' | head -1



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
Rabbit for host:  sed -n -e "/RABBIT_GATEWAY_BROKERHOST/ s/.*= *//p" /etc/sysconfig/gateway.conf | sed -e 's/"//g' | head -1
Rabbit for worker: sed -n -e "/RABBIT_AGENT_BROKERHOST/ s/.*= *//p" /etc/sysconfig/gateway.conf | sed -e 's/"//g' | head -1
Guacomole:  sed -n -e "/CONNECTION_BROKER_HOST/ s/.*= *//p" /etc/sysconfig/gateway.conf | sed -e 's/"//g' | head -1


Bundle store IP :  sed -n -E "/BUNDLE_STORE_URL/ s/.*(http|https):\/\/*//p"  /etc/sysconfig/gateway.conf | grep -Po '[^/]*' | head -1
Docker registry:  sed -n -E "/SERVICE_DOCKER_REGISTRY_URL/ s/.*(http|https):\/\/*//p"  /etc/sysconfig/gateway.conf | grep -Po '[^/]*' | head -1
Docker server/External executioner: sed -n -e "/CONTAINER_DOCKER_SERVER_IP/ s/.*= *//p" /etc/sysconfig/gateway.conf | sed -e 's/"//g' | head -1

*******HA***************

Primary IP: sed -n -e "/PRIM_IP/ s/.*= *//p" /etc/sysconfig/gateway.conf | sed -e 's/"//g' | head -1
Sec IP:  sed -n -e "/SEC_IP/ s/.*= *//p" /etc/sysconfig/gateway.conf | sed -e 's/"//g' | head -1
Ter IP:  sed -n -e "/TER_IP/ s/.*= *//p" /etc/sysconfig/gateway.conf | sed -e 's/"//g' | head -1






***************************
###################################################
***********************AMQP************************

If HA , info can be acquired from HAproxy

