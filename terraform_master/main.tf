provider "aws" {
	shared_credentials_file = "/c/Users/dmb/.aws/credentials"
  	profile                 = "mario"
	region = "us-east-2"
}



# iam (ROL) para lambda

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
EOF
}



resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.test_lambda_tf.arn}"
  principal     = "s3.amazonaws.com"
  source_arn    = "${aws_s3_bucket.bucket.arn}"
}



resource "aws_lambda_function" "test_lambda_tf" {
  filename      = "test_lambda.zip"
  function_name = "test_lambda_function_name"
  role          = "${aws_iam_role.iam_for_lambda.arn}"
  handler       = "test_lambda.lambda_handler"

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = "${filebase64sha256("test_lambda.zip")}"

  runtime = "python3.7"

  environment {
    variables = {
      foo = "bar"
    }
  }
}

resource "aws_s3_bucket" "bucket" {
  bucket = "s3mario"
}


resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = "${aws_s3_bucket.bucket.id}"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.test_lambda_tf.arn}"
    events              = ["s3:ObjectCreated:*"]
  }
}

output "s3mario_bucket_id" {
  value       = "${aws_s3_bucket.bucket.id}"
  description = "The bucket ID."
}