Name:		meandmyshadow
Summary:	Me and My Shadow is a puzzle/platform game
Version:	0.2
Release:	%mkrel 1
License:	GPLv3
Group:		Games/Arcade
URL:		http://meandmyshadow.sourceforge.net
Source0:	https://sourceforge.net/projects/%{name}/files/%{version}/%{name}-%{version}-src.tar.gz
Patch0:		meandmyshadow-0.2-install.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	curl-devel
BuildRequires:	libarchive-devel
BuildRequires:	cmake

%description
Me and My Shadow is a puzzle/platform game written by Luka Horvat.
The author has given us permission to GPL the game, and develop it further.
It has an interesting concept and rather unique gameplay.

%prep
%setup -q
%patch0 -p1
%__sed -i s,"Version=.*",,g %{name}.desktop
%__sed -i s,"Categories=.*","Categories=Game;ArcadeGame;",g %{name}.desktop

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc License Controls.txt
%{_bindir}/meandmyshadow
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

