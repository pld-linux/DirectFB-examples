Summary:	DirectFB example programs (demos)
Summary(pl):	Programy przyk�adowe (demonstracyjne) do DirectFB
Name:		DirectFB-examples
Version:	0.9.17
Release:	1
License:	MIT
Group:		Applications/Graphics
Source0:	http://www.directfb.org/download/DirectFB/%{name}-%{version}.tar.gz
# Source0-md5:	f6b96311ee882a4ebd7c0cf10d373709
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= %{version}
BuildRequires:	autoconf
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectFB example programs (demos). See README for description of
each program.

%description -l pl
Programy przyk�adowe (demonstracyjne) do DirectFB. Opis poszczeg�lnych
program�w znajduje si� w pliku README.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/directfb-examples
