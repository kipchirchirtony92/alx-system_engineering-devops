# Firewall

I used `ufw` to configure firewalls on my issued web servers.
<p align="center" />
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png" />
</p>

## Resource

- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29) 
- [Port forwarding with iptables](https://www.cogini.com/blog/port-forwarding-with-iptables/)

## Tasks :page_with_curl:

* **1. Block all incoming traffic but**
  * [1-block_all_incoming_traffic_but](./1-block_all_incoming_traffic_but): Bash
  script that installs a `ufw` firewall to block all incoming traffic except for
  ports `22`, `443` and `80` on a web server.

* **2. Port forwarding**
  * [100-port_forwarding](./100-port_forwarding): `ufw` configuration file that
  configures a firewall to redirect port `8080/TCP` to port `80/TCP`.
  