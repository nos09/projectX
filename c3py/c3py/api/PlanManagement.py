# -*- coding: utf-8 -*-

class PlanManagement(object):

    def __init__(self, client):
        self.client = client

    def createPlan(self, tenantId,payLoad):
        """
        Name Create Plan
        Description	Creates a new plan and enables the Tenant Administrator to grant specific access to users assigned this plan.
        Method	POST
        URI	v1/tenants/tenantId/plans
        CloudCenter Release	
        
            Introduced in CloudCenter 4.0.
            Enhanced in CloudCenter 4.2 to include the numberOfProjects attribute.
            The paymentProfileRequired attribute is deprecated in CloudCenter 4.8.1 and later releases.
        
        Notes	API Notes
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            A successful response provides a resource URL for the plan that is created in the HTTP Location URL.
        
        ESB Header	action: create.tenants.tenantId.plans

        """

        uri = "/v1/tenants/" + str(tenantId) + "/plans/"
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewPlan(self, tenantId,planId=None):
        """
        Name	View Plans
        Description	Displays information for each plan or for a specified plan within the specified tenant.
        Method	GET
        URI	 v1/tenants/tenantId/plans
            v1/tenants/tenantId/plans/planId 
        
        CloudCenter Release	
        
            Introduced in CloudCenter 4.0.
            Enhanced in CloudCenter 4.2 to include the numberOfProjects attribute.
        
        Notes	
        
        API Notes:
        
            For additional context on <PORT> usage in the following example, see Base URI Format.
            The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        
        View Plan Notes:
        
            If you include a planId to identify a plan, the response includes information for that plan only.
            You can sort the response based on the name attribute. See CloudCenter API Overview (Pagination and Sorting) for additional context.
        
        ESB Header	
        
            action: get.tenants.tenantId.plans
            action: get.tenants.tenantId.plans.planId 
        """

        uri = "/v1/tenants/" + str(tenantId) + "/plans/"
        if planId:
            uri = uri + str(planId)
        response = self.client.get(uri)
        return response
    
    def updatePlan(self, tenantId,planId,payload):
        """
        	Name	Update Plan
        Description	Update the configured details for a plan specified by the Plan ID within a tenant specified by the Tenant ID.
        Method	PUT
        URI	vi/tenants/tenantId/plans/planID
        CloudCenter Release	
            Introduced in CloudCenter 4.0.
            Enhanced in CloudCenter 4.2 to include the numberOfProjects attribute.
        
            The paymentProfileRequired attribute is deprecated in CloudCenter 4.8.1 and later releases.
        
        Notes	For additional context on <PORT> usage in the following example, see Base URI Format.
        ESB Header	action: update.tenants.tenantId.plans.planId 
           """
        uri = "/v1/tenants/" + str(tenantId) + "/plans/"+str(planId)
        response = self.client.put(uri,payload)
        return response
    
    def deletePlan(self, tenantId,planId):
        """
        	Name	Delete Plan
        Description	Deletes the specified plan within the specified tenant in this CloudCenter instance. You can Delete any plan if the plan is not assigned to any user.
        Method	DELETE
        URI	v1/tenants/tenantId/plans/planID
        CloudCenter Release	Introduced in CloudCenter 4.0.
        Notes	For additional context on <PORT> usage in the following example, see Base URI Format.
        ESB Header	action: delete.tenants.tenantId.plans.planId 
           """
        uri = "/v1/tenants/" + str(tenantId) + "/plans/"+str(planId)
        response = self.client.delete(uri)
        return response