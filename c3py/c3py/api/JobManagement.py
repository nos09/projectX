# -*- coding: utf-8 -*-

class JobManagement(object):
    
    def __init__(self, client):
        self.client = client
    
    def submitJobs_v2(self,payLoad):
        """
                Name	Submit job (Asynchronous API)		
        Description	Submit job-related information for each resource		
        Method	POST		
        URI	v2/jobs 		
        CloudCenter Release	Introduced in CloudCenter 4.6.		
        	Enhanced in CloudCenter 4.7.0 to include the rootVolumeSize attribute in the cloudParams element.		
        	Enhanced in CloudCenter 4.7.3.1 to include the createIsolatedNetwork attribute in the cloudProperties element.		
        	Enhanced in CloudCenter 4.7.2 to include the Google Cloud Platform LaunchName in the cloudProperties element.		
        	Enhanced in CloudCenter 4.8.0 to include the nodeIds (comma-separated list) in the jobs payload.		
        	Enhanced in CloudCenter 4.8.2 to include the assignIpv6Address attribute in the nics element		
            Notes	General Notes:	     			
        			
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Continue to query the Location URL until this call returns a success or failure HTTP Status Codes.		
        			
        	See Asynchronous APIs for additional context.		
        			
        	API Notes:		
        	Restful JSON Payload: Use the Restful JSON button (available in the CCM UI for N-tier applications) to seamlessly generate the payload for a job deployment request via the UI. You can then copy this payload (before submitting the UI request) and paste it into your RESTClient application to issue the corresponding API call. See Deployment Environments > Restful JSON for APIs for additional context.		
        			
        ESB Header	action: create.jobs		

"""
        uri = "/v2/jobs/" 
        response = self.client.post(uri, payLoad)
        return response
    
    def benchmarkJobs_v2(self,payLoad):
        """
          Name	Submit Benchmark (Asynchronous API)		
        Description	Submit a benchmark job that deploys an application profile across multiple cloud providers or cloud regions from a single cloud provider and produces a report that helps customers optimize cost and performance.		
        Method	POST		
        URI	v2/benchmark 		
        CloudCenter Release	Introduced in CloudCenter 4.6		
        Notes	General Notes:		
        			
        			
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Continue to query the Location URL until this call returns a success or failure HTTP Status Codes.		
        			
        	See Asynchronous APIs for additional context.		
        			
        	API Notes:		
        			
        	The v2 version of this API requires job objects for each cloud combination.		
        			
        	To identify the child, load generator tier – provide the "benchmarkLoadGenerator": "true" setting in the request body.		
        			
        	Provide the appId and appVersion at the benchmark level instead of specifying this information in each job request as these values apply to various jobs.		
        			
        	You do not need to provide the name, appId, and appVersion attributes within the benchmarkJobs settings.		
        			
        ESB Header	action: create.benchmark  		
		

"""
        uri = "/v2/bechmark/" 
        response = self.client.post(uri, payLoad)
        return response
    
    def viewJobs_v2(self,showOnlyStorageEntity=None,showOnlyFavorites=None,appId=None,showDeploymentAttributes=None,showAllJobs=None):
        """
        Name	View jobs		
        Description	Displays job-related information and resource links for each dependent or associated resource		
        Method	GET		
        URI	v2/jobs		
        	v2/jobs?search=[commaseparatedlistofSearchvalues]		
        	v2/jobs?search=[deploymentEntity.name,fle,aug25]		
        	v2/jobs?showOnlyStorageEntity=true		
        	v2/jobs?showOnlyFavorites=true&appId=appId&showDeploymentAttributes=true		
        	v2/jobs?showAllJobs		
        			
        CloudCenter Release	Introduced in CloudCenter 4.6.		
        	Enhanced in CloudCenter 4.8.0 to include the showAllJobs query parameter and list 50 records by default.		
        	Enhanced in CloudCenter 4.8.2 to include the approvalRequestAction and approvalRequestStatus attributes.		
        			
        Notes	General Notes:		
        			
        			
        	Ports: For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Default page size: Displays the complete list of jobs. See CloudCenter API Overview > Pagination for query choices.		
        	Sort: Use this attribute to sort through responses for this API. See sort for additional context.		
        			
        	Search: Use this attribute to narrow down the list of jobs and/or deployments, See search for additional details.		
        			
        	Query parameters: See the Optional Query Parameters row in the Request Attributes section below.		
        	Links: All resources that are independent of the job display a resource link with minimal information (id, resource). To view details about such resources, follow the corresponding links.  		
        	API Notes:		
        			
        	Default API response:		        			
        	Only displays a list of jobs. Excludes the following jobs:		  			     			
        	Project phase jobs		
        benchmark jobs		
        		ery parameters display benchmarks along with jobs.		
        			
        ESB Header	action: get.jobs		
        	action: get.jobs		
        	actionparam: search=[searchValue,searchValue,searchValue]		
        	action: get.jobs		
        	actionparam: showOnlyStorageEntity=true		
        	action: get.jobs		
        	actionparam:showOnlyFavorites=true&appId=appId&showDeploymentAttributes=true		
			

"""
        uri = "/v2/jobs/"
        if showOnlyStorageEntity:
            uri += " ?showOnlyStorageEntity=true"
        elif showOnlyFavorites and appId and showDeploymentAttributes:
            uri += "?showOnlyFavorites=true&appId=" + str(appId) + "&showDeploymentAttributes=true"
        elif showAllJobs:
            uri += "?showAllJobs"
            
        response = self.client.get(uri)        
        return response
    
    
    def viewJobDetails_v2(self, jobId,includeNodeDetails=None,includeNodeCostDetails=None,includeTaskDetails=None):
        """
        Name	View jobs		
        Description	Displays job-related information and resource links for each dependent or associated resource		
        Method	GET		
        URI	v2/jobs/jobId		
        	v2/jobs/jobId?includeNodeDetails=true&includeNodeCostDetails=true&includeTaskDetails=true		
        			
        CloudCenter Release	Introduced in CloudCenter 4.6		
        	Enhanced to include the virtualMachineId and externalServiceInstance attributes in CloudCenter 4.8.1.		
        	Enhanced in CloudCenter 4.8.2 to include the approvalRequestAction and approvalRequestStatus attributes.		
        			
        Notes	General Notes:		
        			
        			
        	Ports: For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Query parameters: See the Optional Query Parameters row in the Request Attributes section below. See View Jobs for examples. 		
        			
        	Links: All resources that are independent of the job display a resource link with minimal information (id, resource). To view details about such resources, follow the corresponding links.		
        			
        	API Notes:		
        			
        			
        	Child job details:		
        	Details for a child job are not displayed in the parent job details. Instead, use the child job link to view details for the child job.		
        	Correspondingly, each child job contains a link back to the parent job.		
        	Action attributes: The parent actions and child actions are segregated as applicable to the child or the parent.		
        			
        	Approval attributes: All attributes relating to approval are grouped under the parent job.		
        			
        ESB Header	action: get.jobs.jobId		
        	action: get.jobs.jobId		
        	actionparam:includeNodeDetails=true&includeNodeCostDetails=true&includeTaskDetails=true		
			
        """
        uri = "/v2/jobs/" + str(jobId) + "?"
        for key, value in zip(locals().keys(), locals().values()):
            if value!=None and key!="jobId" and key!="uri":
                uri += "%s=%s&" % (key, value)
        #if includeDetails:
        #    uri += "?includeNodeDetails=true&includeNodeCostDetails=true&includeTaskDetails=true"
        response = self.client.get(uri)
        return response
    def viewBenchmark_v2(self,benchmarkId):
        """
        Name	View benchmark details		
        Description	Displays details of the child jobs of a benchmark job and the benchmark results if the benchmark job is Finished.		
        Method	GET		
        URI	v2/benchmark /benchmarkId  		
        CloudCenter Release	Introduced in CloudCenter 4.6		
        Notes	General Notes:				
        	Ports: For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Links: All resources that are independent of the job display a resource link with minimal information (id, resource). To view details about such resources, follow the corresponding links.		
        	API Notes:		
                	Child job details:		
        	Details for a child job are not displayed in the parent job details. Instead, use the child job link to view details for the child job.		
        	Correspondingly, each child job contains a link back to the parent job. 		
        		 ESB Header	action: get.benchmark .jobId 		

"""
        uri = "/v2/benchmark/" + str (benchmarkId)           
        response = self.client.get(uri)        
        return response    
    
    def updateJob_v2(self,jobId,payLoad):
        """
        Name	Update Job
        Description	Updates a CloudCenter Deployment.
        Method	PUT
        URI	v2/jobs/jobid
        CloudCenter Release	
        
            Introduced in CloudCenter 4.6
            Enhanced in CloudCenter 4.8.2 to include three new enumerations for the supportedActions attribute (CANCEL_APPROVAL_REQUEST, EXTEND_AGE, and RESEND_APPROVAL_REQUEST).
        
        Notes	
        
        General Notes:
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            See View ACL Resource Details to SHARE deployments.
        
        API Notes:
        
            Existing actions (prior to CloudCenter 4.8.2), SUSPEND, RESUME, PROMOTE, MIGRATE (PUT) and TERMINATE (DELETE API), can also be used for ServiceNow approval flows based on your deployment environment requirements when using ServiceNow–CloudCenter integration. See Create ServiceNow Extension for additional context and details on switching on these workflows.
        
        ESB Header	action: update.jobs.jobid		

        """
        uri = "/v2/jobs/" + str(jobId)         
        response = self.client.put(uri,payLoad)        
        return response    
  
    def deleteJob_v2(self,jobId,hide=None):
        """
        Name	Delete Job (Asynchronous API)
        Description	Delete a deployment. This API returns a reference to a tracking ID that can be used to retrieve the delete operation.
        Method	DELETE
        URI	
        
            /v2/jobs/jobId
            /v2/jobs/jobId?hide=true
        
        CloudCenter Release	Introduced in CloudCenter 4.6
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            Default = terminate and hide ( if no variable is passed). See Termination for additional context.
            If hide = true and successful, then behavior is the same as terminate and hide.
            If hide = false and successful, then  only terminate (without hiding).
        
        ESB Header	
        
            action: delete.jobs.jobId
            action: delete.jobs.jobId
            actionparam: hide=true		

        """
        uri = "/v2/jobs/" + str(jobId)   
        if hide:
            uri += "?hide=true"
        response = self.client.delete(uri)        
        return response
    
    
    def deleteAllDeployments_v2(self,environmentId,hide=None):
        """
        Name	Delete All Deployments in a Deployment Environment (Asynchronous API)		
        Description	Deletes all deployments in a given deployment environment. Only the deployment environment owner can perform this operation.		
        			
        	This API returns a reference to a tracking ID that can be used to retrieve the delete operation status.		
        Method	DELETE		
        URI	v2/jobs/?environmentId=environmentId&hide=true		
        CloudCenter Release	Introduced in CloudCenter 4.8.2		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Default = terminate and hide ( if no variable is passed). See Termination for additional context.		
        	If hide = true and successful, then behavior is the same as terminate and hide.		
        	If hide = false and successful, then  only terminate (without hiding).		
        			
        ESB Header	action: delete.jobs.jobId		
        	actionparam: environmentId=environmentId&hide=true		
			
       """
        uri = "/v2/jobs?environmentId="  + str(environmentId)   
        if hide:
            uri += "&hide=true"
        response = self.client.delete(uri)        
        return response
    
    def deleteJob_v1(self,jobId):
        """
        Name	Delete Deployment (Asynchronous API)
        Description	Delete a deployment. This API returns a reference to a tracking ID that can be used to retrieve the delete operation.
        Method	DELETE
        URI	/v1/jobs/jobId
        CloudCenter Release	CloudCenter 3.x and 4.x
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: delete.jobs.jobId	

        """
        uri = "/v1/jobs/" + str(jobId)   
        response = self.client.delete(uri)        
        return response
    
    def fetchJobAssociatedVMDetails_v1(self,jobId,syncFromCloud):
        """
        Name	Fetch Job-Associated VM Details		
        Description	Fetch the VM details for the specified job.		
        Method	GET		
        URI	/v1/jobs/jobId/nodes		
        	/v1/jobs/jobId/nodes?syncFromCloud=value		
        			
        CloudCenter Release	CloudCenter 3.x and 4.x		
        			
        	Enhanced in CloudCenter 3.2.6.9 to include the syncFromCloud attribute.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: get.jobs.jobId.nodes		
        	action: get.jobs.jobId.nodes		
        	actionparam: syncFromCloud=value		
			
       """
        uri = "/v1/jobs/" + str(jobId) + "/nodes"
        if syncFromCloud:
            uri += "?syncFromCloud=true"
        response = self.client.get(uri)        
        return response
    
    def getJobDetails_v1(self,jobId):
        """
        Name	Get Job Details
        Description	Retrieve Job details. The status of the submitted job as well as all other details of the job, including details of the VMs that are launched can be retrieved using the resource URL returned in the location header in response of the job submission AP.
        Method	GET
        URI	/v1/jobs/jobId
        CloudCenter Release	
        
            CloudCenter 3.x and 4.x
            Enhanced in CloudCenter 3.2.5 to include the accessLink attribute.
            Enhanced in CloudCenter 3.2.6 to include the appId, appName, hostname, startTime, endTime, environment, enviornmentId, depInitiatingUserId, and environmentApprovalStatus attributes.
            Enhanced in CloudCenter 3.2.6.5 to include the preventTermination attribute.
            Enhanced in CloudCenter 3.2.6.9 to include the msg attribute.
            Enhanced in CloudCenter 4.0.0 to include the following attributes:
                The statusMsg attribute.
                The nics{nicID}, allocationMode, and order attributes (see IP Allocation Mode for additional information).
            Enhanced in CloudCenter 4.2 to include the provisionBareMetal, deploymentStatus, and deploymentInfo attributes.
            Enhanced in CloudCenter 4.4 to include the metadatas information.
            Enhanced in CloudCenter 4.6 to include the excludeTerminatedNodes query attribute.
            Enhanced in CloudCenter 4.8.2 to include the approvalRequestAction and approvalRequestStatus attributes.
        
        Notes	
        
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            Job details are continuously updated during the application provisioning.
            This API also allows you to exclude terminated VMs for each tier, when you use the {jobId}?excludeTerminatedNodes=true parameter in the request body.
        
        ESB Header	action: get.jobs.jobId 		

"""
        uri = "/v1/jobs/" + str(jobId)           
        response = self.client.get(uri)        
        return response 
    
    def getWindowVMsCredential_v1(self,jobId,nodeId):
        """
        Name	Get Windows VM(s) credentials
        Description	Retrieve the Windows VM(s) credentials. This is the initial system-generated VM password for the user during the job orchestration. If the user changes the password at a later stage, that password is not  reflected in this API's response.
        Method	GET
        URI 
            v1/jobs/jobId/credentials
            v1/jobs/jobId/credentials?nodeId=nodeId
        
        CloudCenter Release	    CloudCenter 3.x and 4.x
        Notes	       
            For additional context on <PORT> usage in the following example(s), see Base URI Format.
            You cannot retrieve passwords for terminated jobs.
            Use the child Job ID of the Windows server node(s) for which you need to retrieve the password. See the Get Job Details API for additional details on retrieving the child Job ID.
                ESB Header	        
            action: get.jobs.jobId.credentials
            action: get.jobs.jobId.credentials
            actionparam: nodeId=nodeId
"""
        uri = "/v1/jobs/" + str(jobId) +  "/credentials" 
        if nodeId:
            uri+= "?nodeId=" + str(nodeId)
        response = self.client.get(uri)        
        return response 
    
    def listJobs_v1(self,appDetails,status):
        """
        Name	List Jobs		
        Description	Retrieve a list of all jobs submitted by a user		
        Method	GET		
        URI	/v1/jobs		
        			
        	/v1/jobs?appDetails=true&status=running		
        			
        CloudCenter Release	CloudCenter 3.x and 4.x		
        	Enhanced in CloudCenter 4.2 to:		
        	List both jobs and deployments as jobs.		
        	Include the provisionBareMetal, displayName, appLogoPath, depInitiatingUserId, environmentId, environmentApprovalStatus, cost, isOwner, deploymentInfo, type, deploymentStatus and terminateProtection attributes.		
        	Enhanced in CloudCenter 4.5 to include optional query parameters identified in the Request Attributes section below.		
        	Enhanced in CloudCenter 4.8.2 to include the approvalRequestAction and approvalRequestStatus attributes.		
        			
        Notes	API Overview Notes		   			
        			
        	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	The CloudCenter GET APIs display up to 20 entities in the listing by default. If you have more than 20 entities in your resource listing, use the pagination query parameters to view them beyond the first 20 entities returned by default. See the CloudCenter API Overview > Pagination  section for additional context.		
        	List Jobs Notes		
        	The list jobs API does not list Projects and Phase-based deployments. It only lists deployments that are outside the scope of these CloudCenter resources.		
        			
        ESB Header	action: get.jobs	        			
        	actionparam: appDetails=true&status=running		

    """
        uri = "/v1/jobs"
        if status and appDetails:
            uri+= "?appDetails=true&status=running"
        response = self.client.get(uri)        
        return response
    
    def migrateDeployment_v1(self,jobid,payLoad):
        """
        Name	Migrate Deployment
        Description	Migrates a CloudCenter Deployment from one cloud to another after shutting down the old deployment.
        Method	PUT
        URI	v1/jobs/jobid?action=migrate
        CloudCenter Release	CloudCenter 3.x and 4.x
        Notes	
        
        For additional context on <PORT> usage in the following example(s), see Base URI Format.
        ESB Header	action: update.jobs.jobid
        actionparam: action=migrate		

    """
        uri = "/v1/jobs/"+ str(jobid) +"?action=migrate"
        response = self.client.put(uri,payLoad)        
        return response 
    
    def reconfigureRunningJob_v1(self,jobid,payLoad):
        """
        Name	Reconfigure Running Job (Asynchronous API)		
        Description	Reconfigures a running job.		
        Method	PUT		
        URI	v1/jobs/jobId?action=reconfigure		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        	Modified in 3.2.6.8 to ensure asynchronous job reconfiguration		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: put.jobs.jobId		
        	actionparam: action=reconfigure		
		

    """
        uri = "/v1/jobs/"+ str(jobid) +"?action=reconfigure"
        response = self.client.put(uri,payLoad)        
        return response
    
    def restartDeployment_v1(self,jobid,payLoad):
        """
        Name	Restart Deployment		
        Description	Restart a deployment that is in the stopped state or rerun a job that was previously run.		
        Method	POST		
        URI	/v1/jobs/jobId		
        CloudCenter Release	CloudCenter 3.s and 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: create.jobs.jobId		
	
    """
        uri = "/v1/jobs/"+ str(jobid) 
        response = self.client.post(uri,payLoad)        
        return response
    
    def resumeJob_v1(self,jobid,payLoad):
        """
        Name	Resume Job (Asynchronous API)		
        Description	Resume running a stopped or suspended job. The jobs and services for this VM are resumed and the VM and displays the NodeReady state.		
        			
        	This API returns a reference to a tracking ID that can be used to retrieve  the status of the stop operation.		
        Method	PUT		
        URI	/v1/jobs/jobId?action=resume		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.jobs.jobId		
        	actionparam: action=resume		
    """
        uri = "/v1/jobs/"+ str(jobid) + "?action=resume"
        response = self.client.put(uri,payLoad)        
        return response
    
    def stopJob_v1(self,jobid,payLoad):
        """
                Name	Stop Job (Asynchronous API)		
        Description	Stop (terminate) a running job. This API returns a reference to a tracking ID that can be used to retrieve the status of the stop operation.		
        Method	PUT		
        URI	/v1/jobs/jobId?action=stop		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.jobs.jobId		
        	actionparam: action=stop		
		
    """
        uri = "/v1/jobs/"+ str(jobid) + "?action=stop"
        response = self.client.put(uri,payLoad)        
        return response
    
    def submitJob_v1(self,jobid,payLoad):
        """
              Name	Submit Job (Asynchronous API)		
        Description	Provides a HTTP Location URL that you can use to query the system until this call returns a success or failure HTTP Status Codes.		
        Method	POST		
        URI	/v1/jobs 		
        CloudCenter Release	CloudCenter 3.x and 4.0.		
        			
        	Enhanced in CloudCenter 3.2.6 to include the policies attribute.		
        			
        	Enhanced in CloudCenter 3.2.6.5 to include the volumeInfos and preventTermination attributes.		
        	Enhanced in CloudCenter 4.0 to include the following attributes:		
        	The nics{nicID}, allocationMode, and order attributes (see IP Allocation Mode for additional context).		
        	The SSHKeyName, SSHPublicKey, SSHPrivateKey, and SSHPersistPrivateKey attributes (see SSH Options for additional context).		
        	Enhanced in CloudCenter 4.1.1 to include the following attributes:		
        	TenantName and TenantId attributes (see OpenStack Configurations for additional context).		
        	The SSHCloudKeyName attribute for OpenStack clouds (see SSH Options for additional context). This attribute is available in the cloudParams section of the request entity for each app tier.		
        	Enhanced in CloudCenter 4.2 to include the phaseId and projectId attributes.		
        	Enhanced in CloudCenter 4.4 to include the metadatas attribute.		
        	Enhanced in CloudCenter 4.5.0 to include the deploymentIsolationTag attribute.		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        	Continue to query the Location URL until this call returns a success or failure HTTP Status Codes.		
        			
        	See Asynchronous APIs for additional context.		
        			
        	SaaS application-based job submissions are independent of deployment environments and do not require the following attributes:		
        			
        			
        	parameters.cloudParams.*		
        	environment (deployment environment)		
        			
        ESB Header	action: create.jobs		
		
		
    """
        uri = "/v1/jobs/"+ str(jobid) 
        response = self.client.post(uri,payLoad)        
        return response
    
    
    def suspendJob_v1(self,jobid,payLoad):
        """
        Name	Suspend Job (Asynchronous API)		
        Description	Suspend a running job. The VM is powered off and remains in the NodeSuspended state.		
        			
        	This API returns a reference to an operation status tracking ID that can be used to retrieve the status of the stop operation.		
        Method	PUT		
        URI	/v1/jobs/jobId?action=suspend		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.jobs.jobId		
        	actionparam: action=suspend		
		
		
    """
        uri = "/v1/jobs/"+ str(jobid) + "?action=suspend"
        response = self.client.put(uri,payLoad)        
        return response
    
    def synchronizeVMCloudInformation_v1(self,jobid,payLoad):
        """
        Name	Synchronize VM Cloud Information (Asynchronous API)		
        Description	Synchronize the latest VM information from the cloud.		
        Method	PUT		
        URI	v1/jobs/jobId?action=synchronize_nodes		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        	Enhanced in CloudCenter 3.2.6.6. to include the additionalParameters attribute		
        			
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.jobs.jobId		
        	actionparam: action=synchronize_nodes		
        		
    """
        uri = "/v1/jobs/"+ str(jobid) + "?action=synchronize_nodes"
        response = self.client.put(uri,payLoad)        
        return response
    
    
    def upgradeRunningDeployment_v1(self,jobid,payLoad):
        """
       Name	Upgrade Running Deployment (Asynchronous API)		
        Description	Upgrades the running deployment for an application to a newer version.		
        Method	PUT		
        URI	/v1/jobs/jobId?action=upgrade&version=version		
        CloudCenter Release	CloudCenter 3.x and 4.x		
        Notes	For additional context on <PORT> usage in the following example(s), see Base URI Format.		
        ESB Header	action: update.jobs.jobIdaction=upgrade&version=		
        	actionparam: version		
       		
    """
        uri = "/v1/jobs/"+ str(jobid) + "?action=synchronize_nodes"
        response = self.client.put(uri,payLoad)        
        return response