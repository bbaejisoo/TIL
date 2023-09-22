provider "aws" {
    access_key = var.AWS_ACCESS_KEY
    secret_key = var.AWS_SECRET_KEY
    region     = var.AWS_REGION
}

# provider "kubernetes" {
#     host                   = data.aws_eks_cluster.dev.endpoint
#     token                  = data.aws_eks_cluster_auth.dev.token
#     cluster_ca_certificate = base64decode(data.aws_eks_cluster.dev.certificate_authority.0.data)
# }