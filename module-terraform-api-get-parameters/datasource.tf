data "aws_acm_certificate" "edtech_ssl" {

  domain   = "*.${var.domain}"
  statuses = ["ISSUED"]
}