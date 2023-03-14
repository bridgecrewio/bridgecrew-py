#!/bin/sh
################################################################################
# Download all Kubernetes resources and scan with Bridgecrew Cloud CLI
################################################################################

# kubectl api-resources --verbs=list --namespaced -o name  | xargs -n1 -I{} bash -c "kubectl get {} --all-namespaces -oyaml && echo ---"
RESOURCES="clusterroles
clusterrolebindings
configmaps
cronjobs
daemonsets
deployments
endpoints
horizontalpodautoscalers
ingresses
jobs
limitranges
networkpolicies
poddisruptionbudgets
pods
podsecuritypolicies
replicasets
replicationcontrollers
resourcequotas
roles
rolebindings
serviceaccounts
services
statefulsets"

export BC_SOURCE=kubernetesWorkloads


for resource in $RESOURCES;
do
  kubectl get $resource --all-namespaces -oyaml | yq eval 'del(.items[] | select(.metadata.ownerReferences)) ' -  > /data/runtime.${resource}.yaml
done

# Skip namespaces if exists 
if [ -f /etc/bridgecrew/skip ] && [ -s /etc/bridgecrew/skip ]; then
  skip="--skip-check $(cat /etc/bridgecrew/skip)" 
else
  skip=""
fi

if [ -f /etc/bridgecrew/apikey ]; then
  apikey=$(cat /etc/bridgecrew/apikey)
  if [ -f /etc/bridgecrew/repoid ]; then
    repoid=$(cat /etc/bridgecrew/repoid)
  else
    repoid="runtime/unknown"
  fi

  bridgecrew -s -d /data --bc-api-key "$apikey" --repo-id "$repoid" --branch runtime $skip
else
  bridgecrew -s -d /data $skip
fi
