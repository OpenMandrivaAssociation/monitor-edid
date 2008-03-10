# EDIT IN SVN NOT IN SOURCE PACKAGE (NO PATCH ALLOWED).

%define	name	monitor-edid
%define	version	1.16
%define	release	%mkrel 1

Summary:	Get monitor details
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Configuration/Other
Url:		http://wiki.mandriva.com/en/Tools/monitor-edid
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
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_sbindir}/*
