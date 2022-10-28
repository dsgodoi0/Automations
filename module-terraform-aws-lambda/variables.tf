variable role_name {
  description = "nome da role que será criada para o lambda"
  type        = string
  default     = ""
}

variable policy_name {
  description = "nome da policy que será criada para o lambda"
  type        = string
  default     = ""
}

variable lambda_name {
  description = "nome função lambda "
  type        = string
  default     = ""
}

variable lambda_description {
  description = "versão do python, exemplo: python3.9 "
  type        = string
  default     = ""
}

variable lambda_filename {
  description = "nome do pacote da automação que deve estar compactado em .zip e por default deixar o nome como: lambda_function.zip"
  type        = string
  default     = "" 
}

variable lambda_runtime {
  description = "versão do python, exemplo: python3.9 "
  type        = string
  default     = ""
}

variable lambda_timeout {
  description = "timeout default desejado"
  type        = number
  default     = 20
}

variable account_id {
  description = "Account de destino"
  type        = string
}

variable lambda_handler {
  description = "Account de destino"
  type        = string
}
