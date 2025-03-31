# UntitledDesktopRPM

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![trello](https://img.shields.io/badge/Trello-UDE-blue])](https://trello.com/b/HmfuRY2K/untitleddesktop)
[![Discord](https://img.shields.io/discord/717037253292982315.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/4wgH8ZE)

RPM packages for the UntitledDesktopEnvironment. You can start using packages from this repository by creating the file `/etc/yum.repos.d/ude-rpms.repo` with the following content:
```ini
[ude-rpms]
name=UntitledDesktopRPM
baseurl=https://rpms.madladsquad.com/
enabled=1
gpgcheck=0
```
