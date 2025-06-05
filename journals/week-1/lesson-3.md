# Journal Lesson 3 - IP Address Management

**Introduction**
In Lesson 3, the main goal was to gain a comprehensive understanding of IP address management on both Windows and Ubuntu EC2 instances within an AWS VPC. I learned how public and private Elastic Network Interfaces (ENIs) map to subnets, and how to view, configure, and troubleshoot IP settings using native OS tools and AWS CLI commands.

**Key Learnings**

1. **AWS VPC ENI Concepts**
   - Differentiated public vs. private subnets and their associated ENIs.
   - Understood how AWS auto-assigns primary private IPs, maps public IPv4 addresses via the Internet Gateway, and attaches ENIs at device indices.
   - Practiced AWS CLI commands to describe interfaces, assign or unassign private and Elastic IPs.

2. **Windows Networking Commands**
   - Used `ipconfig` to view IPv4 addresses, subnet masks, and default gateways for each adapter.
   - Explored `ipconfig /all` to inspect DHCP settings, lease times, DNS servers, MAC addresses, and NetBIOS configurations.

3. **DHCP Fundamentals**
   - Reviewed the DHCP lease process (DISCOVER, OFFER, REQUEST, ACK) and renewal/rebinding behaviors.
   - Discussed pros and cons of dynamic (DHCP) vs. static IP assignment and when to use each in cloud vs. on-prem environments.

4. **Linux Networking with `ip` and Netplan**
   - Interpreted `ip addr` output: interface indices, flags, MTU, MAC, IPv4/IPv6 addresses, scopes, and metrics.
   - Used `ip route` to view and manipulate the kernel routing table, add static routes, and set default gateways.
   - Practiced modifying IP configurations on Ubuntu EC2: adding, deleting, and flushing addresses; cycling interfaces.
   - Learned Netplan’s declarative YAML configuration under `/etc/netplan/`, including example static and DHCP setups, and commands (`generate`, `apply`, `try`) for rendering and applying changes.

**Reflection**
By combining AWS networking concepts with hands-on OS-level commands, I now feel somehow confident managing IP addressing and routing on cloud instances. Understanding both dynamic DHCP workflows and static configuration tools like Netplan equips me to design resilient, scalable network architectures in AWS and troubleshoot connectivity issues effectively.