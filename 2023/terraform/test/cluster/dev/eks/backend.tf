# terraform state를 local이 아닌 S3로 지정하여 remote하게 관리
terraform {
    backend "s3" {
        bucket = "futurewiz-tf-dev"
        key = "dev/eks/terraform.tfstate"
        region = "ap-northeast-2"
        dynamodb_table = "terraform-state-lock"
        encrypt = true
    }
}