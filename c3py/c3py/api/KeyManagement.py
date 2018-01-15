# -*- coding: utf-8 -*-
class KeyManagement(object):

    def __init__(self, client):
        self.client = client

    def createAPIKey(self, userId,payLoad):
        """
        Name	Create API Key		
        Description	The API key is also referred to as the management key or access key is required to use CloudCenter APIs.		
        			
        	Users can generate/regenerate an API key		
        	Tenant administrator can generate/regenerate the API key for any user within their tenant		
        			
        	CloudCenter validates the user name and password of API clients making HTTPS Request.		
        Method	POST		
        URI	v1/users/userId/keys		
        CloudCenter Release	Introduced in CloudCenter 3.x.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: create.users.userId.keys		

        """

        uri = "/v1/users/" + str(userId) + "/keys/"
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewKeys(self):
        """
    Name	View keys		
    Description	This API call allows users to view their own user keys, unlike the View User's Keys API, which is only for administrators.		
    			
    	Key refer to:		
    			
    	The API management key or access key is required to use CloudCenter APIs. See API Management Key for additional context.		
    	SSH Keys		
    	SFTP Keys		
    			
    Method	GET		
    URI	v1/user/keys		
    CloudCenter Release	Introduced in CloudCenter 4.0.		
    Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
    ESB Header	action: get.user.keys		

        """

        uri = "/v1/users/keys/" 
        response = self.client.get(uri)
        return response
    
    def viewUserKeys(self, userId):
        """
        Name	View User's Keys		
        Description	The API key is also referred to as the management key or access key is required to use CloudCenter APIs. See API Management Key for additional context. This admin only API allows admins to view the keys for any user belonging to this admin's tenant.		
        Method	GET		
        URI	v1/users/userId/keys		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
        			
        ESB Header	action: get.users.userId.keys		
		

        """

        uri = "/v1/users/" + str(userId) + "/keys/" 
        response = self.client.get(uri)
        return response
    
