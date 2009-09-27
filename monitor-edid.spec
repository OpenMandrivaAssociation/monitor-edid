# EDIT IN SVN NOT IN SOURCE PACKAGE (NO PATCH ALLOWED).

%define	name	monitor-edid
%define	version	2.3
%define	release	%mkrel 2

Summary:	Get monitor details
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		System/Configuration/Other
Url:		http://wiki.mandriva.com/en/Tools/monitor-edid
%ifarch %ix86
BuildRequires:	liblrmi-devel
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExcludeArch:	%{sunsparc} %arm %mips

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
%doc README NEWS
%{_bindir}/*
%{_sbindir}/*
