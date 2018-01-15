class ACLManagement(object):

    def __init__(self, client):
        self.client = client

    def viewACLEntities(self):
        """
        Name:	View ACL Entities
        Description:
        	Displays applicable permissions for CloudCenter Resources managed by Access Control Lists (ACLs) (ACLs).
        Method:	GET
        URI:    v1/aclResources

        CloudCenter Release
        Introduced in CloudCenter 4.2.
        Enhanced in CloudCenter 4.3 to include the IMAGE resourceName.

        Notes:
        For additional context on <PORT> usage in the following example(s), see Base URI Format.
        Only resource owners and users with WRITE perms can view all the fields for this resource. Other users can only view common fields like name, description, and so forth. See Permission Control for additional context.

        ESB Header:
    	   action: create.aclResources
        """

        uri = "/v1/aclResources"
        response = self.client.get(uri)
        return response

    def viewACLResourceDetails(self, resourceID, resourceName):
        """
        Name:	View ACL Resource Details
        Description:	Displays configured permissions for CloudCenter Resources managed by Access Control Lists (ACLs).

        Method:	GET
        URI:	v1/acls/?id=id&resourceName=resourceName

        CloudCenter Release	Introduced in CloudCenter 4.2.

        Notes:
        For additional context on <PORT> usage in the following example(s), see Base URI Format.
        The resourceName attribute is mandatory in the request URI.
        If you include a resourceType to identify a CloudCenter resource, the response includes information for that resource only.
        Only resource owners and users with WRITE perms can view all the fields for this resource. Other users can only view common fields like name, description, and so forth. See Permission Control for additional context.

        ESB Header:
        action: create.acls
        actionparam: id=id&resourceName=resourceName
        """

        uri = "/v1/acls/?id=" + str(resourceID) + "&" + "resourceName=" + resourceName
        response = self.client.get(uri)
        return response

    def updateACLResourceDetails(self, payLoad):
        """
        Name:	Update ACL Resource Details
        Description:
        Updates permissions for any CloudCenter Resource managed by Access Control Lists (ACLs).

        Method:	PUT
        URI:	v1/acls/

        CloudCenter Release	Introduced in CloudCenter 4.2.

        Notes:
        For additional context on <PORT> usage in the following example(s), see Base URI Format.
        The resourceName attribute is mandatory in the request URI.

        ESB Header:
        	action: update.acls
        """
        uri = "/v1/acls/"
        response = self.client.put(uri, payLoad)
        return response
