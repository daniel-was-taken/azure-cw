# Cloud Computing coursework 2

## Files for Azure function
The files in the github repository contain the function app for Azure.

## Files for OpenFaaS function
To pull the image for openFaaS function use `docker pull ghcr.io/daniel-was-taken/coursework-function:latest`

## Testing via wrk in VM
### Azure
    wrk -t10 -c100 -d300s -s /home/vllr8510/functions/azure_post.lua https://azure-cw2.azurewebsites.net/api/http_trigger?size=50
### OpenFaaS
    wrk -t10 -c100 -d300s -s /home/vllr8510/functions/post.lua http://40.81.140.169:8080/function/coursework-function

    
