variable "AWS_REGION" {
  default = "eu-west-1"
}

variable "volume_tags" {
  type = map(any)
}

variable "route_table" {
  type = map(any)
}

variable "internet_gateway_tags" {
  type = map(any)
}
variable "ingress_cidr_blocks" {
  type = list(string)
}
variable "ingress_rules" {
  type = list(string)
}
variable "egress_cidr_blocks" {
  type = list(string)
}

variable "egress_rules" {
  type = list(string)
}

variable "rules" {
  type = any
  #   type = map(list(object({
  #     from_port = number,
  #     to_port   = number,
  #     protocol  = string,
  #   })))
}

variable "security_group_tag" {
  type = map(any)
}
variable "subnets" {
  type = any
}

variable "tf_vpc" {
  type = any
}

variable "health_check_timeout" {
  type = number
}

variable "health_check_interval" {
  type = number
}

variable "single_config" {
  type = bool
}

variable "role_arn" {
  type = string
}

variable "cluster_version" {
  type = string
}

variable "node_group_name" {
  type = string
}

variable "instance_types" {
  type = list(string)
}

variable "no_of_nodes" {
  type = number
}