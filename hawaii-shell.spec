%define Werror_cflags %nil
%define _disable_ld_no_undefined 1
%define snap 20150403

Summary:	Hawaii shell
Name:		hawaii-shell
Version:	0.4.0
Release:	0.%{snap}.2
License:	GPLv2+ and LGPLv2.1+
Group:		Graphical desktop/Other
URL:		https://hawaii-desktop.github.io
# git archive --format=tar --prefix=hawaii-shell-0.4.0-$(date +%Y%m%d)/ HEAD | xz -vf > hawaii-shell-0.4.0-$(date +%Y%m%d).tar.xz
Source0:	https://github.com/hawaii-desktop/hawaii-desktop/archive/%{name}-%{version}-%{snap}.tar.xz
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
%rename hawaii-shell-sddm-theme < 0.4.0

%track
prog %{name} = {
    url = https://github.com/hawaii-desktop/%{name}/archive/
    regex = "v(__VER__)\.tar\.gz"
    version = %{version}
}

%description
This is the Hawaii desktop environment shell.

It contains a Qt platform theme plugin,
shells for different form factors such as desktop,
netbook and tablet and QML plugins.

%prep
%setup -qn %{name}-%{version}-%{snap}
%apply_patches

%build
%cmake_qt5 -DENABLE_SYSTEMD:BOOL=ON -DQTWAYLAND_SCANNER_EXECUTABLE=%{_libdir}/qt5/bin/qtwaylandscanner -DENABLE_MAINLINE_QTXDG:BOOL=ON -DCMAKE_BUILD_TYPE=RelWithDebInfo
%make

%install
%makeinstall_std -C build

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
%dir %{_datadir}/hawaii/themes/Wind/
%{_sysconfdir}/xdg/hawaii/shellrc
%{_bindir}/hawaii
%{_bindir}/hawaii-session
%{_bindir}/starthawaii
%{_userunitdir}/hawaii-kms.service
%{_userunitdir}/hawaii-nested.service
%{_userunitdir}/hawaii.target
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
%{_datadir}/greenisland/org.hawaii.desktop
%{_datadir}/hawaii/themes/Wind/*.qml
%{_datadir}/hawaii/themes/Wind/*.ini
%{_datadir}/wayland-sessions/hawaii.desktop
