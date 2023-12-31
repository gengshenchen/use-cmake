# Restore old style debuginfo creation for rpm >= 4.14.
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# -*- rpm-spec -*-
BuildRoot:      %_topdir/demo6-installer-3.8.6-Linux
Summary:        demo6 built using CMake
Name:           demo6-installer
Version:        3.8.6
Release:        1
License:        MIT
Group:          unknown
Vendor:         karl group


Requires: uuid-devel












Prefix: /opt/demo6





%define _rpmdir %_topdir/RPMS
%define _srcrpmdir %_topdir/SRPMS
%define _rpmfilename demo6-installer-3.8.6-Linux.rpm
%define _unpackaged_files_terminate_build 0





%description
DESCRIPTION
===========

This is an installer created using CPack (https://cmake.org). No additional installation instructions provided.



# This is a shortcutted spec file generated by CMake RPM generator
# we skip _install step because CPack does that for us.
# We do only save CPack installed tree in _prepr
# and then restore it in build.
%prep
mv $RPM_BUILD_ROOT %_topdir/tmpBBroot

%install
if [ -e $RPM_BUILD_ROOT ];
then
  rm -rf $RPM_BUILD_ROOT
fi
mv %_topdir/tmpBBroot $RPM_BUILD_ROOT



%clean








%files
%defattr(-,root,root,-)
%dir "/opt/demo6"
%dir "/opt/demo6/bin"
"/opt/demo6/bin/demo"
%dir "/opt/demo6/include"
"/opt/demo6/include/config.h"
"/opt/demo6/include/math.h"
%dir "/opt/demo6/lib"
"/opt/demo6/lib/libmathkarl.so"




%changelog
* Sun Jul 4 2010 Eric Noulard <eric.noulard@gmail.com> - 3.8.6-1
  Generated by CPack RPM (no Changelog file were provided)


