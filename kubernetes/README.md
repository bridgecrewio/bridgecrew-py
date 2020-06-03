# Bridgecrew Kubernetes Runtime

A container built to execute the Bridgecrew Cloud CLI within a Kubernetes environment.  

This downloads all Kubernetes resources as yaml, runs a scan against them, and pushes to the Bridgecrew API.

## Usage

The Bridgecrew Kubernetes runtime scanner is deployed into a Kubernetes cluster as a Cron Job.  Using a Bridgecrew 
API key the results can be forwarded to the Bridgecrew platform where you can compare with build time violations.  

The first step is to create a secret for your Bridgecrew api key.  Skip this step if you're not integrating the results with Bridgecrew.

Replace `<my_api_key>` below with your key from Bridgecrew.  
Also replace `<my_cluster_name>` with the name of your cluster so it shows up in the platform.  
```$xslt  
kubectl create ns bridgecrew
kubectl create secret generic bridgecrew-rt-secret --from-literal=apikey=<my_api_key> \
        --from-literal=repoid='runtime/<my_cluster_name>' -n bridgecrew
```

Next deploy the cron job using the provided manifest with runs once per hour

```$xslt
kubectl apply -f bridgecrew-cronjob.yaml
```

To executing a scan immediately, use the below example to trigger a onetime scan
The example below shows how to run a one-time scan.

```
kubectl create job bridgecrew-scan --from=cronjob/bridgecrew -n bridgecrew
```


Review the output in the Bridgecrew console or directly from the logs 

```$xslt
kubectl get jobs -n bridgecrew
kubectl logs job/checkov -n bridgecrew
```


