Name:           nautilus-dropbox
Version:        2.10.0
Release:        2%{?dist}
Summary:        Dropbox integration for Nautilus

License:        GPLv3
URL:            https://www.dropbox.com/
Source0:        https://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2

BuildRequires:  nautilus-devel
BuildRequires:  python-docutils
BuildRequires:  desktop-file-utils
BuildRequires:  pygtk2


%description
Nautilus Dropbox is an extension that integrates
the Dropbox web service with your GNOME Desktop.

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install
rm %{buildroot}%{_libdir}/nautilus/extensions-3.0/libnautilus-dropbox.la
desktop-file-validate %{buildroot}%{_datadir}/applications/dropbox.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/dropbox
%{_libdir}/nautilus/extensions-3.0/libnautilus-dropbox.so
%{_datadir}/applications/dropbox.desktop
%{_datadir}/icons/hicolor/*x*/apps/dropbox.png
%{_mandir}/man1/dropbox.1.gz
%{_datadir}/%{name}

%changelog
* Tue Dec 23 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.10.0-2
- Add Icon Cache scriptlets

* Sun Dec 21 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.10.0-1
- Initial build
