module "load_balancer_controller_irsa_role" {
    source = "terraform-aws-modules/iam/aws//modules/iam-role-for-service-accounts-eks"

    role_name = "load-balancer-controller"
    attach_load_balancer_controller_policy = true

    oidc_providers = {
        ex = {
            provider_arn = module.eks.oidc_provider_arn
            namespace_service_accounts = ["kube-system:aws-load-balancer-controller"]
        }
    }
    tags = {
        Env = "dev"
    }
}

module "ebs_csi_irsa_role" {
    source = "terraform-aws-modules/iam/aws//modules/iam-role-for-service-accounts-eks"
    
    role_name             = "ebs-csi-switch-dev"
    attach_ebs_csi_policy = true
    
    oidc_providers = {
        ex = {
            provider_arn               = module.eks.oidc_provider_arn
            namespace_service_accounts = ["kube-system:ebs-csi-controller-sa"]
        }
    }
    tags = {
        Env = "dev"
    }
}