# -*- coding: utf-8 -*-
class ReportManagement(object):

    def __init__(self, client):
        self.client = client

    def viewReport_v1(self, tenantId, reportType, startDate, endDate):
        """
        Name	View Reports
        Description	Displays the specified report for the specified tenant (see Enterprise > Tenant).
        	This API does not support sorting.
        	This API supports the CSV format for the response. See Response Schema > CSV (Only for Reports).

        Method	GET
        URI	v1/tenants/tenantId/reports?reportType=report_type&startDate=start_date&endDate=end_date
        CloudCenter Release	Introduced in CloudCenter 4.0
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.

        ESB Header	action: get.tenants.tenantId.reports
        	actionparam: reportType=report_type&startDate=start_date&endDate=end_date

        """

        uri = "/v1/tenants/"  + str(tenantId) + "/reports?reportType=" + str(reportType) + "&startDate=" + str(startDate) + "&endDate=" + str(endDate)
        response = self.client.get(uri)
        return response

    def createReporFilter_v1(self):
        """
        Name	Create Report Filter
        Description	Saves the currently set filter combination for quick usage when you use this API the next time around for the reports identified in the Request Body section of this API.
        Method	POST
        URI	v1/reportFilters
        CloudCenter Release	Introduced in CloudCenter 4.6
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	You can only access filters that you saved. You cannot access a filter that was saved by another user.

                ESB Header	action: create.reportFilters
        """

        uri = "/v1/reportFilters/"
        response = self.client.post(uri)
        return response

    def viewReportFilters_v1(self, reportType,filterId):
        """
        Name	View Report Filters
        Description	Displays information for any custom filter(s) for the  Usage Summary Report and the VM Inventory Report.
        Method	GET
        URI	v1/reportFilters
        	v1/reportFilters/filterId
        	v1/reportFilters?reportType=reportType

        CloudCenter Release	Introduced in CloudCenter 4.6
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	You can only access filters that you saved. You cannot access a filter that was saved by another user.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	If you include an filterId to identify a particular filter, the response includes information for only that filter.

        ESB Header	action: get.reportFilters

        """

        uri = "v1/reportFilters"
        if filterId:
            uri += "/" + str(filterId)
        elif reportType:
            uri += "?reportType=" + str(reportType)

        response = self.client.get(uri)
        return response


    def updateReportFilter_v1(self, filterId,payload):
        """
        	Name	Update Report Filter
        Description	Updates a custom filter for the  Usage Summary Report and the VM Inventory Report.
        Method	PUT
        URI	v1/reportFilters/filterId
        CloudCenter Release	Introduced in CloudCenter 4.6
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	You can only access filters that you saved. You cannot access a filter that was saved by another user.

        ESB Header	action: update.reportFilters

           """
        uri = "v1/reportFilters/" + str(filterId)
        response = self.client.put(uri,payload)
        return response

    def deleteFilterReport_v1(self, filterId):
        """
        Name	Delete Report Filter
        Description	Delete the specified custom filter from the list of filters for the Usage Details Report or the Managed VM Inventory Report.
        Method	DELETE
        URI	v1/reportFilters/filterId
        CloudCenter Release	Introduced in CloudCenter 4.6.
        Notes	For additional context on <PORT> usage in the following example, see Base URI Format.
        ESB Header	action: delete.tenants.tenantId.activationProfiles.activationProfileId

           """
        uri = "v1/reportFilters/" + str(filterId)
        response = self.client.delete(uri)
        return response

    def viewResourceSummaryReport_v2(self, tenantId,limit=None,endDate=None,startDate=None,mySummary=None,includeSubTenantSummary=None,reportType=None):
        """
        Name	View Resource Summary Report
        Description	Displays the resource report for all tenants or for your tenant by cloud/application.
        Method	GET
        URI	v2/tenants/tenantId/reports?reportType=reportType&includeSubTenantSummary=boolean&mySummary=boolean&startDate=start_date&endDate=end_date&limit=limit
        CloudCenter Release	Introduced in CloudCenter 4.6
        Notes	  General Notes:
                For additional context on <PORT> usage in the following example(s), see Base URI Format.
                The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
            API Notes:
                Call this API by issuing either the mySummary attribute or the includeSubTenantSummary attributes as false. Both attributes cannot both be true in the same API call.
                Default response:   First four resource details (can be changed using the limit attribute)
                    By cloud
                    All tenants (mySummary or mySummaryOnly=false or includeSubTenantSummary=true)
                    The mySummaryOnly attribute is available as a:
                        Response parameter in CloudCenter 4.8.0 and later releases.
                        Query parameter in CloudCenter 4.8.1 and later releases.
                This API does not support sorting.
                This API supports the CSV format for the response. See Response Schema > CSV (Only for Reports).
        ESB Header	action: get.tenants.tenantId.reports
        actionparam: reportType=report_type&includeSubTenantSummary=boolean&mySummary=boolean&startDate=start_date&endDate=end_date&limit=limit
                """

        uri = "v2/tenants/" + str(tenantId) +"/reports?"
        for key, value in zip(locals().keys(), locals().values()):
            if value!=None and key!="uri" and key!="tenantId":
            #print(value)
                uri = uri + "%s=%s&" % (key, value)
        response = self.client.get(uri)
        return response

    def viewUsageSummaryReport_v2(self,tenantId, reportType,startDate,endDate,groupBy):
        """
        Name	View Usage Summary Report
        Description	Displays the usage summary report for all tenants or for your tenant by cloud/application.
        Method	GET
        URI	v2/tenants/tenantId/reports?reportType=USAGE_SUMMARY_REPORT&startDate=startDate&endDate=endDate&groupBy=TENANT
        	v2/tenants/tenantId/reports?reportType=USAGE_SUMMARY_REPORT&startDate=startDate&endDate=endDate&groupBy=CLOUD

        CloudCenter Release	Introduced in CloudCenter 4.6
        Notes	General Notes:

        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	API Notes:
        	Default: Group all clouds by tenant.
        	This API does not support sorting.
        	This API supports the CSV format for the response. See Response Schema > CSV (Only for Reports).

        ESB Header	action: get.tenants.tenantId.reports
        	actionparam: reportType=USAGE_SUMMARY_REPORT&startDate=startDate&endDate=endDate&groupBy=TENANT
        	action: get.tenants.tenantId.reports
        	actionparam: reportType=USAGE_SUMMARY_REPORT&startDate=startDate&endDate=endDate&groupBy=CLOUD 
        """

        uri = "v2/tenants/" + str(tenantId) + "/reports?reportType=USAGE_SUMMARY_REPORT&startDate=" + str(startDate) + "&endDate=" + str(endDate) + "&groupBy=" + str(groupBy)
        response = self.client.get(uri)
        return response

    def viewUsageDetailsReport_v2(self, tenantId,order=None,sort=None,size=None,page=None,endDate=None,startDate=None,mySummary=None,includeSubTenantSummary=None,reportType="USAGE_DETAILS_REPORT"):
        """
        Name	View Usage Details Report
        Description	Displays the usage details report for my tenant or for a specific sub-tenant.
        Method	GET
        URI	v2/tenants/tenantId/reports?reportType=reportType&includeSubTenantSummary=boolean&mySummary=boolean&startDate=start_date&endDate=end_date&page=page&size=size&sort=sort&order=order
        CloudCenter Release	Introduced in CloudCenter 4.6.
        	Enhanced in CloudCenter 4.8.1 to include the userGroups attribute. Additionally, you can use userGroupId as a query parameter in this API.
        Notes	General Notes:

        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	API Notes:
        	Default response: My tenant.
        	This API supports the CSV format for the response. See Response Schema > CSV (Only for Reports).
        	Access Control:
        	This API is only available to admin users.
        	Admin users can access data to their managed tenant or sub-tenants by changing the tenantId path attribute in the request as displayed in the examples below.

        ESB Header	action: get.tenants.tenantId.reports
        	actionparam: reportType&includeSubTenantSummary=boolean&mySummary=boolean&startDate=start_date&endDate=end_date&page=page&size=size&sort=sort&order=order
 """

        uri = "v2/tenants/" + str(tenantId) +"/reports?"
        for key, value in zip(locals().keys(), locals().values()):
            if value!=None and key!="uri" and key!="tenantId":
            #print(value)
                uri = uri + "%s=%s&" % (key, value)
        response = self.client.get(uri)
        return response

    def ViewManagedVMInventoryReport_v2(self, tenantId,order=None,sort=None,size=None,page=None,endDate=None,startDate=None,reportType="MANAGED_VM_INVENTORY_REPORT"):
        """
        Name	View Managed VM Inventory Report
        Description	Displays the Managed VM Inventory report for all cloud regions and accounts my tenant or for a specific sub-tenant.
        Method	GET
        URI	v2/tenants/tenantId/reports?reportType=reportType&startDate=start_date&endDate=end_date&
        	 page=page&size=size&sort=sort&order=order
        CloudCenter Release	Introduced in CloudCenter 4.6
        	Deprecated in CloudCenter 4.8.0. Use the View Managed VMs API instead.
        Notes	General Notes:
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	API Notes:
        	Default response: My tenant.
        	This API supports the CSV format for the response. See Response Schema > CSV (Only for Reports).
        	Access Control:
        	This API is only available to admin users.
        	Admin users can access data to their managed tenant or sub-tenants by changing the tenantId path attribute in the request as displayed in the examples below.
        ESB Header	action: get.tenants.tenantId.reports
        	actionparam:  reportType=reportType &startDate=start_date&endDate=end_date& page=page
        	&size=size&sort=sort&order=order

        """
        uri = "v2/tenants/" + str(tenantId) +"/reports?"
        for key, value in zip(locals().keys(), locals().values()):
            if value!=None and key!="uri" and key!="tenantId":
            #print(value)
                uri = uri + "%s=%s&" % (key, value)
        response = self.client.get(uri)
        return response

    def ViewUnManagedVMInventoryReport_v2(self, tenantId,size=None,page=None,regionId=None,cloudAccountId=None,endDate=None,startDate=None):
        """
        Name	View Unmanaged VM Inventory Report
        Description	Displays the Unmanaged VM Inventory report for all cloud regions and accounts my tenant or for a specific sub-tenant.
        Method	GET
        URI	v2/tenants/tenantId/reports?reportType=reportType&startDate=start_date&endDate=end_date &cloudAccountId= cloudAccountId&regionId=regionId&page=page&size=size
        CloudCenter Release	Introduced in CloudCenter 4.6
        	***********Deprecated in CloudCenter 4.8.0. Use the View Managed and Unmanaged VMs API instead.		******************
        Notes	General Notes:
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	API Notes:
        	Default response: My tenant.
        	This API supports the CSV format for the response. See Response Schema > CSV (Only for Reports).
        	Access Control:
        	This API is only available to admin users.
        	Admin users can access data to their unmanaged cloud accounts or regions by changing the  cloudAccountId or regionId path attribute in the request as displayed in the examples below.

        ESB Header	action: get.tenants.tenantId.reports
        	actionparam: reportType=reportType&startDate=start_date&endDate=end_date& cloudAccountId= cloudAccountId&regionId=regionId&page=page&size=size 
                """
        uri = "v2/tenants/" + str(tenantId) +"/reports?reportType=UNMANAGED_VM_INVENTORY_REPORT&"
        for key, value in zip(locals().keys(), locals().values()):
            if value!=None and key!="uri" and key!="tenantId":
            #print(value)
                uri = uri + "%s=%s&" % (key, value)
        response = self.client.get(uri)
        return response

    def viewRunningVMHistoryReport_v2(self, tenantId=None,startDate=None,endDate=None):
        """
        Name	View Running VM History Report
        Description	Displays the View Running VM History report for the selected cloud regions, my tenant or for a specific sub-tenant, users, or groups. See Running VM History Report for additional context.
        Method	GET
        URI	v2/tenants/tenantId/reports?reportType=VM_COUNT_REPORT&startDate=start_date&endDate=end_date   
        CloudCenter Release	Introduced in CloudCenter 4.7.
        Notes	General Notes:
        			  	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview  > Pagination  section for additional context.
        	API Notes:
        	Default response: All regions, all users, today.
        	Access Control: You can access the following historical details:
        	Cloud Accounts for which you have Read permission
          Cloud Regions which are configured for you.
        ESB Header	action: get.tenants.tenantId.reports
        	actionparam:  reportType=VM_COUNT_REPORT &startDate=start_date&endDate=end_date 
        """

        uri = "v2/tenants/" + str(tenantId) + "/reports?reportType=VM_COUNT_REPORT&startDate=" + str(startDate) + "&endDate=" + str(endDate)

        response = self.client.get(uri)
        return response
