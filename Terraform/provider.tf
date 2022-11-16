provider "aws" {
  region = var.AWS_REGION
  default_tags {
    tags = {
      created_by = "Maciej Groszyk"
      bootcamp   = "poland1"
    }
  }
}

# provider "helm" {
#   kubernetes {
#     config_path = "~/.kube/config"
#   }
# }

provider "helm" {
  kubernetes {
    host                   = module.compute.cluster_endpoint
    cluster_ca_certificate = base64decode(module.compute.cluster_ca_certificate.0.data)
    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      args        = ["eks", "get-token", "--cluster-name", var.cluster_name]
      command     = "aws"
    }
  }
}

terraform {
  backend "s3" {
    bucket = "mg-state"
    key    = "mg-state"
    region = "eu-west-1"
  }
}
