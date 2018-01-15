class CloudPropertiesManagement(object):

    def __init__(self, client):
        self.client = client

    def viewCloudInstanceType(self,regionName=None,propertyType=None,depEnvId=None,cloudAccountid=None,AccessKeyPairs=None):
        """
                Name	View Cloud Properties		
        Description	Displays information about cloud properties for the specified region.		
        Method	GET		
        URI	v1/cloudProperties/regionName		
        	v1/cloudProperties/regionName?propertyType=propertyType&depEnv=depEnvId&cloudAccount=cloudAccountid		
        	v1/cloudProperties/cloudType?propertyType=AccessKeyPairs&depEnv=depEnvId&TenantId=TenantId		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	Enhanced in CloudCenter 4.1.1 to include the TenantName and TenantId attributes (see OpenStack Configurations for additional context).		
        	Enhanced in CloudCenter 4.7.2 to include the Google Cloud Platform Network and AvailableNetworks options in the propertyType attribute.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
        	You can display information for a specific property, deployment environment, and account by including the propertyType, depEnv, and/or cloudAccount query parameters with this API.		
        			
        ESB Header	action: get.cloudProperties.regionName		
        	action: get.cloudProperties.regionName		
        	actionparam: propertyType=propertyType&depEnv=depEnv&cloudAccount=cloudAccount		
        	action: get.cloudProperties.cloudType		
        	actionparam: propertyType=AccessKeyPairs&depEnv=depEnvId&TenantId=TenantId		
        			Args:
                        


        """
        if str(regionName):
            if str(propertyType) and str(depEnvId) and str(cloudAccountid):
                uri = "/v1/cloudProperties" + str(regionName) + "/?propertyType=" + str(propertyType) + "&depEnv=" + str(depEnvId) + "&cloudAccount=" + str(cloudAccountid)
            uri = "/v1/cloudProperties/" + str(regionName) 
#        if :
#            uri = uri + str(cloudImageId)
        response = self.client.get(uri)
        return response
