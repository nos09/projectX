# -*- coding: utf-8 -*-

class FederatedManagement(object):

    def __init__(self, client):
        self.client = client

    def initiateFederatedLinkfromParentCCM(self, tenantId,regionId,payLoad):
        """
                Name	Initiate Federated Link from Parent CCM
        Description	During the federated registration process, the tenant admin for the Parent CCM initiates the request to link to a Subordinate CCM by providing the Child CCM's URL and Tenant Name along with the tenant admin's credentials (email and password).
        Method	POST
        URI	v1/tenants/tenantId/links
        CloudCenter Release	Introduced in CloudCenter 4.3.
        Notes	Available in CloudCenter 4.3 to 4.5.
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.

        	To allow a parent CCM to manage the subordinate CCM, the subordinate CCM tenant administrator must be registered with the parent CCM tenant. Admins can link:


        	One Subordinate CCM tenant to only one Parent CCM tenant
        	Multiple tenants within one Subordinate CCM to one Parent CCM tenant
        	The Child CCM tenant admin receives an email and a system notification on the first login after the request is sent.

        ESB Header	action: create.tenants.tenantId.links


        """

        uri = "/v1/tenants/" + str(tenantId) + "/links/"
        response = self.client.post(uri, payLoad)
        return response

    def ApproveLinkRequestfromChildCCM(self, tenantId,linkId,payLoad):
        """
          Name	Approve Link Request from Child CCM
        Description	The tenant admin for the Child CCM receives a request and can decide the permissions to provide to the Parent CCM when approving the request.
        Method	PUT
        URI	v1/tenants/tenantId/links/linkId
        CloudCenter Release	Introduced in CloudCenter 4.3.
        Notes	Available in CloudCenter 4.3 to 4.5.
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The Child CCM tenant admin can change the assigned permissions even after the link exchange is established.
        	Other than these permission options, all other information is visible and accessible by the Parent CCM

        ESB Header	action: update.tenants.tenantId.links.linkId

      """
        uri = "/v1/tenants/" + str(tenantId) + "/links/" + str(linkId)
        response = self.client.put(uri, payLoad)
        return response

    def ApproveLinkConfirmationfromParentCCM(self, tenantId,linkId,payLoad):
        """
        Name	Accept Link Confirmation from Parent CCM
        Description	The tenant admin for the Parent CCM accepts the confirmation that is received from the Child CCM's tenant adminstrator
        Method	PUT
        URI	v1/tenants/tenantId/links/linkId
        CloudCenter Release	Introduced in CloudCenter 4.3.
        Notes	Available in CloudCenter 4.3 to 4.5.
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	If this handshake using each other's certificate is mutually authenticated, the link is successfully established.

        	Once a link request is approved between the parent and the subordinate, the Child CCM admin must import the parent certificate (Upload Link Certificate) to its trust store and sends its own certificate back to the parent.

        ESB Header	action: update.tenants.tenantId.links.linkId

         """
        uri = "/v1/tenants/" + str(tenantId) + "/links/" + str(linkId)
        response = self.client.put(uri, payLoad)
        return response

    def ViewEstablishedLinkDetails(self, tenantId,linkId=None):
        """
        Name	View Established Link Details
        Description	Displays configured information for the specified, established link in a federated deployment (see Federated CCM Management for additional context).
        Method	GET
        URI	v1/tenants/1/links
        	v1/tenants/1/links/7

        CloudCenter Release	Introduced in CloudCenter 4.3.
        Notes	Available in CloudCenter 4.3 to 4.5.
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.

        ESB Header	action: delete.tenants.tenantId.links.linkId

         """
        uri = "/v1/tenants/" + str(tenantId) + "/links/"
        if linkId:
            uri = uri + + str(linkId)
        response = self.client.get(uri)
        return response

    def ViewChildCCMDetails(self, tenantId):
        """
        Name	View Child CCM Details
        Description	Displays configured information for all Child CCMs or for the specified Child CCM in a federated deployment (see Federated CCM Management for additional context).
        Method	GET
        URI	v1/tenants/3/links?type=CLOUD_CENTER_LINK_TO_CHILD
        CloudCenter Release	Introduced in CloudCenter 4.5.2.
        Notes	Available in CloudCenter 4.5.2. 
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	When submitting jobs from a linked Child CCM in a Federated CCM environment, use the additional target CCID parameter, -H "x-cliqr-ccid: ccm4", in the HTTP header. In place of ccm4, use your remote deployment identifier, CloudCenter ID (CCID) – remoteCloudCenterId, that is included in the response to this API call (see the example below).

        ESB Header	action: get.tenants.tenantId
        	actionparam: type=CLOUD_CENTER_LINK_TO_CHILD

         """
        uri = "/v1/tenants/" + str(tenantId) + "/links?type=CLOUD_CENTER_LINK_TO_CHILD/"
        response = self.client.get(uri)
        return response

    def ViewParentCCMDetails(self, tenantId):
        """
        Name	View Parent CCM Details
        Description	Displays configured information for the specified Parent CCM in a federated deployment (see Federated CCM Management for additional context).
        Method	GET
        URI	v1/tenants/3/links?type=CLOUD_CENTER_LINK_TO_PARENT
        CloudCenter Release	Introduced in CloudCenter 4.5.2.
        Notes	Available in CloudCenter 4.5.2. 
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.

        ESB Header	action: get.tenants.tenantId
        	actionparam: type=CLOUD_CENTER_LINK_TO_PARENT


         """
        uri = "/v1/tenants/" + str(tenantId) + "/links?type=CLOUD_CENTER_LINK_TO_PARENT/"
        response = self.client.get(uri)
        return response

    def UpdateLinkPermissionsfromChildCCM(self, tenantId,linkId,payLoads):

        """
        Name	Update Link Permissions from Child CCM
        Description	Allows the Child CCM tenant admin to update the Parent Manager Permission Options (remoteLaunchOk, remoteTerminationOk, remotePolicyCreationOk, and remoteAppProfileCreationOk) any time after the link is established.
        Method	PUT
        URI	v1/tenants/tenantId/links/linkId
        CloudCenter Release	Introduced in CloudCenter 4.3.
        Notes	Available in CloudCenter 4.3 to 4.5.
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	If this handshake using each other's certificate is mutually authenticated, the link is successfully established.

        	Once a link request is approved between the parent and the subordinate, the Child CCM admin can update the Parent Manger Permission options. This task does not require approval by the Parent CCM.

        ESB Header	action: update.tenants.tenantId.links.linkId

	         """
        uri = "/v1/tenants/" + str(tenantId) + "/links/" + str(linkId)
        response = self.client.put(uri,payLoads)
        return response

    def UpdateAccesstoChildCCMACLfromParentCCM(self, tenantId,linkId,payLoads):

        """
        Name	Update Link Permissions from Child CCM
        Description	Allows the Child CCM tenant admin to update the Parent Manager Permission Options (remoteLaunchOk, remoteTerminationOk, remotePolicyCreationOk, and remoteAppProfileCreationOk) any time after the link is established.
        Method	PUT
        URI	v1/tenants/tenantId/links/linkId
        CloudCenter Release	Introduced in CloudCenter 4.3.
        Notes	Available in CloudCenter 4.3 to 4.5.
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	If this handshake using each other's certificate is mutually authenticated, the link is successfully established.

        	Once a link request is approved between the parent and the subordinate, the Child CCM admin can update the Parent Manger Permission options. This task does not require approval by the Parent CCM.

        ESB Header	action: update.tenants.tenantId.links.linkId

	         """
        uri = "/v1/acls/"
        response = self.client.put(uri,payLoads)
        return response

    def PropagateChangestoChildCCM(self,resourceId,propagatableResourceType,payLoads):

        """
                Name	Propagate Changes to Child CCM (Asynchronous API)
        Description Propagates resource changes to the specified Child CCM if the resource owner configured this information (Save future changes to selected Linked Subordinate Managers) for the specified Parent CCM in a federated deployment (see Federated CCM Management for additional context).
        Method	POST
        URI	v1/resources/resourceId/type/propagatableResourceType

        CloudCenter Release	Introduced in CloudCenter 4.5.2.

        Notes

            Available in CloudCenter 4.5.2.

            API Notes:
                For additional context on <PORT> usage in the following example(s), see Base URI Format.
                See Asynchronous APIs for additional context.
                Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
                The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
             Propagation Notes:
                You can only propagate the following CloudCenter resources (see Federated CCM Management for additional context):
                    Applications
                    Application Profiles
                    Services
                    Policies (action, custom, scaling, and aging policies)
                Each Child CCM has its own sub-task and corresponding Link ID for each sub-task listed in the subtaskResults section.

                Once a link is established and a user has the required permission in a federated CCM environment, this user can use the Parent CCM credentials and DNS name to make REST calls to the Child CCM. Parent CCM users must remember to use the Child CCM Resource ID if they want to configure the corresponding resource on the Child CCM.

        ESB Header	 action: create.resources.resourceId.type.propagatableResource
        """
        uri = "/v1/resources/" + str(resourceId) + "/type/" + str(propagatableResourceType)
        response = self.client.post(uri,payLoads)
        return response

    def ViewPropagatedLinkDetails(self,resourceId,propagatableResourceType,resourceIds=None):

        """
                Name	View Propagated Link Details
        Description	Displays the propagated link details for each Child CCM if the resource owner configured this information (Save future changes to selected Linked Subordinate Managers) for the specified Parent CCM in a federated deployment (see Federated CCM Management for additional context).
        Method	GET
        URI

            v1/resources/resourceId/type/propagatableResourceType
            v1/resources/resourceId/type/propagatableResourceType/?resourceIds=resourceId,resourceId,...

        CloudCenter Release	Introduced in CloudCenter 4.5.2.
        Notes

            Available in CloudCenter 4.5.2.

            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
            You can only propagate the following CloudCenter resources (see Federated CCM Management for additional context):
                Applications
                Application Profiles
                Services
                Policies (action, custom, scaling, and aging policies)
            When you propagate a resource from the parent to the child CCM, CloudCenter adds the propagated resource details to both sides.

        ESB Header

        action: get.resources.resourceId.type.propagatableResource
           """
        uri = "/v1/resources/" + str(resourceId) + "/type/" + str(propagatableResourceType)
        if resourceId:
            uri = uri + str(resourceIds)
        response = self.client.get(uri)
        return response

    def DeleteEstablishedLink(self, tenantId,linkId):
        """"
        Name	Delete  Established Link
        Description	Deletes an established link in a federated setup from the Parent CCM.
        Method	DELETE
        URI	v1/tenants/tenantId/links/linkId
        CloudCenter Release	Introduced in CloudCenter 4.3.
        Notes	Available in CloudCenter 4.3 to 4.5.
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	Once approved, the Child CCM cannot delete the link to the Parent CCM.

        ESB Header	action: delete.tenants.tenantId.links.linkId
        """
        uri = "/v1/tenants/" + str(tenantId) + "/links/" + str(linkId)
        response = self.client.put(uri)
        return response
