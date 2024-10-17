Name:		texlive-xetex-tibetan
Version:	28847
Release:	2
Summary:	XeTeX input maps for Unicode Tibetan
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/tibetan
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-tibetan.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-tibetan.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a map for use with Jonathan Kew's TECkit,
to translate Tibetan to Unicode (range 0F00-0FFF).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-tibetan/loctib.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-tibetan/loctib.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-tibetan/wylie.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-tibetan/wylie.tec
%doc %{_texmfdistdir}/doc/xetex/xetex-tibetan/Changelog
%doc %{_texmfdistdir}/doc/xetex/xetex-tibetan/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
