%define upstream_name    Text-Kakasi
%define upstream_version 2.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl binding for KAKASI the kanji kana simple inverter
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc COPYING README README.jp
%{_mandir}/*/*
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text

%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 2.40.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.40.0-2mdv2011.0
+ Revision: 556173
- rebuild for perl 5.12

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.40.0-1mdv2010.0
+ Revision: 405710
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.04-7mdv2009.0
+ Revision: 258617
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.04-6mdv2009.0
+ Revision: 246632
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.04-4mdv2008.1
+ Revision: 152330
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-3mdv2008.0
+ Revision: 67087
- rebuild


* Mon Jul 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-2mdv2007.0
- spec cleanup
- fix directory ownership

* Fri May 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.04-1mdk
- 2.04

* Wed Nov 17 2004 Michael Scherer <misc@mandrake.org> 1.05-7mdk
- Rebuild for new perl

