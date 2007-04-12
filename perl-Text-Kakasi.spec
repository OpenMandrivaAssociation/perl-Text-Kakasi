%define module  Text-Kakasi
%define name    perl-%{module}
%define version 2.04
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl binding for KAKASI the kanji kana simple inverter
License:        GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{version}.tar.bz2
Requires:       kakasi >= 2.3.1
BuildRequires:  perl-devel
BuildRequires:  kakasi-devel >= 2.3.1
BuildRequires:  kakasi-dict
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides libkakasi interface for perl. libkakasi is a part
of KAKASI.
KAKASI is the language processing filter to convert Kanji characters
to Hiragana, Katakana or Romaji and may be helpful to read Japanese
documents.
More information about KAKASI is available at <http://kakasi.namazu.org/>.


%prep
%setup -q -n %{module}-%{version} 

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

