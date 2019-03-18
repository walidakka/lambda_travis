provider "aws" {
  region  = "${var.aws_region}"
  profile = "${var.aws_profile}"
}

resource "aws_lambda_function" "function" {
  function_name    = "${var.function_name}"
  filename         = "./Lambda_code/package.zip"
  source_code_hash = "${base64sha256(file("./Lambda_code/package.zip"))}"
  handler          = "main.handler"
  runtime          = "${var.lambda_runtime}"
  role             = "${aws_iam_role.lambda_exec.arn}"
  tags {
    "Name"   = "${var.function_name}"
  }
}

resource "aws_iam_role" "lambda_exec" {
  name = "${var.function_name}-Role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "lambda_exec_policy" {
  name = "vpc_lambda"
  role = "${aws_iam_role.lambda_exec.id}"

  policy = <<EOF
{
"Version": "2012-10-17",
"Statement": [
  {
    "Action": "s3:*",
    "Effect": "Allow",
    "Resource": "*"
  }
]
}
EOF
}
