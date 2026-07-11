%global tl_name uebungsblatt
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.0
Release:	%{tl_revision}.1
Summary:	A LaTeX class for writing exercise sheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uebungsblatt
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uebungsblatt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uebungsblatt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a LaTeX class for writing exercise sheets for a
lecture. Features: - quick typesetting of exercise sheets or their
revisions, - simple user friendly commands, - elegant page formatting, -
automatic numbering of exercises and sub-exercises, - the number of the
exercise sheet is extracted automatically from the file name, - static
information about the lectures and the authors needs to provided at one
point only.

