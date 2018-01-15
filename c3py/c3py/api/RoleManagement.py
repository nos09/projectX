# -*- coding: utf-8 -*-

class RoleManagement(object):

    def __init__(self, client):
        self.client = client

    def createRole(self, tenantId,payLoad):
        """
        Name	Create Role
        Description	Creates a new User Role and enables the tenant administrator to grant specific access to users assigned this role.
        Method	POST
        URI	v1/tenants/tenantId/roles
        CloudCenter Release	 Introduced in CloudCenter 4.0.
            Effective 4.5.7:
                The perms attribute now includes the MANAGE_EXPORT and MANAGE_IMPORT options.
                The objectType attribute now includes the EXPORT and IMPORT options.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: create.tenants.tenantId.roles
        """

        uri = "/v1/tenants/" + str(tenantId) + "/roles/"
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewRole(self, tenantId,roleId=None):
        """
        Name View Roles
        Description	Displays information for each User Role or for a specified user role within the specified tenant.  
        Method	GET
        URI	 v1/tenants/tenantId/roles
            v1/tenants/tenantId/roles/roleId
        
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	  For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
            If you include a roleId to identify a role, the response includes information for that role only.
        
        ESB Header	 action: get.tenants.tenantId.roles
            action: get.tenants.tenantId.roles.roleId
        """

        uri = "/v1/tenants/" + str(tenantId) + "/roles/"
        if roleId:
            uri = uri + str(roleId)
        response = self.client.get(uri)
        return response
    
    def updateRole(self, tenantId,roleId,payload):
        """
        	Name	Update Role
        Description	Updates any attribute in the configured Roles with the specified Role ID within the specified tenant.
        Method	PUT
        URI	v1/tenants/tenantId/roles/roleId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: update.tenants.tenantId.roles.roleId
           """
        uri = "/v1/tenants/" + str(tenantId) + "/roles/"+str(roleId)
        response = self.client.put(uri,payload)
        return response
    
    def deleteRole(self,tenantId, roleId):
        """
        	Name	Delete Role
        Description	Deletes the specified User Role within the specified tenant in this CloudCenter instance.
        A Role ID is unique to a CloudCenter instance.
        Method	DELETE
        URI	v1/tenants/tenantId/roles/roleId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: delete.tenants.tenantId.roles.roleId
           """
        uri = "/v1/tenants/" + str(tenantId) + "/roles/"+str(roleId)
        response = self.client.delete(uri)
        return response

