%define real_name UntitledDESessionLogout
%global debug_package %{nil}

Name:		ude-session-logout
Version:	2.3.0.0
Release:	1
Summary:	A log out prompt for the UntitledDesktopEnvironment
License:	MIT
URL:		https://github.com/MadLadSquad/%{real_name}
Source0:	%url/releases/download/v%version/%name-%version.tar.xz
BuildRequires:  cmake, gcc-c++, make, pkgconf, untitled-imgui-framework
Requires:	untitled-imgui-framework

%description
A log out prompt for the UntitledDesktopEnvironment

%prep
%setup -q

%build
UVKBuildTool --generate . || exit
sed -i "s/build-mode-vendor: true/build-mode-vendor: false/g" uvproj.yaml
sed -i "s/install-framework: true/install-framework: false/g" uvproj.yaml
echo "install-framework: false" >> uvproj.yaml

%install
UVKBuildTool --build "%{buildroot}/usr" %{_prefix} . || exit

%files
%{_libdir}/lib%{name}Lib.so
%{_bindir}/%{name}
%{_datadir}/config/%{name}/
%{_includedir}/%{name}/
%{_datadir}/applications/com.madladsquad.ude-session-logout.desktop
%{_datadir}/icons/ude-session-logout.png

%changelog
* Sat Mar 15 2025 MadLadSquad <contact@madladsquad.com> - 1.0-1
- Initial RPM package
