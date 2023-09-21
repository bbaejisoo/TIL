module "s3_bucket_tfstate" {
    source = "terraform-aws-modules/s3-bucket/aws"
    bucket = "futurewiz-tf-dev"
    create_bucket = false
    versioning = {
        enable = true
    }
}