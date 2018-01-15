Component:  cat /etc/*release | grep -i COMPONENT | sed -e 's/"//g' | sed 's/.*=//'   or  cat /usr/local/osmosix/etc/component
version:cat /etc/*release | grep -i VERSION | head -1 |sed -e 's/"//g' | sed 's/.*=//'  or /usr/local/osmosix/etc/version
cloud:cat /usr/local/osmosix/etc/cloud

