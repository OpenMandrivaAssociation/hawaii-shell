%define Werror_cflags %nil
%define _disable_ld_no_undefined 1

Summary:	Hawaii shell
Name:		hawaii-shell
Version:	0.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Patch0:		0001-Fix-Wayland-protocols-build-on-compilers-other-than-.patch
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(GreenIsland)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5Compositor) >= 5.4.0
BuildRequires:	pkgconfig(Qt5WaylandClient)
BuildRequires:	pkgconfig(Qt5Xdg)
BuildRequires:	pkgconfig(weston)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libsystemd-daemon)
BuildRequires:	pam-devel

Requires:	weston
Requires:	dbus-x11
Requires:	hawaii-widget-styles >= 0.4.0
Requires:	greenisland >= 0.5.90
Requires:	%{_lib}qt5gui5-x11
Requires:	%{_lib}qt5waylandclient5
Requires:	%{_lib}qt5waylandcompositor5
Requires:	%{_lib}qt5dbus5
Requires:	plasma-workspace
Requires:	qt5-qttools
Requires:	qt5-qttools-qtdbus
Requires(post,postun,preun):	rpm-helper
Requires(post,preun):	update-alternatives

%track
prog %{name} = {
    url = http://downloads.sourceforge.net/project/mauios/hawaii/
    regex = "%{name}-(__VER__)\.tar\.gz"
    version = %{version}
}

%description
Hawaii shell.

%package sddm-theme
Summary:	Hawaii theme for SDDM
Group:		Graphical desktop/Other
Requires:	sddm
Requires:	hawaii-shell = %{EVRD}

%description sddm-theme
Hawaii theme for SDDM display manager.

%prep
%setup -q
%apply_patches
%build
%cmake_qt5 -DENABLE_SYSTEMD:BOOL=ON -DQTWAYLAND_SCANNER_EXECUTABLE=%{_libdir}/qt5/bin/qtwaylandscanner -DENABLE_MAINLINE_QTXDG:BOOL=ON -DCMAKE_BUILD_TYPE=RelWithDebInfo
%make

%install
%makeinstall_std -C build

%post
%systemd_post hawaii-notifications-daemon hawaii-polkit-agent hawaii-shell
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop default.desktop %{_datadir}/xsessions/hawaii.desktop 11

%postun
%systemd_postun hawaii-notifications-daemon hawaii-polkit-agent hawaii-shell

%preun
%systemd_preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove default.desktop %{_datadir}/xsessions/hawaii.desktop
fi

%files
%dir %{_sysconfdir}/xdg/hawaii
%dir %{_libdir}/qml/Hawaii
%dir %{_libdir}/qml/Hawaii/Components
%dir %{_libdir}/qml/Hawaii/Components/ListItems
%dir %{_libdir}/qml/Hawaii/Controls/
%dir %{_libdir}/qml/Hawaii/Effects
%dir %{_libdir}/qml/Hawaii/Themes
%dir %{_libdir}/qml/QtQuick/Controls/Styles/Wind/
%dir %{_libdir}/qml/QtQuick/Controls/Styles/Wind/images
%dir %{_libdir}/qml/org/hawaii/appchooser
%dir %{_libdir}/qml/org/hawaii/hardware
%dir %{_libdir}/qml/org/hawaii/launcher
%dir %{_libdir}/qml/org/hawaii/misc
%dir %{_libdir}/qml/org/hawaii/mixer
%dir %{_libdir}/qml/org/hawaii/mpris2
%dir %{_libdir}/qml/org/hawaii/notifications
%dir %{_libdir}/qml/org/hawaii/session
%dir %{_libdir}/qml/org/hawaii/settings
%dir %{_datadir}/greenisland/org.hawaii.desktop
%dir %{_datadir}/hawaii/themes/Wind/

%{_sysconfdir}/xdg/hawaii/shellrc
%{_bindir}/hawaii
%{_bindir}/hawaii-session
%{_bindir}/starthawaii
%{_libdir}/plugins/platformthemes/HawaiiPlatformTheme.so
%{_libdir}/qml/Hawaii/Components/*.qml
%{_libdir}/qml/Hawaii/Components/libcomponentsplugin.so
%{_libdir}/qml/Hawaii/Components/plugins.qmltypes
%{_libdir}/qml/Hawaii/Components/qmldir
%{_libdir}/qml/Hawaii/Components/ListItems/*.qml
%{_libdir}/qml/Hawaii/Components/ListItems/qmldir
%{_libdir}/qml/Hawaii/Controls/*.qml
%{_libdir}/qml/Hawaii/Controls/libcontrolsplugin.so
%{_libdir}/qml/Hawaii/Controls/plugins.qmltypes
%{_libdir}/qml/Hawaii/Controls/qmldir
%{_libdir}/qml/Hawaii/Effects/*.qml
%{_libdir}/qml/Hawaii/Effects/qmldir
%{_libdir}/qml/Hawaii/Themes/*.qml
%{_libdir}/qml/Hawaii/Themes/libdeclarative_hawaiithemes.so
%{_libdir}/qml/Hawaii/Themes/qmldir
%{_libdir}/qml/QtQuick/Controls/Styles/Wind/*.qml
%{_libdir}/qml/QtQuick/Controls/Styles/Wind/images/*.png
%{_libdir}/qml/QtQuick/Controls/Styles/Wind/qmldir
%{_libdir}/qml/org/hawaii/appchooser/libappchooserplugin.so
%{_libdir}/qml/org/hawaii/appchooser/qmldir
%{_libdir}/qml/org/hawaii/hardware/libhardwareplugin.so
%{_libdir}/qml/org/hawaii/hardware/plugins.qmltypes
%{_libdir}/qml/org/hawaii/hardware/qmldir
%{_libdir}/qml/org/hawaii/launcher/liblauncherplugin.so
%{_libdir}/qml/org/hawaii/launcher/qmldir
%{_libdir}/qml/org/hawaii/misc/libmiscplugin.so
%{_libdir}/qml/org/hawaii/misc/qmldir
%{_libdir}/qml/org/hawaii/mixer/libmixerplugin.so
%{_libdir}/qml/org/hawaii/mixer/qmldir
%{_libdir}/qml/org/hawaii/mpris2/libmpris2plugin.so
%{_libdir}/qml/org/hawaii/mpris2/plugins.qmltypes
%{_libdir}/qml/org/hawaii/mpris2/qmldir
%{_libdir}/qml/org/hawaii/notifications/libnotificationsplugin.so
%{_libdir}/qml/org/hawaii/notifications/plugins.qmltypes
%{_libdir}/qml/org/hawaii/notifications/qmldir
%{_libdir}/qml/org/hawaii/session/libsessionplugin.so
%{_libdir}/qml/org/hawaii/session/qmldir
%{_libdir}/qml/org/hawaii/settings/libsettingsplugin.so
%{_libdir}/qml/org/hawaii/settings/plugins.qmltypes
%{_libdir}/qml/org/hawaii/settings/qmldir
%{_datadir}/greenisland/org.hawaii.desktop/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/components/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/controlcenter/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/decoration/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/decoration/graphics/dropshadow.png
%{_datadir}/greenisland/org.hawaii.desktop/decoration/graphics/dropshadow.sci
%{_datadir}/greenisland/org.hawaii.desktop/desktop/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/effects/presentwindowsgrid/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/effects/revealdesktop/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/images/CREDITS
%{_datadir}/greenisland/org.hawaii.desktop/images/corner-ripple-ltr.png
%{_datadir}/greenisland/org.hawaii.desktop/images/corner-ripple-rtl.png
%{_datadir}/greenisland/org.hawaii.desktop/images/wallpaper.png
%{_datadir}/greenisland/org.hawaii.desktop/indicators/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/indicators/appchooser/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/indicators/events/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/indicators/network/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/indicators/power/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/indicators/sound/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/launcher/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/overlays/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/qmldir
%{_datadir}/greenisland/org.hawaii.desktop/windows/*.qml
%{_datadir}/greenisland/org.hawaii.desktop/windows/*.js
%{_datadir}/hawaii/themes/Wind/*.qml
%{_datadir}/hawaii/themes/Wind/*.ini

%files sddm-theme
%dir %{_datadir}/sddm/themes/mauiproject
%dir %{_datadir}/sddm/themes/mauiproject/components
%{_datadir}/sddm/themes/mauiproject/README
%{_datadir}/sddm/themes/mauiproject/*.qml
%{_datadir}/sddm/themes/mauiproject/*.png
%{_datadir}/sddm/themes/mauiproject/*.conf
%{_datadir}/sddm/themes/mauiproject/*.desktop
%{_datadir}/sddm/themes/mauiproject/components/*
