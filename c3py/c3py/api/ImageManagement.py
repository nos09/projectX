# -*- coding: utf-8 -*-

class ImageManagement(object):

    def __init__(self, client):
        self.client = client

    def createImage(self, tenantId,payLoad):
        """
        Name	Create Image		
        Description	Creates a new image for the specified tenant.		
        Method	POST		
        URI	v1/tenants/tenantId/images		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.		
        			
        ESB Header	action: create.tenants.tenantId.images		
        Args:
            tenantId: XYZ
            type:string
            imagesId:ABC
            type:string
        """

        uri = "/v1/tenants/" + str(tenantId) + "/images/"
        response = self.client.post(uri, payLoad)
        return response
    
    
    def viewImage(self, tenantId,ImagesId=None,details=None):
        """
        Name	View Image		
        Description	Updates an existing image for the specified tenant. 		
        Method	GET		
        URI	v1/tenants/tenantId/images		
        	v1/tenants/tenantId/images?detail=true		
        	v1/tenants/tenantId/images/imageId		
        	v1/tenants/tenantId/images/imageId?detail=true		
        			
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI		
        	Format.		
        			
        	If you include an imageId to identify a logical image, the response includes information		
        	for that image only.		
        			
        ESB Header	action: get.tenants.tenantId.images		
        	action: get.tenants.tenantId.images		
        	actionparam: detail=true		
        	action: get.tenants.tenantId.images.imageId		
        	action: get.tenants.tenantId.images.imageId		
        	actionparam: detail=true		
        		Args:
            tenantId: XYZ
            type:string
            imagesId:ABC
            type:string
            details:true
            type:boolean
            """

        uri = "/v1/tenants/" + str(tenantId) + "/images/"
        if ImagesId:
            if details:
                uri = uri + str(ImagesId) + "?detail=true"
            uri = uri + str(ImagesId)
        elif details:
            uri = uri + "?detail=true"
        response = self.client.get(uri)
        return response
    
    def updateImage(self, tenantId,ImagesId,payload):
        """
        	Name	Update Image		
        Description	Updates the specified image for the identified cloud region. See Manage Images for additional context.		
        Method	PUT		
        URI	v1/tenants/tenantId/images/imageId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: put.tenants.tenantId.images.imageId		

           """
        uri = "/v1/tenants/" + str(tenantId) + "/images/"+str(ImagesId)
        response = self.client.put(uri,payload)
        return response
    
    def deleteImage(self, tenantId,ImagesId):
        """
        	Name	Delete Image		
        Description	Deletes the specified image for the specified tenant.		
        Method	DELETE		
        URI	v1/tenants/tenantId/images/imageId		
        CloudCenter Release	Introduced in CloudCenter 4.0.		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB HEader	action: delete.tenants.tenantId.images.imageId		

           """
        uri = "/v1/tenants/" + str(tenantId) + "/images/"+str(ImagesId)
        response = self.client.delete(uri)
        return response
