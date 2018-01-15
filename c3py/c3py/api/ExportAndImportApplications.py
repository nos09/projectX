# -*- coding: utf-8 -*-
class ExportAndImportApplications(object):

    def __init__(self, client):
        self.client = client
        
    def ExportApplications(self,payLoad):
        """
            Name	Export Application.		
        Description	Export an application that has been successfully deployed. See Deployment Export/Import for additional context.		
        			
        	This API request is issued as a Job Management API.		
        Method	POST		
        URI	v1/exports		
        CloudCenter Release	Introduced in CloudCenter 4.5.7		
        Notes	Available in CloudCenter 4.5.7.		
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        			
        ESB Header	action: create.exports		

        """

        uri = "/v1/exports/" 
        response = self.client.post(uri, payLoad)
        return response