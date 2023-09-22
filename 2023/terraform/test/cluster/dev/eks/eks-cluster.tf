# S3 backend에서 VPC 정보 불러오기 - 1
data "terraform_remote_state" "vpc" {
    backend = "s3"
    config = {
        bucket = "futurewiz-tf-dev"
        key = "dev/vpc/terraform.tfstate"
        region = "ap-northeast-2"
    }
}

# EKS
module "eks" {
    source = "terraform-aws-modules/eks/aws"
    version = "19.15.4"

    cluster_name = var.cluster_name
    cluster_version = var.cluster_version

    # S3 backend에서 불러오기 - 2
    vpc_id = data.terraform_remote_state.vpc.outputs.vpc_id
    subnet_ids = data.terraform_remote_state.vpc.outputs.private_subnets

    enable_irsa = true

    tags = {
        Env = "dev"
    }

    cluster_addons = {
        coredns = {
            preserve = true
            most_recent = true
        }
        kube-proxy = {
            most_recent = true
        }
        vpc-cni = {
            most_recent = true
            before_compute = true
            # service_account_role_arn = module.vpc_cni_irsa.iam_role_arn
            # Node의 Pod 수 110개 지정하는 설정
            configuration_values = jsonencode({
                env = {
                    ENABLE_PREFIX_DELEGATION = "true"
                    WARM_PREFIX_TARGET = "1"
                }
            })
        }
    }
    create_kms_key = true
    cluster_encryption_config = {
        resources = ["secrets"]
        provider_key_arn = module.kms.key_arn
    }

    manage_aws_auth_configmap = true
    aws_auth_roles = [
        {
            rolearn = module.karpenter.role_arn
            username = "system:node:{{EC2PrivateDNSName}}"
            groups = [
                "system:bootstrappers",
                "system:nodes",
            ]
        },
    ]
    iam_role_additional_policies = {
        additional = aws_iam_policy.additional.arn
    }

    cluster_security_group_additional_rules = {
        ingress_nodes_ephemeral_ports_tcp = {
            description = "Nodes on ephemeral ports"
            protocol = "tcp"
            from_port = 1025
            to_port = 65535
            type = "ingress"
            source_node_security_group = true
        }
    }

    node_security_group_additional_rules = {
        ingress_self_all = {
            description = "Node to node all ports/protocols"
            protocol = "-1"
            from_port = 0
            to_port = 0
            type = "ingress"
            self = true
        }
    }

    eks_managed_node_group_defaults = {
        iam_role_additional_policies = {
            additional = aws_iam_policy.additional.arn
        }

        ebs_optimized = true
        block_device_mappings = {
            xvda = {
                device_name = "/dev/xvda"
                ebs = {
                    volume_size = 30
                    volume_type = "gp3"
                    iops = 3000
                    throughput = 150
                    delete_on_termination = true
                }
            }
        }
        tags = {
            Env = "dev"
        }
    }


    eks_managed_node_groups = {
        test-node1 = {
            name = "test-node1"
            use_name_prefix = false
            instance_types = ["t3.micro"]
            capacity_type  = "SPOT"

            min_size = 1
            max_size = 1
            desired_size = 1
            subnet_ids = data.terraform_remote_state.vpc.outputs.private_subnets
        }
    }




}




# # Addon AWS-EBS-CSI
# data "aws_iam_policy" "ebs_csi_policy" {
#     arn = "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
# }

# module "irsa-ebs-csi" {
#     source  = "terraform-aws-modules/iam/aws//modules/iam-assumable-role-with-oidc"
#     version = "4.7.0"

#     create_role                   = true
#     role_name                     = "AmazonEKSTFEBSCSIRole-${module.eks.cluster_name}"
#     provider_url                  = module.eks.oidc_provider
#     role_policy_arns              = [data.aws_iam_policy.ebs_csi_policy.arn]
#     oidc_fully_qualified_subjects = ["system:serviceaccount:kube-system:ebs-csi-controller-sa"]
# }

# resource "aws_eks_addon" "ebs-csi" {
#     cluster_name             = module.eks.cluster_name
#     addon_name               = "aws-ebs-csi-driver"
#     addon_version            = "v1.22.0-eksbuild.2"
#     service_account_role_arn = module.irsa-ebs-csi.iam_role_arn
#     tags = {
#         "eks_addon" = "ebs-csi"
#         "terraform" = "true"
#     }
# }