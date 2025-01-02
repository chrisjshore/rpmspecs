Name:           libdfl-wayqt-qt6
Version:        0.2.0 
Release:        1%{?dist}
Summary:        Desktop Framework Libraries WayQt
BuildArch:      x86_64
License:        GNU GPLv3
URL:            https://gitlab.com/desktop-frameworks/wayqt
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc,meson,ninja-build,qt6-qtbase-devel,qt6-qtbase-private-devel,qt6-qtwayland-devel,wayland-devel,libpng-devel
Requires:       qt6-qtbase,qt6-qtwayland,libpng

%description
The Qt-based library to handle Wayland and Wlroots protocols to be used with any Qt project.
Additionally, Wayfire's private protocol as well is supported. As the project develops, support for custom protocols may be added.

%prep
%autosetup

%build
%meson --prefix=%{_prefix} --buildtype=release -Duse_qt_version=qt6
%meson_build

%install
%meson_install

%clean
rm -rf %{buildroot}

%files
/usr/lib64/libwayqt-qt6.so
/usr/lib64/libwayqt-qt6.so.0
/usr/lib64/libwayqt-qt6.so.0.2.0
/usr/lib64/pkgconfig/wayqt-qt6.pc
/usr/include/DFL/DF6/wayqt/DataControl.hpp
/usr/include/DFL/DF6/wayqt/DesQShell.hpp
/usr/include/DFL/DF6/wayqt/GammaControl.hpp
/usr/include/DFL/DF6/wayqt/Idle.hpp
/usr/include/DFL/DF6/wayqt/InputInhibition.hpp
/usr/include/DFL/DF6/wayqt/LayerShell.hpp
/usr/include/DFL/DF6/wayqt/Output.hpp
/usr/include/DFL/DF6/wayqt/OutputManager.hpp
/usr/include/DFL/DF6/wayqt/OutputPowerManager.hpp
/usr/include/DFL/DF6/wayqt/Registry.hpp
/usr/include/DFL/DF6/wayqt/ScreenCopy.hpp
/usr/include/DFL/DF6/wayqt/SessionLock.hpp
/usr/include/DFL/DF6/wayqt/ToplevelManager.hpp
/usr/include/DFL/DF6/wayqt/WayQtUtils.hpp
/usr/include/DFL/DF6/wayqt/WayfireShell.hpp
/usr/include/DFL/DF6/wayqt/WindowManager.hpp
/usr/include/DFL/DF6/wayqt/XdgActivation.hpp
/usr/include/DFL/DF6/wayqt/XdgPopup.hpp
/usr/include/DFL/DF6/wayqt/XdgPositioner.hpp
/usr/include/DFL/DF6/wayqt/XdgShell.hpp
/usr/include/DFL/DF6/wayqt/XdgTopLevel.hpp

%changelog
* Wed Dec 25 2024 Christopher Shore
- initial build
