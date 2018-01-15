#****list********

Generic code to check the service running or not be checking the ports

 STAT=`netstat -lpn | grep :$port_no | awk '{print $7}'`
if [ "$STAT" != "" ]; then  echo "DEFAULT TOMCAT PORT IS LISTENING, SO ITS OK"; else echo "8080 PORT IS NOT IN USE SO TOMCAT IS NOT WORKING"; fi

#####CCM

ports: 22/sshd
tomcat: 80/443
ccm-cco: -8443
If monitor present: 4560/8881

db: 5432

*****HA****
master-slave: 5703


########DB

db:5432

******HA

22
2224
3121
5432
5405
21064

######CCM_LB
ports: 22/sshd
tomcat: 80/443
ccm-cco: -8443

########CCO#######

ports: 22/sshd
tomcat: 80/443
ccm-cco: -8443
If monitor present: 4560/8881

******************HA

master-slave: 27017


#############CCO_LB
ports: 22/sshd
ccm-cco: -8443


#############AMQP###########
ports: 22/sshd
tomcat: 80/443
ccm-cco: -8443
worker-amqp:5671
Guacomole: 7788/7789

*************HA

master-slave: 4369/25672


*************AMQP_LB Ports
ssh:22
http:443
worker-amqp:5671
Guacomole: 7788/7789


 
###############Monitor
ssh:22
logstach:4560
logstach:8881
Browser:8882
ccm-vm:8443


#############Repo server
ssh:22
bootstrao\p:80
worker:5000

