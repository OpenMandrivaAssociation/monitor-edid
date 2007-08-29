# EDIT IN SVN NOT IN SOURCE PACKAGE (NO PATCH ALLOWED).

%define	name	monitor-edid
%define	version	1.11
%define	release	%mkrel 1

Summary:	Get monitor details
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Configuration/Other
Url:		http://qa.mandriva.com/twiki/bin/view/Main/Monitor-edid
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExcludeArch:	%{sunsparc}

%description
This package will try to read the monitor details directly from the
monitor.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sbindir}
install monitor-edid monitor-get-edid-using-vbe monitor-probe monitor-probe-using-X $RPM_BUILD_ROOT%{_sbindir}
install monitor-parse-edid $RPM_BUILD_ROOT%{_bindir}
install cvt $RPM_BUILD_ROOT%{_bindir}/vesa-cvt

ln -s monitor-edid $RPM_BUILD_ROOT%{_sbindir}/monitor-get-edid

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_sbindir}/*
