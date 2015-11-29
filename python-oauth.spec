Summary:	Python library for OAuth version 1.0a
Name:		python-oauth
Version:	1.0.1
Release:	3
License:	MIT
Group:		Development/Languages
URL:		http://code.google.com/p/oauth/
BuildRequires:	rpmbuild(macros) >= 1.710
Source0:	http://pypi.python.org/packages/source/o/oauth/oauth-%{version}.tar.gz
# Source0-md5:	30ed3cc8c11d7841a89feab437aabf81
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python library for OAuth version 1.0a.

%prep
%setup -q -n oauth-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{py_sitescriptdir}/oauth-%{version}-py*.egg-info
%{py_sitescriptdir}/oauth
