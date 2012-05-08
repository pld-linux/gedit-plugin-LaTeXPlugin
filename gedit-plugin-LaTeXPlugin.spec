Summary:	LaTeX plugin for gedit
Summary(pl.UTF-8):	Wtyczka LaTeX dla gedita
Name:		gedit-plugin-LaTeXPlugin
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://downloads.sourceforge.net/gedit-latex/LaTeXPlugin-%{version}.tar.gz
# Source0-md5:	714bbe2c24337a8a8ea3e444a5d729fc
Patch0:		%{name}-path.patch
URL:		http://live.gnome.org/Gedit/LaTeXPlugin
Requires:	gedit >= 2.16.0
Requires:	perl
Requires:	rubber
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LaTeX plugin for gedit.

%description -l pl.UTF-8
Wtyczka LaTeX dla gedita.

%prep
%setup -qc
#%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/GeditLaTeXPlugin

mv GeditLaTeXPlugin/ChangeLog .
cp -R GeditLaTeXPlugin $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/
cp GeditLaTeXPlugin.gedit-plugin $RPM_BUILD_ROOT%{_libdir}/gedit/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{_libdir}/gedit/plugins/GeditLaTeXPlugin
%{_libdir}/gedit/plugins/*.gedit-plugin
