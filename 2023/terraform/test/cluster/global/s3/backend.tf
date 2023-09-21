# 주석했다가 1번 진행 후 해제하여 2번 진행
# terraform state를 local이 아닌 S3로 지정하여 remote하게 관리
terraform {
    backend "s3" {
        bucket = "futurewiz-tf-dev"
        key = "global/s3/terraform.tfstate"
        region = "ap-northeast-2"
        dynamodb_table = "terraform-state-lock"
        encrypt = true
    }
}

# 1 번 진행
# 여러 사람과 remote_state 작업을 안전하게하기 위해 Lock을 설정
resource "aws_dynamodb_table" "terraform_state_lock" {
    name = "terraform-state-lock"
    hash_key = "LockID"
    billing_mode = "PAY_PER_REQUEST"

    attribute {
        name = "LockID"
        type = "S"
    }
}