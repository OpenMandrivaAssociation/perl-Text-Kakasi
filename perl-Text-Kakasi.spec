%define upstream_name    Text-Kakasi
Name:		perl-%{upstream_name}
Version:	2.04
Release:	8

Summary:	Perl binding for KAKASI the kanji kana simple inverter
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Text-Kakasi
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Text-Kakasi-2.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	kakasi-devel >= 2.3.1
BuildRequires:	kakasi-dict
Requires:	kakasi >= 2.3.1

%description
This module provides libkakasi interface for perl. libkakasi is a part
of KAKASI.
KAKASI is the language processing filter to convert Kanji characters
to Hiragana, Katakana or Romaji and may be helpful to read Japanese
documents.
More information about KAKASI is available at <http://kakasi.namazu.org/>.

%prep
%setup -q -n Text-Kakasi-2.04

%build
perl Makefile.PL INSTALLDIRS=vendor
make CFLAGS="%{optflags}"

%check
make test || :

%install
%makeinstall_std

%files
%doc COPYING README README.jp
%{_mandir}/*/*
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text

