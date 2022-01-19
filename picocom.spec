Name:           picocom
Version:        3.1
Release:        1
Summary:        Minimal serial communications program

Group:          Communications
License:        GPLv2+
URL:            https://github.com/npat-efault/picocom
Source0:        https://github.com/npat-efault/picocom/archive/%{name}-%{version}.tar.gz

# for groupadd
Requires(pre):  shadow-utils

%description
As its name suggests, [picocom] is a minimal dumb-terminal emulation
program. It is, in principle, very much like minicom, only it's "pico"
instead of "mini"! It was designed to serve as a simple, manual, modem
configuration, testing, and debugging tool. It has also served (quite
well) as a low-tech "terminal-window" to allow operator intervention
in PPP connection scripts (something like the ms-windows "open
terminal window before / after dialing" feature).  It could also prove
useful in many other similar tasks. It is ideal for embedded systems
since its memory footprint is minimal (less than 50K, when
stripped).

%prep
%setup -q

%build
%make_build CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%{ldflags}" UUCP_LOCK_DIR=/run/lock/picocom

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 picocom %{buildroot}%{_bindir}/
install -m 644 picocom.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}/run/lock/picocom
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
cat >%{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf <<'EOF'
d /run/lock/picocom 0775 root dialout - -
EOF

%pre
getent group dialout >/dev/null || groupadd -g 18 -r -f dialout
exit 0

%files
%doc CONTRIBUTORS LICENSE.txt
%{_bindir}/picocom
%{_mandir}/man1/*
%{_prefix}/lib/tmpfiles.d/%{name}.conf
