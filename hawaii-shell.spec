%define Werror_cflags %nil
%define _disable_ld_no_undefined 1

Summary:	Hawaii shell
Name:		hawaii-shell
Version:	0.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Patch0:		0002-Specify-protocol-versions.patch
Patch1:		0003-server-Update-to-Weston-1.6-API.patch
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	libhawaii-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	cmake(QtConfiguration)
BuildRequires:	cmake(QtAccountsService)
BuildRequires:	pkgconfig(polkit-qt5-1)
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
%patch0 -p1
%patch1 -p1

%build
export CC=gcc
export CXX=g++
%cmake
%make

%install
%makeinstall_std -C build

%files
