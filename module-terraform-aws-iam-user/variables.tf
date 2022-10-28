variable "iam_user_name" {
  description = "nome do usuario que será criado para o lambda actions"
  type        = string
  default     = ""
}

variable "iam_group_name" {
  description = "nome do gupo que será criado para o lambda actions"
  type        = string
  default     = ""
}

variable "iam_group_membership" {
  description = "nome do gupo que será criado para o lambda actions"
  type        = string
  default     = ""
}

variable "iam_policy_name" {
  description = "nome da policy que será criada para o lambda actions"
  type        = string
  default     = ""
}

variable "account_id" {
  description = "Account de destino"
  type        = string
}

