# AWS Lambda Deployment with Pulumi and GitHub Actions

This repository automates the deployment of an **AWS Lambda function** using **Pulumi** and **GitHub Actions**. It includes a **Python-based AWS Lambda function** that performs a simple addition operation.

---

## 🛠 Project Structure

```
.
├── iac-l1/                    # Pulumi Infrastructure as Code (IaC)
│   ├── __main__.py             # Pulumi script to create AWS resources
│   ├── requirements.txt        # Python dependencies for Pulumi
│   ├── Pulumi.dev.yaml         # Pulumi configuration file for 'dev' stack
│   ├── Pulumi.yaml             # Pulumi project configuration
│   └── lambda/                 # Lambda function source code
│       ├── addition.py         # Lambda function code
│       ├── requirements.txt    # Dependencies for the Lambda function
│       └── trial.py            # Another example Lambda function
├── .github/workflows/          # GitHub Actions workflow files
│   ├── deploy.yaml             # CI/CD workflow for Pulumi deployment
├── README.md                   # Project documentation
└── .gitignore                  # Ignore unnecessary files
```

---

## 🚀 Deployment Steps

### 1️⃣ Prerequisites
- **AWS Account** (IAM user with necessary permissions)
- **Pulumi CLI** installed (`curl -fsSL https://get.pulumi.com | sh`)
- **GitHub Repository Secrets**:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `PULUMI_ACCESS_TOKEN`

---

### 2️⃣ Setup Local Development

```sh
# Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Install Pulumi dependencies
pip install -r iac-l1/requirements.txt

# Initialize Pulumi
cd iac-l1
pulumi stack init dev
pulumi config set aws:region us-east-1
```

---

### 3️⃣ AWS Lambda Function

The Lambda function performs a simple addition operation:

```python
import json

def lambda_handler(event, context):
    a = 10
    b = 20
    c = a + b
    return {
        "statusCode": 200,
        "body": json.dumps({"result": c})
    }
```

---

### 4️⃣ GitHub Actions Workflow

A **GitHub Actions CI/CD pipeline** automatically deploys the Lambda function when code is pushed to the `main` branch.  

Workflow File: **`.github/workflows/deploy.yaml`**  

```yaml
name: Deploy AWS Lambda with Pulumi

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      - name: Install Pulumi
        run: curl -fsSL https://get.pulumi.com | sh

      - name: Install dependencies
        run: |
          pip install -r iac-l1/requirements.txt
          pip install -r iac-l1/lambda/requirements.txt

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Set Pulumi Access Token
        run: echo "PULUMI_ACCESS_TOKEN=${{ secrets.PULUMI_ACCESS_TOKEN }}" >> $GITHUB_ENV

      - name: Deploy with Pulumi
        run: |
          export PATH=$HOME/.pulumi/bin:$PATH
          cd iac-l1
          pulumi stack select dev
          pulumi up --yes
```

---

## 🔥 Deploying Manually

To deploy using Pulumi manually, run:

```sh
cd iac-l1
pulumi up --yes
```

---

## 📢 Outputs

After deployment, Pulumi exports the Lambda function names:

```sh
Outputs:
    lambda_function_1: "additionLambda-by-sp-4"
    lambda_function_2: "PriyanshuKSharma-2"
    lambda_function_3: "additionLambda-3"
```

---

## 📌 Notes

- Ensure the `lambda/` directory **exists** before running Pulumi.
- If you see `AccessDenied: User is not authorized to perform iam:CreateRole`, update IAM permissions.
- Modify the function handler in `__main__.py` if needed.

---

## 👨‍💻 Author
**Priyanshu K. Sharma** 🚀  
GitHub: [priyanshuksharma](https://github.com/priyanshuksharma)

---

## 🎯 License

This project is **NOT LICENSED**.

