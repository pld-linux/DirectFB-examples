Summary:	DirectFB example programs (demos)
Summary(pl):	Programy przyk³adowe (demonstracyjne) do DirectFB
Name:		DirectFB-examples
Version:	0.9.18
Release:	2
License:	MIT
Group:		Applications/Graphics
Source0:	http://www.directfb.org/download/DirectFB/%{name}-%{version}.tar.gz
# Source0-md5:	73489f632fb8755c6498785540c15561
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= %{version}
BuildRequires:	autoconf
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectFB example programs (demos). See README for description of
each program.

%description -l pl
Programy przyk³adowe (demonstracyjne) do DirectFB. Opis poszczególnych
programów znajduje siê w pliku README.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
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
