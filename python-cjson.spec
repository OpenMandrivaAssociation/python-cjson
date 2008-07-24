# TODO try to integrate the testsuite ?

%define name python-cjson
%define version 1.0.5
%define release %mkrel 3

Summary: A very fast JSON encoder/decoder for Python 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
License: LGPL
Group:   Development/Python
Url:     http://www.ag-projects.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
Requires:      python
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
%setup -q

%build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{py_platsitedir}/cjson.so
%{py_platsitedir}/*egg-info

