# Windows Networking Tools

**Introduction** In Lesson 5, the main goal was to gain hands-on familiarity with essential Windows networking CLI tools for diagnosing and troubleshooting connectivity issues. I explored `ipconfig`, `ping`, `tracert`, `nslookup`, `netstat`, and `route` to understand their outputs, options, and practical use cases.

**Key Learnings**

1. **IP Configuration with `ipconfig`**
   - Viewed basic adapter information (`ipconfig`), interpreted IPv4/IPv6 addresses, subnet masks, and gateways.
   - Used `ipconfig /?` for help and `ipconfig /all` to inspect DHCP leases, DNS servers, MAC addresses, and detailed TCP/IP settings.

2. **Connectivity Testing with `ping`**
   - Sent ICMP Echo Requests and evaluated round-trip times.
   - Leveraged `/t` for continuous pings, `/a` for reverse DNS resolution, and `/n` to specify the number of requests.

3. **Path Discovery with `tracert`**
   - Mapped packet paths across network hops by incrementing TTL values.
   - Identified latency and breakpoints in routes, and used options like `/d` and `/h` for faster or deeper traces.

4. **DNS Queries with `nslookup`**
   - Performed both non-interactive and interactive lookups to resolve hostnames and record types (A, AAAA, MX, etc.).
   - Switched DNS servers on-the-fly and queried specific record types to troubleshoot name resolution issues.

5. **Connection Inspection with `netstat`**
   - Examined active TCP/UDP connections, listening ports, and associated PIDs (`-o`).
   - Reviewed routing tables, protocol statistics, and filtered outputs with `-a`, `-n`, `-p`, and `-s`.

6. **Route Management with `route`**
   - Displayed the local IP routing table and added, deleted, or modified routes.
   - Created persistent routes (`-p`) to ensure static paths survive system reboots.

**Reflection** By mastering these Windows networking tools, I can efficiently diagnose IP, connectivity, and DNS issues, map network paths, and manage routing configurations. These skills are crucial for maintaining robust Windows-based networks and troubleshooting real-world infrastructure problems.

## Project

See project [here](../../projects/windows-networking-tools/README.md) 