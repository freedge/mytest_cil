Name:    mytest_cil
Version: 0.1.0
Release: 1%{?dist}
Summary: mytest cil

License: Apache-2.0 license

Requires: udica policycoreutils setools-console nftables

%description
mytest_cil

%install

%files

%post
A=$(mktemp -d)
cat > ${A}/mytest.cil << EOF
(block mytest
    (blockinherit container)

    (allow process http_cache_port_t ( tcp_socket (  name_bind )))
    (allow process http_port_t ( tcp_socket (  name_connect )))
    (allow process dns_port_t ( tcp_socket (  name_connect )))
    (allow process process ( tcp_socket (  listen )))
    (allow process node_t ( tcp_socket (  node_bind )))
    (allow process node_t ( udp_socket (  node_bind )))
    (allow process unreserved_port_t ( udp_socket (  name_bind )))
    (allow process intranet_packet_t ( packet (  send recv )))
)
EOF
semodule -i ${A}/mytest.cil /usr/share/udica/templates/base_container.cil
rm ${A}/mytest.cil
rmdir ${A}

%changelog
* Sun Aug 21 2022 <rigault.francois@gmail.com> 
- Initial Build.
