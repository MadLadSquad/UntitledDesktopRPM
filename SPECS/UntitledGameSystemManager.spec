%define real_name UntitledGameSystemManager
%global debug_package %{nil}

Name:		untitled-game-system-manager
Version:	2.7.0.1
Release:	1
Summary:	A manager for containerised Linux gaming systems based on Incus
License:	MIT
URL:		https://github.com/MadLadSquad/%{real_name}
Source0:	%url/releases/download/v%version/%name-%version.tar.xz
BuildRequires:  cmake, gcc-c++, make, pkgconf, untitled-imgui-framework, go, incus
Requires:	untitled-imgui-framework, incus

%description
A manager for containerised Linux gaming systems based on Incus

%prep
%setup -q

%build
UVKBuildTool --generate . || exit
sed -i "s/build-mode-vendor: true/build-mode-vendor: false/g" uvproj.yaml
sed -i "s/install-framework: true/install-framework: false/g" uvproj.yaml
echo "install-framework: false" >> uvproj.yaml

%install
cd IncusBindings || exit
go build -mod=vendor -o libUGM_Incus_InternalFuncs.so -buildmode=c-shared . || exit
cd .. || exit

UVKBuildTool --build "%{buildroot}/usr" %{_prefix} . || exit

%files
%{_libdir}/lib%{real_name}Lib.so
%{_libdir}/libUGM_Incus_InternalFuncs.so
%{_bindir}/%{real_name}
%{_datadir}/config/%{real_name}/
%{_includedir}/%{real_name}/
%{_datadir}/applications/com.madladsquad.%{real_name}.desktop
%{_datadir}/icons/%{name}.png

%changelog
* Sat Mar 15 2025 MadLadSquad <contact@madladsquad.com> - 1.0-1
- Initial RPM package
