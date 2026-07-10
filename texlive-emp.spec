%global tl_name emp
%global tl_revision 23483

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Encapsulate MetaPost figures in a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/emp
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Emp is a package for encapsulating MetaPost figures in LaTeX: the
package provides environments where you can place MetaPost commands, and
means of using that code as fragments for building up figures to include
in your document. So, with emp, the procedure is to run your document
with LaTeX, run MetaPost, and then complete running your document in the
normal way. Emp is therefore useful for keeping illustrations in
synchrony with the text. It also frees you from inventing descriptive
names for PostScript files that fit into the confines of file system
conventions.

