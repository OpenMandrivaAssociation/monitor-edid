Summary:	EDID retrieval and parsing tools
Name:		monitor-edid
Version:	3.0
Release:	15
License:	GPLv3+
Group:		System/Configuration/Other
Url:		http://wiki.mandriva.com/en/Tools/monitor-edid
Source0:	%{name}-%{version}.tar.bz2
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
%makeinstall_std

%files
%doc README NEWS
%{_bindir}/*
%{_sbindir}/*

