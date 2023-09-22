resource "aws_eks_addon" "aws_ebs_csi_driver" {
    cluster_name             = module.eks.cluster_name
    addon_name               = "aws-ebs-csi-driver"
    service_account_role_arn = "arn:aws:iam::${var.account_id}:role/ebs-csi-switch-dev"
    addon_version            = "v1.22.0-eksbuild.2"
    resolve_conflicts_on_create        = "OVERWRITE"
}