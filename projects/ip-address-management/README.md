# IP Address Management

## Windows Network Interfaces
For the launched windows instances we see that we have a public network interface to allow connect to the internet which is created on launch and a private network interface which is attached in private subnet to allow network communication internally.

![network interfaces](./screenshots/windows-network-interfaces-1.png)
![network interfaces](./screenshots/windows-network-interfaces-2.png)

### Public Network Interface Details

![public network interface](./screenshots/public-network-interface-details.png)
![public subnet](./screenshots/public-subnet.png)

#### Subnet-to-ENI Mapping (Public Interface)

- The primary ENI is created in the public subnet (e.g., `10.200.123.0/24`), so its primary private IP is drawn from this subnet’s CIDR.
- AWS attaches a public IPv4 address to this ENI via the Internet Gateway associated with the VPC, enabling internet connectivity.
- On EC2 launch, this ENI is bound at device index 0 of the instance.

#### Technical Explanation of IP Assignments

- **Primary Private IP**  
  Automatically allocated from the subnet CIDR (e.g., `10.200.123.45`) when the ENI is created or attached. This IP is the interface’s main address used for all inbound/outbound VPC traffic.  
- **Public IPv4 Address**  
  When _Auto-assign Public IP_ is enabled, AWS allocates a public IP from the AWS pool and maps it to the primary private IP via the Internet Gateway (IGW). This address (e.g., `3.238.80.135`) is reachable from the internet.  
- **Elastic Network Interface (ENI)**  
  The ENI resource (`eni-0abcdef1234567890`) binds both IPs and carries metadata such as MAC address, security groups, and source/dest check settings.

### Viewing and Modifying IPs with AWS CLI

```bash
# Describe the network interface
aws ec2 describe-network-interfaces \
  --network-interface-ids eni-0abcdef1234567890 \
  --profile $PROFILE

aws ec2 describe-network-interfaces \
  --network-interface-ids eni-06c944a8ac9cddb45 \
  --profile $PROFILE

# Allocate a new Elastic IP for VPC
aws ec2 allocate-address \
  --domain vpc \
  --profile $PROFILE

# Associate the Elastic IP to the ENI
aws ec2 associate-address \
  --allocation-id eipalloc-0123456789abcdef0 \
  --network-interface-id eni-0abcdef1234567890 \
  --profile $PROFILE

# Assign an additional private IP to the ENI
aws ec2 assign-private-ip-addresses \
  --network-interface-id eni-0abcdef1234567890 \
  --private-ip-addresses 10.200.123.50 \
  --profile $PROFILE
```

Replace IDs and IPs with those from your environment to replicate or update assignments in AWS.

### Private Network Interface Details

![private network interface](./screenshots/private-network-interface-details.png)
![private subnet](./screenshots/private-subnets.png)

#### Subnet-to-ENI Mapping (Private Interface)

- The secondary ENI is placed in the private subnet (e.g., `10.200.123.0/24`), so its IPs come from the private subnet’s CIDR block.
- Since the private subnet lacks a direct IGW route, this ENI has no public IP; its traffic routes via a NAT Gateway/instance in the public subnet.
- This ENI attaches at device index 1 on the instance, isolating internal management/data traffic.

#### Technical Explanation for Private Network Interface

- **Primary Private IP**  
  Automatically assigned from the private subnet CIDR (e.g., `10.200.123.100`) when the ENI is created or attached. This IP handles all VPC-internal traffic and can be used for instance-to-instance communication without traversing the Internet Gateway.  
- **Secondary Private IPs**  
  You can assign additional private IP addresses to the ENI for hosting multiple applications or services on a single instance. These extra addresses (e.g., `10.200.123.110`, `10.200.123.120`) are in the same subnet and routed internally.  
- **No Public IPv4 Address**  
  Since the ENI is in a private subnet, it does not receive an auto-assigned public IP; all outbound internet traffic would flow through a NAT Gateway or NAT Instance in the public subnet.  

#### Managing Private IPs with AWS CLI

```bash
# Describe the private ENI to view its IPs
aws ec2 describe-network-interfaces \
  --network-interface-ids eni-06c944a8ac9cddb45 \
  --query 'NetworkInterfaces[0].PrivateIpAddresses' \
  --profile $PROFILE

# Assign a secondary private IP to the ENI
aws ec2 assign-private-ip-addresses \
  --network-interface-id eni-06c944a8ac9cddb45 \
  --secondary-private-ip-address-count 1 \
  --profile $PROFILE
  # or specify exact IPs:
  # --private-ip-addresses 10.200.123.110

# Unassign a secondary private IP from the ENI
aws ec2 unassign-private-ip-addresses \
  --network-interface-id eni-06c944a8ac9cddb45 \
  --private-ip-addresses 10.200.123.110 \
  --profile $PROFILE
```

### Windows ipconfig

![ipconfig](./screenshots/windows-ipconfig.png)

#### Understanding `ipconfig` Output

- **Command**: `ipconfig` is a built-in Windows command-line utility that displays the IP configuration of all network adapters on the system.
- **IPv4 Address**: Shows the primary private IP assigned to each interface (e.g., `10.200.123.45`).
- **Subnet Mask**: Indicates the network mask (e.g., `255.255.255.0`) used to determine the host and network portions of the IP address.
- **Default Gateway**: Lists the gateway IP (typically the VPC router or NAT device) used for outbound traffic to other networks or the internet.

By running `ipconfig` on the Windows EC2 instance, you can verify that the primary ENI (device index 0) has its expected private IP/subnet configuration and default gateway pointing to the VPC router.

#### ipconfig /all

![ipconfig-all](./screenshots/windows-ipconfig-all.png)

#### Understanding `ipconfig /all` Output

- **Host Name & Primary DNS Suffix**  
  Shows the Windows computer name and DNS domain (if configured) used for network identification.
- **Physical Address (MAC)**  
  The hardware address of each network adapter (e.g., `02-42-0A-C8-7B-2D`) used for Ethernet-level communication.
- **DHCP Enabled & DHCP Server**  
  Indicates whether the adapter obtained its IP from DHCP and the server’s IP address.
- **Lease Obtained / Lease Expires**  
  Displays the DHCP lease timing, useful for troubleshooting address renewal issues.
- **DNS Servers**  
  Lists the IP addresses of DNS resolvers assigned to the adapter.
- **NetBIOS over Tcpip**  
  Specifies whether NetBIOS name resolution is enabled, affecting legacy Windows networking.

Use `ipconfig /all` when you need a comprehensive view of all network adapter settings and DHCP/DNS configurations.

### DHCP Overview

- **DHCP (Dynamic Host Configuration Protocol)** is a network service that automatically assigns IP configuration to clients from a pre-defined pool of addresses. A DHCP server manages IP leases, subnet masks, default gateways, and DNS settings, ensuring devices can join the network without manual configuration.
- **Lease Process**: Clients broadcast a **DHCPDISCOVER**, receive a **DHCPOFFER** with configuration parameters, send a **DHCPREQUEST** to accept, and receive a **DHCPACK** confirming the assignment and lease duration.
- **Renewal & Rebinding**: Before lease expiry, clients request renewal. If the server is unavailable, they attempt rebinding with any available DHCP server.

#### Manual IP Assignment vs DHCP

- **Manual (Static) Assignment**: Admins configure a fixed IP, subnet mask, gateway, and DNS directly on the device.
  - Pros: Predictable, consistent IP addressing; essential for servers and network infrastructure that need stable addresses.
  - Cons: Prone to human error; harder to scale across many devices.
- **DHCP Disabled/Manual for On-prem Devices**:
  - On-premises servers, printers, and specialized equipment often require known, unchanging IPs for service discovery, firewall rules, or routing.
  - Disabling DHCP prevents accidental address changes that could break connectivity in critical infrastructure.
  - Manual IPs can be documented and reserved to avoid IP conflicts.

Use DHCP for general-purpose client devices (workstations, laptops, mobile devices) to simplify management, and static addressing for network-critical hardware requiring consistent network presence.

