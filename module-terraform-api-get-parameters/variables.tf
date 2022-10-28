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

variable tg_name {
  description = "nome do target group que será criado para o alb get-parameters"
  type        = string
  default     = ""
}

variable sg_name {
  description = "nome do security group que será criado para o alb get-parameters"
  type        = string
  default     = ""
}

variable vpc_id {
  description = "id da vpc da conta"
  type        = string
  default     = ""
}

variable alb_name {
  description = "nome do alb"
  type        = string
  default     = ""
}

variable subnets {
  description = "nome do alb"
  type        = any
  default     = [""]
}

variable domain {
  description = "nome do dominio, para ssl e route53"
  type        = string
  default     = "edtech.com.br"
}

variable record {
  description = "criação do registro dns"
  type        = any
  default     = [""]
}

variable account_id {
  description = "Account de destino"
  type        = string
}
