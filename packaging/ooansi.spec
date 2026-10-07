Name:           ooansi
Version:        0.1.0
Release:        1%{?dist}
Summary:        Applies and strips Select Graphic Rendition (SGR) escape codes from text.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooansi
Source0:        ooansi-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooansi is a sovereign, capability-bounded SGR ESCAPES written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooansi
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooansi-uninstall

%files
/usr/bin/ooansi
/usr/bin/ooansi-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
