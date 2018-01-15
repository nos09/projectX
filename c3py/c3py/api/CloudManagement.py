class CloudManagement(object):

    def __init__(self, client):
        self.client = client

    def createCloud(self, tenantId,payLoad):
        """
        Name	Create Cloud		
        Description	Creates a new cloud representation in the specified tenant.		
        Method	POST		
        URI	v1/tenants/tenantId/clouds		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: create.tenants.tenantId.clouds		
               
        Args:
            tenantID: XYZ
                Type: String
        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/"
        response = self.client.post(uri, payLoad)
        return response
    
    
    def view(self, tenantId,cloudId=None,detail=None):
        """
        Name	View Clouds		
        Description	Displays information for each cloud or for a specified cloud within the specified tenant. 		
        Method	GET		
        URI	v1/tenants/tenantId/clouds		
        	v1/tenants/tenantId/clouds?detail=true		
        	v1/tenants/tenantId/clouds/cloudId		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
        	If you include a cloudId to identify a cloud, the response only includes information for that cloud.		
        			
        ESB Header	action: get.tenants.tenantId.clouds		
        	action: get.tenants.tenantId.clouds		
        	actionparam: detail=true		
        	action: get.tenants.tenantId.clouds.cloudId		
        Args:
            tenantID: XYZ
                Type: String
            cloudId: ABC
                Type: String
            detail: TRUE/FALSE
                Type: Boolean
			        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" 
        if cloudId:
            uri = uri + str(cloudId)
        elif detail==True:
            uri = "/v1/tenants/" + str(tenantId) + "/clouds?detail=true"
        response = self.client.get(uri)
        return response
    
    def updateCloud(self, tenantId,cloudId,payload):
        """
        Name	Update Cloud		
        Description	Update a  cloud representation in the specified tenant.		
        Method	POST		
        URI	v1/tenants/tenantId/clouds/cloudId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.tenants.tenantId.clouds		
        
        Args:
            tenantID: XYZ
                Type: String
            cloudId: ABC
                Type: String
           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)
        response = self.client.put(uri,payload)
        return response
    
    def delete(self, tenantId,cloudId):
        """
	        Name	Delete Clouds		
        Description	Delete specified cloud within the specified tenant. 		
        Method	DELETE		
        URI	v1/tenants/tenantId/clouds/cloudId		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        
        ESB Header	
        	action: delete.tenants.tenantId.clouds.cloudId		
        Args:
            tenantID: XYZ
                Type: String
            cloudId: ABC
                Type: String
           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)
        response = self.client.delete(uri)
        return response