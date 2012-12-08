# EDIT IN SVN NOT IN SOURCE PACKAGE (NO PATCH ALLOWED).

Summary:	EDID retrieval and parsing tools
Name:		monitor-edid
Version:	3.0
Release:	7
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		System/Configuration/Other
Url:		http://wiki.mandriva.com/en/Tools/monitor-edid
%ifarch %ix86 x86_64
BuildRequires:	libx86-devel
%endif
ExcludeArch:	%arm %mips

%description
This package provides tools for EDID retrieval, EDID parsing and
other methods of monitor probing.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README NEWS
%{_bindir}/*
%{_sbindir}/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0-3mdv2011.0
+ Revision: 666477
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0-2mdv2011.0
+ Revision: 606656
- rebuild

* Sun Jan 03 2010 Anssi Hannula <anssi@mandriva.org> 3.0-1mdv2010.1
+ Revision: 486009
- new version 3.0
- update description and summary, adapt buildrequires
- monitor-get-edid-using-vbe:
  o remove all x86emu and vga softbootloader code, and always use the
    LRMI interface which was previously the backup one on 32-bit x86;
    libx86 is now used instead of liblrmi, allowing the use of LRMI
    interface on non-x86 hosts as well (fixes Mandriva bug #53866, which
    was caused by a bug in the removed code)
  o fix the retrieval of VBE vendor strings when using the LRMI interface
  o retrieve up to 4 EDID extension blocks
  o add --skip-vbe-check for skipping call for VBE info; useful if
    calling the program multiple times for different ports
  o on failure, return exit status 2 if successful VBE calls were made
  o never retry in console mode if the card reports that the port does
    not support DDC (usually this means that the port has no display
    devices connected)
  o add basic 15 sec timeout (exit status 3), with --no-timeout for
    disabling it
- monitor-parse-edid:
  o print EDID version and the number of EDID extension blocks
  o accept EDID data with multiple extension blocks
  o add support for Detailed Timing Descriptors in CEA EDID Timing
    Extension
  o add support for Short Video Descriptor formats 1-64 (as defined by
    EIA/CEA-861) in Video Data Blocks of CEA EDID Timing Extension
  o set Interlace flag for ModeLines created for interlaced Detailed
    Timings (and note it in the ModeLine comment)
  o correctly parse some interlaced video timings if the Detailed Timing
    Descriptor specifies field vertical parameters instead of the frame
    parameters (at least Fujitsu-Siemens Myrica VQ32-1T testcase)
  o ignore 1x1 modes (at least Nokia Valuegraph 447w testcase)
  o add support for standard timing descriptors in monitor descriptors
  o add comment "Monitor preferred modeline" only for the modeline the
    monitor reports as preferred, and add "Monitor supported modeline"
    comment for the other modelines
  o allow null manufacturer name, instead check that EDID version is 1.x
    or 2.x (see Mandriva bug #28857)
  o output an error message when --monitorsdb fails (see Mandriva bugs
    #28857 and #40609)
- monitor-edid, monitor-get-edid:
  o do not get duplicate EDIDs if the same EDID is available via
    multiple methods
  o allow retrieval of multiple EDIDs via VBE
  o get VBE info only once even when probing multiple ports
- monitor-edid:
  o add --first support for stopping processing after one EDID has been
    found
- monitor-probe-using-X:
  o accept EDID data that contains extension blocks
- monitor-probe:
  o do not probe using X if DMI probe was successful

* Sun Oct 18 2009 Anssi Hannula <anssi@mandriva.org> 2.5-1mdv2010.0
+ Revision: 458114
- 2.5
- monitor-probe-using-X:
  o disable glx module to speed up X startup, especially if a proprietary
    glx module is in use (fixes a timeout I observed on one system)
  o use -sharevts for X server when plymouth is active, as VT switching
    does not work at that point (fixes Mandriva bug #53736)

* Thu Oct 01 2009 Anssi Hannula <anssi@mandriva.org> 2.4-1mdv2010.0
+ Revision: 452160
- 2.4
- monitor-parse-edid:
  o ignore the Manufacturer Specified Range Timing descriptor if the
    first detailed timing descriptor appears to violate it (this probably
    means that the descriptor is actually something else or in a
    different format; this fixes Lenovo W500 detection, reported by Udo
    Rader)

* Sun Sep 27 2009 Olivier Blin <oblin@mandriva.com> 2.3-2mdv2010.0
+ Revision: 450159
- do not build on arm & mips (from Arnaud Patard)

* Sun Sep 06 2009 Anssi Hannula <anssi@mandriva.org> 2.3-1mdv2010.0
+ Revision: 432076
- 2.3
- monitor-get-edid-using-vbe:
  o update x86emu from xserver git (fixes issues at least with newish
    NVIDIA cards)
  o check if the port supports DDC before trying to read EDID data (this
    should prevent problems when probing nonexistent ports on old cards)
- monitor-edid, monitor-get-edid:
  o probe ports 0-2 by default instead of just 0-1 (many NVIDIA cards
    seem to be using port 2 and the changes in monitor-get-edid-using-vbe
    should make it safe for old problematic NVIDIA cards as well)

* Sat Aug 15 2009 Anssi Hannula <anssi@mandriva.org> 2.2-1mdv2010.0
+ Revision: 416701
- 2.2:
- monitor-edid, monitor-get-edid:
  o support getting EDID from kernel DRM when kernel mode-setting is
    enabled
- monitor-probe-using-X:
  o use resolution from LVDS initial mode when X reports that it is exact,
    making it work with nouveau driver
- include NEWS

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.1-2mdv2009.1
+ Revision: 351610
- rebuild

* Mon Jul 07 2008 Pixel <pixel@mandriva.com> 2.1-1mdv2009.0
+ Revision: 232566
- release 2.1:
- monitor-parse-edid:
  o compute and display the "dpi" of the preferred modelines
  o handle parsing of EDIDs found in "xrandr --prop" or Xorg.log
- monitor-get-edid-using-vbe:
  o fix checking the current vt
  o instead of checking vt >= 7 to know if X is running,
    check wether $DISPLAY is set
- license is now GPLv3+
- remove internal lrmi.c, build with external liblrmi instead
  (Remi Collet and Ville Skytta)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.16-2mdv2009.0
+ Revision: 223301
- rebuild

* Mon Mar 10 2008 Pixel <pixel@mandriva.com> 1.16-1mdv2008.1
+ Revision: 183268
- update URL
- 1.16:
- do not install monitor-get-edid-using-vbe on archs where VBE is not
  available (Remi Collet)

* Wed Jan 23 2008 Pixel <pixel@mandriva.com> 1.15-1mdv2008.1
+ Revision: 157016
- 1.15:
- monitor-probe:
  o probe "using DMI" before "using X"
- monitor-probe-using-X:
  o in last resort, get Intel BIOS mode when "BIOS panel mode is bigger than
    probed programmed mode"

* Thu Jan 10 2008 Pixel <pixel@mandriva.com> 1.14-1mdv2008.1
+ Revision: 147502
- 1.14:
- monitor-edid, monitor-get-edid:
  o call monitor-get-edid-using-vbe with a range of ports, it stops on first
    success (by default it tries port 0 then port 1)

* Tue Jan 08 2008 Pixel <pixel@mandriva.com> 1.13-1mdv2008.1
+ Revision: 146846
- 1.13:
- monitor-get-edid:
  o skip /proc/acpi/video/**/EDID files which can't be valid (#34417)
  o minimal support for getting EDID from different DDC port
    (experimental, need testing before using it in monitor-edid)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 26 2007 Pixel <pixel@mandriva.com> 1.12-1mdv2008.0
+ Revision: 93044
- use make install
- 1.12:
- monitor-probe-using-X:
  o when an EDID is found in Xorg.log, pass it to monitor-parse-edid
  o handle --perl option (passed to monitor-parse-edid)

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 1.11-1mdv2008.0
+ Revision: 74812
- Import monitor-edid



* Thu Aug 31 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.11-1mdv2007.0
- fix ballback to old get_edid() function
- ignore VBIOS checksum failures, use CPU emulator in that case

* Tue Jul 11 2006 Pixel <pixel@mandriva.com> 1.10-1mdv2007.0
- use a fixed FontPath (do not default to unix:-1 in case xfs is not running)

* Wed Jun 07 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.9-5mdv2007.0
- do not build on sparc
- build with $RPM_OPT_FLAGS
- do parallell build
- cosmetics

* Wed May 10 2006 Pixel <pixel@mandriva.com> 1.9-4mdk
- fix a segfault occuring on some boxes in monitor-get-edid-using-vbe, 
  when using try-in-console

* Fri Mar 10 2006 Pixel <pixel@mandriva.com> 1.9-3mdk
- set url to wiki page instead of the cvs

* Fri Jan  6 2006 Pixel <pixel@mandriva.com> 1.9-2mdk
- add missing monitor-get-edid

* Thu Jan  5 2006 Pixel <pixel@mandriva.com> 1.9-1mdk
- monitor-get-edid is now a perl script able to probe /proc/acpi/video
  (or /proc/device-tree on PPC)
- binary monitor-get-edid is now monitor-get-edid-using-vbe
- monitor-edid is able to get more than one head

* Mon Aug  8 2005 Pixel <pixel@mandriva.com> 1.5-1mdk
- add option --try-in-console when probing edid
  since probing edid sometimes only work in console
- use this option by default in monitor-probe

* Wed Apr  6 2005 Pixel <pixel@mandrakesoft.com> 1.4-1mdk
- default on old lrmi code to get ddc via int10
- fix build on vesa-cvt

* Fri Mar 25 2005 Pixel <pixel@mandrakesoft.com> 1.3-1mdk
- added vesa-cvt (allowing to compute reduced-blanking timings)

* Thu Mar 17 2005 Pixel <pixel@mandrakesoft.com> 1.2-1mdk
- new release (added monitor-probe and monitor-probe-using-X)

* Tue Mar  8 2005 Pixel <pixel@mandrakesoft.com> 1.1-1mdk
- new release

* Wed Feb 23 2005 Pixel <pixel@mandrakesoft.com> 1.0-1mdk
- first package
