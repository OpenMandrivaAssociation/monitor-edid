Summary:	EDID retrieval and parsing tools
Name:		monitor-edid
Version:	3.1
Release:	8
License:	GPLv3+
Group:		System/Configuration/Other
Url:		http://wiki.mandriva.com/en/Tools/monitor-edid
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	libx86-devel
ExclusiveArch:	%{ix86} x86_64

%description
This package provides tools for EDID retrieval, EDID parsing and
other methods of monitor probing.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

%files
%doc README NEWS
%{_bindir}/*
%{_sbindir}/*
