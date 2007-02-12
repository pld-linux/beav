Summary:	A binary editor with Emacs-like keybindings
Summary(pl.UTF-8):	Binarny edytor z klawiszologią zbliżoną do Emacsa
Name:		beav
Version:	1.40
Release:	4
License:	GPL
Group:		Applications/Editors
Source0:	ftp://ftp.cdrom.com/pub/simtelnet/msdos/binaryed/%{name}140s.zip
# Source0-md5:	21ebeb1c2fb04ca9ef6dbae842cc1687
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-linux.patch
Patch2:		%{name}-tinfo.patch
BuildRequires:	ncurses-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beav allows you to edit binary files with almost all of the
capabilities of a screen editor. Beav can edit a file and/or do a
search and replace in hex, ASCII, EBCDIC, octal, decimal, and binary
modes. Data can be displayed in byte, word, or double word formats.
While displaying words or double words, the data can be displayed in
Intel's or Motorola's byte swap format. Data of any length can be
inserted at any point in the file and the source of the data can be
the keyboard, another buffer, or a file. Any displayed data can be
sent to a printer in the displayed format. Finally, Beav can even
handle files that are bigger than memory.

%description -l pl.UTF-8
Beav umożliwia edycję plików binarnych w trybie pełnoekranowym. Beav
potrafi modyfikować pliki, wyszukiwać i zastępować w trybach
heksadecymalnym, ASCII, EBCDIC, ósemkowym, dziesiętnym oraz binarnym.
Dane mogą być wyświetlane jako bajt, słowo lub podwójne słowo. Dane w
postaci słowa lub podwójnego słowa mogą być wyświetlone w formacie
Intela lub Motoroli ze zmienioną kolejnością bajtów. W dowolnym
miejscu pliku można wstawić dane dowolnej długości pochodzące z
klawiatury, innego bufora lub pliku. Dowolne wyświetlane dane mogą być
wysłane na drukarkę w wyświetlanym formacie. Beav jest w stanie
obsługiwać nawet pliki nawet większe niż rozmiar pamięci.


%prep
%setup -q -c -T
unzip -L -q -aa %{SOURCE0}

%patch1 -p1
%patch0 -p1
%patch2 -p1

%build
%{__make} -f makefile.uxv \
	CFLAGS="%{rpmcflags} -DUNIX -DSYSV %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install beav $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
