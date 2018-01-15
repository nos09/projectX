class ActivationProfilesManagement(object):

    def __init__(self, client):
        self.client = client

    def createActivationProfile(self, tenantId, payLoad):
        """
        Name:	Create Activation Profile
        Description:
        Creates a new activation profile and enables the Tenant Administrator to activate users with defaults for a plan, bundle, contract, deployment environment, cloud(s) assignment, and application profile(s) that can be imported from the Marketplace.
        Method	POST
        URI	v1/tenants/tenantId/activationProfiles
        CloudCenter Release	Introduced in CloudCenter 4.0.

        Notes:

        For additional context on <PORT> usage in the following example, see Base URI Format.
        Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header:
        	action: create.tenants.tenantId.activationProfiles
        """

        uri = "/v1/tenants/" + str(tenantId) + "/activationProfiles"
        response = self.client.post(uri, payLoad)
        return response

    def viewActivationProfiles(self, tenantId, activationProfileId=None):
        """
        Name:       View Activation Profiles
        Description:
        Displays information for all activation profiles or for a specified activation profile within the specified tenant.
        Method	GET

        URI:
            v1/tenants/tenantId/activationProfiles
            v1/tenants/tenantId/activationProfiles/activationProfileId

        CloudCenter Release	Introduced in CloudCenter 4.0.

        Notes:
        For additional context on <PORT> usage in the following example, see Base URI Format.
        The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        If you include an activationProfileId to identify an activation profile, the response includes information for that activation profile only.

        ESB Header:
            action: get.tenants.tenantId.activationProfiles
            action: get.tenants.tenantId.activationProfiles.activationProfileId
        """

        uri = "/v1/tenants/" + str(tenantId) + "/activationProfiles"
        if activationProfileId:
            uri = "/v1/tenants/" + str(tenantId) + "/activationProfiles/" + str(activationProfileId)
        response = self.client.get(uri)
        return response

    def updateActivationProfile(self, tenantId, activationProfileId, payLoad):
        """
        Name:	Update Activation Profiles by Activation Profile ID
        Description:
        Updates information for the specified activation profiles within the specified tenant.
        Method:	PUT
        URI:	v1/tenants/tenantId/activationProfiles/activationProfileId

        CloudCenter Release:	Introduced in CloudCenter 4.0.

        Notes:	For additional context on <PORT> usage in the following example, see Base URI Format.
        ESB Header:
        	   action: update.tenants.tenantId.activationProfiles.activationProfileId
        """

        uri = "/v1/tenants/" + str(tenantId) + "/activationProfiles/" + str(activationProfileId)
        response = self.client.put(uri, payLoad)
        return response

    def deleteActivationProfile(self, tenantId, activationProfileId):
        """
        Name:	Delete Activation Profile
        Description:
        Delete the specified activation profile within the specified tenant.
        Method:	DELETE
        URI:	v1/tenants/tenantId/activationProfiles/activationProfileId

        CloudCenter Release:	Introduced in CloudCenter 4.0.

        Notes:	For additional context on <PORT> usage in the following example, see Base URI Format.
        ESB Header:
        	action: delete.tenants.tenantId.activationProfiles.activationProfileId
        """

        uri = "/v1/tenants/" + str(tenantId) + "/activationProfiles/" + str(activationProfileId)
        response = self.client.delete(uri)
        return response
