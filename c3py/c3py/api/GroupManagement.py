# -*- coding: utf-8 -*-
class GroupManagement(object):

    def __init__(self, client):
        self.client = client

    def createGroup(self, tenantId,payLoad):
        """
        Name	Create Group
        Description	Creates a new User Group and enables the tenant administrator to grant specific access to a set of users in this group.
        Method	POST
        URI	v1/tenants/tenantId/groups
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.2 to include the createdBySso attribute.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header	action: create.tenants.tenantId.groups
        Args:
            tenantId: XYZ
            type:string
            groupId:ABC
            type:string

        """

        uri = "/v1/tenants/" + str(tenantId) + "/groups/"
        response = self.client.post(uri, payLoad)
        return response


    def viewGroups(self, tenantId,groupId=None):
        """
                Name	View Groups
        Description	Displays information for all Groups or for a specified user group within the specified tenant.
        Method	GET
        URI	v1/tenants/tenantId/groups
        	v1/tenants/tenantId/groups/groupId

        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.2 to include the createdBySso attribute.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	If you include a groupId to identify a user group, the response includes information for that user group only.

        ESB Header	action: get.tenants.tenantId.groups
        	action: get.tenants.tenantId.groups.groupId

                Args:
            tenantId: XYZ
            type:string
            groupId:ABC
            type:string


        """

        uri = "/v1/tenants/" + str(tenantId) + "/groups/"
        if groupId:
            uri = uri + str(groupId)
        response = self.client.get(uri)
        return response

    def updateGroup(self, tenantId,groupId,payload):
        """
        	Name	Update Group
        Description	Updates any attribute in the configured User Group with the specified Group ID within the specified tenant in this CloudCenter instance.
        Method	PUT
        URI	v1/tenants/tenantId/groups/groupId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.2 to include the createdBySso attribute.

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: update.tenants.tenantId.groups.groupId
        Args:
            tenantId: XYZ
            type:string
            groupId:ABC
            type:string

           """
        uri = "/v1/tenants/" + str(tenantId) + "/groups/"+str(groupId)
        response = self.client.put(uri,payload)
        return response

    def deleteGroup(self, tenantId,groupId):
        """
        	Name	Delete Group
        Description	Deletes the specified User Group within the specified tenant in this CloudCenter instance.
        Method	DELETE
        URI	v1/tenants/tenantId/groups/groupId
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: delete.tenants/tenantId/groups/groupId
        Args:
            tenantId: XYZ
            type:string
            groupId:ABC
            type:string

           """
        uri = "/v1/tenants/" + str(tenantId) + "/groups/"+str(groupId)
        response = self.client.delete(uri)
        return response
