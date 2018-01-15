class PolicyManagement(object):

    def __init__(self, client):
        self.client = client

    def viewPolicies(self):
        """
        Name	Get Policies
        Description	Get a list of policies that belong to user. The Submit Job API uses this API to add policies at run time.
        Method	GET
        URI	 /v1/policies
        CloudCenter Release	CloudCenter 3.x and 4.x
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: get.policies
"""
        uri = "/v1/policies"
        response = self.client.get(uri)
        return response

    def createActionPolicy(self, payLoad):
        """
          Name	Create Action Policy
        Description	Creates a new action policy to send an email message, invoke a web service, execute a command or script, or perform any number and combination of these activities when one or more user-defined actions are triggered by the user. See Policy Management for additional context.
        Method	POST
        URI	/v1/actionpolicies
        CloudCenter Release	Introduced in CloudCenter 4.5.
        Notes	
        For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: create.actionpolicies
        """
        uri = "/v1/actionpolicies"
        response = self.client.post(uri, payLoad)
        return response

    def enableActionPolicy(self, actionPolicyId, userId=None):
        """
         Name	Enable  Action Policies
        Description	Enables  an action policy.
        Method	POST
        URI	v1/actionpolicies/actionPolicyId
        CloudCenter Release	Introduced in CloudCenter 4.5
        Notes	
        
        For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: create.actionpolicies.actionPolicyId
        """
        payLoad = {"action":"ENABLE_POLICY", "userId":1 }
        if userId:
            payLoad["userId"] = userId
        uri = "/v1/actionpolicies/" + str(actionPolicyId)
        response = self.client.post(uri, payLoad)
        return response

    def disableActionPolicy(self, actionPolicyId, userId=None):
        """
                 Name	 Disable Action Policies
        Description	Disables an action policy.
        Method	POST
        URI	v1/actionpolicies/actionPolicyId
        CloudCenter Release	Introduced in CloudCenter 4.5
        Notes	
        
        For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: create.actionpolicies.actionPolicyId
        
        """
        payLoad = {"action":"DISABLE_POLICY", "userId":1 }
        if userId:
            payLoad["userId"] = userId
        uri = "/v1/actionpolicies/" + str(actionPolicyId)
        response = self.client.post(uri, payLoad)
        return response

    def viewActionPolicy(self, actionPolicyId=None):
        """
                Name	View Action Policies
        Description	View configurations for an existing action policy or for all configured policies. See Policy Management for additional context.
        Method	GET
        URI	 v1/actionpolicies
            v1/actionpolicies/actionPolicyId
        
        CloudCenter Release	Introduced in CloudCenter 4.5
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        ESB Header	 action: get.actionpolicies
            action: get.actionpolicies.actionPolicyId
                
        """
        uri = "/v1/actionpolicies/"
        if actionPolicyId:
            uri = uri + str(actionPolicyId)
        response = self.client.get(uri)
        return response

    def updateActionPolicy(self, actionPolicyId, payLoad):
        """
        Name	Update Action Policy
        Description	Update configurations for an existing action policy. See Policy Management for additional context.
        Method	 PUT
        URI	v1/actionpolicies/actionPolicyId
        CloudCenter Release	Introduced in CloudCenter 4.5
        Notes	or additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: update.actionpolicies.actionPolicyId
        
        """
        uri = "/v1/actionpolicies/" + str(actionPolicyId)
        response = self.client.put(uri, payLoad)
        return response

    def deleteActionPolicy(self, actionPolicyId):
        """
        Name	Delete Action Policy
        Description	Delete the specified action policy.
        Method	DELETE
        URI	v1/actionpolicies/actionPolicyId
        CloudCenter Release	Introduced in CloudCenter 4.5
        Notes	
        
        For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: delete.actionpolicies.actionPolicyId
        
        """
        uri = "/v1/actionpolicies/" + str(actionPolicyId)
        response = self.client.delete(uri)
        return response
