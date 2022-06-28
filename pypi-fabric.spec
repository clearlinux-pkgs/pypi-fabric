#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9C29BC560041E930 (jeff@bitprophet.org)
#
Name     : pypi-fabric
Version  : 2.7.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/fc/c8/6a002a659d78db66ed134fd390773afd87a638026feef2c8efe6a4492776/fabric-2.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/c8/6a002a659d78db66ed134fd390773afd87a638026feef2c8efe6a4492776/fabric-2.7.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/fc/c8/6a002a659d78db66ed134fd390773afd87a638026feef2c8efe6a4492776/fabric-2.7.0.tar.gz.asc
Summary  : High level SSH command execution
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-fabric-bin = %{version}-%{release}
Requires: pypi-fabric-license = %{version}-%{release}
Requires: pypi-fabric-python = %{version}-%{release}
Requires: pypi-fabric-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(invoke)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(pathlib2)

%description
To find out what's new in this version of Fabric, please see `the changelog

%package bin
Summary: bin components for the pypi-fabric package.
Group: Binaries
Requires: pypi-fabric-license = %{version}-%{release}

%description bin
bin components for the pypi-fabric package.


%package license
Summary: license components for the pypi-fabric package.
Group: Default

%description license
license components for the pypi-fabric package.


%package python
Summary: python components for the pypi-fabric package.
Group: Default
Requires: pypi-fabric-python3 = %{version}-%{release}

%description python
python components for the pypi-fabric package.


%package python3
Summary: python3 components for the pypi-fabric package.
Group: Default
Requires: python3-core
Provides: pypi(fabric)
Requires: pypi(invoke)
Requires: pypi(paramiko)
Requires: pypi(pathlib2)

%description python3
python3 components for the pypi-fabric package.


%prep
%setup -q -n fabric-2.7.0
cd %{_builddir}/fabric-2.7.0
pushd ..
cp -a fabric-2.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656375705
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-fabric
cp %{_builddir}/fabric-2.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-fabric/eadf0675261da2116b63962716fbf09f4cb946ca
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fab

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-fabric/eadf0675261da2116b63962716fbf09f4cb946ca

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
