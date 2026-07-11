%global tl_name xetex-tibetan
%global tl_revision 28847

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	XeTeX input maps for Unicode Tibetan
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/tibetan
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-tibetan.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-tibetan.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a map for use with Jonathan Kew's TECkit, to
translate Tibetan to Unicode (range 0F00-0FFF).

