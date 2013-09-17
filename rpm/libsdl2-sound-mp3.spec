Summary: Simple DirectMedia Layer - Sound File Decoding Library
Name: SDL2_sound
Version: 1.0.1
Release: 1
Source: %{name}-%{version}.tar.gz
URL: http://icculus.org/SDL_sound/
License: LGPL
Group: Development/Libraries
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(flac)

%description
SDL_sound is a library that handles the decoding of several popular sound file
formats, such as .WAV and .MP3. It is meant to make the programmer's sound
playback tasks simpler. The programmer gives SDL_sound a filename, or feeds it
data directly from one of many sources, and then reads the decoded waveform
data back at her leisure.

SDL_sound can also handle sample rate, audio format, and channel conversion
on-the-fly and behind-the-scenes, if the programmer desires. 

%package devel
Summary: Simple DirectMedia Layer - Sound File Decoding Library (Development)
Group: Development/Libraries
Requires: %{name}

%description devel
SDL_sound is a library that handles the decoding of several popular sound file
formats, such as .WAV and .MP3. It is meant to make the programmer's sound
playback tasks simpler. The programmer gives SDL_sound a filename, or feeds it
data directly from one of many sources, and then reads the decoded waveform
data back at her leisure.

SDL_sound can also handle sample rate, audio format, and channel conversion
on-the-fly and behind-the-scenes, if the programmer desires. 

%prep
%setup -q

%build
%configure --disable-static
make

%install
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.txt CHANGELOG.txt CREDITS.txt LICENSE.txt TODO.txt
%{_bindir}/*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGELOG.txt CREDITS.txt LICENSE.txt TODO.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h

