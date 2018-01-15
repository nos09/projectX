import requests
import traceback
import sys
import json


class Client():
    def __init__(self, address, user, apiKey):
        self.address = address
        self.user = user
        self.apiKey = apiKey
        requests.packages.urllib3.disable_warnings()

    def checkHttpErrors(self,response):
####### SUCCESS ######################
        if response.status_code == 200:
            pass
        if response.status_code == 201:
            pass
        if response.status_code == 202:
            pass
        if response.status_code == 204:
            pass
####### Redirection ######################
        if response.status_code >= 300 and response.status_code <= 309:
            print(bcolors.OKBLUE, "The client is callig API using HTTP instead of HTTPS")
####### client Failure ######################
        ###### Validation Error #######
        if response.status_code == 400:
            #print("Damn it. Its that 400 again!!!")
            print("Its a Validation error!! Here are the errors responses that might help:")
            #print()
        ###### Authentication Error #######
        if response.status_code == 401:
            print("Not Authenticated!!")
            #sys.exit(0)
        ###### Permission Control Error #######
        if response.status_code == 403:
            print("Forbidden. You do not have the required Permission Control level to access the CloudCenter Resource")
        ###### Recource Not Found Error #######
        if response.status_code == 404:
            print("Resource Not found!!")
        ###### Server Failure #######
        if response.status_code == 500:
            print("Server Error: The server failed to respond to this request due to an internal error!!")

#### Request Methods ###########################
    def get(self, uri):
        #print(cliqrUrl)
        try:
            cliqrUrl = self.address + uri
            response = requests.get(cliqrUrl, verify=False, auth=(self.user, self.apiKey))
            self.checkHttpErrors(response)
            print(response.status_code)
            return response

        except requests.exceptions.ConnectionError as e:
            print(e)
            print(bcolors.FAIL, "Connection Error!!!" , bcolors.ENDC)
        except requests.exceptions.HTTPError as err:
            print(err)
        except Exception:
            print(traceback.format_exc())

    def post(self, uri, payLoad=None, files=None, fileName=None):
        try:
            cliqrUrl = self.address + uri
            if payLoad:
                headers = {'content-type': 'application/json' }
                payLoad = json.dumps(payLoad)
                #print(type(json.dumps(payLoad)))
                response = requests.post(cliqrUrl, verify=False, data=payLoad, headers=headers, auth=(self.user, self.apiKey))
            else:
                response = requests.post(cliqrUrl, verify=False, headers=headers, auth=(self.user, self.apiKey))
            if files:
                headers = {'Accept': 'application/json'}
                response = requests.post(cliqrUrl, verify=False, headers=headers, auth=(self.user, self.apiKey), files={"archive": ( fileName + ".zip", files)})

            self.checkHttpErrors(response)
            return response
        except requests.exceptions.ConnectionError as e:
            print(e)
            print(bcolors.FAIL, "Connection Error!!!" , bcolors.ENDC)
        except requests.exceptions.HTTPError as err:
            print(err)
        except Exception:
            print(traceback.format_exc())

    def put(self, uri, payLoad=None):
        try:
            cliqrUrl = self.address + uri
            if payLoad:
                headers = {'content-type': 'application/json' }
                payLoad = json.dumps(payLoad)
                #print(type(json.dumps(payLoad)))
                response = requests.put(cliqrUrl, verify=False, data=payLoad, headers=headers, auth=(self.user, self.apiKey))

            self.checkHttpErrors(response)
            return response
        except requests.exceptions.ConnectionError as e:
            print(e)
            print(bcolors.FAIL, "Connection Error!!!" , bcolors.ENDC)
        except requests.exceptions.HTTPError as err:
            print(err)
        except Exception:
            print(traceback.format_exc())

    def delete(self, uri):
        try:
            cliqrUrl = self.address + uri
            headers = {}
            response = requests.delete(cliqrUrl, verify=False, headers=headers, auth=(self.user, self.apiKey))
            self.checkHttpErrors(response)
            return response
        except requests.exceptions.ConnectionError as e:
            print(e)
            print(bcolors.FAIL, "Connection Error!!!" , bcolors.ENDC)
        except requests.exceptions.HTTPError as err:
            print(err)
        except Exception:
            print(traceback.format_exc())

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
