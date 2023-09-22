# Terraform에서 k8s에 접근할 수 있도록 인증 정보를 제공한다.
provider "kubernetes" {
    host = module.eks.cluster_endpoint
    cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)

    exec {
        api_version = "client.authentication.k8s.io/v1beta1"
        command = "aws"
        args = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
    }
}

# Terraform에서 helm을 통해 k8s 내 Add-on를 설치할 수 있도록 인증 정보를 제공한다.
provider "helm" {
    kubernetes {
        host                   = module.eks.cluster_endpoint
        cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
        token                  = data.aws_eks_cluster_auth.eks.token
    }
}

data "aws_availability_zones" "available" {}
# Terraform에서 AWS의 계정 ID를 참조하기 위해 정의한다. 
# 사용은 ${data.aws_caller_identity.current.account_id}
data "aws_caller_identity" "current" {}

# EKS 클러스터와 통신하기 위한 인증 토큰을 가져온다.
data "aws_eks_cluster_auth" "eks" {name = module.eks.cluster_name}

resource "aws_iam_policy" "additional" {
    name = "${var.name}-additional"

    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Action = [
                    "ec2:Describe*",
                ]
                Effect = "Allow"
                Resource = "*"
            },
        ]
    })
}

module "kms" {
    source = "terraform-aws-modules/kms/aws"
    version = "1.1.0"

    aliases = ["eks/${var.name}"]
    description = "${var.name} cluster encryption key"
    enable_default_policy = true
    key_owners = [data.aws_caller_identity.current.arn]

    tags = {
        Env = "dev"
    }
}