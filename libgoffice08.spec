#
# Conditional build:
%bcond_without	gnome	# disable all GNOME components
#
%define		orgname	goffice
#
Summary:	Glib/Gtk+ set of document centric objects and utilities
Summary(pl.UTF-8):	Zestaw zorientowanych dokumentowo obiektów i narzędzi Glib/Gtk+
Name:		libgoffice08
Version:	0.8.17
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goffice/0.8/%{orgname}-%{version}.tar.xz
# Source0-md5:	e2bc2d2f51220d6883f0797d74c385b8
Patch0:		%{name}-pcre.patch
URL:		http://www.gtk.org/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.2.4
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libart_lgpl-devel >= 2.3.11
BuildRequires:	libglade2-devel >= 1:2.6.2
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.20.0}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pcretest
BuildRequires:	pkgconfig
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOffice - a Glib/Gtk+ set of document centric objects and utilities.

%description -l pl.UTF-8
GOffice - Zestaw zorientowanych dokumentowo obiektów i narzędzi
Glib/Gtk+.

%package devel
Summary:	Header files for GOffice library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GOffice
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	libart_lgpl-devel >= 2.3.11
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libxml2-devel >= 1:2.6.26

%description devel
This is the package containing the header files for GOffice.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe GOffice.

%package static
Summary:	Static GOffice library
Summary(pl.UTF-8):	Statyczna biblioteka GOffice
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GOffice library.

%description static -l pl.UTF-8
Statyczna biblioteka GOffice.

%package apidocs
Summary:	GOffice library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki GOffice
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GOffice library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GOffice.

%prep
%setup -qn %{orgname}-%{version}
%patch -P0 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	%{?with_gnome:--with-gnome} \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/goffice/%{version}/plugins/*/*.{a,la} \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{orgname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{orgname}-%{version}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgoffice-0.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoffice-0.8.so.8
%dir %{_libdir}/goffice
%dir %{_libdir}/goffice/%{version}
%dir %{_libdir}/goffice/%{version}/plugins
%dir %{_libdir}/goffice/%{version}/plugins/*
%attr(755,root,root) %{_libdir}/goffice/%{version}/plugins/*/*.so
%{_libdir}/goffice/%{version}/plugins/*/*.xml
%{_libdir}/goffice/%{version}/plugins/*/*.ui
%{_datadir}/goffice
%{_pixmapsdir}/goffice

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoffice-0.8.so
%{_includedir}/libgoffice-0.8
%{_pkgconfigdir}/libgoffice-0.8.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgoffice-0.8.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/goffice-0.8
