Name:    mytest_cil
Version: 0.1.0
Release: 4%{?dist}
Summary: mytest cil

License: Apache-2.0 license

Requires: udica policycoreutils
BuildRequires: nftables
Recommends: setools-console nftables policycoreutils-python-utils netcat conntrack-tools

Source0: mytest.cil
Source1: secmark.nft

%description
mytest_cil

%install
mkdir -p -m0755 %{buildroot}/usr/share/mytest
install %{SOURCE0}  %{buildroot}/usr/share/mytest/
install %{SOURCE1}  %{buildroot}/usr/share/mytest/

%files
/usr/share/mytest/mytest.cil
/usr/share/mytest/secmark.nft

%post
semodule -i /usr/share/mytest/mytest.cil /usr/share/udica/templates/base_container.cil

%changelog
* Sun Aug 21 2022 <rigault.francois@gmail.com> 
- Initial Build.
