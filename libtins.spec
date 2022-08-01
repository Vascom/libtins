Name:           libtins
Version:        4.4
Release:        1%{?dist}
Summary:        A high-level, multiplatform C++ network packet sniffing and crafting library

License:        BSD
URL:            https://github.com/mfontanini/libtins
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  boost-devel
BuildRequires:  doxygen

%description
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        docs
Summary:        Document files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    docs
The %{name}-docs package contains document files for
developing applications that use %{name}.

%prep
%autosetup


%build
%cmake -DLIBTINS_BUILD_TESTS=OFF -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
%cmake_build --target docs

%install
%cmake_install
mv %{buildroot}/usr/lib/cmake %{buildroot}%{_libdir}/


%files
%license LICENSE
%doc CHANGES.md CONTRIBUTING.md README.md THANKS
%{_libdir}/*.so.*

%files devel
%{_includedir}/tins
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/%{name}

%files docs
%doc %{__cmake_builddir}/docs


%changelog
* Mon Aug 01 2022 Vasiliy Glazov <vascom2@gmail.com> - 4.4-1
- Initial packaging for Fedora
