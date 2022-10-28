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
  description = "Role Lambda"
}

#############################################################################
#                                                                           #
#                               POLICY LAMBDA                               #
#                                                                           #
#############################################################################

resource "aws_iam_policy" "iam_policy" {

  name        =  var.policy_name
  path        = "/"
  description = "Policy Lambda"
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid": "VisualEditor0",
        "Effect" : "Allow",

        "Action" : [
            "ssm:*"
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
  description = var.lambda_description
  function_name = var.lambda_name
  role          = aws_iam_role.iam_role.arn
  handler       = var.lambda_handler
  runtime       =  var.lambda_runtime
  timeout = var.lambda_timeout
}
