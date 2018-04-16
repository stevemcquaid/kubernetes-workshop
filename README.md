# Kubernetes: From Code to Deployment

| Schedule        | Topic           | Time  |
| ------------- |:-------------:| -----:|
| 8:30 - 9 AM | Welcome/Intros | 10m |
| 9 - 9:45 AM | K8S Overview (L) | 60m |
| 9:45 - 10 AM | Download Tools (W) | 15m |
| 10 – 10:30 AM | Morning Break | 30m |
| 10:30 - 11 AM | Kubectl + Multiple Contexts (W) | 30m |
| 11 AM - 11:15 AM | Hello World (W) | 15m |
| 11:15 - 11:45 AM | Networking: Ingresses + Traffic Routing (L) | 30m |
| 12 - 1 PM | Lunch (Hall B, upstairs from breakout rooms) | 60m |
| 1 - 1:30 PM | Networking: Deploy Ingress Controller + Ingress Resource (W) | 30m |
| 1:30 - 2 PM | Large Cluster: Joining Forces (W) | 30m |
| 2 - 3 PM | Afternoon break:  Snacks and Sodas | 60m |
| 3 - 3:30 PM | Commit to Deploy with K8s | 30m |
| 3:30 - 4 PM | Monitoring: Prometheus + App Metrics (W) | 30m |
| 4 - 4:30PM | Office Hours + Questions (W) | 60m
| 4:30 | Wrap | |


#### Other Topics of Interest: 
  * kops/kubeadm
  * Disaster Recovery Concerns/ ETCD
  * Strategies for porting Legacy Applications
  * k8s plugins/Custom Resource Definitions
    * Extensibility/Metrics/HPA?


# Links
  1) `kubectl` - https://kubernetes.io/docs/tasks/tools/install-kubectl/
  2) `bash` for windows - https://www.windowscentral.com/how-install-bash-shell-command-line-windows-10
  3) 



# Agenda:
  * Welcome/Intros
    * Name, occupation, hobby, purpose for taking this workshop
  * Download Tools
    * docker
    * kubectl
    * minikube 
  * Overview of k8s
    * Abstract
    * kubectl
    * control plane
        * kube-api
        * kube-scheduler
        * kube-controller-manager
        * kubelet
        * kube-proxy
  * Setup MiniKube
    * install
    * kubectl get namespaces
    * kubectl create -f
  * kubectl
    * multiple contexts
  * Hello World App Deployment
  * Networking
    * Overlay Network
    * Pods
    * Service
    * Kube-Proxy
    * Ingress
    * Ingress Controller
    * Load Balancing
  * Legacy App Migration
  * Monitoring
  * kops/kubeadm
  * Disaster Recovery Concerns
    * Schools of Thought
    * etcd
  * Extensibility
    * Monitor k8s API
    * k8s plugin
    * CRD
  * Office Hours for Custom Apps
  * Metrics/HPA

