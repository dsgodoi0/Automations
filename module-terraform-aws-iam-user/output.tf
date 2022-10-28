output "AWS_ACCESS_KEY_ID" {
  value = aws_iam_access_key.iam_key.id
  sensitive   = true
}

output "AWS_SECRET_ACCESS_KEY" {
  value = aws_iam_access_key.iam_key.secret
  sensitive   = true
}


