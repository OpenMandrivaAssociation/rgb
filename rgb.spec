Summary:	Uncompile an rgb color
Name:		rgb
Version:	1.1.0
Release:	8
Group:		Development/X11
License:	MIT
Url:		https://xorg.freedesktop.org/releases/individual/app/
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)

%description
The showrgb program reads an rgb color-name database compiled for use with
the dbm database routines and converts it back to source form.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/showrgb
%{_datadir}/X11/rgb.txt
%doc %{_mandir}/man1/showrgb.*

