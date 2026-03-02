resource "aws_vpc" "finops_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "finops-vpc"
  }
}

resource "aws_subnet" "subnet1" {
  vpc_id            = aws_vpc.finops_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "finops-subnet-1"
  }
}

resource "aws_subnet" "subnet2" {
  vpc_id            = aws_vpc.finops_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "finops-subnet-2"
  }
}