SERVICE=""
if P=$(pgrep $SERVICE)
then
    echo "$SERVICE is running, PID is $P"
else
    echo "$SERVICE is not running"
fi


SERVCIE list / component

ccm:

config-server
cliqr-admin
hazelcast-server
mgmtserver
capacity-manager
notification


CCO:

capacity-collector
cliqr-cis
config-server
gateway
mongod

RABBIT
cliqr-connection-broker
cliqr-guacamole-client
config-server
beam.smp ##for rabbitmq server 


DB:
postmaster # postgres

DB HA
pcsd


