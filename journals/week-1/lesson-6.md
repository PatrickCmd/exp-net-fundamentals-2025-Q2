# Windows Firewall Rules

**Introduction** In Lesson 6, the main goal was to demonstrate how to enable external access to a custom application running on port 8000 by configuring Windows Defender Firewall inbound rules on an EC2 instance.

**Key Learnings**

1. **Security Group Considerations** - Verified that the AWS Security Group allowed TCP 8000 only from a specific source IP, blocking other traffic—even internal requests when hairpinning. - Learned that AWS Internet Gateway does not support hairpin NAT, so accessing the public IP from inside an instance can still fail.

2. **Windows Defender Firewall Behavior** - Discovered that Windows Server blocks new listening ports by default, preventing inbound connections even if the service is running and the SG is open. - Used PowerShell `New-NetFirewallRule` to create an inbound rule named "Allow TCP 8000" permitting traffic on port 8000.

3. **Verification and Testing** - Confirmed the rule via `netstat -an | findstr ":8000"` and by watching successful pings from my laptop’s browser. - Observed that disabling the firewall rule restored the timeout, proving the rule’s necessity.

**Reflection** By combining cloud-level Security Group settings with host-level Windows Firewall rules, I ensured reliable external connectivity to my Flask application on port 8000. This exercise reinforced the need to manage both network and OS firewalls when exposing services in the cloud.

## Lab

See lab [here](../../projects/windows-firewall-rules/README.md)
