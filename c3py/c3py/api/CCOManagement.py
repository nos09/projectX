class CCOManagement(object):

    def __init__(self, client):
        self.client = client

    def updateCCOConfig(self, tenantId,cloudId,regionId,payLoad):
        """
        Name	Update CCO Configuration		
        Description	Use this API for both the initial CCO registration as well as subsequent updates for a cloud group. See CCO and Register the CCO with the CCM for additional context.		
        Method	PUT		
        URI	v1/tenants/tenantId/clouds/cloudId/regions/regionId/gateway		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example, see Base URI Format.		
        ESB Header	action: update.tenants.tenantId.clouds.cloudId.regions.regionId.gateway		

        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/gateway"
        response = self.client.put(uri, payLoad)
        return response
    
    
    def viewCCOConfig(self, tenantId,cloudId,regionId):
        """
        Name	View CCO Configuration		
        Description	Use this API to view the CCO registration details. See CCO and Register the CCO with the CCM for additional context.		
        Method	GET		
        URI	v1/tenants/tenantId/clouds/cloudId/regions/regionId/gateway		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example, see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
        			
        ESB Header	action: get.tenants.tenantId.clouds.cloudId.regions.regionId.gateway		
		

        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/gateway"
        response = self.client.get(uri)
        return response