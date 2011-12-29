# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/uebungsblatt
# catalog-date 2008-08-24 14:43:48 +0200
# catalog-license lppl
# catalog-version v1.5.0
Name:		texlive-uebungsblatt
Version:	v1.5.0
Release:	1
Summary:	A LaTeX class for writing exercise sheets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uebungsblatt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uebungsblatt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uebungsblatt.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a LaTeX class for writing exercise
sheets for a lecture. Features: - quick typesetting of exercise
sheets or their revisions, - simple user friendly commands, -
elegant page formatting, - automatic numbering of exercises and
sub-exercises, - the number of the exercise sheet is extracted
automatically from the file name, - static information about
the lectures and the authors needs to provided at one point
only.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uebungsblatt/uebungsblatt.cls
%{_texmfdistdir}/tex/latex/uebungsblatt/uebungsblatt.sty
%doc %{_texmfdistdir}/doc/latex/uebungsblatt/README
%doc %{_texmfdistdir}/doc/latex/uebungsblatt/history.txt
%doc %{_texmfdistdir}/doc/latex/uebungsblatt/uebungsblatt-doc.pdf
%doc %{_texmfdistdir}/doc/latex/uebungsblatt/uebungsblatt-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
