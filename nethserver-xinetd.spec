Name: nethserver-xinetd
Version: 1.0.0
Release: 1%{?dist}
Summary: Conifigure xinetd
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: xinetd

%description
Install and configure an Adagios instance on NethServer

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING

%changelog
* Tue Aug 25 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- Initial nethserver-xinetd package, for Adagios - Feature #3229 [NethServer]

* Tue Jul 21 2015 Davide Principi <davide.principi@nethesis.it>
- Initial version
