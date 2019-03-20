variable "aws_region" {
  default = "eu-west-1"
}

variable "aws_profile" {}

variable "function_name" {
  default = "test_function"
}

variable "lambda_runtime" {
  default = "python3.7"
}
