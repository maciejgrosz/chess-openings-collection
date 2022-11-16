output "cluster_endpoint" {
    description = "Cluster endpoint"
    value = "${aws_eks_cluster.eks_cluster.endpoint}"
}

output "cluster_ca_certificate" {
    description = "cluaster ca certificate"
    value = "${aws_eks_cluster.eks_cluster.certificate_authority}"
}



