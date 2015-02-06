###
###
### THIS PACKAGE IS AUTOMATICALLY GENERATED, DO NOT EDIT
###
###
Summary: A compatibility layer for Netscape 4 plugins
Name: nspluginwrapper-i386
Version: 0.9.90.1
Release: 7
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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9.90.1-6mdv2010.0
+ Revision: 430185
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.90.1-5mdv2009.0
+ Revision: 241096
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.9.90.1-3mdv2008.0
+ Revision: 69369
- use %%mkrel


* Wed Jun 07 2006 Gwenole Beauchesne <gb.public@free.fr> 0.9.90.1-2mdk
- ship with mkruntime
- enable -debug packages
- add possibility to build biarch packages at once
- fix repackage.sh to stop generating deps on non x86 platforms

* Tue Jun 06 2006 Gwenole Beauchesne <gb.public@free.fr> 0.9.90.1-1mdk
- first Mandriva Linux release
- don't use QEMU on IA-64 platforms

