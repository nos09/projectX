# -*- coding: utf-8 -*-

class InventoryManagement(object):

    def __init__(self, client):
        self.client = client

    def listVMs(self, tenantId,regionName,depEnvId, payLoad, ccmOnly=True):
        """
        Name	List VMs
        Description	Displays configured information for all VMs or for the specified VM. You can view a list by specifying any attribute used to Create Tenant.
        Method	GET
        URI	v1/tenants/tenantId/vms?regionName=regionName&depEnvId=depEnvId&ccmOnly=true

        	v1/tenants/tenantId/vms?regionName=regionName&depEnvId=depEnvId&nonCcmOnly=true

        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Updated in CloudCenter 4.6.1 to include vmOperationData.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	The response includes information for the specified tenantId only.
        	Use the View Deployment Environments to retrieve the depEnvId.
        	You can display information for VMs in a specific tenant by including the regionName, depEnvId, and type of deployment environment (ccmOnly or nonCcmOnly) query parameters with this API.

        ESB Header	action: get.tenants.tenantId.vms
        	actionparam: regionName=regionName&depEnvId=depEnvId&ccmOnly=true

        	action: get.tenants.tenantId.vms
        	actionparam: regionName=regionName&depEnvId=depEnvId&nonCcmOnly=true


        """

        uri = "/v1/tenants/"+ str(tenantId) + "/vms?regionName=" +str(regionName) + "&depEnvId=" + str(depEnvId)
        if str(ccmOnly)=="true":
           uri = uri + "&ccmOnly=true"
        response = self.client.get(uri, payLoad)
        return response


    def poweroffvms(self, tenantId,ImagesId=None,details=None):
        """

            """
        pass

    def viewunmanagedClouds(self, tenantId):
        """
        Name	View Non-Managed (nonManaged) Cloud Details
        Description	Displays information for each cloud region or for a specified cloud region for the specified cloud within the specified tenant.  
        Method	GET
        URI	v1/tenants/tenantId/nonManagedClouds
        CloudCenter Release	Introduced in CloudCenter 4.6.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.

        	For all available cloud families, logged-in users see all regions to which each user has access.

        	If the cloud regions status ≠ RUNNING (based on last known status in the CCM database), then this cloud region is not displayed.

        	Displays all cloud accounts owned by the user in that cloud family. Any cloud account that is explicitly shared to this user is not displayed.

        	If a cloud group has no regions or cloud accounts available – if either the size of cloudRegions or cloudAccounts = 0, then the cloud family is not displayed (both attributes are required to retrieve this list from the CCO).

            ESB Header	action: get.tenants.tenantId.nonManagedClouds


           """
        uri = "/v1/tenants/" + str(tenantId) + "/nonManagedClouds/"
        response = self.client.get(uri,payload)
        return response
