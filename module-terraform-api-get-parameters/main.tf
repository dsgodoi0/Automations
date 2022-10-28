
#############################################################################
#                                                                           #
#                                ROLE LAMBDA                                #
#                                                                           #
#############################################################################

resource "aws_iam_role" "iam_role" {

  name = var.role_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })

  path        = "/"
  description = "Role Lambda Get-Parameters"
}

#############################################################################
#                                                                           #
#                               POLICY LAMBDA                               #
#                                                                           #
#############################################################################

resource "aws_iam_policy" "iam_policy" {

  name        =  var.policy_name
  path        = "/"
  description = "Policy Lambda Get-Parameters"
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid": "VisualEditor0",
        "Effect" : "Allow",

        "Action" : [
            "ssm:DescribeParameters",
            "ssm:GetParameterHistory",
            "ssm:GetParametersByPath",
            "ssm:GetParameters",
            "ssm:GetParameter"
        ],
        "Resource" : "*"
      },
      {
        "Sid": "VisualEditor1",
        "Effect" : "Allow",

        "Action" : [
            "ssm:*"
        ],
        "Resource" : "*"
      }
    ]
  })
}

#############################################################################
#                                                                           #
#                           ROLE ATTACHMENT POLICY                          #
#                                                                           #
#############################################################################

resource "aws_iam_role_policy_attachment" "iam_role_policy_attachment" {
  role       = aws_iam_role.iam_role.name
  policy_arn = aws_iam_policy.iam_policy.arn
}

#############################################################################
#                                                                           #
#                                  LAMBDA                                   #
#                                                                           #
#############################################################################

resource "aws_lambda_function" "lambda_function" {
  filename      = var.lambda_filename
  function_name = var.lambda_name
  role          = aws_iam_role.iam_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       =  var.lambda_runtime
  timeout = var.lambda_timeout
}

#############################################################################
#                                                                           #
#                                TG LAMBDA                                  #
#                                                                           #
#############################################################################

resource "aws_lb_target_group" "lambda-target_group" {
  name        = var.tg_name
  target_type = "lambda"

}

#############################################################################
#                                                                           #
#                                SG LAMBDA                                  #
#                                                                           #
#############################################################################

resource "aws_security_group" "allow_tls" {
  name        = var.sg_name
  description = "SG para alb-get-parameters "
  vpc_id      = var.vpc_id

  ingress {
    description      = "TLS from VPC"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
   ingress {
    description      = "TLS from VPC"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}

#############################################################################
#                                                                           #
#                               ALB LAMBDA                                  #
#                                                                           #
#############################################################################

resource "aws_lb" "alb_lambda" {
  name               = var.alb_name
  internal           = true
  load_balancer_type = "application"
  security_groups    = [aws_security_group.allow_tls.id]
  subnets            = var.subnets
}

resource "aws_lb_listener" "listener_alb_lambda" {
   load_balancer_arn  = aws_lb.alb_lambda.arn
    port               = "80"
    protocol           = "HTTP"
        
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.lambda-target_group.arn
  }
}


resource "aws_lb_listener" "listener_alb_lambda_433_ssl" {
  load_balancer_arn = aws_lb.alb_lambda.arn
  port              = "443"
  protocol          = "HTTPS"
  certificate_arn   = data.aws_acm_certificate.edtech_ssl.arn
  ssl_policy        = "ELBSecurityPolicy-FS-1-2-Res-2020-10"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.lambda-target_group.arn
  }
}

#############################################################################
#                                                                           #
#                         ALB ATTACHMENT LAMBDA                             #
#                                                                           #
#############################################################################

resource "aws_lambda_permission" "with_lb" {
  statement_id  = "AllowExecutionFromlb"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function.function_name
  principal     = "elasticloadbalancing.amazonaws.com"
  source_arn    = aws_lb_target_group.lambda-target_group.arn
}

resource "aws_lb_target_group_attachment" "test" {
  target_group_arn = aws_lb_target_group.lambda-target_group.arn
  target_id        = aws_lambda_function.lambda_function.arn
  depends_on       = [aws_lambda_permission.with_lb]
}

#############################################################################
#                                                                           #
#                                DNS LAMBDA                                 #
#                                                                           #
#############################################################################
data "aws_route53_zone" "edtech" {
  provider     = aws.atena
  name         = var.domain
  private_zone = "false"



}



output "zone_id" {
    value = data.aws_route53_zone.edtech.zone_id
}


resource "aws_route53_record" "alb_lambda" {
  provider = aws.atena
  zone_id = data.aws_route53_zone.edtech.zone_id
  name    = "${var.record}.${var.domain}"
  type    = "CNAME"
  ttl     = 10
  records = [aws_lb.alb_lambda.dns_name]



}

