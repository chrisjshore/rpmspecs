Name:           libdfl-login1-qt6
Version:        0.2.0 
Release:        1%{?dist}
Summary:        Desktop Framework Libraries Login1
BuildArch:      x86_64
License:        GNU GPLv3
URL:            https://gitlab.com/desktop-frameworks/login1
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc,meson,ninja-build,qt6-qtbase-devel
Requires:       qt6-qtbase

%description
DFL Login1 class implements a part of the systemd logind dbus protocol.

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
/usr/lib64/libdf6login1.so
/usr/lib64/libdf6login1.so.0
/usr/lib64/libdf6login1.so.0.2.0
/usr/lib64/pkgconfig/df6login1.pc
/usr/include/DFL/DF6/DFLogin1.hpp

%changelog
* Wed Dec 25 2024 Christopher Shore
- initial build
