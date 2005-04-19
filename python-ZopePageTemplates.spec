
%define	module	ZopePageTemplates

Summary:	Zope Page Templates which works outside Zope
Summary(pl):	Zope Page Templates dzia³aj±ce poza ¶rodowiskiem Zope
Name:		python-%{module}
Version:	1.4.0
Release:	1
License:	distributable
Group:		Development/Languages/Python
Source0:	http://mesh.dl.sourceforge.net/sourceforge/zpt/%{module}-%{version}.tgz
# Source0-md5:	165f1cfedb0efa0ee3ce57087a1f4a01
URL:		http://zpt.sourceforge.net/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zope Page Templates  is a Python package that implements Page
Templates like in Zope, but works outside of Zope. In fact, you don't
need to install any part of Zope to use them. This means that you can
use the elegance and ease of page templates in your own web
applications, reporting frameworks, documentation systems, etc.

%description -l pl
Zope Page Templates jest bibliotek± Pythona, która implementuje wzroce 
stron takie jak w Zope, ale dzia³a bez jego udzia³u. Oznacza to, ¿e 
mo¿esz u¿ywaæ eleganckiego i prostego mechanizmu tworzenia wzorców stron 
WWW, w swojej w³asnej aplikacji.


%prep
%setup -q -n %{module}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt COPYING.txt version.txt ZPL.txt
%{py_sitescriptdir}/%{module}
