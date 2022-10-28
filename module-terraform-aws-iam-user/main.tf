#############################################################################
#                                                                           #
#                                 IAM USER                                  #
#                                                                           #
#############################################################################

resource "aws_iam_user" "iam_user" {
  name = var.iam_user_name
  path = "/"
}

#############################################################################
#                                                                           #
#                               KEY IAM USER                                #
#                                                                           #
#############################################################################

resource "aws_iam_access_key" "iam_key" {
  user = aws_iam_user.iam_user.name
}

#############################################################################
#                                                                           #
#                              POLICY IAM USER                              #
#                                                                           #
#############################################################################

resource "aws_iam_user_policy" "iam_policy" {
  name = var.iam_policy_name
  user = aws_iam_user.iam_user.name
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "lambda:UpdateFunctionCode",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

#############################################################################
#                                                                           #
#                                 IAM GROUP                                 #
#                                                                           #
#############################################################################

resource "aws_iam_group" "iam_group" {
  name = var.iam_group_name
}

#############################################################################
#                                                                           #
#                           IAM GROUP MEMBERSHIP                            #
#                                                                           #
#############################################################################

resource "aws_iam_group_membership" "iam_group_membership" {
  name = var.iam_group_membership

  users = [
    aws_iam_user.iam_user.name
  ]

  group = aws_iam_group.iam_group.name
}

#############################################################################
#                                                                           #
#                             POLICY IAM GROUP                              #
#                                                                           #
#############################################################################

resource "aws_iam_policy" "iam_policy" {
  name        = var.iam_policy_name
  description = "Policy Deploy Actions"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "lambda:UpdateFunctionCode",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

#############################################################################
#                                                                           #
#                       ATTACHMENT POLICY IAM GROUPS                        #
#                                                                           #
#############################################################################

resource "aws_iam_group_policy_attachment" "policy_attachment_group" {
  group      = aws_iam_group.iam_group.name
  policy_arn = aws_iam_policy.iam_policy.arn
}

