# Setup Cloud Environment using Web Console (ClickOps)

## Journal Summary

In this lesson, the main goal was to learn how to set up foundational AWS networking and compute resources entirely through the web console (ClickOps). By manually creating a VPC, subnets, security groups, key pairs, and EC2 instances, I achieved a deep understanding of each step in the provisioning process and the rationale behind various configuration choices.

Key takeaways:

- **VPC & Subnets**: Learned how to create a custom VPC with a single Availability Zone, define public and private subnets, and verify the subnet CIDR assignments.  
- **Internet Gateway & Routing**: Attached an Internet Gateway and configured route tables to allow public subnet traffic to the internet while maintaining isolation for the private subnet.  
- **Key Pair Management**: Generated both PEM and PPK key pairs, understood best practices for secure key storage and file permissions, and practiced using these keys with native SSH and PuTTY.  
- **Security Groups**: Designed inbound rules to permit RDP from my IP and all internal VPC traffic, reinforcing the principle of least privilege and network segmentation.  
- **Windows EC2 Instance**: Launched a Windows Server instance, attached a secondary ENA for management traffic, and connected via RDP—gaining familiarity with Windows AMI selection and encrypted password retrieval.  
- **Ubuntu EC2 Instance**: Provisioned an Ubuntu instance with a gp3 root volume, attached a secondary ENA, and connected via SSH—practicing both PuTTY-based and native SSH workflows.  
- **Network Interface Attachments**: Learned to create and attach ENAs for enhanced network segmentation and management flexibility.  

Reflection:

Performing these tasks manually helped me appreciate the underlying AWS resource relationships and the importance of naming conventions and tagging strategies. It also highlighted how Infrastructure as Code (IaC) can automate and document these steps, setting the stage for the next lessons on CloudFormation and deployment scripting.

## Project
See the complete project [here](../../projects/cloud-setup-clickops/README.md)

