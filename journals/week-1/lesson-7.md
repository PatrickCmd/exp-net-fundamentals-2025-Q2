# Linux Networking Tools

**Introduction**
In Lesson 7, the main goal was to explore key Linux networking utilities and configuration files used for DNS resolution, connection inspection, data transfer, and packet analysis. This included both static config files and dynamic command-line tools.

**Key Learnings**

1. **DNS Configuration Files**
   - `/etc/hosts`: Static host-to-IP mappings for local overrides, blocking, and quick testing.
   - `/etc/systemd/resolved.conf`: Controlled upstream DNS, fallback servers, search domains, and caching via `systemd-resolved`.

2. **DNS Query with `dig`**
   - Queried specific DNS record types (A, MX, TXT, etc.) and traced resolution paths.
   - Used `+short`, `+trace`, and server override (`@8.8.8.8`) for concise and iterative lookups.

3. **Connection and Socket Inspection**
   - `netstat`: Listed active TCP/UDP sockets, listening ports, routing tables, and protocol stats.
   - `lsof`: Mapped open network sockets to processes, useful for debugging port conflicts and resource leaks.

4. **Data Transfer Tools**
   - `curl`: Flexible transfers with custom headers, methods, authentication, and versatile protocol support.
   - `wget`: Non-interactive downloader optimized for file retrieval, recursion, mirroring, and resumable downloads.
   - Understood the differences: `curl` for interactive APIs and streams, `wget` for batch file downloads.

5. **Packet Analysis with `tcpdump`**
   - Captured live traffic on interfaces, applied filter expressions (host, port, protocol), and saved to PCAP.
   - Used verbosity flags, packet count limits, and read/write options for targeted capture and review in tools like Wireshark.

**Reflection**
Practicing these tools and config files deepened my understanding of how Linux handles DNS lookup, network connections, data transfer, and packet capture. I now have a beginning solid toolkit for diagnosing networking issues, testing services, and analyzing traffic on Linux systems.