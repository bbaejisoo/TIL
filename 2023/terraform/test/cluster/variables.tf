variable "account_id" {
    default = ""
    description = "AWS Account Number"
}

variable "AWS_ACCESS_KEY" {
    default = ""
    description = "ACCESS KEY"
}

variable "AWS_SECRET_KEY" {
    default = ""
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

variable "cluster_name" {
    default = "Futurewiz-dev"
    description = "Futurewiz Test EKS Cluster"
}

variable "cluster_version" {
    default = 1.27
    description = "EKS Cluster Version"
}