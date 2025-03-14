%define real_name UntitledIBusHandwriting

Name:		untitled-ibus-handwriting
Version:	1.3.0.1
Release:	1
Summary:	A handwriting recognition input method plugin for ibus
License:	MIT
URL:		https://github.com/MadLadSquad/%{real_name}
Source0:	%url/releases/download/v%version/%name-%version.tar.xz
BuildRequires:  cmake, gcc-c++, make, pkgconf, untitled-imgui-framework, rust, cargo, ibus
Requires:	untitled-imgui-framework, ibus

%description
A handwriting recognition input method plugin for ibus

%prep
%setup -q

%build
cd hanzi_lookup || exit
cargo build --release || exit
cd .. || exit

UVKBuildTool --generate . || exit
sed -i "s/build-mode-vendor: true/build-mode-vendor: false/g" uvproj.yaml
sed -i "s/install-framework: true/install-framework: false/g" uvproj.yaml
echo "install-framework: false" >> uvproj.yaml

%install
UVKBuildTool --build "%{buildroot}/usr" %{_prefix} . || exit

%files
%{_libdir}/lib%{real_name}Lib.so
%{_bindir}/%{real_name}
%{_datadir}/config/%{real_name}/
%{_prefix}/etc/%{real_name}/
%{_includedir}/%{real_name}/
%{_datadir}/icons/%{name}.png

%changelog
* Sat Mar 15 2025 MadLadSquad <contact@madladsquad.com> - 1.0-1
- Initial RPM package
