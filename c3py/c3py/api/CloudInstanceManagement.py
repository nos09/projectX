class CloudInstanceManagement(object):

    def __init__(self, client):
        self.client = client

    def createCloudInstanceType(self, tenantId,cloudId,regionId,payLoad):
        """
        Name	Create Cloud Instance Type
        Description	Creates a new cloud instance types (see Map Images) for the specified cloud Region.
        Method	POST
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/instanceTypes
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.2 to include the supportHardwareProvision and the localStorageCount  attributes.
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header	action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.instanceTypes


        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/instanceTypes"
        response = self.client.post(uri, payLoad)
        return response


    def viewCloudInstanceType(self, tenantId,cloudId,regionId,cloudInstanceTypeId=None):
        """

        Name	View Cloud Instance Types
        Description	Displays information for each cloud instance type (see Map Images) or for a specified cloud instance type  for the specified cloud and cloud region within the specified tenant.
        Method	GET
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/instanceTypes
        	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/instanceTypes/cloudInstanceTypeId

        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.2 to include the supportHardwareProvision and the  localStorageCount attributes.
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview > Pagination  section for additional context.
        	If you include a cloudInstanceTypeId to identify a cloud instance type, the response includes information for that cloud cloud instance type only.

        ESB Header	action: get.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.instanceTypes
        	action: get.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.instanceTypes.
        	cloudInstanceTypeId


        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/instanceTypes/"
        if cloudInstanceTypeId:
            uri = uri + str(cloudInstanceTypeId)
        response = self.client.get(uri)
        return response

    def updateCloudInstanceType(self, tenantId,cloudId,regionId,cloudInstanceTypeId,payload):
        """
        	Name	Update Instance Type by Instance Type ID
        Description	Update a configured cloud instance type (see Map Images) for the specified cloudRegion by providing the Instance Type ID.
        Method	PUT
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/instanceTypes/cloudInstanceTypeId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.2 to include the supportHardwareProvision and the localStorageCount  attributes.
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: update.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.instanceTypes.
        	cloudInstanceTypeId

           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/instanceTypes/"+str(cloudInstanceTypeId)
        response = self.client.put(uri,payload)
        return response

    def deleteCloudInstanceType(self, tenantId,cloudId,regionId,cloudInstanceTypeId):
        """
		Name	Delete Instance Type by Instance Type ID
        Description	Delete a configured cloud instance type (see Map Images) for the specified cloudRegion by providing the Instance Type ID.
        Method	PUT
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/instanceTypes/cloudInstanceTypeId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.2 to include the supportHardwareProvision and the localStorageCount  attributes.
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: delete.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.instanceTypes.
        	cloudInstanceTypeId
           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/instanceTypes/"+str(cloudInstanceTypeId)
        response = self.client.delete(uri)
        return response

    def syncCloudRegionInstanceType(self, tenantId,cloudId,regionId,cloudImageId):
        """
        Name	Sync Cloud Instance Types
        Description	This API allows administrators to sync information when they see a change in cloud provider instance type definitions and price information. See Manage Instance Types for additional context. 

        	Public Clouds: The instance type information is synced from the Package Store.
        	Datacenters and Private Clouds (only applicable to OpenStack only): The instance type information is directly synced from the cloud.

        Method	POST
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/syncInstanceTypes
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	A successful response returns a HTTP 200.
        	Sync instances is only supported for Amazon, SoftLayer, and OpenStack clouds (see the description above for additional context).
        	Sync instances is not supported for VMware.

        ESB Header	action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.syncInstanceTypes

           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/syncInstanceTypes"
        response = self.client.post(uri)
        return response

    def createCloudInstanceTypeOverride(self, tenantId,payLoad):
        """
        Name	Create Cloud Instance Type Override
        Description	Allows administrators to configure an instance type override for users within the tenant.
        Method	POST
        URI	v1/tenants/tenantId/tenantInstanceTypes
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.

        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header	action: create.tenants.tenantId.tenantInstanceTypes

           """
        uri = "/v1/tenants/" + str(tenantId) + "/tenantInstanceTypes/"
        response = self.client.post(uri,payLoad)
        return response

    def viewCloudInstanceTypeOverride(self, tenantId,tenantInstanceTypeId=None):
        """
        Name	View Cloud Instance Type Override
        Description	Displays administrators to configure an instance type override for users within the tenant.
        Method	View
        URI	v1/tenants/tenantId/tenantInstanceTypes
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.

        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header	action: get.tenants.tenantId.tenantInstanceTypes

           """
        uri = "/v1/tenants/" + str(tenantId) + "/tenantInstanceTypes/"
        if tenantInstanceTypeId:
            uri = uri + str(tenantInstanceTypeId)
        response = self.client.get(uri)
        return response

    def updateCloudInstanceTypeOverride(self, tenantId,tenantInstanceTypeId,payLoad):
        """
        Name	Update Cloud Instance Type Override
        Description	Allows administrators to update an instance type override for users within the tenant.
        Method	PUT
        URI	v1/tenants/tenantId/tenantInstanceTypes
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.

        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header	action: update.tenants.tenantId.tenantInstanceTypes

           """
        uri = "/v1/tenants/" + str(tenantId) + "/tenantInstanceTypes/" + str(tenantInstanceTypeId)
        response = self.client.put(uri,payLoad)
        return response
