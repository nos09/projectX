class DeploymentEnvironmentManagement(object):

    def __init__(self, client):
        self.client = client

    def createDeploymentEnvironment(self,payLoad):
        """
        Name	Create Deployment Environment		
        Description	Create deployment environments to map the cloud infrastructure to deployed applications.		
        Method	POST		
        URI	/v1/environments		
        CloudCenter Release	Updated in CloudCenter 4.0		
        	Enhanced in CloudCenter 4.2 to include the cloudId, totalDeployments, and costDetails attributes and to reflect a modified associatedClouds attribute. 		
        	Enhanced in CloudCenter 4.4 to reflect a modified associatedClouds attribute – see Deployment Environments for additional context.  		
        	Includes the regionId of each associated cloud account.  		
        	Contains new sections called cloudAssociationDefaults and default.  		
        	Enhanced in CloudCenter 4.8.2 to include the extensionId attribute (see Example 2 below and ServiceNow Extensions for additional context).		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Updated to work with the Create Deployment Environment.		
        	The following changes are specific to CloudCenter 4.x and are not available in the Create Deployment Environment 3.x version of this API:		
        	cloudGroupName and cloudGroup are no longer available 		
        	cloudId is now regionId		
        	cloudType is now regionName		
        	cloudName is now regionDisplayName		
        	cloudFamily is now an enumeration		
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.		
        			
        ESB Header	action: create.environments		
        Args:
            
        """

        uri = "/v1/environments/" 
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewDeploymentEnvironment(self, depEnvId=None):
        """
        Name	View Deployment Environment(s)		
        Description	Displays information for all Deployment Environment or for a specified deployment environment.		
        Method	GET		
        URI	v1/environments 		
        	v1/environments/depEnvId		
        			
        CloudCenter Release	Introduced in CloudCenter 3.2.5.		
        	Updated to work with CloudCenter 4.x. See Create Deployment Environment for additional details.		
        	Enhanced in CloudCenter 4.2 to include the cloudId, totalDeployments, and costDetails attributes and to reflect a modified associatedClouds attribute		
        	Enhanced in CloudCenter 4.4 to reflect a modified associatedClouds attribute – see Deployment Environments for additional context.		
        	Includes the regionId of each associated cloud account.		
        	Contains new sections called cloudAssociationDefaults and default. 		
        	Enhanced in CloudCenter 4.8.2 to include the extensionId attribute (see ServiceNow Extensions for additional context).		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
        			
        ESB Header	action: get.environments 		
        	action: get. environments.depEnvId		
            
            Args:
                depEnvId:xys
                Type:string
        			

        """

        uri = "/v1/environments/" + str(depEnvId)
        if depEnvId:
            uri = uri + str(depEnvId)
        response = self.client.get(uri)
        return response
    
    def updateDeploymentEnvironment(self,depEnvId,payload):
        """
        	Name	Update Deployment Environment		
        Description	Updates the information for a specified Deployment Environment.		
        Method	PUT		
        URI	v1/environments/depEnvId		
        CloudCenter Release	Updated in CloudCenter 4.0		
        	Enhanced in CloudCenter 4.2 to include the cloudId, totalDeployments, and costDetails attributes and to reflect a modified associatedClouds attribute.		
        	Enhanced in CloudCenter 4.4 to reflect a modified associatedClouds attribute – see Deployment Environments for additional context.  		
        	Includes the regionId of each associated cloud account.   		
        	Contains new sections called cloudAssociationDefaults and default.  		
        	Enhanced in CloudCenter 4.8.2 to include the extensionId attribute (see ServiceNow Extensions for additional context).		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        			
        	Updated to work with the REST API v1.0 for CloudCenter 4.x		
        			
        	See Create Deployment Environment for additional details		
        			
        ESB Header	action: update. environments.depEnvId		
        Args:
                depEnvId:xys
                Type:string

           """
        uri = "/v1/environments/" + str(depEnvId)
        response = self.client.put(uri,payload)
        return response
    
    def deleteDeploymentEnvironment(self, depEnvId):
        """
        	Name	Delete Deployment Environment		
        Description	Deletes the specified Deployment Environment.		
        Method	DELETE		
        URI	v1/environments/depEnvId		
        CloudCenter Release	Updated to work with the REST API v1.0 for CloudCenter 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        			
        	See Create Deployment Environment for additional details		
        			
        ESB Header	action: delete.environments.depEnvId	
            Args:
                depEnvId:xys
                Type:string        
          """
        uri = "/v1/environments/" + str(depEnvId)
        response = self.client.delete(uri)
        return response
    # -*- coding: utf-8 -*-

