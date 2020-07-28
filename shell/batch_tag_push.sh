for i in `kubeadm config images list`
do
    imageName=${i#k8s.gcr.io/}  
    docker tag  k8s.gcr.io/$imageName reg.test.local/google_containers/$imageName
    docker push reg.test.local/google_containers/$imageName
done
