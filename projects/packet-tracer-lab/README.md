# Getting Started with Cisco Packet Tracer

## Simple Network

![Simple network](./screenshots/packet-tracer-simple-network.png)

![Router config](./screenshots/packet-tracer-router-config.png)

## Configuring the Router

After launching Packet Tracer and placing a router, use the IOS CLI to set up an IP address on the Gigabit interface and bring it online:

```text
Router> en
```  
- `en` (enable): Elevates from user EXEC mode to privileged EXEC mode, giving access to configuration commands.

```text
Router# conf t
```  
- `conf t` (configure terminal): Enters global configuration mode, where you can modify device settings.

```text
Router(config)# int gi0/0/0
```  
- `int gi0/0/0` (interface GigabitEthernet0/0/0): Selects the first GigabitEthernet interface for configuration.

```text
Router(config-if)# ip address
% Incomplete command.
```  
- Typing `ip address` alone shows that you must supply both an IP address and subnet mask.

```text
Router(config-if)# ip address 192.168.0.1 255.255.255.0
```  
- Sets the interface IPv4 address to `192.168.0.1` with a `/24` subnet mask.

```text
Router(config-if)# no shut
```  
- `no shutdown`: Enables the interface (interfaces are administratively down by default).

Once complete, verify with `show ip interface brief` to confirm the interface is up and has the correct address.

## Server Config

### DNS config

![dns config](./screenshots/server-dns-config.png)

### FastEthernet0 Config

![fastethernet config](./screenshots/server-FastEthernet0-config.png)

### Turn dns service

![dns service](./screenshots//server-turn-on-dhcp-service.png)

## PC Packet - ip renewal simulation (ipconfig /renew)

![ip renew](./screenshots/pc-cmd-ip-renew.png)

### Packet Details - OSI Model

![packet details](./screenshots/pc-packet-details.png)

#### Packet Data Unit (PDU) - Outbound

![pdu](./screenshots/packet-data-unit.png)

### Switch Packet PDU Info - OSI Model

![Switch OSI model](./screenshots/switch-packet-pdu-info-osi-model.png)

### Switch Packet PDU Info - Inbound

![Switch OSI model](./screenshots/switch-packet-inbound-pdu.png)

### Switch Packet PDU Info - Outbound

![Switch OSI model](./screenshots/switch-packet-outbound-pdu.png)

### Packet State - Router and Server 

![packet router server](./screenshots/pakcet-router-server.png)

**Screenshot State:** The router has received an ICMP Echo Request and forwarded it out of its GigabitEthernet interface toward the server’s FastEthernet0 port. This view highlights how the router uses its routing table and ARP resolution to encapsulate and deliver the packet across the network segment.

**FastEthernet0 receives the frame**

![receive packet](./screenshots/packet-server-1.png)

![ping](./screenshots/packet-server-2.png)

1. The Ping process starts the next ping request.
2. The Ping process creates an ICMP Echo Request message and sends it to the lower process.
3. The destination IP address is in the same subnet. The device sets the next-hop to destination.

![process](./screenshots/packet-server-3.png)

1. The ARP process constructs a request for the target IP address.
2. The device encapsulates the PDU into an Ethernet frame.

Router drops the packer

![packet router](./screenshots/packet-router-1.png)

Packet sent back to the switch

![Packet Back](./screenshots/packet-back-switch.png)

Packet back to PC with IP requested

![packet back](./screenshots/packet-back-pc-1.png)

![packet back](./screenshots/packet-back-pc-2.png)
