# TODO try to integrate the testsuite ?
%define oname python-cjson

Summary: A very fast JSON encoder/decoder for Python 
Name: python2-cjson
Version: 1.1.0
Release: 1
Source0: http://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License: LGPL
Group:   Development/Python
Url:     https://www.ag-projects.com/
BuildRequires: python2-devel
Requires:      python
%rename	python-cjson

%description
This module implements a very fast JSON encoder/decoder for Python.

JSON stands for JavaScript Object Notation and is a text based lightweight 
data exchange format which is easy for humans to read/write and for machines 
to parse/generate. JSON is completely language independent and has multiple 
implementations in most of the programming languages, making it ideal for 
data exchange and storage.

The module is written in C and it is up to 250 times faster when compared 
to the other python JSON implementations which are written directly in python. 
This speed gain varies with the complexity of the data and the operation and 
is the the range of 10-200 times for encoding operations and in the range of 
100-250 times for decoding operations.

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

%build

%install
python2 setup.py install --root %{buildroot}

%files
%doc README ChangeLog
%{py2_platsitedir}/cjson.so
%{py2_platsitedir}/*egg-info



%changelog
* Wed Jul 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-6mdv2011.0
+ Revision: 549840
- P0: security fix for CVE-2010-1666 (fedora)

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.5-5mdv2010.0
+ Revision: 442076
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-4mdv2009.0
+ Revision: 259525
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-3mdv2009.0
+ Revision: 247395
- rebuild

* Wed Jan 09 2008 Michael Scherer <misc@mandriva.org> 1.0.5-1mdv2008.1
+ Revision: 147125
- import python-cjson


