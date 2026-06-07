Name:           rmonitor
Version:        TEMPLATE_VERSION
Release:        1%{?dist}
Summary:        A project template for creating unified local terminal utilities in Rust
License:        MIT
URL:            https://github.com/local76/rMonitor
Source0:        %{name}-%{version}.tar.gz

%description
A project template for creating unified local terminal utilities in Rust.

%prep
%setup -q

%build
cargo build --release --locked

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_datadir}/applications
install -d $RPM_BUILD_ROOT/%{_datadir}/pixmaps
install -m 755 target/release/rmonitor $RPM_BUILD_ROOT/%{_bindir}/rmonitor
install -m 644 packaging/desktop/rmonitor.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/rmonitor.desktop
install -m 644 assets/brand/app_icon.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/rmonitor.png

%files
%{_bindir}/rmonitor
%{_datadir}/applications/rmonitor.desktop
%{_datadir}/pixmaps/rmonitor.png
