Summary:	Emacs News and Mail reader
Summary(pl.UTF-8):	Emacsowy czytnik poczty oraz grup usenet
Name:		xemacs-gnus-pkg
Version:	5.8.8
%define		etc_ver 0.27
Release:	4
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.gnus.org/pub/gnus/gnus-%{version}.tar.gz
# Source0-md5:	eb3c7db29f1bc84996f11784f408a80c
Source1:	ftp://ftp.gnus.org/pub/gnus/etc-%{etc_ver}.tar.gz
# Source1-md5:	c98e5575541d4e5f7b9c8abcf2bf4fc0
URL:		http://www.gnus.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xemacs
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
Requires:	xemacs-gnus-pkg = %{version}

%description -n xemacs-gnus-info-pkg
Info documentation for GNUS.

%description -n xemacs-gnus-info-pkg -l pl.UTF-8
Dokumentacja info dla GNUSa.

%prep
%setup -q -n gnus-%{version} -a1
cat <<EOF >lisp/auto-autoloads.el
(autoload 'gnus "gnus" nil t)
EOF

%build
mv -f aclocal.m4 acinclude.m4
%{__aclocal}
%{__autoconf}
%configure
%{__make} EMACS=xemacs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages/lisp/gnus,%{_infodir}}

# remove .el file if corresponding .elc exists
for i in lisp/*.el; do test ! -f ${i}c || rm -f $i ; done
cp -a etc-%{etc_ver} $RPM_BUILD_ROOT%{_datadir}/xemacs-packages%{_sysconfdir}
install lisp/*.el* $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gnus
install texi/gnus{,-[0-9]*} $RPM_BUILD_ROOT%{_infodir}

%post -n xemacs-gnus-info-pkg	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -n xemacs-gnus-info-pkg	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README GNUS-NEWS ChangeLog
%{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages%{_sysconfdir}/*

%files -n xemacs-gnus-info-pkg
%defattr(644,root,root,755)
%{_infodir}/*.info*
