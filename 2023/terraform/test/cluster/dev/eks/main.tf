# provider "kubernetes" {
#     host = module.eks.cluster_endpoint
#     cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)

#     exec {
#         api_version = "client.authentication.k8s.io/v1beta1"
#         command = "aws"
#         args = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
#     }
# }


# EKS
module "eks" {
    source = "terraform-aws-modules/eks/aws"
    version = "19.15.4"

    cluster_name = var.cluster_name
    cluster_version = var.cluster_version

    vpc_id = data.aws_vpc.dev.id
    subnets = data.aws_subnet_ids.dev.ids

    enable_irsa = true

    tags = {
        Env = "dev"
    }

    manage_aws_auth_configmap = true

    eks_managed_node_groups = {
        

    }




}



# data
data "aws_vpc" "dev" {
    tags = {
        Env = "dev"
    }
}

data "aws_subnet_ids" "dev" {
    vpc_id = data.aws_vpc.dev.id

    tags = {
        Env = "dev"
    }
}






# # single_instance test
# resource "aws_instance" "test-instnace" {
#     ami           = var.AMIS[var.AWS_REGION]
#     instance_type = "t2.micro"
#     tags = {
#         Name = "test-instance"
#     }
# }