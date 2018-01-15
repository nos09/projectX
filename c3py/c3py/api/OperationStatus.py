# -*- coding: utf-8 -*-
class OperationStatus(object):

    def __init__(self, client):
        self.client = client

    def getOperationStatus(self, operationId ):
        """
        Name	Get Operation Status
        Description	Retrieve status of the asynchronous operation
        Method	GET
        URI	/v1/operationStatus/operationId
        CloudCenter Release	CloudCenter 3.x and 4.x
        	Enhanced in CloudCenter 3.2.6.6. to include the additionalParameters attribute

        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: get.operationStatus/operationId


        """
        uri = "/v1/operationStatus/" + str(operationId)

        response = self.client.get(uri)
        return response
