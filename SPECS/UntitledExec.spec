%define real_name UntitledExec
%global debug_package %{nil}

Name:		untitled-exec
Version:	5.0.0.1
Release:	1
Summary:	Cross-platform library for executing applications as separate processes
License:	MIT
URL:		https://github.com/MadLadSquad/%{real_name}
Source0:	%url/releases/download/v%version/%name-%version.tar.xz
BuildRequires:  cmake, gcc-c++, make, pkgconf

%description
A cross-platform library for executing applications as separate processes

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
%{_libdir}/libuexec.so
%{_libdir}/pkgconfig/uexec.pc
%{_includedir}/uexec/

%changelog
* Sat Mar 15 2025 MadLadSquad <contact@madladsquad.com> - 1.0-1
- Initial RPM package
