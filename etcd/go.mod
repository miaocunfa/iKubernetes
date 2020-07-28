module etcdhelper

go 1.14

require (
	github.com/coreos/etcd v3.3.22+incompatible // indirect
	github.com/coreos/pkg v0.0.0-20180928190104-399ea9e2e55f // indirect
	github.com/grafana/loki v1.5.0 // indirect
	github.com/openshift/api v0.0.0-20200714125145-93040c6967eb
	go.etcd.io/etcd v3.3.22+incompatible
	go.uber.org/zap v1.15.0 // indirect
	k8s.io/apimachinery v0.18.6
	k8s.io/kubectl v0.18.6
)

replace github.com/coreos/go-systemd => github.com/coreos/go-systemd/v22 v22.1.0
