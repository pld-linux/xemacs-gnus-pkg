Summary:	Emacs News and Mail reader
Summary(pl):	Emacsowy czytnik poczty oraz grup usenet
Name:		xemacs-gnus-pkg
Version:	5.8.8
%define		etc_ver 0.27
Release:	3
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.gnus.org/pub/gnus/gnus-%{version}.tar.gz
Source1:	ftp://ftp.gnus.org/pub/gnus/etc-%{etc_ver}.tar.gz
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

%description -l pl
Dzieki pakietowi Gnus mo¿esz czytaæ newsy i pocztê z u¿yciem XEmacsa.
Gnus mo¿e pobieraæ listy z najró¿niejszych ¼róde³ w tym z lokalnego
spoola jak i plików mbox.

%prep
%setup -q -n gnus-%{version} -a1
cat <<EOF >lisp/auto-autoloads.el
(autoload 'gnus "gnus" nil t)
EOF

%package -n xemacs-gnus-info-pkg
Summary:        Info documentation for GNUS
Summary(pl):    Dokumentacja info dla GNUSa
Group:          Applications/Editors/Emacs
Requires:       xemacs-gnus-pkg = %{version}

%description -n xemacs-gnus-info-pkg
Info documentation for GNUS.

%description -n xemacs-gnus-info-pkg -l pl
Dokumentacja info dla GNUSa.

%build
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

gzip -9nf README GNUS-NEWS ChangeLog


%post -n xemacs-gnus-info-pkg
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -n xemacs-gnus-info-pkg
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages%{_sysconfdir}/*

%files -n xemacs-gnus-info-pkg
%defattr(644,root,root,755)
%{_infodir}/*
