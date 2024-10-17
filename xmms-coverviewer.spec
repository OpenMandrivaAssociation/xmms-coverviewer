%define name	xmms-coverviewer
%define oname   xmms-coverviewerxp
%define version	0.12
%define prerel rc2
%define release	%mkrel 0.1%prerel.2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XMMS plugin that displays images related to the files being played
License:	GPL
Group: 		Sound
Source:		http://prdownloads.sourceforge.net/coverviewer/%{oname}-cvs-%prerel.tar.bz2
URL:		https://coverviewer.sourceforge.net/
Requires:	xmms >= 1.2.4
#gw the script for fetching the covers needs this
Requires: 	pygtk2.0
BuildRequires:	xmms-devel >= 1.2.4
BuildRequires:	libgdk-pixbuf-devel
BuildRequires:	id3lib-devel
BuildRequires:	libxml2-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
CoverViewer scans your directories for images and displays them while
playing songs in xmms. It can also retrieve covers directly from
internet using a script (A sample script using amazon.com is provided in
%{_datadir}/coverviewer)

%prep
%setup -q -n %oname-cvs-%prerel

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/General/libcoverview.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS
%{_libdir}/xmms/General/libcoverview.so
%{_datadir}/coverviewer



