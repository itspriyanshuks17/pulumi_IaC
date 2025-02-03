import pulumi
import pulumi_aws as aws
import json

# IAM Role for Lambda
lambda_role = aws.iam.Role("lambdaRole",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"}
        }]
    })
)

# Attach AWS Lambda Basic Execution Role
aws.iam.RolePolicyAttachment("lambdaBasicExecution",
    role=lambda_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
)

# Zip Lambda function
lambda_archive = pulumi.AssetArchive({
    ".": pulumi.FileArchive("./lambda")  # Ensure the correct path
})


# Create Lambda Function
lambda_function = aws.lambda_.Function("additionLambda-by-sp",
    runtime="python3.9",
    role=lambda_role.arn,
    handler="addition.lambda_handler",
    code=lambda_archive,
)

# Export Lambda Function Name
pulumi.export("lambda_function_name", lambda_function.name)
