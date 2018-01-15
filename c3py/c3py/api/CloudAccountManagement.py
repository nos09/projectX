#coding=utf-8

class CloudAccountManagement(object):

    def __init__(self, client):
        self.client = client

    def createCloudAccount(self, tenantId, cloudId, payLoad):
        """
        Name	Create Cloud Account (Asynchronous API)
        Description	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        Method	POST
        URI	v1/tenants/tenantId/clouds/cloudId/accounts
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Continue to query the Location URL until this call returns a success or failure HTTP Status Codes.
        	See Asynchronous APIs for additional context.

        ESB Header	action: create.tenants.tenantId.clouds.cloudId.accounts

        """

        uri = "v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId) +"/accounts"
        response = self.client.post(uri, payLoad)
        return response

    def viewCloudAccount(self, tenantId, cloudId, cloudAccountId=None,accountName=None, MyDisplayName=None):
        """
        Name	View Cloud Accounts
        Description	Displays information for each cloud account or for a specified cloud account within the specified tenant.
        Method	GET
        URI	v1/tenants/tenantId/clouds/cloudId/accounts
        	v1/tenants/tenantId/clouds/cloudId/accounts/cloudAccountId 
        	v1/tenants/tenantId/clouds/cloudId/accounts?accountName=me@mycompany.com  
        	v1/tenants/tenantId/clouds/cloudId/accounts?displayName=My Display Name                  

        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	If you include a cloudAccountId, accountName, or displayName, the response includes information for the cloud account with that ID, name, or display name only.
        	You can include both an accountName and displayName, in which case the response includes information for the cloud account with that name and display name only.
        	Only cloud account owners and users with WRITE perms (at a minimum) can view all the fields for a cloud account. Other users can only view common fields like account name, display name, description, and so forth. See Permission Control for additional context.

        ESB Header	action: get.tenants.tenantId.clouds.cloudId.accounts
        	action: get.tenants.tenantId.clouds.cloudId.accounts.cloudAccountId 
        	action: get.tenants.tenantId.clouds.cloudId.accounts
        	actionparam: accountName=me@mycompany.com  
        	action: get.tenants.tenantId.clouds.cloudId/accounts
        	actionparam: displayName=My Display Name  


        """

        uri = "v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId) +"/accounts/"
        if cloudAccountId:
            uri = uri + str(cloudAccountId)
        elif accountName:
            uri = uri + "?accountName=" + str(accountName)
        elif MyDisplayName:
            uri = uri + "?displayName" + str(MyDisplayName)
        response = self.client.get(uri)
        return response



    def updateCloudAccount(self, tenantId, cloudId ,cloudAccountId, payLoad):
        """
        Name	Update Cloud Accounts by Cloud Account ID.
        Description	Update the configured details for a cloud account specified by the cloudAccountId within the specified tenant. 
        Method	PUT
        URI	v1/tenants/tenantId/clouds/cloudId/accounts/cloudAccountId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: update.tenants.tenantId.clouds.cloudId.accounts.cloudAccountId

        """

        uri = "v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId) +"/accounts/" + str(cloudAccountId)
        response = self.client.put(uri, payLoad)
        return response

    def deleteCloudAccount(self, tenantId, cloudId ,cloudAccountId):
        """
        Name	Delete Cloud Account
        Description	Deletes the specified cloud account from the specified cloud within the specified tenant.
        Method	DELETE
        URI	v1/tenants/tenantId/clouds/cloudId/accounts/cloudAccountId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: delete.tenants.tenantId.clouds.cloudId.accounts.cloudAccountId

        """

        uri = "v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId) +"/accounts/" + str(cloudAccountId)
        response = self.client.delete(uri)
        return response

    def performCloudAction(self, tenantId, cloudId ,cloudAccountId, payLoad):
        """
        Name	Perform Cloud Account Actions (Asynchronous API)
        Description	Allows you to configure cloud account actions.

        	Unspecified attributes are not changed.
        Method	POST
        URI	v1/tenants/tenantId/clouds/cloudId/accounts/cloudAccountId 
        CloudCenter Release	Introduced in CloudCenter 4.1.2
        Notes	API Notes:

        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	See Synchronous and Asynchronous APIs for additional context

        	User Action Notes:

        	The request body changes based on the selected action.

        ESB Header	action: create.tenants.tenantId.clouds.cloudId.accounts.cloudAccountId

        """

        uri = "v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId) +"/accounts/" + str(cloudAccountId)
        response = self.client.post(uri, payLoad)
        return response
