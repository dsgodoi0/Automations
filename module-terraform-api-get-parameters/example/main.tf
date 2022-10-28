
provider "aws" {
  region  = "us-east-1"
  profile = "ops-payer"

  assume_role {
    role_arn    = "arn:aws:iam::${local.account_id}:role/OrganizationAccountAccessRole"
  }
}

provider "aws" {
  alias   = "atena"
  region  = "us-east-1"
  profile = "atena"
}
# Configure terraform

data "aws_acm_certificate" "edtech_ssl" {

  domain   = "*.edtech.com.br"
  statuses = ["ISSUED"]
}

terraform {
  backend "s3" {
    profile                     = "aws-profile"
    bucket                      = "bucket_name"
    key                         = "hmg/lambda/nome_do_tfstate.tfstate"
    region                      = "us-east-1"
    encrypt                     = true
    skip_credentials_validation = true
    skip_metadata_api_check     = true
  }
}

locals {
  account_id = ""
}


module lambda-get-parameters {
    source = "../"
    role_name = ""
    policy_name = ""
    lambda_name = ""
    account_id = ""
    lambda_filename = ""
    lambda_runtime = ""
    lambda_timeout = ""
    tg_name = ""
    sg_name = ""
    vpc_id = ""
    alb_name = ""
    subnets = ["",""]
    record = ""
}