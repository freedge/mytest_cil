Name:    mytest_cil
Version: 0.1.0
Release: 7%{?dist}
Summary: mytest cil

License: Apache-2.0 license

Requires: udica policycoreutils
BuildRequires: nftables
Recommends: setools-console nftables policycoreutils-python-utils netcat conntrack-tools

Source0: mytest.cil
Source1: secmark.nft
Source2: exchange-bmc-os-info.cil

%description
mytest_cil

%install
mkdir -p -m0755 %{buildroot}/usr/share/mytest
install %{SOURCE0}  %{buildroot}/usr/share/mytest/
install %{SOURCE1}  %{buildroot}/usr/share/mytest/
install %{SOURCE2}  %{buildroot}/usr/share/mytest/

%files
/usr/share/mytest/mytest.cil
/usr/share/mytest/secmark.nft
/usr/share/mytest/exchange-bmc-os-info.cil

%post
semodule -i /usr/share/mytest/mytest.cil /usr/share/udica/templates/base_container.cil
semodule -i /usr/share/mytest/exchange-bmc-os-info.cil /usr/share/udica/templates/base_container.cil

%changelog
* Wed Aug 24 2022 <rigault.francois@gmail.com>
- Try something with ipmi

* Sun Aug 21 2022 <rigault.francois@gmail.com>
- Initial Build.
