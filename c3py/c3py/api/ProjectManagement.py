# -*- coding: utf-8 -*-

class ProjectManagement(object):

    def __init__(self, client):
        self.client = client

    def createProject(self, payLoad):
        """
        Name	Create Project
        Description	Creates a new CloudCenter project that includes one or more deployment environments.
        Method	POST
        URI	v1/projects
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: create.projects
                """

        uri = "/v1/projects/"  
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewProject(self, projectId=None,size=None):
        """
        Name	View Projects
        Description	Displays information for a specific project or for all configured projects.
        Method	GET
        URI	
        
            v1/projects
            v1/projects?size=0 (view all created projects, beyond 20, by using size=0)
            v1/projects/projectId 
        
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
        
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        
        ESB Header	
        
            action: get.projects
            action: get.projects
            actionparam: size=0
            action: get.projects.projectId 
        """

        uri = "/v1/projects/"
        if projectId:
            uri = uri + str(projectId)
        if size==0:
            uri =uri + "?size=0"
        response = self.client.get(uri)
        return response
    
    def updateProject(self, projectId,payload):
        """
        	Name	Update Project
        Description	
        
        Updates the configured details for a project specified by the Project ID.
        
        Unspecified attributes are changed to a NULL value.
        Method	PUT
        URI	v1/projects/projectId
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: update.projects.projectId
           """
        uri = "/v1/projects/" +str(projectId)
        response = self.client.put(uri,payload)
        return response
    
    def deleteProject(self, projectId):
        """
            Name	Delete Project
        Description	Deletes the specified project. You can Delete any project if the project is not published (see isDraft for additional context).
        Method	DELETE
        URI	v1/projects/projectId
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            Published projects can be deleted if the phases of the project does not have any active deployments.
        
        ESB Header	action: delete.projects.projectId
           """
        uri = "/v1/projects/" +str(projectId)
        response = self.client.delete(uri)
        return response
    
    def publishProject(self, projectId,payLoad):
        """
        Name	Publish Project
        Description	
        
        Publishes a CloudCenter project that includes one or more deployment environments.
        
         
        Method	POST
        URI	v1/projects/projectId?publish=true
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: create.projects.projectId
        actionparam: publish=true
           """
        uri = "/v1/projects/" + str(projectId) + "?publish=true"
        response = self.client.put(uri,payLoad)
        return response

