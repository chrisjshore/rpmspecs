Name:           libdfl-utils-qt6
Version:        0.2.0 
Release:        1%{?dist}
Summary:        Desktop Framework Libraries Utils
BuildArch:      x86_64
License:        GNU GPLv3
URL:            https://gitlab.com/desktop-frameworks/utils
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc,meson,ninja-build,qt6-qtbase-devel
Requires:       qt6-qtbase

%description
This library provides single-instance Application classes for Core and Gui, advanced file-system watcher, a very simple IPC,
functions to return XDG variables, desktop file parsing, and read various system info like battery, network, storage, cpu
and RAM info.

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
/usr/lib64/libdf6utils.so
/usr/lib64/libdf6utils.so.0
/usr/lib64/libdf6utils.so.0.2.0
/usr/lib64/pkgconfig/df6utils.pc
/usr/include/DFL/DF6/DFUtils.hpp

%changelog
* Wed Dec 25 2024 Christopher Shore
- initial build
