#!/usr/bin/env bash
install_package() {
  dnf builddep -y "SPECS/$1.spec"
  rpmbuild -ba "SPECS/$1.spec"
  RPM=$(find ~/rpmbuild/RPMS/x86_64/ -name "$2-*.rpm" ! -name "*-debuginfo.rpm" ! -name "*-debugsource.rpm" | grep -v "debug"  | sort | tail -n 1)
  rpm --addsign "$RPM"
  dnf install -y "$RPM"
}

install_package UntitledCLIParser
install_package UntitledDBusUtils
install_package UntitledExec
install_package UntitledI18N
install_package UntitledOpen
install_package UntitledXDGBasedir

install_package UntitledImGuiFramework

install_package UntitledDESessionLogout
install_package UntitledGameSystemManager
install_package UntitledIBusHandwriting
