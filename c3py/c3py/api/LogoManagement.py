# -*- coding: utf-8 -*-

class LogoManagement(object):

    def __init__(self, client):
        self.client = client

    def upLoadLog(self, logoImageFile):
        """
                Name	Download Logs
        Description	Download logs for the CCO or CCM components. See Download Log File  for additional context.
        Method	GET
        URI	v1/downloadLogs?componentType=CCM (CCM)

        	v1/downloadLogs?componentType=CCO&regionId=CCORegionId  (CCO)

        CloudCenter Release	Introduced in CloudCenter 4.7.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.

        	Users with the following permissions can download log files:

        	Server	API Permissions
        	CCM	Only root admin
        	CCO	Any tenant admin with the following permissions:

        		Has access to the cloud region
        		Has a user cloud account configured on the CCO


        ESB Header	action (CCM): get.downloadLogs
        	actionparam: componentType=CCM 

        	action (CCO): get.logs
        	actionparam: componentType=CCO&regionId=CCORegionId


        """
        uri = "/appstore/upload   --form logoImageFile=" + str(logoImageFile)

        response = self.client.post(uri)
        return response
