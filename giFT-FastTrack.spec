Summary:	FastTrack plugin for giFT
Summary(pl):	Wtyczka FastTrack dla giFT
Name:		giFT-FastTrack
Version:	0.8.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://download.berlios.de/gift-fasttrack/%{name}-%{version}.tar.gz
# Source0-md5:	515e090a190fc9c18faa114a61a2b6f7
URL:		http://developer.berlios.de/projects/gift-fasttrack/
BuildRequires:	giFT-devel >= 0.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
giFT-FastTrack is a plugin for giFT (http://giftproject.org) which
enables users of giFT to participate in the FastTrack network. The
required cryptographic algorithms have been successfully reverse
engineered and searching/downloading already work.

%description -l pl
giFT-FastTrack jest wtyczk± dla giFT (http://giftproject.org)
pozwalaj±c± u¿ytkownikom giFT udzielaæ siê w sieci FastTrack. Wymagane
algorytmy kryptograficzne zosta³y z³amane i szukanie/¶ci±ganie ju¿
dzia³a.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/giFT/*.so*
%{_libdir}/giFT/*.la
%{_datadir}/giFT/FastTrack
%{_mandir}/man1/*
