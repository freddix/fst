%define		gitver	20661444547412e688ff9100dc8a111731ee2860

Summary:	Standalone wrapper for Windows VST plug-ins
Name:		fst
Version:	1.8.1
Release:	3
License:	GPL v2
Group:		Applications
# git clone --depth=1 git://repo.or.cz/fst.git
# cd fst ; git archive --format=tar --prefix=fst-1.8.1/ HEAD | xz > fst-1.8.1-20661444547412e688ff9100dc8a111731ee2860.tar.xz
Source0:	%{name}-%{version}-%{gitver}.tar.xz
# Source0-md5:	88b6e7914c417c5c43fa837f3b36cbec
BuildRequires:	gtk+-devel
BuildRequires:	wine-devel
BuildRequires:	jack-audio-connection-kit-devel
Requires:	jack-audio-connection-kit
Requires:	wine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Standalone wrapper for Windows VST plug-ins.

%prep
%setup -q

%ifarch %{x8664}
sed -i "s/m32/m64/g" Makefile

%build
%{__make} \
	CC="%{__cc}"				\
	CFLAGS="%{rpmcflags} %{rpmldflags}"	\
	CXX="%{__cxx}"				\
	CXXFLAGS="%{rpmcxxflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D fst.exe.so $RPM_BUILD_ROOT%{_libdir}/%{name}/fst.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/fst.so

