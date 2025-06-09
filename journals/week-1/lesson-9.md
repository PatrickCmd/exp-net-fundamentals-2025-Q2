# CLoud Networking - AWS

## Introduction

The main goal of this lesson was to explore cloud networking concepts on AWS: designing VPCs with public and private subnets, configuring Internet Gateways, route tables, and security groups, and automating the entire infrastructure using CloudFormation and the AWS CLI.

## Key Learnings

- **VPC Fundamentals**: Created two distinct VPCs (Requester and Accepter) with non-overlapping CIDR blocks, enabled DNS support and hostnames, and tagged resources for visibility.
- **Subnet Design**: Deployed public and private subnets across multiple Availability Zones, associated public subnets to Internet Gateways via route tables, and isolated private subnets.
- **Internet Gateway & Routing**: Configured IGWs and public route tables to allow internet egress for resources in public subnets; verified connectivity.
- **Security Groups**: Defined security groups to permit SSH/RDP only from a specified IP (MyIpCidr) and allow all internal VPC traffic.
- **VPC Peering**: Established a peering connection between the two VPCs, learned to update private route tables so instances in private subnets can communicate peer-to-peer.
- **Infrastructure as Code**: Automated provisioning with a CloudFormation template, parameterized for CIDRs, region, and networking settings.
- **Change Set Deployment**: Used the AWS CLI `cloudformation deploy` command with `--no-execute-changeset` to generate a change set, and reviewed the outcome in the console before execution.

## Challenges and Reflections

- Crafting a flexible template required careful parameterization for reusability across environments.
- Ensuring correct dependencies (IGW attachments, route table associations) in CloudFormation made the stack creation idempotent.
- Understanding `--no-execute-changeset` streamlined safe deployments by decoupling creation from execution.
- Verifying peering routes in private subnets reinforced the importance of route table placement and security group rules.

## Next Steps

- Launch EC2 instances into each subnet to validate end-to-end connectivity (public and private).
- Automate instance provisioning with userdata scripts for basic network tests (ping, traceroute).
- Investigate advanced CloudFormation features: nested stacks and stack sets for multi-account deployments.

## Lab

See lab [here](../../projects/cloud-networking/README.md)
