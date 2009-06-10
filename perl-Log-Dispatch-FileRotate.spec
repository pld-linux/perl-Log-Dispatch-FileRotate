#
# Conditional build:
%bcond_with	tests	# perform "make test": very long
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Log
%define		pnam	Dispatch-FileRotate
Summary:	Log::Dispatch::FileRotate - log to files that archive/rotate themselves
Summary(pl.UTF-8):	Log::Dispatch::FileRotate - logowanie do plików, które są archiwizowane lub podlegają rotacji
Name:		perl-Log-Dispatch-FileRotate
Version:	1.19
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Log/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8fabfe387bb070580f7c97c18853ae25
URL:		http://search.cpan.org/dist/Log-Dispatch-FileRotate/
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-Log-Dispatch
%{?with_tests:BuildRequires:	perl-Log-Log4perl}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a simple object for logging to files under the
Log::Dispatch::* system, and automatically rotating them according to
different constraints. This is basically a Log::Dispatch::File wrapper
with additions.

%description -l pl.UTF-8
Niniejszy moduł udostępnia prosty obiekt obsługujący logowanie do
plików w systemie Log::Dispatch::* i dokonujący automatycznej rotacji
tych plików na podstawie różnych reguł. W zasadzie jest to nakładka na
Log::Dispatch::File zawierająca dodatki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	< /dev/null
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
%doc Changes
%{perl_vendorlib}/Log/Dispatch/*
%{_mandir}/man3/*
