Name:           libdfl-applications-qt6
Version:        {{VERSION}}
Release:        1%{?dist}
Summary:        Desktop Framework Libraries Applications
BuildArch:      x86_64
License:        GNU GPLv3
URL:            https://gitlab.com/desktop-frameworks/applications
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc,meson,ninja-build,qt6-qtbase-devel,libdfl-ipc-qt6
Requires:       qt6-qtbase,libdfl-ipc-qt6

%description
This library provides a thin wrapper around QApplication, QGuiApplication and QCoreApplication, to provide
single-instance functionality. Further, with the use of DFL::IPC it also provides a smooth two-way communication
between the first and the subsequent instances.

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
/usr/lib64/libdf6application.so
/usr/lib64/libdf6application.so.0
/usr/lib64/libdf6application.so.0.2.0
/usr/lib64/libdf6coreapplication.so
/usr/lib64/libdf6coreapplication.so.0
/usr/lib64/libdf6coreapplication.so.0.2.0
/usr/lib64/libdf6guiapplication.so
/usr/lib64/libdf6guiapplication.so.0
/usr/lib64/libdf6guiapplication.so.0.2.0
/usr/lib64/pkgconfig/df6application.pc
/usr/lib64/pkgconfig/df6coreapplication.pc
/usr/lib64/pkgconfig/df6guiapplication.pc
/usr/include/DFL/DF6/DFApplication.hpp
/usr/include/DFL/DF6/DFCoreApplication.hpp
/usr/include/DFL/DF6/DFGuiApplication.hpp

%changelog
* Wed Dec 25 2024 Christopher Shore
- initial build
