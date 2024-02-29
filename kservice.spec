#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kservice
Version  : 6.0.0
Release  : 213
URL      : https://download.kde.org/stable/frameworks/6.0/kservice-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/kservice-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/kservice-6.0.0.tar.xz.sig
Summary  : Advanced plugin and service introspection
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kservice-bin = %{version}-%{release}
Requires: kservice-data = %{version}-%{release}
Requires: kservice-lib = %{version}-%{release}
Requires: kservice-license = %{version}-%{release}
Requires: kservice-locales = %{version}-%{release}
Requires: kservice-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : docbook-xml
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : libxml2
BuildRequires : libxslt
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KService
## Introduction
KService allows to query information about installed applications and their associated file types.

%package bin
Summary: bin components for the kservice package.
Group: Binaries
Requires: kservice-data = %{version}-%{release}
Requires: kservice-license = %{version}-%{release}

%description bin
bin components for the kservice package.


%package data
Summary: data components for the kservice package.
Group: Data

%description data
data components for the kservice package.


%package dev
Summary: dev components for the kservice package.
Group: Development
Requires: kservice-lib = %{version}-%{release}
Requires: kservice-bin = %{version}-%{release}
Requires: kservice-data = %{version}-%{release}
Provides: kservice-devel = %{version}-%{release}
Requires: kservice = %{version}-%{release}

%description dev
dev components for the kservice package.


%package lib
Summary: lib components for the kservice package.
Group: Libraries
Requires: kservice-data = %{version}-%{release}
Requires: kservice-license = %{version}-%{release}

%description lib
lib components for the kservice package.


%package license
Summary: license components for the kservice package.
Group: Default

%description license
license components for the kservice package.


%package locales
Summary: locales components for the kservice package.
Group: Default

%description locales
locales components for the kservice package.


%package man
Summary: man components for the kservice package.
Group: Default

%description man
man components for the kservice package.


%prep
%setup -q -n kservice-6.0.0
cd %{_builddir}/kservice-6.0.0

%build
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709238577
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DKDE_INSTALL_SYSCONFDIR=/usr/share
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DKDE_INSTALL_SYSCONFDIR=/usr/share
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709238577
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kservice
cp %{_builddir}/kservice-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kservice/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kservice-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kservice/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kservice-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kservice/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kservice-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kservice/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kservice-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kservice/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kservice-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kservice/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kservice-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kservice/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kservice6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kbuildsycoca6
/usr/bin/kbuildsycoca6

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kservice.categories
/usr/share/qlogging-categories6/kservice.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KService/KApplicationTrader
/usr/include/KF6/KService/KService
/usr/include/KF6/KService/KServiceAction
/usr/include/KF6/KService/KServiceGroup
/usr/include/KF6/KService/KSycoca
/usr/include/KF6/KService/KSycocaEntry
/usr/include/KF6/KService/KSycocaType
/usr/include/KF6/KService/kapplicationtrader.h
/usr/include/KF6/KService/kservice.h
/usr/include/KF6/KService/kservice_export.h
/usr/include/KF6/KService/kservice_version.h
/usr/include/KF6/KService/kserviceaction.h
/usr/include/KF6/KService/kserviceconversioncheck_p.h
/usr/include/KF6/KService/kservicegroup.h
/usr/include/KF6/KService/ksycoca.h
/usr/include/KF6/KService/ksycocaentry.h
/usr/include/KF6/KService/ksycocatype.h
/usr/lib64/cmake/KF6Service/KF6ServiceConfig.cmake
/usr/lib64/cmake/KF6Service/KF6ServiceConfigVersion.cmake
/usr/lib64/cmake/KF6Service/KF6ServiceTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Service/KF6ServiceTargets.cmake
/usr/lib64/libKF6Service.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Service.so.6.0.0
/usr/lib64/libKF6Service.so.6
/usr/lib64/libKF6Service.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kservice/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kservice/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kservice/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kservice/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kservice/e458941548e0864907e654fa2e192844ae90fc32

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man8/kbuildsycoca6.8
/usr/share/man/es/man8/kbuildsycoca6.8
/usr/share/man/fr/man8/kbuildsycoca6.8
/usr/share/man/it/man8/kbuildsycoca6.8
/usr/share/man/man8/kbuildsycoca6.8
/usr/share/man/nl/man8/kbuildsycoca6.8
/usr/share/man/pt_BR/man8/kbuildsycoca6.8
/usr/share/man/tr/man8/kbuildsycoca6.8
/usr/share/man/uk/man8/kbuildsycoca6.8

%files locales -f kservice6.lang
%defattr(-,root,root,-)

