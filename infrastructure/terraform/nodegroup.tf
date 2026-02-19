resource "aws_iam_role" "node_role" {

  name = "finops-node-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [{

      Effect = "Allow"

      Principal = {

        Service = "ec2.amazonaws.com"
      }

      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "worker_node_policy" {

  role = aws_iam_role.node_role.name

  policy_arn =
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
}

resource "aws_eks_node_group" "node_group" {

  cluster_name =
    aws_eks_cluster.eks.name

  node_group_name = "finops-node-group"

  node_role_arn =
    aws_iam_role.node_role.arn

  subnet_ids = [

    aws_subnet.subnet1.id,

    aws_subnet.subnet2.id
  ]

  scaling_config {

    desired_size = 2

    max_size = 5

    min_size = 1
  }

  instance_types = ["t3.medium"]
}