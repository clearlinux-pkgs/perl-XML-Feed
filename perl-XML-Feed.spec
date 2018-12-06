#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Feed
Version  : 0.55
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/XML-Feed-0.55.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/XML-Feed-0.55.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-feed-perl/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
Summary  : 'XML Syndication Feed Support'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-Feed-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Class::ErrorHandler)
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Singleton)
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Format::Mail)
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(Exception::Class)
BuildRequires : perl(Feed::Find)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(HTML::Entities)
BuildRequires : perl(HTML::TokeParser)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Pluggable)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(URI::Fetch)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(XML::Atom)
BuildRequires : perl(XML::LibXML)
BuildRequires : perl(XML::RSS)
BuildRequires : perl(XML::XPath)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
$Id$
This is XML::Feed, an abstraction above the RSS and Atom syndication
feed formats. It supports both parsing and autodiscovery of feeds.

%package dev
Summary: dev components for the perl-XML-Feed package.
Group: Development
Provides: perl-XML-Feed-devel = %{version}-%{release}

%description dev
dev components for the perl-XML-Feed package.


%package license
Summary: license components for the perl-XML-Feed package.
Group: Default

%description license
license components for the perl-XML-Feed package.


%prep
%setup -q -n XML-Feed-0.55
cd ..
%setup -q -T -D -n XML-Feed-0.55 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/XML-Feed-0.55/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-Feed
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-XML-Feed/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed/Content.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed/Enclosure.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed/Entry.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed/Entry/Format/Atom.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed/Entry/Format/RSS.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed/Format/Atom.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed/Format/RSS.pm
/usr/lib/perl5/vendor_perl/5.28.1/XML/Feed/Util.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Feed.3
/usr/share/man/man3/XML::Feed::Content.3
/usr/share/man/man3/XML::Feed::Enclosure.3
/usr/share/man/man3/XML::Feed::Entry.3
/usr/share/man/man3/XML::Feed::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-Feed/deblicense_copyright
