Name: rgb
Version: 1.0.3
Release: %mkrel 4
Summary: Uncompile an rgb color
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The showrgb program reads an rgb color-name database compiled for use with
the dbm database routines and converts it back to source form.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/showrgb
%{_datadir}/X11/rgb.txt
%{_mandir}/man1/showrgb.*


