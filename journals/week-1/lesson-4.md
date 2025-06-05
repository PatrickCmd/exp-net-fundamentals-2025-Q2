# Packet Tracer Simulation

**Introduction** In Lesson 4, the main goal was to simulate a complete network topology in Cisco Packet Tracer, configure devices end-to-end, and trace packet flows through each layer of the OSI model. This exercise reinforced how routers, switches, and hosts interact in a virtual environment before deploying real hardware.

**Key Learnings**

1. **Topology Design and Device Placement** - Built a simple network with a PC, switch, router, and server. - Connected interfaces correctly and verified link states.

2. **Router and Server Configuration** - Configured router interfaces with IP and enabled them. - Set up a DNS/DHCP service on the server and assigned FastEthernet settings. - Simulated a client renewing its IP with `ipconfig /renew`.

3. **Packet Tracing and OSI Layers** - Used Packet Tracer’s Simulation mode to capture PDUs at each hop. - Observed how frames encapsulate/decapsulate through switch, router, and host. - Analyzed ARP broadcasts, ICMP Echo Requests/Replies, and routing decisions in real time.

4. **Troubleshooting Workflow** - Identified where packets were dropped or forwarded incorrectly. - Inspected ARP tables and routing tables to resolve connectivity issues. - Validated end-to-end communication using ping and DNS resolution.

**Reflection** This simulation provided hands-on experience with device CLI, network services, and protocol behaviors. Tracing packets step-by-step in Packet Tracer deepened my understanding of the OSI model and the interactions between layer-2 switching and layer-3 routing in a managed topology.