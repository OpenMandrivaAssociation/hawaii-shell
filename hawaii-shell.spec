%define _disable_ld_no_undefined 1

Summary:	Hawaii shell
Name:		hawaii-shell
Version:	0.3.0
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
BuildRequires:	cmake(PolkitQt-1)
BuildRequires:  pkgconfig(Qt5Compositor) >= 5.4.0
BuildRequires:	pkgconfig(weston)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)

Requires:		weston
Requires:		dbus-x11
Requires:		hawaii-widget-styles >= 0.3.0
Requires:		greenisland >= 0.3.0
Requires:		fluid >= 0.3.0

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
%cmake
%make

%install
%makeinstall_std -C build

%files
