module "karpenter" {
    source = "terraform-aws-modules/eks/aws//modules/karpenter"
    
    cluster_name           = var.cluster_name
    irsa_oidc_provider_arn = module.eks.oidc_provider_arn
    
    policies = {
        AmazonSSMManagedInstanceCore = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
    }
    
    tags = {
        Env = "dev"
    }
}