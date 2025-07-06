%define real_name UntitledImGuiFramework
%global debug_package %{nil}

Name:		untitled-imgui-framework
Version:	1.3.0.0
Release:	1
Summary:	Cross-platform desktop application development framework
License:	MIT
URL:		https://github.com/MadLadSquad/%{real_name}
Source0:	%url/releases/download/v%version/%name-%version.tar.xz
BuildRequires:  cmake, gcc-c++, make, pkgconf, yaml-cpp, yaml-cpp-devel, utf8cpp-devel, vulkan-headers, vulkan-validation-layers, vulkan-loader-devel, vulkan-loader, glfw, glfw-devel, freetype, fontconfig, fontconfig-devel, untitled-dbus-utils, untitled-cli-parser, untitled-exec, untitled-i18n, untitled-open, untitled-xdg-basedir
Requires:	yaml-cpp, vulkan-loader, glfw, freetype, fontconfig, untitled-dbus-utils, untitled-cli-parser, untitled-exec, untitled-i18n, untitled-open, untitled-xdg-basedir

%description
A cross-platform desktop application development framework based on the dear imgui library

%prep
%setup -q

%build
sed -i "s/lib\/pkgconfig/lib64\/pkgconfig/g" UVKBuildTool/Templates/%{real_name}/BuildFiles/CMakeInstall.tmpl || exit
./install.sh ci || exit
./create-project.sh ebuild --skip-compilation || exit

sed -i "s/build-mode-vendor: true/build-mode-vendor: false/g" Projects/ebuild/uvproj.yaml
echo "system-wide: true" >> Projects/ebuild/uvproj.yaml
echo "install-framework: true" >> Projects/ebuild/uvproj.yaml

%install
cd UVKBuildTool/build || exit
./UVKBuildTool --build %{buildroot}/usr %{_prefix} ../../Projects/ebuild || exit

cmake .. -G"Unix Makefiles" -DCMAKE_BUILD_TYPE=RELEASE -DUBT_INSTALL=ON -DCMAKE_INSTALL_PREFIX="/usr/" -DUBT_FRAMEWORK_DIR="%{_includedir}/%{real_name}" -DUBT_DATA_INSTALL_PREFIX="%{_datadir}" || exit
make -j "$(grep -c processor /proc/cpuinfo)" || exit
cmake --install . --prefix="%{buildroot}/usr/" || exit

%files
%{_libdir}/lib%{real_name}.so
%{_libdir}/pkgconfig/%{real_name}.pc
%{_includedir}/%{real_name}/
%{_bindir}/UVKBuildTool
%{_libdir}/libUVKBuildToolLib.so
%{_datadir}/UVKBuildTool/
%exclude %{_datadir}/utf8cpp
%exclude %{_includedir}/utf8cpp
%exclude %{_datadir}/config/ebuild
%exclude %{_includedir}/ebuild
%exclude %{_libdir}/libebuildLib.so
%exclude %{_bindir}/ebuild

%changelog
* Sat Mar 15 2025 MadLadSquad <contact@madladsquad.com> - 1.0-1
- Initial RPM package
