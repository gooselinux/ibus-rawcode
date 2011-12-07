Name:       ibus-rawcode
Version:    1.3.0.20100421
Release:    2%{?dist}
Summary:    The Rawcode engine for IBus input platform
License:    GPLv2+
Group:      System Environment/Libraries
URL:        https://fedorahosted.org/ibus-rawcode/
Source0:    https://fedorahosted.org/releases/i/b/ibus-rawcode/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  ibus-devel

Requires:   ibus
Patch1: bug-600209.patch

%description
The Rawcode engine for IBus platform.

%prep
%setup -q
%patch1 -p1 -b .1-auxiliary-text-for-space

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f $RPM_BUILD_ROOT%{python_sitearch}/_rawcode.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-rawcode
%{_datadir}/ibus-rawcode
%{_datadir}/ibus/component/*

%changelog
* Wed Jun 16 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.0.20100421-2
- added auxiliary text support, for space hit
- Resolves: bug 600209

* Wed Apr 21 2010 Pravin Satpute <psatpute@redhat.com> - 1.3.0.20100421-1
- upstream new release
- fixed bug 584233, 584240 

* Mon Feb 08 2010 Adam Jackson <ajax@redhat.com> 1.2.99.20100208-2
- Rebuild for new libibus.so.2 ABI.

* Mon Feb 08 2010 Pravin Satpute <pravin.d.s@gmail.com> - 1.2.99.20100208-1
- updated patches for code enhancements from phuang for ibus-1.2.99
- new upstream release

* Fri Dec 11 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-4
- resolved bug 546521

* Tue Nov 17 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-3
- resolved bug 531989

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.20090703-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Pravin Satpute <psatpute@redhat.com> - @VERSON@-1
- upstream release 1.2.0

* Sun Jun 28 2009 Matthias Clasen <mclasen@redhat.com> - 1.0.0.20090303-3
- Rebuild against newer ibus

* Tue Mar 03 2009 Pravin Satpute <pravin.d.s@gmail.com> - 1.0.0.20090303-2
- removed mod_path
- added build requires ibus-devel

* Tue Mar 03 2009 Pravin Satpute <pravin.d.s@gmail.com> - 1.0.0.20090303-1
- The first version.
