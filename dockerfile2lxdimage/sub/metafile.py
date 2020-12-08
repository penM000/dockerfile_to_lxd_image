startup_service = """
[Unit]
Description= startup
After=multi-user.target
Before=shutdown.target
[Service]
ExecStart = /usr/local/bin/startup.sh
Restart = no
Type = simple
RemainAfterExit=yes

[Install]
WantedBy = multi-user.target

"""
startup_sh = """
#!/bin/bash
iptables -P FORWARD ACCEPT
sudo aa-complain /usr/sbin/tcpdump
"""
