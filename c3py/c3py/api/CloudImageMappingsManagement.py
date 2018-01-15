class CloudImageMappingsManagement(object):

    def __init__(self, client):
        self.client = client

    def createCloudImageMapping(self, tenantId,cloudId,regionId,payLoad):
        """
        Name	Create Cloud Image Mapping	
        Description	Creates a new image mapping for the specified cloud region. See Manage Images  for additional context on mapping the logical image to ensure that this API call is successful.	
        Method	POST	
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/images	
        CloudCenter Release	Introduced in CloudCenter 4.0.	
        	Enhanced in CloudCenter 4.2 to include the supportHardwareProvision and the localStorageCount  attributes.	
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.	
        		
        Notes	API Notes:	
        		
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.	
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.	
        		
        	Cloud Image Mapping Notes:	
        		
        	At least one valid entry in the mappings attribute is required for this API call to succeed.	
        	The id attribute is required for each cloudInstanceType listed in the mappings array.	
        		
        ESB Header	action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.images	

        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/images"
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewCloudImageMapping(self, tenantId,cloudId,regionId,cloudImageId=None):
        """
        Name	View Cloud Image Mapping		
        Description	Displays information for each mapped image or for a specific image for the identified cloud region. See Manage Images for additional context.		
        Method	GET		
        URI	v1/tenants/tenantId/clouds/cloudId/regions/regionId/images		
        	v1/tenants/tenantId/clouds/cloudId/regions/regionId/images/cloudImageId		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
        	If you include a cloudImageId to identify a cloud image, the response includes information for that cloud image only.		
        			
        ESB Header	action: get.tenants.tenantId.clouds.cloudId.regions.regionId.images		
        	action: get.tenants.tenantId.clouds.cloudId.regions.regionId.images.cloudImageId		
        			

        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/images/"
        if cloudImageId:
            uri = uri + str(cloudImageId)
        response = self.client.get(uri)
        return response
    
    def updateCloudImageMapping(self, tenantId,cloudId,regionId,cloudImageId,payload):
        """
        Name	Update Cloud Image Mapping		
        Description	Updates the specified image mapping for the identified cloud region. See Manage Images  for additional context. 		
        Method	PUT		
        URI	v1/tenants/tenantId/clouds/cloudId/regions/regionId/images/cloudImageId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.tenants.tenantId.clouds.cloudId.regions.regionId.images.cloudImageId		
           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/images/"+str(cloudImageId)
        response = self.client.put(uri,payload)
        return response
    
    def deleteCloudImageMapping(self, tenantId,cloudId,regionId,cloudImageId):
        """
        Name	Delete Cloud Image Mapping		
        Description	Delete the specified image mapping for the identified cloud region. See Manage Images  for additional context. 		
        Method	DELETE		
        URI	v1/tenants/tenantId/clouds/cloudId/regions/regionId/images/cloudImageId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: delete.tenants.tenantId.clouds.cloudId.regions.regionId.images.cloudImageId		
           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/images/"+str(cloudImageId)
        response = self.client.delete(uri)
        return response
    
    def syncCloudRegionImageMapping(self, tenantId,cloudId,regionId,cloudImageId):
        """
        Name	Sync Cloud Region Image Mappings		
        Description	Syncs cloud image mappings from the Package Store. This feature allows administrators to sync information when they see a change in the cloud provider image mapping definition. 		
        			
        	This API can only be invoked for one cloud region at a time; not all cloud regions belonging to a cloud.		
        Method	POST		
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/syncImageMappings		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	A successful response returns a HTTP 200.		
        	This API is only applicable:		
        	For Public Clouds and currently only available for AWS and SoftLayer.		
        			
        	For system (see Manage Images) images for supported clouds.		
        			
        ESB Header	action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.syncImageMappings		
		
           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/syncImageMappings"
        response = self.client.post(uri)
        return response