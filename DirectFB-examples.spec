Summary:	DirectFB example programs (demos)
Summary(pl.UTF-8):   Programy przykładowe (demonstracyjne) do DirectFB
Name:		DirectFB-examples
Version:	0.9.25
Release:	1
License:	MIT
Group:		Applications/Graphics
Source0:	http://www.directfb.org/download/DirectFB-extra/%{name}-%{version}.tar.gz
# Source0-md5:	835e850fddba8d8214d39ddd0646c3e8
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= 1:%{version}
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectFB example programs (demos). See README for description of
each program.

%description -l pl.UTF-8
Programy przykładowe (demonstracyjne) do DirectFB. Opis poszczególnych
programów znajduje się w pliku README.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/directfb-examples
