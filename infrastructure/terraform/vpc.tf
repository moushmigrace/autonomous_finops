############################
# VPC
############################

resource "aws_vpc" "finops_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "finops-vpc"
  }
}

############################
# Internet Gateway
############################

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.finops_vpc.id

  tags = {
    Name = "finops-igw"
  }
}

############################
# Public Subnet 1
############################

resource "aws_subnet" "subnet1" {
  vpc_id                  = aws_vpc.finops_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "finops-subnet-1"

    # REQUIRED FOR EKS LOADBALANCER
    "kubernetes.io/cluster/finops-cluster" = "shared"
    "kubernetes.io/role/elb"               = "1"
  }
}

############################
# Public Subnet 2
############################

resource "aws_subnet" "subnet2" {
  vpc_id                  = aws_vpc.finops_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true

  tags = {
    Name = "finops-subnet-2"

    # REQUIRED FOR EKS LOADBALANCER
    "kubernetes.io/cluster/finops-cluster" = "shared"
    "kubernetes.io/role/elb"               = "1"
  }
}

############################
# Route Table
############################

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.finops_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "finops-public-rt"
  }
}

############################
# Route Table Associations
############################

resource "aws_route_table_association" "subnet1_assoc" {
  subnet_id      = aws_subnet.subnet1.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "subnet2_assoc" {
  subnet_id      = aws_subnet.subnet2.id
  route_table_id = aws_route_table.public_rt.id
}