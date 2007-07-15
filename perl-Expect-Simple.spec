#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Expect
%define	pnam	Simple
Summary:	Expect::Simple - wrapper around the Expect module
Summary(pl.UTF-8):	Expect::Simple - wrapper dla modułu Expect
Name:		perl-Expect-Simple
Version:	0.02
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Expect/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	23c72fa4461f07522eb8c8511bad5d43
URL:		http://search.cpan.org/dist/Expect-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Expect
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expect::Simple is a wrapper around the Expect module which
should suffice for simple applications. It hides most of the
Expect machinery; the Expect object is available for tweaking if
need be.

%description -l pl.UTF-8
Expect::Simple to wrapper dla modułu Expect. Powinien wystarczyć dla
prostych aplikacji. Ukrywa większość maszynerii Expecta; obiekt
Expect jest dostępny w razie potrzeby.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Expect/*.pm
%{_mandir}/man3/*
