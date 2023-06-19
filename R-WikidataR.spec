#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-WikidataR
Version  : 2.3.3
Release  : 43
URL      : https://cran.r-project.org/src/contrib/WikidataR_2.3.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/WikidataR_2.3.3.tar.gz
Summary  : Read-Write API Client Library for Wikidata
Group    : Development/Tools
License  : MIT
Requires: R-Hmisc
Requires: R-WikidataQueryServiceR
Requires: R-WikipediR
Requires: R-crayon
Requires: R-dplyr
Requires: R-httr
Requires: R-jsonlite
Requires: R-pbapply
Requires: R-progress
Requires: R-readr
Requires: R-stringr
Requires: R-tibble
BuildRequires : R-Hmisc
BuildRequires : R-WikidataQueryServiceR
BuildRequires : R-WikipediR
BuildRequires : R-crayon
BuildRequires : R-dplyr
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : R-pbapply
BuildRequires : R-progress
BuildRequires : R-readr
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
WikidataR
=========
An combined R package for reading, writing and handling Wikidata semantic data (via APIs).

%prep
%setup -q -c -n WikidataR
cd %{_builddir}/WikidataR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641148842

%install
export SOURCE_DATE_EPOCH=1641148842
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikidataR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikidataR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WikidataR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc WikidataR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/WikidataR/DESCRIPTION
/usr/lib64/R/library/WikidataR/INDEX
/usr/lib64/R/library/WikidataR/LICENSE
/usr/lib64/R/library/WikidataR/Meta/Rd.rds
/usr/lib64/R/library/WikidataR/Meta/features.rds
/usr/lib64/R/library/WikidataR/Meta/hsearch.rds
/usr/lib64/R/library/WikidataR/Meta/links.rds
/usr/lib64/R/library/WikidataR/Meta/nsInfo.rds
/usr/lib64/R/library/WikidataR/Meta/package.rds
/usr/lib64/R/library/WikidataR/NAMESPACE
/usr/lib64/R/library/WikidataR/NEWS
/usr/lib64/R/library/WikidataR/R/WikidataR
/usr/lib64/R/library/WikidataR/R/WikidataR.rdb
/usr/lib64/R/library/WikidataR/R/WikidataR.rdx
/usr/lib64/R/library/WikidataR/R/sysdata.rdb
/usr/lib64/R/library/WikidataR/R/sysdata.rdx
/usr/lib64/R/library/WikidataR/extdata/WD.globalvar.RDS
/usr/lib64/R/library/WikidataR/help/AnIndex
/usr/lib64/R/library/WikidataR/help/WikidataR.rdb
/usr/lib64/R/library/WikidataR/help/WikidataR.rdx
/usr/lib64/R/library/WikidataR/help/aliases.rds
/usr/lib64/R/library/WikidataR/help/paths.rds
/usr/lib64/R/library/WikidataR/html/00Index.html
/usr/lib64/R/library/WikidataR/html/R.css
/usr/lib64/R/library/WikidataR/tests/testthat.R
/usr/lib64/R/library/WikidataR/tests/testthat/test_geo.R
/usr/lib64/R/library/WikidataR/tests/testthat/test_gets.R
/usr/lib64/R/library/WikidataR/tests/testthat/test_search.R
