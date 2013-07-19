Summary:	DirectFB example programs (demos)
Summary(pl.UTF-8):	Programy przykładowe (demonstracyjne) do DirectFB
Name:		DirectFB-examples
Version:	1.7.0
Release:	1
License:	MIT
Group:		Applications/Graphics
Source0:	http://www.directfb.org/downloads/Extras/%{name}-%{version}.tar.gz
# Source0-md5:	8b60c867af295481c32a8c7fc5802307
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= 1:1.6.0
BuildRequires:	automake
BuildRequires:	pkgconfig
Requires:	DirectFB >= 1:1.6.0
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
%attr(755,root,root) %{_bindir}/df_*
%attr(755,root,root) %{_bindir}/pss
%attr(755,root,root) %{_bindir}/spacedream
%{_datadir}/directfb-examples
