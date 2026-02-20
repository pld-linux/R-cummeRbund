%define		packname	cummeRbund

Summary:	Analysis, exploration, manipulation, and visualization of Cufflinks high-throughput sequencing data
Name:		R-%{packname}
Version:	2.4.0
Release:	2
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	f6236638b8305fd6ac7c58bd5f9bb89d
URL:		http://bioconductor.org/packages/release/bioc/html/cummeRbund.html
BuildRequires:	R
BuildRequires:	R-BiocGenerics >= 0.3.2
BuildRequires:	R-Gviz
BuildRequires:	R-cran-fastcluster
BuildRequires:	R-cran-ggplot2
BuildRequires:	R-cran-plyr
BuildRequires:	R-cran-reshape2
BuildRequires:	R-cran-RSQLite
BuildRequires:	R-rtracklayer
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-BiocGenerics >= 0.3.2
Requires:	R-Gviz
Requires:	R-cran-fastcluster
Requires:	R-cran-ggplot2
Requires:	R-cran-plyr
Requires:	R-cran-reshape2
Requires:	R-cran-RSQLite
Requires:	R-rtracklayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows for persistent storage, access, exploration, and manipulation
of Cufflinks high-throughput sequencing data. In addition, provides
numerous plotting functions for commonly used visualizations.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/reports
