Summary:	Uncompile an rgb color
Name:		rgb
Version:	1.0.6
Release:	7
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org/releases/individual/app/
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)

%description
The showrgb program reads an rgb color-name database compiled for use with
the dbm database routines and converts it back to source form.

%prep
%setup -q

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/showrgb
%{_datadir}/X11/rgb.txt
%{_mandir}/man1/showrgb.*

