# -*- coding: utf-8 -*-

class VMManagement(object):

    def __init__(self, client):
        self.client = client

    def viewVMs(self, regionId=None,cloudAccountId=None):
        """
        	Name	View Managed VMs
        Description	View managed VMs as described in VM Management. 
        Method	GET
        URI	v1/virtualMachines?listType=MANAGED_VMS 
        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	General Notes:For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. If you do not want to use paginated results, use the size=0 setting to receive all results. See the CloudCenter API Overview  > Pagination  section for additional context.
        	API Notes:
        	The cloudAccount must be owned by the user issuing the API call – be aware that ACL-shared cloud accounts result in a validation error.
        	This API supports standard pagination parameters. See CloudCenter API Overview for additional context.
        	ESB Header	action: get. virtualMachines
        	actionparam: listType=MANAGED_VMS 
        """

        uri = "/v1/virtualMachines?listType=MANAGED_VMS "
        response = self.client.get(uri)
        return response

    def viewUnmanagedVMs(self,  regionId=None,cloudAccountId=None):
        """
        Name	View  Unmanaged VMs
        Description	View unmanaged VMs as described in VM Management. 
        Method	GET
        URI	v1/virtualMachines?listType=UNMANAGED_VMS&regionId=regionId&cloudAccountId=cloudAccountId
        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	General Notes:


        	For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. If you do not want to use paginated results, use the size=0 setting to receive all results. See the CloudCenter API Overview  > Pagination  section for additional context.

        	API Notes:
        	The cloudAccount must be owned by the user issuing the API call – be aware that ACL-shared cloud accounts result in a validation error.
        	This API supports standard pagination parameters. See CloudCenter API Overview for additional context.
        	The regionId and cloudAccountId request attributes are required if the listType=UNMANAGED_VMS

        ESB Header	action: get. virtualMachines
	actionparam: listType=UNMANAGED_VMS&regionId= regionId&cloudAccountId=cloudAccountId
 
        """

        uri = "/v1/virtualMachines?listType=UNMANAGED_VMS&regionId=" + str(regionId) + "&cloudAccountId=" + str(cloudAccountId)
        response = self.client.get(uri)
        return response

    def downloadCSVReports(self,listType=None,startDate=None,endDate=None,size=None,regionId=None,cloudAccountId=None):
        """
        Name	Download CSV Reports
        Description	Download CSV Reports for Managed and Unmanaged VMs based on specific query parameters.
        Method	GET
        URI	/v1/virtualMachines.csv?listType=MANAGED_VMS&startDate=startDate&endDate=endDate&size=size

        	v1/virtualMachines?listType=UNMANAGED_VMS&regionId=regionId&cloudAccountId=cloudAccountId

        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	General Notes:


        	For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	API Notes:
        	The cloudAccount must be owned by the user issuing the API call – be aware that ACL-shared cloud accounts result in a validation error.
        	This API supports standard pagination parameters. See CloudCenter API Overview for additional context.

        ESB Header	action: get. virtualMachines
        	actionparam: listType=MANAGED_VMS&startDate=startDate&endDate=endDate&size=size

        	action: get. virtualMachines
        	actionparam: listType=UNMANAGED_VMS&regionId= regionId&cloudAccountId=cloudAccountId
        """

        uri = "/v1/virtualMachines.csv?"
        for key, value in zip(locals().keys(), locals().values()):
            if value!=None and key!="uri":
                uri = uri + "%s=%s&" % (key, value)

        response = self.client.get(uri)
        return response

    def viewVMDetails(self, virtualMachinesId=None):
        """
        Name	View VM Details
        Description	View VM Details as described in VM Management. 
        Method	GET
        URI	v1/virtualMachines/ virtualMachinesId 
        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	General Notes:


        	For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	API Notes:
        	The cloudAccount must be owned by the user issuing the API call – be aware that ACL-shared cloud accounts result in a validation error.
        	This API supports standard pagination parameters. See CloudCenter API Overview for additional context.

        ESB Header	action: get. virtualMachines. virtualMachinesId
        """

        uri = "/v1/virtualMachines/"
        if virtualMachinesId:
            uri += str(virtualMachinesId)

        response = self.client.get(uri)
        return response

    def importVMToCloudcenter(self, payLoad, actionId=None):
        """
        Name	Import VM to CloudCenter
        Description	A CloudCenter user who is the administrator and who is the cloud account owner can import a VM listed in the Unmanaged into the Managed category. See VM Management > Import to CloudCenter for additional context.

        	This API is similar to the Create Action Execution API, but explicitly added here for accountability.
        Method	POST
        URI	v1/actions/actionId/executions
        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header	action: create.actions.actionId.executions
                """

        uri = "/v1/actions/"
        if actionId:
            uri += str(actionId) + "/actions"

        response = self.client.post(uri,payLoad)
        return response

    def syncVM(self, payLoad, actionId=None):
        """
        Name	Sync VM
        Description	Sync VM as described in the Importing Unmanaged VMs use case. 
        Method	GET
        URI	v1/actions/actionId/executions
        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	General Notes:


        	For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	API Notes: See Importing Unmanaged VMs for the following information:
        	Manual Sync Import Use Case
        	To retrieve the actionId

        ESB Header	action: get.actions.actionId.executions
        """
        uri = "/v1/actions/"
        if actionId:
            uri += str(actionId) + "/actions"

        response = self.client.get(uri,payLoad)
        return response

    def syncVM(self, jobId=None):
        """
        Name	View VM User Data
        Description	View VM User Data as described in the Migrating Deployments use case. 
        Method	GET
        URI	 /job/service/nodeUserData/jobId 
        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	General Notes:


        	For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	API Notes:

        	If you provide the parent's Job ID, then the user data for the corresponding child jobs is displayed.
        	If you provide the child's Job ID, then the user data for that particular job is displayed.

        ESB Header	action: get.service.nodeUserData.jobId

        """
        uri = " /job/service/nodeUserData/"
        if actionId:
            uri += str(jobId)

        response = self.client.get(uri)
        return response
