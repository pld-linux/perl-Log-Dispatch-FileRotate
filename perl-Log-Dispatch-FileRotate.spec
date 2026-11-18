#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Log
%define		pnam	Dispatch-FileRotate
Summary:	Log::Dispatch::FileRotate - log to files that archive/rotate themselves
Summary(pl.UTF-8):	Log::Dispatch::FileRotate - logowanie do plików, które są archiwizowane lub podlegają rotacji
Name:		perl-Log-Dispatch-FileRotate
Version:	1.38
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Log/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eed7814b9d291d5f7267d578e099c102
URL:		http://search.cpan.org/dist/Log-Dispatch-FileRotate/
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-Log-Dispatch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Path-Tiny >= 0.018
BuildRequires:	perl-Test-Pod >= 1.41
BuildRequires:	perl-Test-Warn
%endif
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
%{perl_vendorlib}/Log/Dispatch/FileRotate.pm
%{perl_vendorlib}/Log/Dispatch/FileRotate
%{_mandir}/man3/Log::Dispatch::FileRotate*.3pm*
