class ServiceManagement(object):

    def __init__(self, client):
        self.client = client

    def createService(self, tenantId,payLoad):
        """
            Name	Create Service
    Description	Creates a new service for the specified tenant. See Service Properties for additional information.
    Method	POST
    URI	v1/tenants/tenantId/services
    CloudCenter Release	  Introduced in CloudCenter 4.0.
        Enhanced in CloudCenter 4.2 to include the defaultImageId, serviceType, and serviceActions attributes.
        Enhanced in CloudCenter 4.3 to include the externalBundleLocation attribute and to deprecate the bundleRequired attribute
    Notes	  For additional context on <PORT> usage in the following example(s), see Base URI Format.
        Upload the logo image before creating a service (see Upload Logo). If you do not upload a logo and provide the existing logo path (logoPath) prior to creating a service, then the logo image from the currently provided path is deleted and this logo image is moved to another location after the service is created.
    ESB Header	action: create.tenants.tenantId.service
        """

        uri = "/v1/tenants/" + str(tenantId) + "/services/"
        response = self.client.post(uri, payLoad)
        return response


    def viewService(self, tenantId,serviceId=None,parentService=None):
        """
        Name	View Services
        Description	Displays information for all configured services or for a specified service. Both out-of-box CloudCenter Services and custom services are included in this API.
        Method	GET
        URI	v1/tenants/tenantId/services
        	v1/tenants/tenantId/services/serviceId
        	v1/tenants/tenantId/services?parentService=true

        CloudCenter Release	Introduced in CloudCenter 4.0.
        	Enhanced in CloudCenter 4.2 to include the defaultImageId and serviceActions attributes.
        	Enhanced in CloudCenter 4.3 to include the externalBundleLocation attribute and to deprecate the bundleRequired attribute

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: get.tenants.tenantId.service
        	action: get.tenants.tenantId.service.serviceId
        	action: get.tenants.tenantId.service
        	actionparam: parentService=true
            Args:
                tenantId:string
                serviceId:string
                parentService:true

            """

        uri = "/v1/tenants/" + str(tenantId) + "/services/"
        if serviceId:
            uri = uri + str(serviceId)
        response = self.client.get(uri)
        return response

    def updateService(self, tenantId,serviceId,payload):
        """

           """
        uri = "/v1/tenants/" + str(tenantId) + "/services/"+str(serviceId)
        response = self.client.put(uri,payload)
        return response

    def deleteService(self, serviceId):
        """

           """
        uri = "/v1/tenants/" + str(tenantId) + "/services/"+str(serviceId)
        response = self.client.delete(uri)
        return response

    def syncServiceRegion(self, tenantId,cloudId,regionId,serviceId):
        """

           """
        uri = "/v1/tenants/" + str(tenantId) + "/clouds/" + str(cloudId)+ "/regions/" +str(regionId) + "/syncRegions"
        response = self.client.post(uri)
        return response
