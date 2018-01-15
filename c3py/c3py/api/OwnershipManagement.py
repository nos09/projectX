# -*- coding: utf-8 -*-

class OwnershipManagement(object):

    def __init__(self, client):
        self.client = client

    def updateOwnershipStatus(self, report=None,dependent=None,payLoad=None ):
        """
        Name	Update Ownership Transfer
        Description	Updates ownership of CloudCenter Resources in addition to listing errors during the transfer process as specified in the Transferring Ownership use case.
        Method	PUT
        URI	v1/acls/transfer?report=true&dependents=true

        	v1/acls/transfer?report=true

        	v1/acls/transfer?dependents=true

        	v1/acls/transfer

        CloudCenter Release	Introduced in CloudCenter 4.8.1.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Understand possible errors during the transfer process by using the report=true&dependents=true optional query parameters. Used for validation of complete ownership transfer, that is, including dependent resource ownership (if source user is the owner).
        	Transfer complete ownership, including dependent resources, by using the dependents=true optional query parameter.
        	Transfer ownership without dependencies by not using an optional query parameter.

        ESB Header	action: update.acls.transfer
        	actionparam: report=true&dependents=true

        	action: update.acls.transfer
        	actionparam: dependents=true

        	action: update.acls.transfer

        Args:
        report:string
        type: true/None
        dependent: string
        type:true/None
        """
        uri = "/v1/acls/transfer"

        if report or  dependent :
            uri= uri + "?report=" + str(report) + "&dependents=" + str(dependent)

        response = self.client.put(uri,payLoad)
        return response

    def viewDeploymentsAndVMs(self,sourceId):
        """
                Name	View Deployments and VMs
        Description	Displays a a complete list of deployments and virtual machines as explained in the Transferring Ownership use case.
        Method	GET
        URI	v1/acls/transfer/sourceUserId/resources
        CloudCenter Release	Introduced in CloudCenter 4.8.1.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The resources attribute is mandatory in the request URI.
        	Only resource owners and users with WRITE perms can view all the fields for this resource. Other users can only view common fields like name, description, and so forth.
        	See Permission Control for additional context.

        ESB Header	action: create.acls.transfer.sourceUserId.resources

        """
        uri = "/v1/acls/transfer/"+ str(sourceId)+  "/resources"

        response = self.client.get(uri)
        return response
