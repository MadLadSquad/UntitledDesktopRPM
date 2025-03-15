%define real_name UntitledOpen

Name:		untitled-open
Version:	2.6.0.2
Release:	1
Summary:	Cross-platform C/C++ library for opening links and file pickers natively
License:	MIT
URL:		https://github.com/MadLadSquad/%{real_name}
Source0:	%url/releases/download/v%version/%name-%version.tar.xz
BuildRequires:  cmake, gcc-c++, make, pkgconf, dbus, dbus-devel, xdg-desktop-portal-devel
Requires:	dbus, xdg-desktop-portal

%description
A cross-platform C/C++ library for opening links and file pickers natively

%prep
%setup -q

%build
sed -i "s/lib\/pkgconfig/lib64\/pkgconfig/g" CMakeLists.txt
mkdir build || exit
cd build || exit
cmake .. -G"Unix Makefiles" -DCMAKE_BUILD_TYPE=RELEASE -DUIMGUI_INSTALL=ON -DCMAKE_INSTALL_PREFIX="/usr/"
make || exit

%install
cd build || exit
cmake --install . --prefix="%{buildroot}/usr/" || exit

%files
%{_libdir}/lib%{real_name}.so
%{_libdir}/pkgconfig/%{real_name}.pc
%{_includedir}/%{real_name}/

%changelog
* Sat Mar 15 2025 MadLadSquad <contact@madladsquad.com> - 1.0-1
- Initial RPM package
