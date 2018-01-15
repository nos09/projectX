# -*- coding: utf-8 -*-
class TenantManagement(object):

    def __init__(self, client):
        self.client = client

    def createTenant(self, payLoad):
        """
    	Name	Create Tenant
        Description	Creates a new tenant and enables the tenant administrator to perform tenant management tasks.
        Method	POST
        URI	v1/tenants
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	The minAppFeeRate, ccTransactionFeeRate, revShareRate, and enableConsolidatedBilling, and the enableConsolidatedBilling attributes are deprecated.
        	Enhanced in CloudCenter 4.6.0 to include the includeDeleted query parameter and the deleted response parameter
        	Enhanced in CloudCenter 4.8.1 to include the createUserSecurityGroup and allowVmConnection attributes.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	To create a tenant, you must select an existing user as the tenant admin. So be sure to Create the User first. Once this user becomes a tenant administrator, his or her name is removed from the Users list. See Manage Admin Users for additional context.
        	Upload the logo image before creating a service (see Upload Logo). If you do not upload a logo and provide the existing logo path (loginLogo or homepageLogo) prior to creating a tenant, then the logo image from the currently-provided path is deleted and this logo image is moved to another location after the tenant is created.

        	The cliqr_user_security_group is created only if both the createUserSecurityGroup and the allowVmConnection attributes are both set to true. The security group is not created if a security group rule is not associated with it. See Security and Firewall Rules for additional context. See Example 2.

        ESB Header	action: create.tenants

        """
        uri = "/v1/tenants/"
        response = self.client.post(uri, payLoad)
        return response


    def viewTenant(self,detail=None,includeDeleted=None, tenantId=None):
        """
        Name	View Tenants
        Description	Displays configured information for all tenants or for the specified tenant. You can view a list by specifying any attribute used to create the tenant.
        Method	GET
        URI	v1/tenants
        	v1/tenants/tenantId
        	v1/tenants?detail=true
        	v1/tenants?includeDeleted=true

        CloudCenter Release	Introduced in CloudCenter 4.0.
        	The minAppFeeRate, ccTransactionFeeRate, revShareRate, and enableConsolidatedBilling attributes are deprecated.
        	Enhanced in CloudCenter 4.6.0 to include the includeDeleted query parameter and the deleted response parameter
        	Enhanced in CloudCenter 4.8.1 to include the createUserSecurityGroup and allowVmConnection attributes (see Create Tenant > Example 2)

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format. 
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	If you include a tenantId to identify a tenant, the response includes information for that tenant only.

        ESB Header	action: get.tenants
        	action: get.tenants.tenantId
        	action: get.tenants
        	actionparam: detail=true
        Args:tenantId: string
        includeDeleted:true
        detail:true

	        """

        uri = "/v1/tenants"

        if tenantId:
            uri = uri + "/" +  str(tenantId)
        if detail==None:
            uri = "uri + ?detail=true"
        elif includeDeleted==None:
            uri = uri + "?includeDeleted=true"
        response = self.client.get(uri)
        return response

    def updateTenant(self, tenantId,payload):
        """
        	Name	Update Tenant
        Description	Updates the configured details for this tenant based on the specified Tenant ID.
        Method	PUT
        URI	/v1/tenants/tenantId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	The minAppFeeRate, ccTransactionFeeRate, revShareRate, and enableConsolidatedBilling attributes are deprecated.
        	Enhanced in CloudCenter 4.6.0 to include the includeDeleted query parameter and the deleted response parameter
        	Enhanced in CloudCenter 4.8.1 to include the createUserSecurityGroup and allowVmConnection attributes.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Upload the logo image before creating a service (see Upload Logo). If you do not upload a logo and provide the existing logo path (loginLogo or homepageLogo) prior to creating a tenant, then the logo image from the currently-provided path is deleted and this logo image is moved to another location after the tenant is created.

        ESB Header	action: update.tenants.tenantId

           """
        uri = "/v1/tenants/" + str(tenantId)
        response = self.client.put(uri,payload)
        return response

    def deleteTenant(self, tenantId):
        """
        	Name	Delete Tenant (Asynchronous API)
        Description	Deletes the specified tenant.
        Method	DELETE
        URI	v1/tenants/tenantId
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.

        	The tenant deletion is successful only when the following conditions are completed:
         All the running jobs must be terminated for all users – users cannot be deleted before the jobs are terminated.
   	All users in the tenant are deleted
        	All the sub tenants under the tenant must be deleted prior to issuing this API call. If any sub-tenant is not deleted, then a validation message states that you do this first.
            ESB Header	action: delete.tenants.tenantId

           """
        uri = "/v1/tenants/" + str(tenantId)
        response = self.client.delete(uri)
        return response

    def performTenantActions(self, userId):
        """
                Name	Perform Tenant Actions (Asynchronous API)
        Description	Identifies actions that users can perform within a tenant (at least one attribute is required).
        This API is useful when you promote a user to be the tenant owner admin. All actions are subject to having the required permissions (see Permission Control for additional context).
        Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        Method	POST
        URI	/v1/users/userId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	API Notes:
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	See Asynchronous APIs for additional context.
        	Assign Tenant Actions Notes:
        	Unspecified attributes are not changed.
        ESB Header	action: create.users.userId
"""
        uri = "/v1/users/" + str(userId)
        response = self.client.put(uri)
        return response
