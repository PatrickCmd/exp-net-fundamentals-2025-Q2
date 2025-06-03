# Setup Cloud Environment using Web Console (ClickOps)

## Launch VPC with One Availability Zone and Subnets

Follow these steps to create a VPC with a single Availability Zone, one public subnet, and one private subnet (VPC CIDR: `10.200.123.0/24`):

1. **Open the VPC Dashboard**  
   ![Open VPC Dashboard](screenshots/create-vpc-1.png)

2. **Click Create VPC and More**  
   ![Create VPC Button](screenshots/create-vpc-2.png)

3. **Configure Your VPC**  
   - _Name tag_: `network-bootcamp-vpc`  
   - _IPv4 CIDR block_: `10.200.123.0/24`  
   - _Availability Zone_: choose one (e.g., `us-east-1a`)  
   - Leave other settings at defaults  
   ![VPC Configuration](screenshots/create-vpc-3.png)

4. **Review and Create**  
   ![Review and Create](screenshots/create-vpc-4.png)

By default, AWS will create one public and one private subnet in your chosen AZ using the specified CIDR block. Verify both subnets under **Subnets** in the VPC console (look for tags like `network-bootcamp-PublicSubnetAZ1` and `network-bootcamp-PrivateSubnetAZ1`).

## Create Key Pairs

Follow these steps to generate key pairs for SSH and RDP access:

1. **Navigate to Key Pairs**  
   ![Open Key Pairs](screenshots/create-keypair-pem.png)

2. **Create PEM Key Pair**  
   - _Key pair name_: `network-bootcamp-key`  
   - _File format_: `pem`  
   ![Create PEM Key Pair](screenshots/create-keypair-pem.png)

3. **Create PPK Key Pair (Windows)**  
   - _Key pair name_: `network-bootcamp-key`  
   - _File format_: `ppk`  
   ![Create PPK Key Pair](screenshots/create-keypair-ppk.png)

**Key Pair Details and Best Practices**  
- AWS key pairs provide secure SSH/RDP authentication for EC2 instances without passwords.  
- The `.pem` private key is used with Linux/macOS SSH clients (`ssh -i nwtbootcampkey.pem ec2-user@<public-ip>`).  
- The `.ppk` private key is used with PuTTY on Windows; import `.pem` into PuTTYgen to generate `.ppk`.  
- Restrict permissions on your private keys: `chmod 400 nwtbootcampkey.pem`.  
- Store keys securely—do not commit them to version control or share publicly.  
- You can associate this key pair with any new EC2 instance in the same region and account.  

## Launch Windows Server EC2 Instance

Follow these steps to launch a Windows Server EC2 instance:

1. **Open the EC2 Console**  
   ![EC2 Console](screenshots/create-windows-server-1.png)

2. **Click Launch Instance**  
   ![Launch Instance](screenshots/create-windows-server-2.png)

3. **Select a Free Tier Eligible Windows AMI**  
   ![Select Windows AMI](screenshots/create-windows-server-3.png)

4. **Choose Instance Type**  
   - _Instance type_: `t3.large`  
   ![Instance Type](screenshots/create-windows-server-4.png)

5. **Configure Instance Details**  
   - _Network_: `network-bootcamp-vpc`  
   - _Subnet_: `network-bootcamp-PublicSubnetAZ1`  
   - _Auto-assign Public IP_: Enable  
   ![Configure Details](screenshots/create-windows-server-5.png)

6. **Select Key Pair**  
   - _Key pair name_: `network-bootcamp-key` (pem)  
   ![Select Key Pair](screenshots/create-keypair-pem.png)

7. **Add Security Group**  
   - _Security group name_: `allow-rdp-login`  
   - _Inbound rules_:  
     - **RDP**: Source = My IP  
     - **All traffic**: Source = `10.200.123.0/24`  
   ![Security Group](screenshots/create-windows-server-5.png)

   **Security Group Rationale**  
   - **RDP (TCP 3389)** with _My IP_ ensures that only your current public address can initiate remote desktop sessions, reducing exposure to unauthorized access.  
   - **All traffic** with _Custom: 10.200.123.0/24_ allows unrestricted communication between instances in your VPC (public and private subnets) for management and inter-service traffic without opening ports to the internet.

8. **Review and Launch**  
   Verify your settings and click **Launch** to start the instance.

## Launch and Attach Network Interface (ENA)

Follow these steps to create a secondary network interface in your VPC and attach it to the Windows instance:

1. **Open Network Interfaces**  
   ![Open Network Interfaces](screenshots/create-windows-server-nic-1.png)

2. **Create Network Interface**  
   - _Description_: `network-bootcamp-nic`  
   - _Interface type_: `ena`  
   - _Subnet_: `network-bootcamp-PrivateSubnetAZ1`  
   - _Auto-assign private IP_: Enable  
   - _Security group_: `allow-rdp-login`  
   ![Create NIC](screenshots/create-windows-server-nic-2.png)

3. **Attach Network Interface**  
   - Select the NIC `network-bootcamp-nic`  
   - Click **Actions > Attach**  
   - Choose **Instance**: your Windows Server instance  
   ![Attach NIC](screenshots/attach-network-interface-windows-box.png)  
   ![Attach NIC Confirmation](screenshots/attach-network-interface-windows-box-2.png)

**Network Interface Rationale**  
- Separates management and application traffic by using a secondary ENA, improving security and network segmentation.  
- Enables you to move or reassign the interface between instances without recreating configurations.

