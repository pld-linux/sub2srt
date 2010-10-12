Summary:	Tool for .sub to .srt conversion
Summary(pl.UTF-8):	Narzędzie do konwersji .sub do .srt
Name:		sub2srt
Version:	0.5.3
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.robelix.com/sub2srt/download/%{name}-%{version}.tar.gz
# Source0-md5:	ce2dd86b008ab61b70cd1f2ed6054a4b
URL:		http://www.robelix.com/sub2srt/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sub2srt is a simple tool to convert two common subtitle formats
(microdvd and subrip - both are known as ".sub") to subviewer ".srt"
format.

%description -l pl.UTF-8
sub2srt jest prostym narzędziem do konwersji dwóch popularnych
formatów napisów (microdvd oraz subrip - oba znane jako ".sub") do
formatu subviewera ".srt".

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -a sub2srt $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/sub2srt
