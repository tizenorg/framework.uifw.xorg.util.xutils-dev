Name:	 xorg-x11-xutils-dev
Summary: X.Org build utilities
Version: 7.7
Release: 1
License: MIT/X11
Group:   Development/System
URL:     http://www.x.org
Source: %{name}-%{version}.tar.gz

# some file to be intalled can be ignored when rpm generates packages
%define _unpackaged_files_terminate_build 0

%define DEF_SUBDIRS util-macros

Provides: %{DEF_SUBDIRS}

%description
Description: %{summary}
 This package provides build utilties tha ship with the X Window System, including:
  - util-macros, autotools macros for X.Org

%prep
%setup -q

%build
# Build all xutils
{
    for xutil in %{DEF_SUBDIRS}; do
        pushd $xutil
		./autogen.sh
        %reconfigure
	    make
        popd
    done
}

%install
rm -rf %{buildroot}
# Install all xutils
{
   for xutil in %{DEF_SUBDIRS} ; do
      pushd $xutil
      make install DESTDIR=%{buildroot}
      popd
   done
}

%remove_docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/aclocal/*
%{_datadir}/pkgconfig/*

