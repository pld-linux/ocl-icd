# TODO: separate OpenCL and ocl-icd devel parts?
Summary:	OpenCL generic Installable Client Driver support
Summary(pl.UTF-8):	Ogólna obsługa sterowników klienckich (ICD) dla OpenCL
Name:		ocl-icd
Version:	2.0.4
Release:	0.1
License:	BSD
Group:		Libraries
#Source0Download: https://forge.imag.fr/frs/?group_id=395
Source0:	https://forge.imag.fr/frs/download.php/451/%{name}-%{version}.tar.gz
# Source0-md5:	98fb9c2c4df8f9416fb59acf18368702
URL:		https://forge.imag.fr/projects/ocl-icd/
BuildRequires:	OpenCL-devel >= 1.2
BuildRequires:	asciidoc
BuildRequires:	ruby
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package aims at creating an Open Source alternative to vendor
specific OpenCL ICD loaders.

%description -l pl.UTF-8
Ten pakiet to próba stworzenia mającej otwarte źródła alternatywy
dla specyficznych dla producenta bibliotek wczytujących ICD OpenCL.

%package devel
Summary:	Header file for OpenCL-ICD library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki OpenCL-ICD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for OpenCL-ICD library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki OpenCL-ICD.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_libdir}/libOpenCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenCL.so.1
%{_mandir}/man7/libOpenCL.7*
%{_mandir}/man7/libOpenCL.so.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenCL.so
%{_includedir}/ocl_icd.h
%{_pkgconfigdir}/OpenCL.pc
%{_pkgconfigdir}/ocl-icd.pc
