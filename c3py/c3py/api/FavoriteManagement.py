# -*- coding: utf-8 -*-

class FavoriteManagement(object):

    def __init__(self, client):
        self.client = client


    def createFavorite(self, payLoad):
        """
        	Name	Create Favorite
        Description	Create a new favorite as described in UI Behavior.
        Method	POST
        URI	v1/favorites
        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	General Notes:


        	For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	API Notes:
        	You can only manage your own favorites.
        	This API only applies to VIRTUAL_MACHINE and JOB resources.
        	The created attribute is a read-only attribute and cannot be configured.
        	The resource must pre-exist and you must have access to that resource or the request results in a validation error

        ESB Header	action: create.favorites

        """

        uri = "/v1/tenants/" + str(tenantId) + "/services/"
        response = self.client.post(uri, payLoad)
        return response



    def viewFavorite(self, resourceType=None):
        """
        Name	View Favorite
        Description	View VMs or jobs that you have marked as favorites.
        Method	GET
            URI	v1/favorites?resourceType=VIRTUAL_MACHINE
        	v1/favorites?resourceType=JOB

        CloudCenter Release	Introduced in CloudCenter 4.8.0.
        Notes	General Notes:


        	For additional context on <PORT> usage in the following example, see Base URI Format.
        	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.
        	API Notes:
        	You can only view your own favorites.
        	This API only applies to VIRTUAL_MACHINE and JOB resources.
        	The resource must pre-exist and you must have access to that resource or the request results in a validation error

        ESB Header	action: get.favorites
        	actionparam: resourceType=VIRTUAL_MACHINE

        	action: get.favorites
        	actionparam: resourceType=JOB

            Args: resourceType=JOB/VIRTUAL_MACHINE

        """

        uri = "/v1/favorites?"
        if resourceType:
            uri = uri + "resourceType=" + str(resourceType)
        response = self.client.get(uri)
        return response


    def deleteFavorite(self, favoriteId):
        """
        	Name	Delete Favorite
        Description	Delete the specified favorite marking as specified in UI Behavior.
        Method	DELETE
        URI	v1/favorites/favoriteId
        CloudCenter Release	Introduced in CloudCenter 4.8.
        Notes	For additional context on <PORT> usage in the following example, see Base URI Format.
        	API Notes:
        	You can only delete your own favorites.
        	This API only applies to VIRTUAL_MACHINE and JOB resources.
        	The resource must pre-exist and you must have access to that resource or the request results in a validation error

        ESB Header	action: delete.favorites.favoriteId

        """
        uri = "/v1/favorites/" + str(favoriteId)
        response = self.client.delete(uri)
        return response
