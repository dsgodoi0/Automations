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

terraform {
  backend "s3" {
    profile                     = "aws-profile"
    bucket                      = "bucket_name"
    key                         = "hmg/lambda-default/lambda.tfstate"
    region                      = "us-east-1"
    encrypt                     = true
    skip_credentials_validation = true
    skip_metadata_api_check     = true
  }
}

locals {
  account_id = ""
}

module lambda {
    source = "../"
    role_name = ""
    policy_name = ""
    lambda_name = ""
    lambda_description = ""
    account_id = ""
    lambda_filename = ""
    lambda_handler = ""
    lambda_runtime = ""
    lambda_timeout = ""
}