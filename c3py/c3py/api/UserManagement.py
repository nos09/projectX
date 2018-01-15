# -*- coding: utf-8 -*-

class UserManagement(object):

    def __init__(self, client):
        self.client = client

    def createUserWithoutActivation(self, payLoad):
        """
        Name	Create User without Activation		
        Description	Creates a new user and places the user in the NEW state.		
        Method	POST		
        URI	/v1/users		
        CloudCenter Release	Introduced in CloudCenter 4.0.		Replaces the 3.x version of this API.		
        			
        Notes	API Notes:				
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	See Synchronous APIs for additional context.		
        			
        	User Creation Notes:		
        			
        	When you create a user, this user's status defaults to NEW and the user is not functional.		
        	For this user to be functional (for example, to make API calls), the admin must first  activate this user.		
        	To obtain the tenantId, issue the View Users API request. Your tenantId is listed in the response. Use this tenantId to create a new user within a particular tenant.		
        			
        ESB Header	action: create.users		
        """

        uri = "/v1/users/" 
        response = self.client.post(uri, payLoad)
        return response

    def createUserWithActivation(self, payLoad):
        """
                Name	Create User with Activation (Asynchronous API)		
        Description	Creates a new user and starts activation of this user based on the default activation profile defined by the tenant administrator.		
        Method	POST		
        URI	/v1/users		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	Replaces the 3.x version of this API.		
        	Enhanced in CloudCenter 4.2 to include the activationProfileId attribute.		
        			
        Notes	API Notes:		
        			
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	See Asynchronous APIs for additional context.		
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.		
        			
        	User Creation Notes:		
        			
        	When you create a user, this user's status defaults to NEW and the user is not functional.		
        	For this user to be functional (for example, to make API calls), the admin must first  activate this user.		
        	To obtain the tenantId, issue the View Users API request. Your tenantId is listed in the response. Use this tenantId to create a new user within a particular tenant.		
        	One valid entry in the activateRegions array is required for this API call to succeed.		
        			
        ESB Header	action: create.users		

        """

        uri = "/v1/users/" 
        response = self.client.post(uri, payLoad)
        return response

    def viewUser(self, userId=None):
        """
        Name	View Users		
        Description	Displays configured information for all users or for a specified user.		
        Method	GET		
        URI	v1/users		
        	v1/users/userId		
        	v1/users/userId?detail=true		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	Replaces the 3.x version of this API.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
        	If you include a userId to identify a user, the response includes information for that user only.        			
        	You can sort the response based on the firstName and emailAddr attributes. See CloudCenter API Overview (Pagination and Sorting) for additional context.			
        ESB Header	action: get.users		
        	action: get.users.userId 		
        	action: get.users.userId		
        	actionparam: detail=true		
			        """

        uri = "/v1/users/" 
        if userId:
            uri = uri + str(userId) + "?detail=true"
                
        response = self.client.get(uri)
        return response
    
    def updateUser(self, userId,payload):
        """
        	Name	Update User		
        Description	Updates the configured user details for a user with the specified user ID.		
        			
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.		
        Method	PUT		
        URI	v1/users/userId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	Enhanced in CloudCenter 4.2 to include the activationProfileId and hasSubscriptionPlanType attributes.		
        			
        Notes	API Notes:		        			
        	For additional context on <PORT> usage in the following example, see Base URI Format.	        			
        	This API follows standard HTTP PUT idempotent semantics for all request attributes – except the password attribute.		
        			
        	Update User Notes:	        			
        	Repeat the entire response returned by the View Users API as the request for this Update User API – even if you are only updating one field.		
        	For this user to be functional (for example, to make API calls), the admin must first activate this user.		
        	Even though the value of the id, username, type, and accountSource attributes cannot be changed (cannot changed their value), they must still be included along with their values derived from the GET response. If either of these conditions are not fulfilled, the API call fails.		
        	The system ignores any other attribute that is not listed in the Request sections.	        			
          ESB Header	action: update/users/userId		
           """
        uri = "/v1/users/" + str(userId) 
        response = self.client.put(uri,payload)
        return response
    
    def deleteUser(self, userId):
        """
        	Name	Delete User		
        Description	Deletes the disabled user with the specified User ID.		
        Method	DELETE		
        URI	v1/users/userId		
        	v1/users?searchField=externalId&searchString=rash&searchOper=cn		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	Enhanced in CloudCenter 4.4 to support user deletion based on the External ID.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	A user cannot be successfully deleted unless the "status" attribute of the user is NEW or DISABLED.		
        			
        ESB Header	action: delete.users.userId		
        	action: delete.users		
        	actionparam: searchField=externalId&searchString=rash&searchOper=cn		

           """
        uri = "/v1/users/" + str(userId) 
        response = self.client.delete(uri)
        return response
    
    def performUserAction(self, userId):
        """
                    Name	Perform User Actions (Asynchronous or Synchronous API based on the requested action – identified in the examples below)		
        Description	Allows you to perform actions that a specified user can perform (at least one attribute is required).		
        This API is useful when you change passwords or qualify the user account with additional attributes.		
        	Unspecified attributes are not changed.		
        Method	POST		
        URI	/v1/users/userId (or any other attribute provided in the Request section.)		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	Payload change for MANAGE_CLOUDS (see Example 10 below) in CloudCenter 4.6 and later.		
        			
        Notes	API Notes:					
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.		
        	See Synchronous and Asynchronous APIs for additional context		
        			
        	User Action Notes:	The request body changes based on the selected action.					
        ESB Header	action: create.users.userId		

           """
        uri = "/v1/users/" + str(userId)
        response = self.client.post(uri)
        return response