Name:           ooansi
Version:        0.2.0
Release:        1%{?dist}
Summary:        ANSI terminal sequence generator.
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/ooansi
Source0:        ooansi-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooansi is a sovereign, capability-bounded ANSI terminal sequence generator written
in pure openOODA, featuring zero ambient authority, TrueColor RGB formatting,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooansi
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooansi-uninstall

%files
/usr/bin/ooansi
/usr/bin/ooansi-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to pure openOODA 0.2.0 with MCP server and multi-distro packaging parity
