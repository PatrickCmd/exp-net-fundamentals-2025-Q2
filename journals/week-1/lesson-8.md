# Lesson 8: Linux Firewall Rules

## Introduction

The main goal of this lesson was to explore and master Linux firewalling tools—understanding how UFW, firewalld, and iptables leverage the kernel’s Netfilter framework to control network traffic. We focused on crafting outbound rules, verifying their behavior, and ensuring persistence across reboots.

## Key Learnings

- Kernel-Level Packet Filtering: Linux uses Netfilter under the hood, exposing tools such as **iptables** (legacy IPv4 filtering) and **nftables** (modern replacement).

- UFW (Uncomplicated Firewall):
  - A user-friendly wrapper around iptables for quick rule definition.
  - Default policies (`deny incoming`, `allow outgoing`) and rule files under `/etc/ufw/`.
  - Commands to block outbound traffic (e.g., `sudo ufw deny out 4000/tcp`) and view status.

- firewalld:
  - A zone-based, dynamic firewall daemon common on Red Hat–derived distributions.
  - Difference between runtime (lost on reboot) and permanent rules (requires `--permanent` + reload).
  - Creating rich rules to drop egress TCP port 4000 without touching iptables directly.

- iptables:
  - Organizes rules into tables (`filter`, `nat`, `mangle`, `raw`) and chains (`INPUT`, `OUTPUT`, `FORWARD`).
  - Common operations:
    - Append: `sudo iptables -A OUTPUT -p tcp --dport 4000 -j DROP`
    - Insert: `sudo iptables -I OUTPUT 1 -p tcp --dport 4000 -j DROP`
    - Delete: `sudo iptables -D OUTPUT -p tcp --dport 4000 -j DROP`
    - Flush: `sudo iptables -F`
    - Default policy: `sudo iptables -P OUTPUT DROP`
  - Listing rules with counters: `sudo iptables -L -n -v`.

- Persistence of Rules:
  - Debian/Ubuntu: `iptables-persistent` package + `sudo netfilter-persistent save`.
  - RHEL/CentOS 7: `sudo service iptables save && systemctl restart iptables`.
  - RHEL/CentOS 8+: Install `iptables-services`, enable the service, and use `iptables-save`/`iptables-restore`.

## Challenges and Reflections

- Syntax Variations: Subtle differences between UFW, firewalld rich rules, and raw iptables commands required careful quoting and flag use.
- DROP vs REJECT: Observing how DROP silently hangs connections versus REJECT immediately returns errors.
- Persistence Methods: Each distribution had its own method, underscoring the value of exploring unified solutions like nftables.

## Next Steps

- Expand the **iptables** section with deeper NAT (MASQUERADE, DNAT), mangle, and raw table examples.
- Add IPv6 variants using **ip6tables** and firewalld IPv6 zone rules.
- Investigate migrating custom rulesets to **nftables** for a more streamlined, future-proof firewall management experience.
