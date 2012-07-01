Summary:	Emacs News and Mail reader
Summary(pl.UTF-8):	Emacsowy czytnik poczty oraz grup usenet
Name:		xemacs-gnus-pkg
Version:	1.94
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/gnus-%{version}-pkg.tar.gz
# Source0-md5:	e7a90a1e3eb657623697a9997d3d4d17
URL:		http://www.gnus.org/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	xemacs
Requires:	xemacs-eterm-pkg
Requires:	xemacs-fsf-compat-pkg
Requires:	xemacs-mailcrypt-pkg
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-mh-e-pkg
Requires:	xemacs-w3-pkg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You can read news (and mail) from within XEmacs by using Gnus. The
news can be gotten by any nefarious means you can think of -- NNTP,
local spool or your mbox file. All at the same time, if you want to
push your luck.

%description -l pl.UTF-8
Dzięki pakietowi Gnus można czytać newsy i pocztę z użyciem XEmacsa.
Gnus może pobierać listy z najróżniejszych źródeł w tym z lokalnego
spoola jak i plików mbox.

%package -n xemacs-gnus-info-pkg
Summary:	Info documentation for GNUS
Summary(pl.UTF-8):	Dokumentacja info dla GNUSa
Group:		Applications/Editors/Emacs
Requires:	xemacs-gnus-pkg = %{epoch}:%{version}

%description -n xemacs-gnus-info-pkg
Info documentation for GNUS.

%description -n xemacs-gnus-info-pkg -l pl.UTF-8
Dokumentacja info dla GNUSa.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%post -n xemacs-gnus-info-pkg	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -n xemacs-gnus-info-pkg	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/gnus/GNUS-NEWS lisp/gnus/ChangeLog*
%{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages%{_sysconfdir}/*

%files -n xemacs-gnus-info-pkg
%defattr(644,root,root,755)
%{_infodir}/*.info*
