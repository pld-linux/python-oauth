Summary:	Python library for OAuth version 1.0a
Name:		python-oauth
Version:	1.0.1
Release:	1
License:	MIT
Group:		Development/Languages
URL:		http://code.google.com/p/oauth/
Source0:	http://pypi.python.org/packages/source/o/oauth/oauth-%{version}.tar.gz
# Source0-md5:	30ed3cc8c11d7841a89feab437aabf81
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python library for OAuth version 1.0a.

%prep
%setup -q -n oauth-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--skip-build \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{py_sitescriptdir}/oauth-%{version}-py*.egg-info
%{py_sitescriptdir}/oauth
