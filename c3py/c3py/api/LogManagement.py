# -*- coding: utf-8 -*-
class LogManagement(object):

    def __init__(self, client):
        self.client = client

    def downloadLog(self, componentType, CCORegionId=None):
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
        if componentType=="CCM":
            uri = "/v1/downloadLogs?componentType=" + str(componentType)
        elif componentType=="CCO" and CCORegionId !=None:
            uri = "v1/downloadLogs?componentType=CCO&regionId=" + str(CCORegionId) 
        else:
            uri = "/v1/downloadLogs"
        
        response = self.client.get(uri)
        return response

    def viewLogElements(self, nodeType=None,regionId=None, nodeId=None):
        """   
                Name	View Log Elements		
        Description	View log levels and log tracking status for the CCO, CCM, or Application VM servers. See Locate Log Files for additional context.		
        Method	GET		
        URI	v1/logs (CCM)		
        			
        	v1/logs?nodeType=CCO&regionId=CloudRegionId (CCO)		
        	v1/logs?nodeType=WORKER &regionId=CloudRegionId &nodeId=nodeId (depends on the cloud – Application VM)		
        			
        CloudCenter Release	Introduced in CloudCenter 4.4.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        			
        	The following table provides additional details on permissions to issue this API.		
        			
        	Server	API Permissions	
        	CCM	Only root admin	
        	CCO	Any tenant admin with the following permissions:	
        			
        		Has access to the cloud region	
        		Has a user cloud account configured on the CCO	
        			
        	Worker (Application VM)	Any user who has MANAGE or AUTHORIZE access to the deployment environment used to start the job (that started the node).	
        			
        ESB Header	action (CCM): get.logs		
        			
        	action (CCO): get.logs		
        	actionparam: nodeType=CCO&regionId=CloudRegionId 		
        			
        	action (Application VM): get.logs		
        	actionparam: nodeType=WORKER &regionId=CloudRegionId &nodeId=nodeId (depends on the cloud)		
        		"""	

        uri = "/v1/logs"
        if nodeType=="CCO" and regionId!=None:
            uri = uri + "?nodeType=CCO&regionId=" + str(regionId)
        
        if nodeType=="WORKER" and regionId!=None and nodeId!=None:
            uri = uri + "?nodeType=WORKER&regionId=" + str(regionId) + "&nodeId=" + str(nodeId)
        
        response = self.client.get(uri)
        return response
            
    def updateLogElements(self, payload, nodeType=None,regionId=None, nodeId=None):
        """   
        Name	Update Log Elements
        Description	
        
        View log levels and log tracking status for the CCO, CCM, or Application VM servers. See Locate Log Files for additional context.
        Method	PUT
        URI	
        
            v1/logs (CCM must be up and running)
            v1/logs?nodeType=CCO&regionId=CloudRegionId (CCO must be up and running)
            v1/logs?nodeType=WORKER &regionId=CloudRegionId &nodeId=nodeId (the cloud must be in the RUNNING state and the Application VM must be configured and NodeReady)
        
        CloudCenter Release	Introduced in CloudCenter 4.4.
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            You can provide a varied combination of levels and status for each log package.
            You cannot enable and update the level together for any package. However, you can issue them as separate requests as displayed in the examples below.
        
            The following table provides additional details on permissions to issue this API.
            Server	API Permissions
            CCM	Only root admin
            CCO	Any tenant admin with the following permissions:
                Has access to the cloud region
                Has a user cloud account configured on the CCO
            Worker (Application VM)	Any user who has MANAGE or AUTHORIZE access to the deployment environment used to start the job (that started the node).
        
        ESB Header	
        
            action: put.logs (CCM must be up and running) 
            action: put.logs
            actionparam: nodeType=CCO&regionId=CloudRegionId (CCO must be up and running)
            action: put.logs
            actionparam: nodeType=WORKER &regionId=CloudRegionId &nodeId=nodeId (the cloud must be in the RUNNING state and the Application VM must be configured and NodeReady)
                """
                
        uri = "/v1/logs"
        if nodeType=="CCO" and regionId!=None:
            uri = uri + "?nodeType=CCO&regionId=" + str(regionId)
        
        if nodeType=="WORKER" and regionId!=None and nodeId!=None:
            uri = uri + "?nodeType=WORKER&regionId=" + str(regionId) + "&nodeId=" + str(nodeId)
        
        response = self.client.put(uri,payload)
        return response
