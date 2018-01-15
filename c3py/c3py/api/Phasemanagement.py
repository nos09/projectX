# -*- coding: utf-8 -*-

class Phasemanagement(object):

    def __init__(self, client):
        self.client = client

    def createPhase(self, projectId,payLoad):
        """
        Name	Create Phase
        Description	Adds a new phase to an existing CloudCenter project
        Method	POST
        URI	v1/projects/projectId/phases
        CloudCenter Release	Introduced in CloudCenter 4.2
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
        
            If a phase name is not provided, then CloudCenter uses the phase name of the deployment environment.
        
        ESB Header	action: create.projects.projectId.phases
        """

        uri = "/v1/projects/" + str(projectId) + "/phases/"
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewPhase(self, projectId,phaseId=None,status=None):
        """
                Name	View Phases
        Description	Displays information for a specific phase or for all configured phases within a project .
        Method	GET
        URI	
        
            v1/projects/projectId/phases
            v1/projects/projectId/phases/phaseId
            v1/projects/projectId/phases?status=active
            Filter jobs returned for a phase using the status filter. For example,
                status = all
                status = active
                Individual status separated by |
        
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        
        ESB Header	
        
            action: get.projects.projectId.phases
            action: get.projects.projectId.phases.phaseId
            action: get.projects.projectId.phases
            actionparam: status=active

        """

        uri = "/v1/tenants/" + str(projectId) + "/phases/"
        if phaseId:
            uri = uri + str(phaseId)
        elif status:
            uri = uri + "?status=" + str(status)
        response = self.client.get(uri)
        return response
    
    def updatePhase(self, projectId,phaseId,payload):
        """
        	Name	Update Phase
        Description	
        
        Updates the configured details for a phase within a project as specified by the Phase ID.
        
        Unspecified attributes are changed to a NULL value.
        Method	PUT
        URI	
        
        v1/projects/projectId/phases/phaseId
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            The phase name is a mandatory request attribute and you must provide a value.
        
        ESB Header	action: update.projects.projectId.phases.phaseId
           """
        uri = "/v1/tenants/" + str(projectId) + "/images/"+str(phaseId)
        response = self.client.put(uri,payload)
        return response
    
    def deletePhase(self, projectId,phaseId):
        """
        	Name	Delete Phase
        Description	Deletes the specified phase within a project.
        Method	DELETE
        URI	v1/projects/projectId/phases/phaseID
        CloudCenter Release	Introduced in CloudCenter 4.2.
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
        
            You can only delete phases if a project is in the Draft (isDraft = true) state.
        
        ESB Header	action: delete.projects.projectId.phases.phaseID
           """
        uri = "/v1/tenants/" + str(projectId) + "/images/"+str(phaseId)
        response = self.client.delete(uri)
        return response
