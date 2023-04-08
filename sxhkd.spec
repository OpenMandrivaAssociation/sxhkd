Summary:	A simple X hotkey daemon
Name:		sxhkd
Version:	0.6.2
Release:	1
License:	BSD
Group:		Development/X11
URL:		https://github.com/baskerville/%{name}
Source0:	https://github.com/baskerville/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	systemd
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-keysyms)

%description
sxhkd is an X daemon that reacts to input events by executing commands.

Its configuration file is a series of bindings that define the associations
between the input events and the commands.

The format of the configuration file supports a simple notation for mapping
multiple shortcuts to multiple commands in parallel.


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_docdir}/%{name}/examples
%{_unitdir}/%{name}.service
%{_mandir}/man*/%{name}.1.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%before_configure
%make_build

%install
%make_install PREFIX="%{_prefix}"

# systemd
install -p -D -m 0644 contrib/systemd/%{name}.service \
	%{buildroot}/%{_unitdir}/%{name}.service

