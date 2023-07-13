# AWS를 공급자로 사용하고,
# ap-northeast-2 리전에 인프라를 배포하겠다는 의미입니다.
provider "aws" {
    region = "ap-northeast-2"
}

# 각 유형의 공급자마다 서버, 데이터베이스 및 로드밸런서와 같이 
# 우리가 작성할 수 있는 다양한 종류의 리소스가 있습니다.
# resource "<PROVIDER>_<TYPE>" "<NAME>" {
#     [CONFIG ...]
# }
# EC2 인스턴스를 배포하기 위한 내용입니다.
# ami, instance_type을 사용하고자하는 내용으로 설정합니다.
resource "aws_instance" "ec2_instnace" {
    ami = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
}
