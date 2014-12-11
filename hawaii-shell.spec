%define Werror_cflags %nil
%define _disable_ld_no_undefined 1

Summary:	Hawaii shell
Name:		hawaii-shell
Version:	0.5.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	libhawaii-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	cmake(QtConfiguration)
BuildRequires:	cmake(QtAccountsService)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Runner)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:	pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5Compositor) >= 5.4.0
BuildRequires:	pkgconfig(Qt5WaylandClient)
BuildRequires:	pkgconfig(weston)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libsystemd-daemon)
#BuildRequires:  greenisland-devel

Requires:	weston
Requires:	dbus-x11
Requires:	hawaii-widget-styles >= 0.2.0
#Requires:	greenisland >= 0.3.0
Requires:	fluid >= 0.3.0
Requires:	%{_lib}qt5gui5-x11
Requires:	%{_lib}qt5waylandclient5
Requires:	%{_lib}qt5waylandcompositor5
Requires:	%{_lib}qt5dbus5
Requires:	plasma-workspace
Requires:	qt5-tools
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

%build
%cmake_qt5 -DENABLE_SYSTEMD:BOOL=ON -DQTWAYLAND_SCANNER_EXECUTABLE=%{_libdir}/qt5/bin/qtwaylandscanner -DCMAKE_BUILD_TYPE=RelWithDebInfo
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
%dir %{_datadir}/plasma/look-and-feel/org.hawaii.lookandfeel.desktop
%dir %{_datadir}/plasma/look-and-feel/org.hawaii.lookandfeel.desktop/contents
%dir %{_datadir}/plasma/plasmoids/org.hawaii.appchooser
%dir %{_datadir}/plasma/plasmoids/org.hawaii.appchooser/contents
%dir %{_datadir}/plasma/plasmoids/org.hawaii.notifications
%dir %{_datadir}/plasma/plasmoids/org.hawaii.notifications/contents
%dir %{_datadir}/plasma/shells/org.hawaii.shells.desktop
%dir %{_datadir}/plasma/shells/org.hawaii.shells.desktop/contents
%dir %{_datadir}/plasma/wallpapers/org.hawaii.wallpapers.gradient
%dir %{_datadir}/plasma/wallpapers/org.hawaii.wallpapers.gradient/contents
%dir %{_datadir}/plasma/wallpapers/org.hawaii.wallpapers.solid
%dir %{_datadir}/plasma/wallpapers/org.hawaii.wallpapers.solid/contents
%dir %{_libdir}/qml/org/hawaii
%dir %{_libdir}/qml/org/hawaii/appchooser
%dir %{_libdir}/qml/org/hawaii/appchooser/private
%dir %{_libdir}/qml/org/hawaii/private
%dir %{_libdir}/qml/org/hawaii/private/notifications
%{_prefix}/etc/xdg/autostart/hawaii-shell-desktop.desktop
%{_prefix}/etc/xdg/menus/hawaii-applications.menu
%{_prefix}/etc/xdg/plasma-workspace/env/hawaii.sh
%{_bindir}/ksetcursortheme
%{_bindir}/ksetdefaultsettings
%{_prefix}/lib/systemd/user/hawaii-*.service
%{_prefix}/lib/systemd/user/hawaii.target
%{_prefix}/lib/systemd/user/baloo_file.service
%{_prefix}/lib/systemd/user/kdeinit5.service
%{_prefix}/lib/systemd/user/krunner.service
%{_prefix}/lib/systemd/user/ksmserver5.service
%{_prefix}/lib/systemd/user/kwin_x11.service
%{_prefix}/lib/systemd/user/plasma-desktop-shell.service
%{_prefix}/lib/systemd/user/plasma5.target
%{_libdir}/qml/org/hawaii/appchooser/private/*
%{_libdir}/qml/org/hawaii/private/notifications/*
%{_datadir}/kservices5/plasma-*org.hawaii.*.desktop
%{_datadir}/desktop-directories/hawaii-*.directory
%{_datadir}/plasma/look-and-feel/org.hawaii.lookandfeel.desktop/contents/*
%{_datadir}/plasma/look-and-feel/org.hawaii.lookandfeel.desktop/metadata.desktop
%{_datadir}/plasma/plasmoids/org.hawaii.appchooser/metadata.desktop
%{_datadir}/plasma/plasmoids/org.hawaii.appchooser/contents/*
%{_datadir}/plasma/plasmoids/org.hawaii.notifications/metadata.desktop
%{_datadir}/plasma/plasmoids/org.hawaii.notifications/contents/*
%{_datadir}/plasma/shells/org.hawaii.shells.desktop/metadata.desktop
%{_datadir}/plasma/shells/org.hawaii.shells.desktop/contents/*
%{_datadir}/plasma/wallpapers/org.hawaii.wallpapers.*/metadata.desktop
%{_datadir}/plasma/wallpapers/org.hawaii.wallpapers.*/contents/*
%{_datadir}/wayland-sessions/hawaii.desktop
%{_datadir}/xsessions/hawaii.desktop

%files sddm-theme
%dir %{_datadir}/sddm/themes/mauiproject
%dir %{_datadir}/sddm/themes/mauiproject/components
%{_datadir}/sddm/themes/mauiproject/README
%{_datadir}/sddm/themes/mauiproject/*.qml
%{_datadir}/sddm/themes/mauiproject/*.png
%{_datadir}/sddm/themes/mauiproject/*.conf
%{_datadir}/sddm/themes/mauiproject/*.desktop
%{_datadir}/sddm/themes/mauiproject/components/*
