resource "aws_eks_cluster" "eks_cluster" {
  name     = "terraformEKScluster"
  role_arn = var.role_arn
  version  = var.cluster_version

# Adding VPC Configuration
  vpc_config {             # Configure EKS with vpc and network settings 
   security_group_ids = [var.security_group_id]
   subnet_ids         = var.subnets_list  
    }

}

resource "aws_eks_node_group" "node" {
  cluster_name    = aws_eks_cluster.eks_cluster.name
  node_group_name = var.node_group_name
  node_role_arn   = var.role_arn
  subnet_ids      = var.subnets_list
  instance_types = var.instance_types

  scaling_config {
    desired_size = var.no_of_nodes
    max_size     = var.no_of_nodes
    min_size     = var.no_of_nodes
  }
}
