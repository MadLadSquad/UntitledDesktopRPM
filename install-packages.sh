#!/usr/bin/env bash
install_package() {
  dnf builddep -y "SPECS/$1.spec"
  rpmbuild -ba "SPECS/$1.spec"
  RPM=$(find ~/rpmbuild/RPMS/x86_64/ -name "$2-*.rpm" ! -name "*-debuginfo.rpm" ! -name "*-debugsource.rpm" | grep -v "debug"  | sort | tail -n 1)
  rpm --addsign "$RPM"
  dnf install -y "$RPM"
}

install_package UntitledCLIParser untitled-cli-parser
install_package UntitledDBusUtils untitled-dbus-utils
install_package UntitledExec untitled-exec
install_package UntitledI18N untitled-i18n
install_package UntitledOpen untitled-open
install_package UntitledXDGBasedir untitled-xdg-basedir

install_package UntitledImGuiFramework untitled-imgui-framework

install_package UntitledDESessionLogout ude-session-logout
install_package UntitledGameSystemManager untitled-game-system-manager
install_package UntitledIBusHandwriting untitled-ibus-handwriting
