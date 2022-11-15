output "subnets_list" {
    description = "List of subnets"
    value = "${aws_subnet.subnets.* .id}"
}

output "vpc_id" {
    description = "The id of the VPC"
    value = aws_vpc.maciejgroszyk_tf_vpc.id
}   

output "security_group_id" {
    description = "The id of the security group"
    value = aws_security_group.mg_security_group_tf.id
}