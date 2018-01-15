class BundleManagement(object):
    def __init__(self, client):
        self.client = client

    def createBundle(self, tenantId, payLoad):
        """
        Name:	Create Bundle		
        Description:	Creates a new bundle and enables the Tenant Administrator Tasks to grant specific access to users assigned this bundle.		
        Method:	POST		
        URI:	v1/tenants/tenantId/bundles		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        vides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.		
        ESB Header	action: create.tenants.tenantId.bundles		   
        """

        uri = "/v1/tenants/" + str(tenantId) + "/bundles/"
        response = self.client.post(uri,payLoad)
        return response

    def viewBundles(self, tenantId, bundleId):
        """
    	Name	View Bundles		
    	Description	Displays information for each bundle or for a specified bundle within the specified tenant.		
    	Method	GET		
    	URI	v1/tenants/tenantId/bundles		
    		 v1/tenants/tenantId/bundles/bundleId		
    				
    	CloudCenter Release	Introduced in CloudCenter 4.0.		
    	Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
    		The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
    		If you include a bundleId to identify a bundle, the response includes information for that bundle only. 		
    				
    	ESB Header	action: get.tenants.tenantId.bundles		
    		action: get.tenants.tenantId.bundles.bundleId		
				
        """

        uri = "/v1/tenants/" + str(tenantId) + "/bundles/"
        if bundleId:
            uri = uri + str(bundleId)
        response = self.client.get(uri)
        return response

    def updateBundle(self, tenantId,bundleId, payload):
        """
        Name	Update Bundle		
        Description	Updates the configured details for a bundle specified by the Bundle ID within a specified tenant.		
        Method	PUT		
        URI	v1/tenants/tenantId/bundles/bundleID		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.tenants.tenantId.bundles.bundleID		

        """

        uri = "/v1/tenants/" + str(tenantId) + "/bundles/" + str(bundleId)
        response = self.client.put(uri,payload)
        return response
    
    def deleteBundle(self, tenantId,bundleId):
        """
        Name	Delete Bundle		
        Description	Deletes the specified bundle within the specified tenant in this CloudCenter instance.		
        Method	DELETE		
        URI	v1/tenants/tenantId/bundles/bundleId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: delete.tenants.tenantId.bundles.bundleId		
        """

        uri = "/v1/tenants/" + str(tenantId) + "/bundles/" + str(bundleId)
        response = self.client.delete(uri)
        return response