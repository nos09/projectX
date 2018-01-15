class CloudFamilyManagement(object):

    def __init__(self, client):
        self.client = client

    def ViewCloudFamilies(self, tenantId, familyId=None):
        """
        Name	List Cloud Families for a Tenant		
        Description	Displays information for each cloud family or for a specified cloud family within the specified tenant.		
        Method	GET		
        URI	v1/cloudfamilies		
        	v1/cloudfamilies/cloudfamiliesId		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        	Enhanced in CloudCenter 4.7.2 to include the Alibaba Cloud in the cloudFamilies and the  cloudFamiliesId attributes.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.		
        	If you include a cloudFamiliesId to identify a cloud family, the response includes information for that cloud family only. 		
        	The pageResource attributes do not apply to this API.		
        			
        ESB Header	action: get.cloudfamilies		
        	action: get.cloudfamilies.cloudfamiliesId		
        			
	      """

        uri = "v1/cloudFamilies/"
        if familyId:
            uri = uri + str(familyId)
        response = self.client.get(uri)
        return response