Name:           nautilus-dropbox
Version:        2.10.0
Release:        1%{?dist}
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
%configure
make %{?_smp_mflags}


%install
%make_install
rm %{buildroot}%{_libdir}/nautilus/extensions-3.0/libnautilus-dropbox.*a
desktop-file-validate %{buildroot}%{_datadir}/applications/dropbox.desktop


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/dropbox
%{_libdir}/nautilus/extensions-3.0/%{name}.so
%{_datadir}/applications/dropbox.desktop
%{_datadir}/icons/hicolor/*x*/apps/dropbox.png
%{_mandir}/man1/dropbox.1.gz
%{_datadir}/%{name}

%changelog
* Sun Dec 21 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.10.0-1
- Initial build
