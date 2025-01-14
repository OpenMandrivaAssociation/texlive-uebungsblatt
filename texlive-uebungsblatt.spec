Name:		texlive-uebungsblatt
Version:	15878
Release:	2
Summary:	A LaTeX class for writing exercise sheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uebungsblatt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uebungsblatt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uebungsblatt.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
