#2019年10月30日21:13:41
#author: miaocunfa

## 1、自签CA证书
``` bash
# 使用kubeadm创建的kubernetes集群CA证书默认位置
[root@master ~]# cd /etc/kubernetes/pki/

生成秘钥miao.key, 为了安全打开子shell
[root@master pki]# (umask 077; openssl genrsa -out miao.key 2048)

基于私钥生成证书miao.csr, -subj 指明用户名, 证书持有者必须跟用户名保持一致
[root@master pki]# openssl req -new -key miao.key -out miao.csr -subj "/CN=miao"

证书miao.csr由ca.crt签署, 生成miao.crt
[root@master pki]# openssl x509 -req -in miao.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out miao.crt -days 365

查看证书信息
[root@master pki]# openssl x509 -in miao.crt -text -noout
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number:
            b5:b9:5d:d2:88:e9:25:4e
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=kubernetes
        Validity
            Not Before: Oct 30 12:57:49 2019 GMT
            Not After : Oct 29 12:57:49 2020 GMT
        Subject: CN=miao
```

## 2、创建客户端config
```
# kubectl config --kubeconfig=/tmp.test.conf 用于指明新增在/tmp/miao.config

# config文件创建k8s集群
[root@master ~]# kubectl config set-cluster mycluster --kubeconfig=/tmp/miao.config --server="https://172.31.194.108:6443" --certificate-authority=/etc/kubernetes/pki/ca.crt --embed-certs=true

# config文件新增用户miao
[root@master ~]# kubectl config set-credentials miao --kubeconfig=/tmp/miao.config --client-certificate=/etc/kubernetes/pki/miao.crt --client-key=/etc/kubernetes/pki/miao.key --embed-certs=true 

# config文件新增上下文
[root@master ~]# kubectl config set-context miao@mycluster --kubeconfig=/tmp/miao.config --cluster=mycluster --user=miao

# 指定当前用户
kubectl config --kubeconfig=/tmp/miao.config use-context miao@mycluster
```
