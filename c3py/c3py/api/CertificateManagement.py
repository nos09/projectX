class CertificateManagement(object):

    def __init__(self, client):
        self.client = client

    def uploadCertificate(self, tenantId,fileName):
        """
        Name	Upload certificate
        Description	Imports a certificate for a CloudCenter component as specified in Federated Certificate Management.
        Method	POST
        URI	v1/certificate/import?fileName=fileName
        CloudCenter Release	Introduced in CloudCenter 4.3.1.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.

        	Once uploaded, this file cannot be downloaded.
        ESB Header	action: certificate/import
        	actionparam: fileName=fileName


        """

        uri = "v1/certificate/import?fileName=" + str(fileName)
        response = self.client.post(uri)
        return response


    def downloadCertificate(self):
        """
        Name	Download Self Certificate
        Description	Downloads your own Certificate Authentication file.
        Method	GET
        URI	v1/certificate/self/download

        	v1/certificate/self

        CloudCenter Release	Introduced in CloudCenter 4.2.1.
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: get.certificate.self.download
        	action: get.certificate.self


        """

        uri = "/v1/certificate/self"
        response = self.client.get(uri)
        return response
