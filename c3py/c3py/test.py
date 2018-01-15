from c3_api import c3Api
import json

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

address = "https://10.127.193.138"
user = "cliqradmin"
key = "2A661A771F8B1205"

CloudCenter = c3Api(address,user,key)

#reponse=CloudCenter.BundleManagement.viewBundle(1)

#connection_file = open('payLoads/createBundle.json', 'r')
#conn_string = json.load(connection_file)
#reponse=CloudCenter.BundleManagement.createBundle(1,conn_string)



###update bundle

#connection_file = open('payLoads/updateBundle.json', 'r')
#conn_string = json.load(connection_file)
#response=CloudCenter.BundleManagement.updateBundle(1,3,conn_string)


#payLoad = json.load(open('payLoads/updateActionPolicy.json'))
#payLoad = json.load(open('payLoads/createActionPolicy.json'))

#request = CloudCenter.policyManagement.createActionPolicy(payLoad)
request = CloudCenter.PolicyManagement.viewActionPolicy(4)
#request = CloudCenter.policyManagement.updateActionPolicy(4,payLoad)
#request = CloudCenter.policyManagement.enableActionPolicy(4,userId=2)
#request = CloudCenter.policyManagement.disableActionPolicy(4,userId=2)
#request = CloudCenter.policyManagement.deleteActionPolicy(4)
#request = CloudCenter.ACLManagement.viewACLEntities()

#pp_json(request.json())
#print(request.status_code)
#print(type(payLoad))

#CloudCenter.ApplicationManagement.exportApplicationProfiles(2, 3, 4, 5)

#response = CloudCenter.LogManagement.downloadLog("CCM")
#print(response.status_code)
#with open('/tmp/logs.txt', 'wb') as f:
#    f.write(response.content)
#pp_json(response.json)

#end_date = 1513036800
#start_date = 1512950400

#response = CloudCenter.ReportManagement.viewReport_v1(1, "USER_SESSION_ACTIVITY_REPORT", start_date, end_date)
pp_json(response.json())
