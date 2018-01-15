class ApplicationManagement(object):
    def __init__(self, client):
        self.client = client

    def deleteApplicationProfile(self, appId):
        """
        Name:	Delete Application Profile
        Description:	Deletes an Application Profile
        Method:	DELETE
        URI:	/v1/apps/appId
        CloudCenter Release:	CloudCenter 3.x and 4.x
        Notes:	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header:
        	action: delete.apps.appId
        """

        uri = "/v1/apps/" + str(appId)
        response = self.client.delete(uri)
        return response

    def exportApplicationProfiles(self, appId, *args):
        """
        Name:	Export Application Profiles
        Description:	Downloads and exports a zip file containing application profiles for all requested applications.
        Method:	GET
        URI:	/v1/apps/portation?appId=appId1&&appId=appId2&&appId=appIdN
        CloudCenter Release:	CloudCenter 3.x and 4.x
        Notes:	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header:
            action: get.apps
            actionparam: portation.appId=appId1&&appId=appId2&&appId=appIdN
        """

        uri = "/v1/apps/portation?appId=" + str(appId)
        for value in args:
            uri = uri + "&&appId=" + str(value)
        response = self.client.get(uri)
        return response

    def getAllVersionsofanApplication(self, appId):
        """
        Name:	Get All Versions of an Application
        Description:	Retrieve a list of all versions of an application
        Method:	GET
        URI:	/v1/apps/appId/allVersions
        CloudCenter Release:
            CloudCenter 3.x and 4.x
        Notes:	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header:
        	action: get.apps.appId.allVersions
        """

        uri = "/v1/apps/" + str(appId) + "/allVersions"
        response = self.client.get(uri)
        return response

    def getApplicationDetails(self, appId, appVersion=None):
        """
        Name:	Get Application Details
        Description:	Retrieve details of an application for a specific version. If no version is specified, this API retrieves details of the latest version.
        Method:	GET
        URI:
            /v1/apps/appId?version=appVersion
            /v1/apps/appId
        CloudCenter Release:
            CloudCenter 3.x and 4.x
            Enhanced in CloudCenter 4.1.2 to include the serviceTiers.hwprofile attributes
            Enhanced in CloudCenter 4.2 to:
                Change category to profileCategory
                Include the logoPath and appCategories attributes
            The supportsCuda and cudaSupport attributes are deprecated in CloudCenter 4.7.2.

        Notes:
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.

        ESB Header:
            action: get.apps.appId
            actionparam: version=appVersion
            action: get.apps/appId

        Args:
                appId: application ID
                appVersion: application version
        """
        uri = "/v1/apps/" + str(appId)
        if appVersion:
            uri = "/v1/apps/" + str(appId) + "?version=" + str(appVersion)
        response = self.client.get(uri)
        return response

    def getSupportedCloudDetails(self, appId, depEnvId, cloudId, appVersion):
        """
        Name:	Get Supported Cloud Details
        Description:	Retrieve details of supported cloud environments for the specified application(s) along with the instance types and properties
        Method:	GET
        URI:	 /v1/apps/appId/depEnvId/cloudConfigs/cloudId?version=appVersion
        CloudCenter Release:
            CloudCenter 3.x and 4.x
            Enhanced in 3.2.6.5 to include the depEnvId attribute
        Notes:
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.

        ESB Header:
            action: get.apps.appId.depEnvId.cloudConfigs.cloudId
            actionparam: version=appVersion

        Args:
                appId: application id
                depEnvId: deployment environment ID
                cloudId: cloud ID
                appVersion: version of the application

        Example:
            /v1/apps/64/1/cloudConfigs/Amazon-us-west-2?version=1.0
        """
        uri = " /v1/apps/" + str(appId) + str(depEnvId) + "cloudConfigs" + cloudId + "?version=" + str(appVersion)
        response = self.client.get(uri)
        return response

    def importApplicationProfiles(self, fileObj):
        """        Name:	Import Application Profiles
        Description:	Import application profiles into a system from a ZIP file containing profile definitions. See User States and Actions for additional context.
        Method:	POST
        URI:	/v1/apps/portation
        CloudCenter Release:	CloudCenter 3.x and 4.x
        Notes:
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header:
        	  action: create.apps.portation

        Args:
            fileObj: zip file containig application profiles.
        """

        uri = "/v1/apps/portation"
        response = self.client.post(uri, files=fileObj, fileName=fileName)
        return response

    def listApplications(self):
        """
        Name:	List Applications
        Description:	Retrieve a list of all available applications
        Method:	GET
        URI:	/v1/apps
        CloudCenter Release:
            CloudCenter 3.x and 4.x
            Enhanced in CloudCenter 3.2.6.5 to include the executor and category attributes (see Application Profiles for additional information)
            Enhanced in CloudCenter 4.7.0 to display the perms associated with the application.

        Notes:
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.

        ESB Header:
            action: get.apps
        """

        uri = "/v1/apps"
        response = self.client.get(uri)
        return response

    def listApplicationbyCategory(self, category_option, *args):
        """
        Name:	List Application by Category
        Description:
            Filters application(s) using the category that you specify in the query. You can specify single or multiple category options. See List Application Profile Categories for a list of categoriesself.
            See Application Profiles for additional information.
        Method:	GET
        URI:	v1/apps?category=category_option_1&category=category_option_2&....
        CloudCenter Release	CloudCenter 3.x and 4.x

        Notes:
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.

        ESB Header:
            action: get.apps
            actionparam: category=category_option_1&category=category_option_2&...

        Args:
            category_option: Application profile category. The category_option differs based on the options available in the List Application Profile Categories. See Application Profiles for a list of supported categories.
            *args: category_option_1, category_option_2 .. N
        """

        uri = "/v1/apps?category=" + str(category_option_1)
        for value in args:
            uri = uri + "&category=" + str(value)
        response = self.client.get(uri)
        return response

    def listApplicationProfileCategory(self):
        """
        Name:	List Application Profile Categories
        Description:    Provides a list of all application profile categories. The application category mapping to the application profile types. See Application Profiles for additional information.
        Method:	GET
        URI:    /v1/apps/categories
        CloudCenter Release:    CloudCenter 3.x and 4.x
        Notes:
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        ESB Header:
        	  action: get.apps.categories
        """
        uri = "/v1/apps/categories"
        response = self.client.get(uri)
        return response

    def updateApplication(self, appId, version, payLoad):
        """
        Name:	Update an Application
        Description:
            Updates the name, description, and version of the application and its service tiers.
            Other fields can not be updated
        Method:	PUT
        URI:	/v1/apps/appId?version=version
        CloudCenter Release:	CloudCenter 3.x and 4.x
        Notes:	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header:
	       action: update.apps.appId
           actionparam: version=version
        """

        uri  = "/v1/apps/" + str(appId) + "?version=" + str(version)
        response = self.client.put(uri, payLoad)
        return response

    def validateWorkflow(self, serviceTierId, depEnvId, cloudId):
        """
        Name:   Validate Workflow (Asynchronous API)
        Description:	Validates a workflow parameter for the Cisco UCSD.
        Method:	POST
        URI:    /v1/apps/validations?serviceTierId=serviceTierId&depEnvId=depEnvId&cloudId=cloudId
        CloudCenter Release:
            CloudCenter 3.x and 4.x
            Enhanced in CloudCenter 3.2.6.6. to include the additionalParameters attribute

        Notes:
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header:
            action: create.apps.validations
            actionparam: serviceTierId=serviceTierId&depEnvId=depEnvId&cloudId=cloudId
        """
        uri = "/v1/apps/validations?serviceTierId=" + serviceTierId + "&depEnvId=" + depEnvId + "&" + "cloudId=" + cloudId
        response = self.client.post(uri)
        return response
