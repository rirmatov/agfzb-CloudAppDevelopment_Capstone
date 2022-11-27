/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */

 const { CloudantV1 } = require("@ibm-cloud/cloudant");
 const { IamAuthenticator } = require("ibm-cloud-sdk-core");
 
 async function main(params) {
     
   const authenticator = new IamAuthenticator({ apikey:"API_KEY" });
   const cloudant = CloudantV1.newInstance({
       authenticator: authenticator
     
 });
   
   cloudant.setServiceUrl("COUCH_URL");
   
   return new Promise(function (resolve, reject) {
   cloudant.postAllDocs({ db: 'dealerships', includeDocs: true })            
            .then((result)=>{
              // console.log(result.result.rows);
              let code = 200;
              if (result.result.rows.length == 0) {
                  code = 404;
              }
              resolve({
                  statusCode: code,
                  headers: { 'Content-Type': 'application/json' },
                  body: result.result.rows
              });
            }).catch((err)=>{
              reject(err);
            })
   })

}
