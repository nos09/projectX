class CloudStorageManagement(object):

    def __init__(self, client):
        self.client = client

    def createCloudStorageType(self, tenantId,cloudId,regionId,payLoad):
        """
        Name	Create Cloud Storage Type
        Description	Creates a new storage type for the specified cloud region. See Configure Cloud Storage for additional context.
        Method	POST
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/storageTypes
        CloudCenter Release	Introduced in CloudCenter 4.7.0
        	Updated in CloudCenter 4.8.2 to have configurable values for minVolumeSize and maxVolumeSize.

        Notes	API Notes:

        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	Cloud Storage Types Notes:
        	At least one valid entry in the storage attribute is required for this API call to succeed.
        	The id attribute is required for each cloudStorageType listed in the mappings array.

        ESB Header	action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.storageTypes

        Args:
            tenantID: XYZ
                Type: String
            cloudId: ABC
                Type: String
            cloudRegionId: PQR
                Type: string

        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" + str(regionId) + "/storageTypes"
        response = self.client.post(uri, payLoad)
        return response


    def viewCloudStorageType(self, tenantId,cloudId,regionId,storageTypeId=None):
        """
                API	 Details
        Name

        View Cloud Storage Type(s)
        Description

        Displays information for each storage type for the specified cloud region. See Configure Cloud Storage for additional context.
        Method	GET
        URI

            v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/storageTypes
            v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/storageTypes/storageTypeId

        CloudCenter Release

            Introduced in CloudCenter 4.7.0

        Notes

            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
            If you include a storageTypeId to identify a cloud storage, the response includes information for that cloud storage only.

        ESB Header

            action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.storageTypes
            action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.storageTypes.storageTypeId
        Args:
            tenantID: XYZ
                Type: String
            cloudId: ABC
                Type: String
            cloudRegionId: PQR
                Type: string
            storageTypeId: MNO
                Type: string

        """

        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/storageTypes/"
        if storageTypeId:
            uri = uri + str(storageTypeId)
        response = self.client.get(uri)
        return response

    def updateCloudStorageType(self, tenantId,cloudId,regionId,storageTypeId,payload):
        """
                Name	View Cloud Storage Type(s)
        Description	Displays information for each storage type for the specified cloud region. See Configure Cloud Storage for additional context.
        Method	GET
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/storageTypes
        	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/storageTypes/storageTypeId

        CloudCenter Release	Introduced in CloudCenter 4.7.0

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	If you include a storageTypeId to identify a cloud storage, the response includes information for that cloud storage only.

        ESB Header	action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.storageTypes
        	action: create.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.storageTypes.storageTypeId


	        Args:
            tenantID: XYZ
                Type: String
            cloudId: ABC
                Type: String
            cloudRegionId: PQR
                Type: string
            storageTypeId: MNO
                Type: string
           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" + str(regionId) + "/storageTypes/" + str(storageTypeId)
        response = self.client.put(uri,payload)
        return response

    def deleteCloudStorageType(self, tenantId,cloudId,regionId,storageTypeId):
        """
        Name	Update Cloud Storage Type
        Description	Updates the specified storage type for the specified cloud region. See Configure Cloud Storage for additional context.
        Method	PUT
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/storageTypes/storageTypeId
        CloudCenter Release	Introduced in CloudCenter 4.7.0
        	Updated in CloudCenter 4.8.2 to have configurable values for minVolumeSize and maxVolumeSize.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: update.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.storageTypes.storageTypeId

	        Args:
            tenantID: XYZ
                Type: String
            cloudId: ABC
                Type: String
            cloudRegionId: PQR
                Type: string
            storageTypeId: MNO
                Type: string
        """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/storageTypes/" + str(storageTypeId)
        response = self.client.delete(uri)
        return response

    def syncCloudStorageTypeRegion(self, tenantId,cloudId,regionId):
        """
                Name	Sync Cloud Storage Types
        Description	Syncs cloud storage from the Package Store. This feature allows administrators to sync information when they see a change in the cloud provider storage type definition'

        	This API can only be invoked for one cloud region at a time; not all cloud regions belonging to a cloud.
        Method	PUT
        URI	v1/tenants/tenantId/clouds/cloudId/regions/cloudRegionId/syncStorageTypes
        CloudCenter Release	Introduced in CloudCenter 4.7.0

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	A successful response returns a HTTP 200.

        ESB Header	action: put.tenants.tenantId.clouds.cloudId.regions.cloudRegionId.syncStorageTypes


        Args:
            tenantID: XYZ
                Type: String
            cloudId: ABC
                Type: String
            cloudRegionId: PQR
                Type: string
                """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/syncStorageTypes"
        response = self.client.post(uri)
        return response
