%define upstream_name    Text-Kakasi
%define upstream_version 2.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl binding for KAKASI the kanji kana simple inverter
License:    GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-devel
BuildRequires:  kakasi-devel >= 2.3.1
BuildRequires:  kakasi-dict
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       kakasi >= 2.3.1

%description
This module provides libkakasi interface for perl. libkakasi is a part
of KAKASI.
KAKASI is the language processing filter to convert Kanji characters
to Hiragana, Katakana or Romaji and may be helpful to read Japanese
documents.
More information about KAKASI is available at <http://kakasi.namazu.org/>.


%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README README.jp
%{_mandir}/*/*
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
