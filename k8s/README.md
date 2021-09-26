# k8s

## Deployment without a manifests
To make persistent tunnel to service inside the minikube containers, 
the `minikube tunnel` should be executed
![tunnel](./screenshots/minikube_tunnel.png)

`kubectl get svc` and `kubectl get pods`
![results of commands](./screenshots/svc_pods.png)

## Deployment using manifests

![manifests](./screenshots/deployment_service.png)

## Helm

![pods services](./screenshots/helm_podsservices.png)

![dashboard](./screenshots/helm_dashboard.png)

 kubectl create secret generic some-random-pass --from-file=./username.txt --from-file=./password.txt
secret/some-random-pass created

