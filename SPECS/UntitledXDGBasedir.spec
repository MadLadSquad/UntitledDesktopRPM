%define real_name UntitledXDGBasedir

Name:		untitled-xdg-basedir
Version:	5.0.0.1
Release:	1
Summary:	C/C++ implementation of the XDG basedir specification
License:	MIT
URL:		https://github.com/MadLadSquad/%{real_name}
Source0:	%url/releases/download/v%version/%name-%version.tar.xz
BuildRequires:  cmake, gcc-c++, make, pkgconf

%description
A C/C++ implementation of the XDG base directory specification

%prep
%setup -q

%build
sed -i "s/lib\/pkgconfig/lib64\/pkgconfig/g" CMakeLists.txt
mkdir build || exit
cd build || exit
cmake .. -G"Unix Makefiles" -DNO_IGNORE_RELATIVE_DIRS=OFF -DCREATE_DIRS=OFF -DCMAKE_BUILD_TYPE=RELEASE -DUIMGUI_INSTALL=ON -DCMAKE_INSTALL_PREFIX="/usr/"
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
