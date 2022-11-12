Name:		texlive-emp
Version:	23483
Release:	1
Summary:	"Encapsulate" MetaPost figures in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/emp
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Emp is a package for encapsulating MetaPost figures in LaTeX:
the package provides environments where you can place MetaPost
commands, and means of using that code as fragments for
building up figures to include in your document. So, with emp,
the procedure is to run your document with LaTeX, run MetaPost,
and then complete running your document in the normal way. Emp
is therefore useful for keeping illustrations in synchrony with
the text. It also frees you from inventing descriptive names
for PostScript files that fit into the confines of file system
conventions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/emp/emp.sty
%doc %{_texmfdistdir}/doc/latex/emp/COPYING
%doc %{_texmfdistdir}/doc/latex/emp/Makefile
%doc %{_texmfdistdir}/doc/latex/emp/README
%doc %{_texmfdistdir}/doc/latex/emp/emp.pdf
%doc %{_texmfdistdir}/doc/latex/emp/empman.pdf
#- source
%doc %{_texmfdistdir}/source/latex/emp/emp.drv
%doc %{_texmfdistdir}/source/latex/emp/emp.dtx
%doc %{_texmfdistdir}/source/latex/emp/emp.ins
%doc %{_texmfdistdir}/source/latex/emp/empman.drv

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
