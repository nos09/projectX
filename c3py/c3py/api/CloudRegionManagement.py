class CloudRegionManagement(object):

    def __init__(self, client):
        self.client = client

    def createCloudRegion(self, tenantId,cloudId,regionId,payLoad):
        """
        Name	Create Cloud Region
        Description	Creates a new cloud region for the specified tenant on the supported cloud.
        Method	POST
        URI	v1/tenants/tenantId/clouds/cloudId/regions
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.5.1 to include the externalActions and externalBundleLocation attributes so you can configure External Service Deployment Lifecycle actions (Pre-VM start, Pre-VM stop, and so forth) at the cloud region level.
        	Enhanced in CloudCenter 4.8.0 to ensure that the enabled parameter is set to true if you do not specify it in the payload.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header	action: create.tenants.tenantId.clouds.cloudId/.regions
        Args
        tenantId:XY
            Type: string
        cloudId:XY
            Type:String

        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/"
        response = self.client.post(uri, payLoad)
        return response

    def viewCloudRegion(self, tenantId,cloudId,regionId=None):
        """
        Name	View Cloud Regions
        Description	Displays information for each cloud region or for a specified cloud region for the specified cloud within the specified tenant.  
        Method	GET
        URI	v1/tenants/tenantId/clouds/cloudId/regions
        	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId

        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.5.1 to include the externalActions and externalBundleLocation attributes so you can configure External Service Deployment Lifecycle actions (Pre-VM start, Pre-VM stop, and so forth) at the cloud region level.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	If you include a cloudRegionId to identify a cloud region, the response includes information for that cloud region only.

        ESB Header	action: get.tenants.tenantId.clouds.cloudId.regions
        	action: get.tenants.tenantId.clouds.cloudId.regions.cloudRegionId
          Args
        tenantId:XY
            Type: string
        cloudId:XY
            Type:String
        regionId:XY
            Type:String


        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/"
        if regionId:
            uri = uri + str(regionId)
        response = self.client.get(uri)
        return response

    def updateCloudRegion(self, tenantId,cloudId,regionId,payload):
        """
        	Name	Update Cloud Region
        Description	Updates a configured cloud region for the specified tenant using the specified Cloud Region ID.  
        Method	PUT
        URI	vi/tenants/tenantId/clouds/cloudId/regions/cloudRegionId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.5.1 to include the externalActions and externalBundleLocation attributes so you can configure External Service Deployment Lifecycle actions (Pre-VM start, Pre-VM stop, and so forth) at the cloud region level.
        	Enhanced in CloudCenter 4.8.0 to ensure that the enabled parameter is set to true if you do not specify it in the payload.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Do not edit the display name, even if configurable.

        ESB Header	action: update.tenants.tenantId.clouds.cloudId.regions.cloudRegionId
        Args
        tenantId:XY
            Type: string
        cloudId:XY
            Type:String
        regionId:XY
            Type:String

           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId)
        response = self.client.put(uri,payload)
        return response

    def deleteCloudRegion(self, tenantId,cloudId,regionId):
        """
        	Name	Delete Cloud Region
        Description	Deletes the specified cloud region from the specified cloud within the specified tenant.

        	This operation succeeds if all jobs in the cloud region across the system have already been terminated and no deployment environment in the system has a mapping to this cloud region. See Cloud Region Configuration for additional context.

        	Effective 4.7.0: You can delete cloud regions – even after jobs have been run on this region.

        	You can now delete Cloud Regions even after the CCO has been registered.

        	Cloud owners can delete regions if there are no running deployments and no association of the region in a Deployment Environment – If there are any, remove them first before trying this operation.

        	Ensure that all the jobs submitted in this region have already been terminated.

        Method	DELETE
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Admins can delete a Cloud region if a CCO was not registered for this region.

        	CloudCenter 4.6.x and Earlier Releases: As other resources (for example, obs or accounts or users) are already associated with an activated cloud region, you cannot perform the following tasks:
        	You can only delete a cloud region if it is not activated.

        	You cannot de-activate an activated cloud region.

        	Effective CloudCenter 4.7.0: You can delete cloud regions – even after jobs have been run on this region.

        ESB Header	action: delete.tenants.tenantId.clouds.cloudId.regions.cloudRegionId
        Args
        tenantId:XY
            Type: string
        cloudId:XY
            Type:String
        regionId:XY
            Type:String
           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId)
        response = self.client.delete(uri)
        return response
