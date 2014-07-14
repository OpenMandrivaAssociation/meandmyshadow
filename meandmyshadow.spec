Summary:	Me and My Shadow is a puzzle/platform game
Name:		meandmyshadow
Version:	0.4.1
Release:	1
License:	GPLv3+
Group:		Games/Arcade
Url:		http://meandmyshadow.sourceforge.net
Source0:	https://sourceforge.net/projects/%{name}/files/%{version}/%{name}-%{version}-src.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(x11)

%description
Me and My Shadow is a puzzle/platform game written by Luka Horvat.
The author has given us permission to GPL the game, and develop it further.
It has an interesting concept and rather unique gameplay.

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/meandmyshadow
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
find . -type f -exec chmod 0644 '{}' \;

%build
%cmake
%make

%install
%makeinstall_std -C build

