#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict): 
    authenticator = IAMAuthenticator("fBILR7THckxF-Rb0dYDqhJD2vqSxcPgmMHcjI3mSrFrQ")
    service = CloudantV1(authenticator = authenticator)
        
    service.set_service_url("https://8b1da65f-617d-47f5-a0d3-b66086257f66-bluemix.cloudantnosqldb.appdomain.cloud")
        
    response = service.post_find(
        db= "reviews",
        selector = {'dealership': {'$eq' : int(dict['id'])}},
        ).get_result()

    try: 
        result={
            'headers': {'Content-Type':'application/json'}, 
            'body': {'data':response} 
            }
        return result 

    except:  
        return { 
            'statusCode': 404, 
            'message': 'Something went wrong'
            }
