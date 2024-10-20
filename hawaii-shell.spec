%define Werror_cflags %nil
%define _disable_ld_no_undefined 1
%define snap %nil

%define devname %mklibname Hawaii -d

Summary:	Hawaii shell
Name:		hawaii-shell
Version:	0.8.0
Release:	1
License:	GPLv2+ and LGPLv2.1+
Group:		Graphical desktop/Other
URL:		https://hawaiios.org/
# git archive --format=tar --prefix=hawaii-shell-0.4.93-$(date +%Y%m%d)/ HEAD | xz -vf > hawaii-shell-0.4.93-$(date +%Y%m%d).tar.xz
#Source0:	https://github.com/hawaii-desktop/hawaii-desktop/archive/%{name}-%{version}-%{snap}.tar.xz
Source0:	https://github.com/hawaii-desktop/hawaii-shell/releases/download/v%{version}/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KF5NetworkManagerQt)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	cmake(GreenIsland)
BuildRequires:	cmake(Hawaii)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(polkit-qt5-1)
BuildRequires:	pkgconfig(Qt5Compositor) >= 5.4.0
BuildRequires:	pkgconfig(Qt5WaylandClient)
BuildRequires:	pkgconfig(Qt5Xdg)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(mobile-broadband-provider-info)
BuildRequires:	pam-devel

Requires:	weston
Requires:	dbus-x11
Requires:	hawaii-widget-styles >= 0.8.0
Requires:	greenisland >= 0.8.1
Requires:	%{_lib}qt5gui5-x11
Requires:	%{_lib}qt5waylandclient5
Requires:	%{_lib}qt5waylandcompositor5
Requires:	%{_lib}qt5dbus5
Requires:	qt5-qttools
Requires:	qt5-qttools-qtdbus
Requires:	qt5-qtwayland
Requires(post,postun,preun):	rpm-helper
Requires(post,preun):	update-alternatives
Obsoletes:	%{mklibname Hawaii -d} < 0.6.0
Provides:	%{mklibname Hawaii -d} = 0.6.0
Obsoletes:	%{mklibname Hawaii 0} < 0.6.0
Provides:	%{mklibname Hawaii 0} = 0.6.0
%rename hawaii-shell-sddm-theme < 0.4.0

%track
prog %{name} = {
    url = https://github.com/hawaii-desktop/%{name}/archive/
    regex = "v(__VER__)\.tar\.xz"
    version = %{version}
}

%description
This is the Hawaii desktop environment shell.

It contains a Qt platform theme plugin,
shells for different form factors such as desktop,
netbook and tablet and QML plugins.

%prep
%setup -q
%autopatch -p1

%build
%cmake_qt5 \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
    -DQtWaylandScanner_EXECUTABLE=%{_libdir}/qt5/bin/qtwaylandscanner

%make

%install
%makeinstall_std -C build

%files
%dir %{_libdir}/qt5/qml/Hawaii
%dir %{_libdir}/qt5/qml/Hawaii/Components
%dir %{_libdir}/qt5/qml/Hawaii/Components/ListItems
%dir %{_libdir}/qt5/qml/Hawaii/Controls/
%dir %{_libdir}/qt5/qml/Hawaii/Effects
%dir %{_libdir}/qt5/qml/Hawaii/Themes
%dir %{_libdir}/qt5/qml/QtQuick/Controls/Styles/Wind/
%dir %{_libdir}/qt5/qml/QtQuick/Controls/Styles/Wind/images
%dir %{_libdir}/qt5/qml/org/hawaiios/hardware
%dir %{_libdir}/qt5/qml/org/hawaiios/launcher
%dir %{_libdir}/qt5/qml/org/hawaiios/misc
%dir %{_libdir}/qt5/qml/org/hawaiios/mixer
%dir %{_libdir}/qt5/qml/org/hawaiios/mpris2
%dir %{_libdir}/qt5/qml/org/hawaiios/notifications
%dir %{_datadir}/hawaii/themes/Wind/
%dir %{_datadir}/hawaii/themes/Wind/images
%{_sysconfdir}/xdg/menus/hawaii-applications.menu
%{_bindir}/hawaii
%{_bindir}/hawaii-session
%{_bindir}/starthawaii
%{_userunitdir}/hawaii.service
%{_userunitdir}/hawaii.target
%{_libdir}/qt5/plugins/platformthemes/HawaiiPlatformTheme.so
%{_libdir}/qt5/qml/Hawaii/Components/*.qml
%{_libdir}/qt5/qml/Hawaii/Components/libcomponentsplugin.so
%{_libdir}/qt5/qml/Hawaii/Components/plugins.qmltypes
%{_libdir}/qt5/qml/Hawaii/Components/qmldir
%{_libdir}/qt5/qml/Hawaii/Components/ListItems/*.qml
%{_libdir}/qt5/qml/Hawaii/Components/ListItems/qmldir
%{_libdir}/qt5/qml/Hawaii/Controls/*.qml
%{_libdir}/qt5/qml/Hawaii/Controls/libcontrolsplugin.so
%{_libdir}/qt5/qml/Hawaii/Controls/plugins.qmltypes
%{_libdir}/qt5/qml/Hawaii/Controls/qmldir
%{_libdir}/qt5/qml/Hawaii/Effects/*.qml
%{_libdir}/qt5/qml/Hawaii/Effects/qmldir
%{_libdir}/qt5/qml/Hawaii/Themes/*.qml
%{_libdir}/qt5/qml/Hawaii/Themes/libdeclarative_hawaiithemes.so
%{_libdir}/qt5/qml/Hawaii/Themes/qmldir
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Wind/*.qml
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Wind/images/*.png
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Wind/qmldir
%{_libdir}/qt5/qml/org/hawaiios/hardware/libhardwareplugin.so
%{_libdir}/qt5/qml/org/hawaiios/hardware/plugins.qmltypes
%{_libdir}/qt5/qml/org/hawaiios/hardware/qmldir
%{_libdir}/qt5/qml/org/hawaiios/launcher/liblauncherplugin.so
%{_libdir}/qt5/qml/org/hawaiios/launcher/qmldir
%{_libdir}/qt5/qml/org/hawaiios/launcher/plugins.qmltypes
%{_libdir}/qt5/qml/org/hawaiios/misc/libmiscplugin.so
%{_libdir}/qt5/qml/org/hawaiios/misc/qmldir
%{_libdir}/qt5/qml/org/hawaiios/mixer/libmixerplugin.so
%{_libdir}/qt5/qml/org/hawaiios/mixer/qmldir
%{_libdir}/qt5/qml/org/hawaiios/mpris2/libmpris2plugin.so
%{_libdir}/qt5/qml/org/hawaiios/mpris2/plugins.qmltypes
%{_libdir}/qt5/qml/org/hawaiios/mpris2/qmldir
%{_libdir}/qt5/qml/org/hawaiios/networkmanager/libnmplugin.so
%{_libdir}/qt5/qml/org/hawaiios/networkmanager/plugins.qmltypes
%{_libdir}/qt5/qml/org/hawaiios/networkmanager/qmldir
%{_libdir}/qt5/qml/org/hawaiios/notifications/libnotificationsplugin.so
%{_libdir}/qt5/qml/org/hawaiios/notifications/plugins.qmltypes
%{_libdir}/qt5/qml/org/hawaiios/notifications/qmldir
%{_datadir}/greenisland/shells/org.hawaiios.desktop
%{_datadir}/hawaii/themes/Wind/*.qml
%{_datadir}/hawaii/themes/Wind/*.ini
%{_datadir}/hawaii/themes/Wind/images/*.png
%{_datadir}/hawaii/themes/Wind/images/*.sci
%{_datadir}/wayland-sessions/hawaii.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/glib-2.0/schemas/org.hawaiios.desktop.*.xml
%{_datadir}/sddm/themes/hawaii
