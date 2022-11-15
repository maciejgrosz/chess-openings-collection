provider "aws" {
  region = var.AWS_REGION
  default_tags {
    tags = {
      created_by = "Maciej Groszyk"
      bootcamp   = "poland1"
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
