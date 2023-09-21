resource "aws_instance" "test-instnace" {
    ami           = var.AMIS[var.AWS_REGION]
    instance_type = "t2.micro"
    tags = {
        Name = "test-instance"
    }
}