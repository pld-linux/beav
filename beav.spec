Summary:	A binary editor with Emacs-like keybindings
Summary(pl):	Binarny edytor z klawiszologi± zbli¿on± do Emacsa
Name:		beav
Version:	1.40
Release:	1
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	ftp://ftp.cdrom.com/pub/simtelnet/msdos/binaryed/%{name}140s.zip
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-linux.patch
Patch2:		%{name}-tinfo.patch
BuildRequires:	unzip
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beav allows you to edit binary files with almost all of the
capabilities of a screen editor. Beav can edit a file and/or do a
search and replace in hex, ASCII, EBCDIC, octal, decimal, and binary
modes. Data can be displayed in byte, word, or double word formats.
While displaying words or double words, the data can be displayed in
Intel's or Motorola's byte swap format. Data of any length can be
inserted at any point in the file and the source of the data can be
the keyboard, another buffer, or a file. Any displayed data can be
sent to a printer in the displayed format. Finally, beav can even
handle files that are bigger than memory.

%description -l pl
Beav pozwala Ci edytoraæ pliki binarne w trybie pe³noekranowym. Beav
potrafi edytowaæ pliki, wyszukiwaæ i zastêpowaæ w trybach
heksadecymalnym, ASCII, EBCDIC, ósemkowym, dziesiêtnym oraz binarnym.
Dane mog± byæ wy¶wietlane jako bajt, word lub double. Dane word oraz
double word dane mog± byæ wy¶wietlane w formacie ,,byte swap'' Intela
lub Motorolli. Beav potrafi edytowaæ pliki o wielko¶ci wiêkszej ni¿
dostêpna fizycznie pamiêæ.

%prep
%setup -q -T -c
unzip -L -q -aa %{SOURCE0}

%patch1 -p1 -b glibc 
%patch0 -p1 -b linux
%patch2 -p1 -b tinfo

%build
%{__make} -f makefile.uxv \
	CFLAGS="%{rpmcflags} -DUNIX -DSYSV %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install beav $RPM_BUILD_ROOT%{_bindir}

gzip -9nf *.txt

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
