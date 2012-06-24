Summary:	A binary editor with Emacs-like keybindings
Summary(pl):	Binarny edytor z klawiszologi� zbli�on� do Emacsa
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

%description -l pl
Beav umo�liwia edycj� plik�w binarnych w trybie pe�noekranowym. Beav
potrafi modyfikowa� pliki, wyszukiwa� i zast�powa� w trybach
heksadecymalnym, ASCII, EBCDIC, �semkowym, dziesi�tnym oraz binarnym.
Dane mog� by� wy�wietlane jako bajt, s�owo lub podw�jne s�owo. Dane w
postaci s�owa lub podw�jnego s�owa mog� by� wy�wietlone w formacie
Intela lub Motoroli ze zmienion� kolejno�ci� bajt�w. W dowolnym
miejscu pliku mo�na wstawi� dane dowolnej d�ugo�ci pochodz�ce z
klawiatury, innego bufora lub pliku. Dowolne wy�wietlane dane mog� by�
wys�ane na drukark� w wy�wietlanym formacie. Beav jest w stanie
obs�ugiwa� nawet pliki nawet wi�ksze ni� rozmiar pami�ci.


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
