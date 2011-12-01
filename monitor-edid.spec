# EDIT IN SVN NOT IN SOURCE PACKAGE (NO PATCH ALLOWED).

%define	name	monitor-edid
%define	version	3.0
%define	release	%mkrel 3

Summary:	EDID retrieval and parsing tools
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		System/Configuration/Other
Url:		http://wiki.mandriva.com/en/Tools/monitor-edid
%ifarch %ix86 x86_64
BuildRequires:	libx86-devel
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExcludeArch:	%{sunsparc} %arm %mips

%description
This package provides tools for EDID retrieval, EDID parsing and
other methods of monitor probing.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS
%{_bindir}/*
%{_sbindir}/*
