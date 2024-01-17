Name:           helm
Version:        3.13.3
Release:        1%{?dist}
Summary:        Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.
URL:            https://github.com/helm/helm
License:        Apache-2.0
Source0:        https://github.com/helm/helm/archive/refs/tags/v%{version}.tar.gz


Provides:       %{name} = %{version}

%description
Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.

# %global debug_package %{nil}

%prep
%autosetup


%build
%make_build


%install
%make_install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
# go test should be here... :)

# %post


# %preun


%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md


%changelog
* Wed June 14 2023 Yannik Mueller - 3.13.3-1
- Initial release
