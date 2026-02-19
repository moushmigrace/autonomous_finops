resource "aws_eks_cluster" "eks" {

  name = "finops-cluster"

  role_arn =
    aws_iam_role.eks_cluster_role.arn

  vpc_config {

    subnet_ids = [

      aws_subnet.subnet1.id,

      aws_subnet.subnet2.id
    ]
  }
}

data "aws_eks_cluster_auth" "eks" {

  name = aws_eks_cluster.eks.name
}