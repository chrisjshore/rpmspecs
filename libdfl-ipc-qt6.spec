Name:           libdfl-ipc-qt6
Version:        {{VERSION}}
Release:        1%{?dist}
Summary:        Desktop Framework Libraries IPC
BuildArch:      x86_64
License:        GNU GPLv3
URL:            https://gitlab.com/desktop-frameworks/ipc
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc,meson,ninja-build,json-devel,qt6-qtbase-devel
Requires:       qt6-qtbase

%description
Two very simple classes for IPC, especially between two instances of the same application. These classes are used in DFL::Application.

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
/usr/lib64/libdf6ipc.so
/usr/lib64/libdf6ipc.so.0
/usr/lib64/libdf6ipc.so.0.2.0
/usr/lib64/pkgconfig/df6ipc.pc
/usr/include/DFL/DF6/DFIpcClient.hpp
/usr/include/DFL/DF6/DFIpcServer.hpp

%changelog
* Wed Dec 25 2024 Christopher Shore
- initial build
