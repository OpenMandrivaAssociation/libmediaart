%define	api	1.0
%define major	0
%define	libname	%mklibname	mediaart %{api} %{major}
%define	girname	%mklibname	mediaart-gir %{api} 
%define	devname	%mklibname	mediaart	-d

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Library for managing media art caches
Name:		libmediaart
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.35.1
BuildRequires:	pkgconfig(gio-2.0) >= 2.35.1
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.35.1

%description
Library tasked with managing, extracting and handling media art caches.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Library tasked with managing, extracting and handling media art caches.


This package contains the shared library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
This package contains files needed for development with %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc
%make

%install
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/MediaArt-%{api}.typelib

%files -n %{devname}
%dir %{_includedir}/%{name}-%{api}
%dir %{_includedir}/%{name}-%{api}/%{name}
%{_includedir}/%{name}-%{api}/%{name}/*
#%doc %{_datadir}/doc/%{name}/*
%{_datadir}/gtk-doc/html/%{name}/*
%{_datadir}/gir-1.0/MediaArt-%{api}.gir
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_datadir}/vala/vapi/%{name}-%{api}.vapi


%changelog
* Tue Apr 01 2014 ovitters <ovitters> 0.4.0-1.mga5
+ Revision: 611147
- new version 0.4.0

* Fri Mar 14 2014 dams <dams> 0.3.0-1.mga5
+ Revision: 603447
- new version 0.3.0

* Wed Feb 19 2014 ovitters <ovitters> 0.2.0-1.mga5
+ Revision: 594700
- imported package libmediaart

