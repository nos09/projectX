#!/usr/bin/python3
import traceback
import sys
from jumpssh import SSHSession

# -*- coding: utf-8 -*-

class get_comp_ip(object):
    def __init__(self, ccm_ip, user, password=None, pKey=None):

        """
        Get components Ips as a dictionary
        To initiate the class it needs the following arguments:

        Args:
            ccm_ip: ccm ip, be it a load balancer. But it needs to have ssh capability
            user: login id of the ssh user
            password: ssh password
            pKey: private key for ssh
        """

        self.ccm_ip = ccm_ip
        self.user = user
        self.password = password
        self.pKey = pKey
        try:
            self.server = SSHSession(self.ccm_ip, self.user, password=self.password).open()
        except:
            print("Unable to initiate ssh connection")
        self.compList = {}

    def check_if_lb(self):
        checker_file_cmd = "ls /etc/haproxy/haproxy.cfg"
        if self.server.get_exit_code(checker_file_cmd) == 0:
            return True
        else:
            return False

    def check_if_HA(self):
        checker_file_cmd = "ls /usr/local/osmosix/etc/harole"

        if self.server.get_exit_code(checker_file_cmd) == 0:
            primary_ccm_ip_cmd = """sed -n -e "/PRIM_IP/ s/.*= *//p" /etc/sysconfig/mgmtserver.conf | sed -e 's/"//g' | head -1"""
            sec_ccm_ip_cmd =  """sed -n -e "/SEC_IP/ s/.*= *//p" /etc/sysconfig/mgmtserver.conf | sed -e 's/"//g' | head -1"""

            self.compList['primary_ccm_ip'] = self.server.get_cmd_output(primary_ccm_ip_cmd)
            self.compList['sec_ccm_ip'] = self.server.get_cmd_output(sec_ccm_ip_cmd)

            return True
        else:
            return False

    def check_version(self):
        pass

    def get_info(self):

        ccm_ip = """sed -n -e "/publicDnsName/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/server.properties | sed -e 's/"//g'"""
        postgres_ip = """sed -n -e "/database.postgres.host/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/db.properties | sed -e 's/"//g' | head -1"""
        cco_ip = """PGPASSWORD=cliqr psql -U cliqr -d cliqrdb -c "select gateway_ip_addr from cloud_gateway_status" | tail -3 | head -1"""
        monitor_ip = """awk -F'[/:]' '/monitorBaseUrl/{print $4}' /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/server.properties"""
        guacamole_ip =  """sed -n -e "/connection.broker.host/ s/.*= *//p" /usr/local/osmosix/etc/rev_connection.properties"""
        rabbit_ip = """sed -n -e "/gateway.brokerHost/ s/.*= *//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/rabbit-gateway.properties"""
        repo_ip = """sed -n -e "/custom.repository.url/ s/.*http:\/\/*//p" /usr/local/apache-tomcat-8.0.29/webapps/ROOT/WEB-INF/gateway.properties"""
        docker_registry_ip = """sed -n -e "/container.docker.server.ip/ s/.*= *//p" /usr/local/osmosix/etc/container.properties"""

### Get components IPs from ccm
        self.compList['ccm'] = self.server.get_cmd_output(ccm_ip).strip()
        #print(self.compList['ccm'])
        self.compList['postgres'] = self.server.get_cmd_output(postgres_ip).strip()
        #print(self.compList['postgres'])
        if (self.compList['postgres'] == 'localhost'):
            self.compList['cco'] = self.server.get_cmd_output(cco_ip).strip()
        else:
            jumpHost_session = self.server.get_remote_session(self.compList['postgres'], password=self.password)
            self.compList['cco'] = jumpHost_session.get_cmd_output(postgres_ip).strip()
        self.compList['monitor'] = self.server.get_cmd_output(monitor_ip).strip()

#### Get components IPs from cco
        jumpHost_session = self.server.get_remote_session(self.compList['cco'], password=self.password)

        self.compList['guacamole_ip'] = jumpHost_session.get_cmd_output(guacamole_ip).strip()
        self.compList['rabbit_ip'] = jumpHost_session.get_cmd_output(rabbit_ip).strip()
        self.compList['repo_ip'] = jumpHost_session.get_cmd_output(repo_ip).strip()
        self.compList['docker_registry_ip'] = jumpHost_session.get_cmd_output(docker_registry_ip).strip()

    def check_status_service(self):
        pass

    def return_complist(self):
        self.get_info()
        return self.compList
