provider "aws" {
  region  = "us-east-1"
  profile = "ops-payer"

  assume_role {
    role_arn = "arn:aws:iam::${local.account_id}:role/OrganizationAccountAccessRole"
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
    bucket                      = "name_bucket"
    key                         = "hmg/iam_user/iam_user.tfstate"
    region                      = "us-east-1"
    encrypt                     = true
    skip_credentials_validation = true
    skip_metadata_api_check     = true
  }
}

locals {
  account_id = ""
}


module iam-user {
  source          = "../"
  iam_user_name   = ""
  iam_group_name  = ""
  iam_group_membership = ""
  iam_policy_name = ""
  account_id      = ""
}

output "secrets" {
   value   = [ "AWS_ACCESS_KEY_ID: ${module.iam-user.AWS_ACCESS_KEY_ID}",
               "AWS_SECRET_ACCESS_KEY: ${module.iam-user.AWS_SECRET_ACCESS_KEY}"]
   sensitive   = true
}