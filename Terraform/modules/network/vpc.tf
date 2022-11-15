resource "aws_vpc" "maciejgroszyk_tf_vpc" {
  cidr_block           = var.tf_vpc["cidr_block"]
  enable_dns_support   = var.tf_vpc["enable_dns_support"]
  enable_dns_hostnames = var.tf_vpc["enable_dns_hostnames"]
  instance_tenancy     = var.tf_vpc["instance_tenancy"]
  tags                 = var.tf_vpc["tags"]
}