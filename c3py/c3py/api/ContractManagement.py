class ContractManagement(object):

    def __init__(self, client):
        self.client = client

    def createContract(self, tenantId,cloudId,regionId,payLoad):
        """
        Name	Create Contract		
        Description	Creates a new contract and enables the Tenant Administrator Tasks to grant specific access to users assigned this contract.		
        Method	POST		
        URI	v1/tenants/tenantId/contracts		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.		
        			
        ESB Header	action: create.tenants.tenantId.contracts		
        Args:
            tenantId:xy
            Type:String

        """

        uri = "/v1/tenants/" + str(tenantId) + "contracts"
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewContract(self, tenantId,contractId=None):
        """
        Name	View Contracts		
        Description	Displays information for each Contract or for a specified contract within the specified tenant. 		
        Method	GET		
        URI	v1/tenants/tenantId/contracts		
        	v1/tenants/tenantId/contracts/contractId 		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview > Pagination  section for additional context.		
        	If you include a contractId to identify a contract, the response includes information for that contract only.		
        			
        ESB Header	action: get.tenants.tenantId.contracts		
        	action: get.tenants.tenantId.contracts.contractId		
			        Args:
            tenantId:xy
            Type:String
            contractId:ab
            Type: String

        """

        uri = "/v1/tenants/" + str(tenantId) + "/contracts/"
        if contractId:
            uri = uri + str(contractId)
        response = self.client.get(uri)
        return response
    
    def updateContract(self, tenantId,contractId,payload):
        """
        	Name	Update Contract		
        Description	Updates any configured contract details for the Contract specified by the Contract ID within a tenant specified by the Tenant ID.		
        Method	PUT		
        URI	vi/tenants/tenantId/contracts/contractId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.tenants.tenantId.contracts.contractId		
        			     Args:
            tenantId:xy
            Type:String
            contractId:ab
            Type: String

                   """
        uri = "/v1/tenants/" + str(tenantId) + "/contracts/"+str(contractId)
        response = self.client.put(uri,payload)
        return response
    
    def deleteContract(self, tenantId,contractId):
        """
        	Name	Delete Contract		
        Description	Deletes the specified Contracts within the specified tenant in this CloudCenter instance.		
        Method	DELETE		
        URI	v1/tenants/tenantId/contracts/contractId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: delete.tenants.tenantId.contracts.contractId		
			        Args:
            tenantId:xy
            Type:String
            contractId:ab
            Type: String

           """
        uri = "/v1/tenants/" + str(tenantId) + "/contracts/"+str(contractId)
        response = self.client.delete(uri)
        return response