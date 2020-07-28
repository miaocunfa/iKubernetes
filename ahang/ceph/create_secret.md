## 1、创建admin secret

在kube-system名称空间创建

``` bash
# 在ceph Mon节点获取admin key
➜  ceph auth get-key client.admin

➜  export CEPH_ADMIN_SECRET='AQA/t5NeSaNVARAA4MG4qnF6tRKJBwuN4UOrMA=='
➜  kubectl create secret generic ceph-secret --type="kubernetes.io/rbd" --from-literal=key=$CEPH_ADMIN_SECRET --namespace=kube-system
```

## 2、创建用户secret

在default名称空间创建

``` bash
# 在ceph Mon节点获取user key
➜  ceph auth get-key client.k8s

➜  export CEPH_KUBE_SECRET='AQCGnKpez4D2LhAAILZwStTAii/zRLmgcnDnIg=='
➜  kubectl create secret generic ceph-user-secret --type="kubernetes.io/rbd" --from-literal=key=$CEPH_KUBE_SECRET --namespace=default
```

## 3、查看secret

``` bash
➜  kubectl get secret ceph-user-secret -o yaml
➜  kubectl get secret ceph-secret -n kube-system -o yaml
```
