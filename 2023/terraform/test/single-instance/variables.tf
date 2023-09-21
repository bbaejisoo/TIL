variable "AWS_ACCESS_KEY" {
    description = "ACCESS KEY"
}

variable "AWS_SECRET_KEY" {
    description = "SECRET KEY"
}

variable "AWS_REGION" {
    default = "ap-northeast-2"
    description = "AWS Seoul Region"
}

variable "AMIS" {
    type = map(string)
    default = {
        ap-northeast-2 = "ami-091aca13f89c7964e"
    }
}
