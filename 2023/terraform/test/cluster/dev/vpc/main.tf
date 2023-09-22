module "vpc" {
    source = "terraform-aws-modules/vpc/aws"
    version = "5.1.0"

    name = "futurewiz-vpc-dev"
    cidr = "10.0.0.0/16"
    azs = ["ap-northeast-2a", "ap-northeast-2b", "ap-northeast-2c"]
    private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
    public_subnets = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]

    # data "aws_availability_zones" "available" {}
    # data "aws_caller_identity" "current" {}
    # private_subnets = slice(data.aws_availability_zones.available.names, 0, 3)

    enable_nat_gateway = true
    enable_dns_hostnames = true
    single_nat_gateway = true

    tags = {
        Env = "dev"
    }

    # elb가 사용하는 subnet을 자동으로 설정하기 위해서 설정
    public_subnet_tags = {
        "kubernetes.io/cluster/${var.cluster_name}" = "shared"
        "kubernetes.io/role/elb"                      = 1
    }

    private_subnet_tags = {
        "kubernetes.io/cluster/${var.cluster_name}" = "shared"
        "kubernetes.io/role/internal-elb"             = 1
    }
}


# # S3 Gateway Endpoint 설정이 필요하면 진행
# module "dev_s3_gateway_endpoint" {
#     source = "terraform-aws-modules/vpc/aws//modules/vpc-endpoints"

#     vpc_id = module.vpc.vpc_id
#     endpoints = {
#         s3 = {
#             service = "s3"
#             service_type = "Gateway"
#             route_table_ids = data.aws_route_tables.private_subnets.ids
#             tags = {
#                 Name = "s3-gateway-endpoint"
#             }
#         }
#     }
#     tags = {
#         Env = "dev"
#     }
# }

# data "aws_route_tables" "private_subnets" {
#     vpc_id = module.vpc.vpc_id

#     filter {
#         name = "tag:Name"
#         values = [ "futurewiz-vpc-dev-private*" ]
#     }
# }