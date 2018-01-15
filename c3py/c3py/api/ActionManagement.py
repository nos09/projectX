class ActionManagement(object):

    def __init__(self, client):
        self.client = client

    def viewActions(self, actionId=None, includeSystemDefinedActions=False):
        """
        Name:	View Actions

        Description:
        View an action or a list of actions as described in Actions Library.
        You can also use this API to retrieve system-defined actions by setting the includeSystemDefinedActions attribute to trueself.

        Method:	GET
        URI:
            v1/actions/actionId
            v1/actions
            v1/actions?includeSystemDefinedActions=true

        CloudCenter Release
        Introduced in CloudCenter 4.8.0.
        Enhanced in CloudCenter 4.8.2 to include two new enumerations for the actionType attribute (CANCEL_APPROVAL_REQUEST and RESEND_APPROVAL_REQUEST).

        Notes:
        For additional context on <PORT> usage in the following example, see Base URI Format.
        Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header:
            action: get.actions
            action: get.actions.actionId
            action: get.actions
            actionparam: includeSystemDefinedActions=true
        """

        uri = "/v1/actions"
        if actionId:
            uri = uri + str(actionId)
        if includeSystemDefinedActions == True:
            uri = "/v1/actions?includeSystemDefinedActions=true"
        response = self.client.get(uri)
        return response

    def viewResourceActions(self, MANAGED_RESOURCE_ID_LIST=None, ACTION_REOURCE_TYPE="VIRTUAL_MACHINE", RESOURCE_ID_LIST=None):
        """
        Name:	View Resource Actions
        Description:
        View a list of supported actions for each resource as described in Actions Library.
        The supported actions are listed based on the object mapping definition in the action or the VM status (for cloud-provider actions).

        For additional context on <PORT> usage in the following example, see Base URI Format.
        Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        API-specific notes:
            resourceType = VIRTUAL_MACHINE.
            ids = Unique IDs for the managed VM, deployment, or application profile.
            cloudResourceIDs = The unmanaged VM ID

        ESB Header:
            action: get.resourcActions
            actionparam: ids=MANAGED_RESOURCE_ID_LIST&&resourceType=ACTION_REOURCE_TYPE
            action: get.actions.actionId
            actionparam:  cloudResourceIds=RESOURCE_ID_LIST&&resourceType=ACTION_RESOURCE_TYPE
        """

        uri = "/v1/resourceActions?ids=" + str(MANAGED_RESOURCE_ID_LIST) + "&&resourceType=" + ACTION_REOURCE_TYPE
        if RESOURCE_ID_LIST:
            uri = "/v1/resourceActions?cloudResourceIds=" + str(RESOURCE_ID_LIST) + "&&resourceType=" + ACTION_REOURCE_TYPE
        response = self.client.get(uri)
        return response

    def createActionExecution(self, payLoad):
        """
        Name:	Create Action Execution

        Description:
        Creates a new action to invoke web service, execute a command, invoke a Puppet/Chef/Ansible service, or execute a command using available/custom parameters.

        Method:	POST
        URI:	v1/actions/actionId/executions

        Notes:
        For additional context on <PORT> usage in the following example, see Base URI Format.
        Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header:
        	  action: create.actions.actionId.executions
        """

        uri = "/v1/actions/actionId/executions"
        response = self.client.post(uri, payLoad)
        return response

    def createNewAction(self, payLoad):
        """
        Description:
        Create a new basic or advanced action as described in Actions Library.

        Method:	POST
        URI:	v1/actions

        Introduced in CloudCenter 4.8.0.
        Enhanced in CloudCenter 4.8.2 to include two new enumerations for the actionType attribute (CANCEL_APPROVAL_REQUEST and RESEND_APPROVAL_REQUEST).

        Notes:
        For additional context on <PORT> usage in the following example, see Base URI Format.
        Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header:
            action: create.actions
        """

        uri = "/v1/actions"
        response = self.client.post(uri, payLoad)
        return response

    def updateAction(self, actionId, payLoad):
        """
        Name:	Update Actions
        Description:	Update an action as described in Actions Library.

        Method	PUT
        URI:	v1/actions/actionId

        CloudCenter Release
        Introduced in CloudCenter 4.8.0.
        Enhanced in CloudCenter 4.8.2 to include two new enumerations for the actionType attribute (CANCEL_APPROVAL_REQUEST and RESEND_APPROVAL_REQUEST).

        Notes:
        For additional context on <PORT> usage in the following example, see Base URI Format.
        Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.

        ESB Header:
        action: update.actions.actionId
        """

        uri = "/v1/actions/" + str(actionId)
        response = self.client.put(uri, payLoad)
        return response

    def deleteAction(self, actionId):
        """
        Name:	Delete Action
        Description:
        Delete the specified action as specified in Actions Library.
        Method:	DELETE
        URI:	v1/actions/actionId
        CloudCenter Release	Introduced in CloudCenter 4.8.
        Notes:	For additional context on <PORT> usage in the following example, see Base URI Format.
        ESB Header:
        	action: delete.actions.actionId
        """

        uri = "/v1/actions/" + str(actionId)
        response = self.client.delete(uri)
        return response
