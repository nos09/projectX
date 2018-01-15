class CloudProviderManagement(object):

    def __init__(self, client):
        self.client = client
        
    def view(self, tenantId,cloudProviderName=None):
        """
        Name	View Cloud Providers		
        Description	Displays cloud capability information for all cloud providers or for a specified cloud provider.		
        Method	GET		
        URI	v1/cloudProviders		
        	v1/cloudProviders/cloudProviderName               		
        			
        CloudCenter Release	Introduced in CloudCenter 4.8.1.		
        Notes	General:		
        			
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	This API is visible to any logged-in user.		
        			
        	API Notes:		
        			
        	These API settings are ignored when deploying on other clouds as it is only supported for the following clouds:		
        	Amazon		
        	VMware with ACI extension enabled		
        	AzureRM		
        	OpenStack 		
        	Alibaba		
        			
        ESB Header	action: get.cloudProviders		
        	action: get.cloudProviders.cloudProviderName		
            
			

			        """

        uri = "v1/cloudProviders/" 
        if cloudProviderName:
            uri = uri + str(cloudProviderName)
        response = self.client.get(uri)
        return response