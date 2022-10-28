provider "aws" {
  region  = "us-east-1"
  profile = "ops-payer"

  assume_role {
    role_arn = "arn:aws:iam::${var.account_id}:role/OrganizationAccountAccessRole"
  }
}

provider "aws" {
  alias   = "atena"
  region  = "us-east-1"
  profile = "atena"
}