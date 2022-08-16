Summary:	EDID retrieval and parsing tools
Name:		monitor-edid
Version:	3.4
Release:	1
License:	GPLv3+
Group:		System/Configuration/Other
Url:		https://gitweb.mageia.org/software/monitor-edid
Source0:	https://gitweb.mageia.org/software/%{name}/snapshot/%{name}-%{version}.tar.xz
Patch0:		monitor-edid-3.4-merge-usr.patch
BuildRequires:	libx86-devel
ExclusiveArch:	%{ix86} %{x86_64}

%description
Monitor-edid is a tool for probing and parsing Extended display
identification data (EDID) from monitors.
For more information about EDID, see https://en.wikipedia.org/wiki/EDID

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%doc README NEWS
%{_bindir}/*
