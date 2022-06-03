#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Feed
Version  : 0.63
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/XML-Feed-0.63.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/XML-Feed-0.63.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-feed-perl/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
Summary  : 'XML Syndication Feed Support'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-Feed-license = %{version}-%{release}
Requires: perl-XML-Feed-perl = %{version}-%{release}
Requires: perl(DateTime::Format::Builder)
Requires: perl(DateTime::Format::Flexible)
Requires: perl(DateTime::Format::ISO8601)
Requires: perl(DateTime::Format::Natural)
Requires: perl(XML::RSS::LibXML)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::ErrorHandler)
BuildRequires : perl(Clone)
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Format::Builder)
BuildRequires : perl(DateTime::Format::Flexible)
BuildRequires : perl(DateTime::Format::ISO8601)
BuildRequires : perl(DateTime::Format::Mail)
BuildRequires : perl(DateTime::Format::Natural)
BuildRequires : perl(DateTime::Format::Strptime)
BuildRequires : perl(DateTime::Format::W3CDTF)
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(Feed::Find)
BuildRequires : perl(HTML::Entities)
BuildRequires : perl(HTML::TokeParser)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(List::MoreUtils)
BuildRequires : perl(Module::Pluggable)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(URI)
BuildRequires : perl(URI::Fetch)
BuildRequires : perl(XML::Atom)
BuildRequires : perl(XML::LibXML)
BuildRequires : perl(XML::Parser)
BuildRequires : perl(XML::RSS)
BuildRequires : perl(XML::RSS::LibXML)
BuildRequires : perl(XML::XPath)
BuildRequires : perl(boolean)

%description
This is XML::Feed, an abstraction above the RSS and Atom syndication
feed formats. It supports both parsing and autodiscovery of feeds.

%package dev
Summary: dev components for the perl-XML-Feed package.
Group: Development
Provides: perl-XML-Feed-devel = %{version}-%{release}
Requires: perl-XML-Feed = %{version}-%{release}

%description dev
dev components for the perl-XML-Feed package.


%package license
Summary: license components for the perl-XML-Feed package.
Group: Default

%description license
license components for the perl-XML-Feed package.


%package perl
Summary: perl components for the perl-XML-Feed package.
Group: Default
Requires: perl-XML-Feed = %{version}-%{release}

%description perl
perl components for the perl-XML-Feed package.


%prep
%setup -q -n XML-Feed-0.63
cd %{_builddir}
tar xf %{_sourcedir}/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
cd %{_builddir}/XML-Feed-0.63
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/XML-Feed-0.63/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-Feed
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-XML-Feed/808cdef4c992763637fe5a5a7551c6cd5186080b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Feed.3
/usr/share/man/man3/XML::Feed::Content.3
/usr/share/man/man3/XML::Feed::Enclosure.3
/usr/share/man/man3/XML::Feed::Entry.3
/usr/share/man/man3/XML::Feed::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-Feed/808cdef4c992763637fe5a5a7551c6cd5186080b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
