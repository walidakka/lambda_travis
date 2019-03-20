resource "aws_lambda_function" "function" {
  function_name    = "${var.function_name}"
  filename         = "./Lambda_code/package.zip"
  source_code_hash = "${base64sha256(file("./Lambda_code/package.zip"))}"
  handler          = "main.handler"
  runtime          = "${var.lambda_runtime}"
  role             = "${aws_iam_role.lambda_exec.arn}"

  tags {
    "Name" = "${var.function_name}"
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
resource "aws_iam_role_policy_attachment" "test-attach" {
  role       = "${aws_iam_role.lambda_exec.name}"
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchFullAccess"
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

resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.function.arn}"
  principal     = "s3.amazonaws.com"
  source_arn    = "${aws_s3_bucket.bucket.arn}"
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = "${aws_s3_bucket.bucket.id}"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.function.arn}"
    events              = ["s3:ObjectCreated:*"]
    filter_suffix       = ".png"
  }
}

resource "aws_s3_bucket" "bucket" {}
