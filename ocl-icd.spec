Summary:	OpenCL generic Installable Client Driver support
Summary(pl.UTF-8):	Ogólna obsługa sterowników klienckich (ICD) dla OpenCL
Name:		ocl-icd
Version:	2.2.14
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/OCL-dev/ocl-icd/releases
Source0:	https://github.com/OCL-dev/ocl-icd/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ef0d426bccf2a795013d3c5794550e5e
URL:		https://github.com/OCL-dev/ocl-icd
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.9
BuildRequires:	khronos-OpenCL-headers >= 2.2
BuildRequires:	libtool
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	xmlto
# this will be provided by the actual driver, I guess
#Provides:	OpenCL = 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package aims at creating an Open Source alternative to vendor
specific OpenCL ICD loaders.

%description -l pl.UTF-8
Ten pakiet to próba stworzenia mającej otwarte źródła alternatywy dla
specyficznych dla producenta bibliotek wczytujących ICD OpenCL.

%package devel
Summary:	Header file for building OpenCL ICD
Summary(pl.UTF-8):	Plik nagłówkowy do budowania OpenCL ICD
Group:		Development/Libraries
Requires:	khronos-OpenCL-headers >= 2.2

%description devel
Header file for building OpenCL installable client drivers (ICD).

%description devel -l pl.UTF-8
Plik nagłówkowy do budowania instalowalnych sterowników klienta
OpenCL.

%package libOpenCL
Summary:	OpenCL generic Installable Client Driver support
Summary(pl.UTF-8):	Ogólna obsługa sterowników klienckich (ICD) dla OpenCL
Group:		Libraries
Suggests:	ocl-icd-driver
Obsoletes:	Mesa-libOpenCL

%description libOpenCL
This package aims at creating an Open Source alternative to vendor
specific OpenCL ICD loaders.

%description libOpenCL -l pl.UTF-8
Ten pakiet to próba stworzenia mającej otwarte źródła alternatywy dla
specyficznych dla producenta bibliotek wczytujących ICD OpenCL.

%package libOpenCL-devel
Summary:	Development files for OpenCL library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki OpenCL
Group:		Development/Libraries
Requires:	%{name}-libOpenCL = %{version}-%{release}
Requires:	khronos-OpenCL-headers >= 2.2
Provides:	OpenCL-devel = 2.2
Obsoletes:	Mesa-libOpenCL-devel

%description libOpenCL-devel
Development files for OpenCL library provided by the ocl-icd loader.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki OpenCL dostarczanej przez ocl-icd.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgexampledir=%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# packaged in man format
%{__rm} $RPM_BUILD_ROOT%{_docdir}/ocl-icd/html/libOpenCL.html

%clean
rm -rf $RPM_BUILD_ROOT

%post	libOpenCL -p /sbin/ldconfig
%postun	libOpenCL -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/ocl_icd.h
%{_pkgconfigdir}/ocl-icd.pc
%{_examplesdir}/%{name}-%{version}

%files libOpenCL
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_libdir}/libOpenCL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenCL.so.1
%{_mandir}/man7/libOpenCL.7*
%{_mandir}/man7/libOpenCL.so.7*

%files libOpenCL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenCL.so
%{_pkgconfigdir}/OpenCL.pc
