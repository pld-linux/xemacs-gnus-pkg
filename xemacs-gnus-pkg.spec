Summary:	Emacs News and Mail reader
Name:		xemacs-gnus-pkg
Version:	5.8.8
%define		etc_ver 0.27
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.task.gda.pl/mirror/ftp.gnus.org/pub/gnus/gnus-%{version}.tar.gz
Source1:	ftp://ftp.task.gda.pl/mirror/ftp.gnus.org/pub/gnus/etc-%{etc_ver}.tar.gz
URL:		http://www.gnus.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is XEmacs News and Mail system
add 

%description -l pl 

%prep
%setup -q -n gnus-%{version} -a1
cat <<EOF >lisp/auto-autoloads.el
(autoload 'gnus "gnus" nil t)
EOF

%build                                                      
./configure
%{__make} EMACS=xemacs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gnus
install -d $RPM_BUILD_ROOT%{_infodir}

# remove .el file if corresponding .elc exists
for i in lisp/*.el; do test ! -f ${i}c || rm -f $i ; done
cp -a etc-%{etc_ver} $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/etc
install lisp/*.el* $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/gnus
install texi/gnus{,-[0-9]*} $RPM_BUILD_ROOT%{_infodir}

gzip -9nf README GNUS-NEWS ChangeLog


%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/etc/*
%{_infodir}/*
