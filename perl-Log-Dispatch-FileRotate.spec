#
# Conditional build:
# _with_tests - perform "make test": very long
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Dispatch-FileRotate
Summary:	Log::Dispatch::FileRotate - log to files that archive/rotate themselves
Summary(pl):	Log::Dispatch::FileRotate - logowanie do plików, które s± archiwizowane lub podlegaj± rotacji
Name:		perl-Log-Dispatch-FileRotate
Version:	1.09
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e6f5591cf114d59b5ff930b1f99e571
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-Log-Dispatch
%{?_with_tests:BuildRequires:	perl-Log-Log4perl}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a simple object for logging to files under the
Log::Dispatch::* system, and automatically rotating them according to
different constraints. This is basically a Log::Dispatch::File wrapper
with additions.

%description -l pl
Niniejszy modu³ udostêpnia prosty obiekt obs³uguj±cy logowanie do
plików w systemie Log::Dispatch::* i dokonuj±cy automatycznej rotacji
tych plików na podstawie ró¿nych regu³. W zasadzie jest to nak³adka na
Log::Dispatch::File zawieraj±ca dodatki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	< /dev/null
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Log/Dispatch/*
%{_mandir}/man3/*
