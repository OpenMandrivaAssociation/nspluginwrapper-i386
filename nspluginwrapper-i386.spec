###
###
### THIS PACKAGE IS AUTOMATICALLY GENERATED, DO NOT EDIT
###
###
Summary: A compatibility layer for Netscape 4 plugins
Name: nspluginwrapper-i386
Version: 0.9.90.1
Release: 2mdv2007.0
Source: nspluginwrapper-i386-0.9.90.1.tar.bz2
License: GPL
Group: Networking/WWW
%ifnarch %ix86 x86_64 ia64
AutoReq: off
%endif
BuildRoot: %_tmppath/%name-%version-%release-buildroot
URL: http://www.gibix.net/projects/nspluginwrapper/

%description
nspluginwrapper makes it possible to use Netscape 4 compatible plugins
compiled for i386 into Mozilla for another architecture, e.g. x86_64.

This package consists in:
  * npviewer: the plugin viewer
  * npwrapper.so: the browser-side plugin
  * nspluginwrapper: a tool to manage plugins installation and update

This package provides the npviewer program for i386.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
tar cf - . | tar xf - -C $RPM_BUILD_ROOT/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
/usr/lib/nspluginwrapper/i386/npviewer.bin

