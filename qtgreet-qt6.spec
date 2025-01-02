Name:           qtgreet-qt6
Version:        2.0.2 
Release:        1%{?dist}
Summary:        Desktop Framework Libraries QtGreet
BuildArch:      x86_64
License:        GNU GPLv3
URL:            https://gitlab.com/desktop-frameworks/wayqt
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc,meson,ninja-build,qt6-qtbase-devel,mpv-devel,qwlroots-devel
Requires:       qt6-qtbase,qt6-qtwayland,greetd,mpv-libs,libdfl-ipc-qt6,libdfl-applications-qt6,libdfl-utils-qt6,libdfl-login1-qt6,libdfl-wayqt-qt6

%description
Qt based greeter for greetd, to be run under wayfire or similar wlr-based compositors.

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
/etc/qtgreet/config.ini
/etc/qtgreet/sway.cfg
/etc/qtgreet/users.conf
/etc/qtgreet/wayfire.ini
/usr/bin/qtgreet
/usr/bin/greetwl
/usr/share/icons/hicolor/scalable/apps/QtGreet.svg
/usr/share/icons/hicolor/512x512/apps/QtGreet.png
/usr/share/qtgreet/README.md
/usr/share/qtgreet/Changelog
/usr/share/qtgreet/ReleaseNotes
/usr/share/qtgreet/backgrounds/BlurryBlob.png
/usr/share/qtgreet/backgrounds/BlurryBlob.svg
/usr/share/qtgreet/backgrounds/BurningDesire.svg
/usr/share/qtgreet/backgrounds/Camel.Sunset.svg
/usr/share/qtgreet/backgrounds/Christmas.svg
/usr/share/qtgreet/backgrounds/Hexagons.svg
/usr/share/qtgreet/backgrounds/LayeredBlobsDark.svg
/usr/share/qtgreet/backgrounds/LayeredBlobsLight.svg
/usr/share/qtgreet/backgrounds/Mountains.Sunset.svg
/usr/share/qtgreet/backgrounds/Rectangles.svg
/usr/share/qtgreet/backgrounds/Rings.svg
/usr/share/qtgreet/backgrounds/Sailboats.svg
/usr/share/qtgreet/backgrounds/SmoothGradient.png
/usr/share/qtgreet/backgrounds/SmoothGradient.svg
/usr/share/qtgreet/backgrounds/Squares.svg
/usr/share/qtgreet/backgrounds/Sunrise.svg
/usr/share/qtgreet/backgrounds/Tree.svg
/usr/share/qtgreet/backgrounds/Water.svg
/usr/share/qtgreet/themes/LytMgr.py
/usr/share/qtgreet/themes/aerial/4k.m3u
/usr/share/qtgreet/themes/aerial/all_sd.m3u
/usr/share/qtgreet/themes/aerial/day.m3u
/usr/share/qtgreet/themes/aerial/index.theme
/usr/share/qtgreet/themes/aerial/layout.hjson
/usr/share/qtgreet/themes/aerial/night.m3u
/usr/share/qtgreet/themes/aerial/style.qss
/usr/share/qtgreet/themes/compact/index.theme
/usr/share/qtgreet/themes/compact/layout.hjson
/usr/share/qtgreet/themes/compact/style.qss
/usr/share/qtgreet/themes/default/index.theme
/usr/share/qtgreet/themes/default/layout.hjson
/usr/share/qtgreet/themes/default/style.qss
/usr/share/qtgreet/themes/sidebar/index.theme
/usr/share/qtgreet/themes/sidebar/layout.hjson
/usr/share/qtgreet/themes/sidebar/style.qss
/var/lib/qtgreet


%changelog
* Wed Dec 25 2024 Christopher Shore
- initial build
