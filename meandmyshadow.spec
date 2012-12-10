Name:		meandmyshadow
Summary:	Me and My Shadow is a puzzle/platform game
Version:	0.4
Release:	1
License:	GPLv3
Group:		Games/Arcade
URL:		http://meandmyshadow.sourceforge.net
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
BuildRequires:	pkgconfig(x11)
BuildRequires:	SDL_ttf-devel

%description
Me and My Shadow is a puzzle/platform game written by Luka Horvat.
The author has given us permission to GPL the game, and develop it further.
It has an interesting concept and rather unique gameplay.

%prep
%setup -q
%__sed -i s,"Version=.*",,g %{name}.desktop
%__sed -i s,"Categories=.*","Categories=Game;ArcadeGame;",g %{name}.desktop
find . -type f -exec chmod 0644 '{}' \;

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/meandmyshadow
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

