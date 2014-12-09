%define Werror_cflags %nil
%define _disable_ld_no_undefined 1

Summary:	Hawaii shell
Name:		hawaii-shell
Version:	0.5.0
Release:	1
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
Requires(post,postun,preun):	rpm-helper

%track
prog %{name} = {
    url = http://downloads.sourceforge.net/project/mauios/hawaii/
    regex = "%{name}-(__VER__)\.tar\.gz"
    version = %{version}
}

%description
Hawaii shell.

%prep
%setup -q

%build
%cmake_qt5 -DENABLE_SYSTEMD:BOOL=ON -DQTWAYLAND_SCANNER_EXECUTABLE=%{_libdir}/qt5/bin/qtwaylandscanner -DCMAKE_BUILD_TYPE=RelWithDebInfo
%make

%install
%makeinstall_std -C build

%post
%systemd_post hawaii-notifications-daemon hawaii-polkit-agent hawaii-shell

%postun
%systemd_postun hawaii-notifications-daemon hawaii-polkit-agent hawaii-shell

%preun
%systemd_preun

%files
%dir %{_libdir}/hawaii/qml/Hawaii/Shell
%dir %{_datadir}/hawaii/backgrounds/org.hawaii.backgrounds.gradient
%dir %{_datadir}/hawaii/backgrounds/org.hawaii.backgrounds.solid
%dir %{_datadir}/hawaii/backgrounds/org.hawaii.backgrounds.wallpaper
%dir %{_datadir}/hawaii/containments/org.hawaii.containments.desktop
%dir %{_datadir}/hawaii/containments/org.hawaii.containments.panel
%dir %{_datadir}/hawaii/elements/org.hawaii.elements.appchooser
%dir %{_datadir}/hawaii/elements/org.hawaii.elements.indicators
%dir %{_datadir}/hawaii/elements/org.hawaii.elements.spacer
%dir %{_datadir}/hawaii/shells/org.hawaii.shells.desktop
%dir %{_datadir}/hawaii/shells/org.hawaii.shells.tablet
%dir %{_datadir}/hawaii/elements/org.hawaii.elements.launcher
%dir %{_datadir}/hawaii/styles/Aluminium
%dir %{_datadir}/hawaii/styles/Flat
%{_bindir}/hawaii*
%{_prefix}/lib/systemd/user/hawaii-*.service
%{_prefix}/lib/systemd/user/hawaii.target
%{_libdir}/hawaii/plugins/dataproviders/libhawaiidatetime.so
%{_libdir}/hawaii/plugins/dataproviders/libhawaiimixer.so
%{_libdir}/hawaii/plugins/platformthemes/hawaii.so
%{_libdir}/hawaii/qml/Hawaii/Shell/*
%{_libdir}/weston/hawaii-desktop.so
%{_libexecdir}/hawaii-screensaver
%{_libexecdir}/hawaii-shell-client
%{_libexecdir}/starthawaii
%{_datadir}/hawaii/backgrounds/org.hawaii.backgrounds.gradient/*
%{_datadir}/hawaii/backgrounds/org.hawaii.backgrounds.solid/*
%{_datadir}/hawaii/backgrounds/org.hawaii.backgrounds.wallpaper/*
%{_datadir}/hawaii/containments/org.hawaii.containments.desktop/*
%{_datadir}/hawaii/containments/org.hawaii.containments.panel/*
%{_datadir}/hawaii/elements/org.hawaii.elements.appchooser/*
%{_datadir}/hawaii/elements/org.hawaii.elements.indicators/*
%{_datadir}/hawaii/elements/org.hawaii.elements.launcher/*
%{_datadir}/hawaii/elements/org.hawaii.elements.spacer/*
%{_datadir}/hawaii/shells/org.hawaii.shells.desktop/*
%{_datadir}/hawaii/shells/org.hawaii.shells.tablet/*
%{_datadir}/hawaii/styles/Aluminium/*
%{_datadir}/hawaii/styles/Flat/*
%{_datadir}/wayland-sessions/hawaii.desktop
