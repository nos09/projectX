# -*- coding: utf-8 -*-
class MarketPlaceManagement(object):

    def __init__(self, client):
        self.client = client

    def exportMarketplaceApplicationProfiles(self, publishedAppId ):
        """
        Name	Export Marketplace Application Profiles		
        Description	Downloads a ZIP file containing Marketplace application profiles for all applications requested.		
        Method	GET		
        URI	v1/apps/portation?appId=publishedAppId&&appId=publishedAppId&&appId=publishedAppId1&&type=PublishedApp		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: get.apps.portation		
        	actionparam: appId=publishedAppId&&appId=publishedAppId&&appId=publishedAppId1&&type=PublishedApp		
        		

        """
        uri = "v1/apps/portation?appId=" + str(publishedAppId) + "&&type=PublishedApp"
             
        response = self.client.get(uri)
        return response

    def importMarketplaceApplicationProfiles(self, fileName ):
        """
        Name	Import Marketplace Application Profiles		
        Description	Import marketplace application profiles by passing PublishedApp as the type for Marketplace application profiles that need to be downloaded.		
        Method	POST		
        URI	/v1/apps/portation?type=PublishedApp		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: create.apps.portation		
        	actionparam: type=PublishedApp		
	

        """
        uri = "/v1/apps/portation?type=PublishedApp -F file=@" + str(fileName) 
             
        response = self.client.post(uri)
        return response
    
    def deleteMarketplaceApplicationProfiles(self, appId ):
        """
        Name	Delete Marketplace Application Profiles		
        Description	Delete an application profile that has already been published to the CloudCenter Marketplace.		
        Method	DELETE		
        URI	/v1/apps/appId?type=PublishedApp		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: delete.apps.appId		
        	actionparam: type=PublishedApp		
        """
        uri = "/v1/apps/"  + str(appId) + "?type=PublishedApp" 
             
        response = self.client.delete(uri)
        return response
     