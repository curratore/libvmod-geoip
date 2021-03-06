Summary: geoip VMOD for Varnish
Name: vmod-geoip
Version: 0.1
Release: 1%{?dist}
License: MIT
Group: System Environment/Daemons
Source0: libvmod-geoip.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish >= 4.0, GeoIP, geoip-geolite
BuildRequires: make, python-docutils, GeoIP-devel

%description
geoip VMOD

%prep
%setup -n libvmod-geoip

%build
./configure --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
make
make check

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Tue Nov 14 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20121114
- Initial version.
