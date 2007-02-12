Summary:	LaTeX plugin for gedit
Summary(pl.UTF-8):   Wtyczka LaTeX dla gedita
Name:		gedit-plugin-LaTeXPlugin
Version:	20061112
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://www.michaels-website.de/files/LaTeXPlugin-%{version}.tar.bz2
# Source0-md5:	b567b881101855a239da311d8bd7eb4c
Patch0:		%{name}-path.patch
URL:		http://live.gnome.org/Gedit/LaTeXPlugin
Requires:	gedit2 >= 2.16.0
Requires:	perl
Requires:	rubber
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeX plugin for gedit.

%description -l pl.UTF-8
Wtyczka LaTeX dla gedita.

%prep
%setup -qc
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/LaTeXPlugin

mv LaTeXPlugin/ChangeLog .
cp -R LaTeXPlugin $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/
cp LaTeXPlugin.gedit-plugin $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{_libdir}/gedit-2/plugins/LaTeXPlugin
%{_libdir}/gedit-2/plugins/*.gedit-plugin
