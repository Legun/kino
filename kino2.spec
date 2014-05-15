Summary:    Simple non-linear video editor
Name:       kino
Version:    1.3.4
Release:    1%{?dist}
License:    GPL
Source0:    http://downloads.sourceforge.net/kino/%{name}-%{version}.tar.gz
Group:      Applications/Multimedia
Url:        http://www.kinodv.org/
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:   gtk2, mjpegtools, mencoder, mplayer
%{?_with_extffmpeg:Requires: ffmpeg}
Obsoletes: kino-devel <= %{version}
Obsoletes: kino-dvtitler <= 0.2.0-2

%description
The new generation of digital camcorders use the Digital Video (DV) data
format. Kino allows you to record, create, edit, and play movies recorded
with DV camcorders. Unlike other editors, this program uses many keyboard
commands for fast navigating and editing inside the movie.


%prep
%setup -q -n "%{name}-%{version}"

%build

%install
rm -rf %{buildroot}

%__mkdir -p %buildroot/%{_bindir}/
%__mkdir -p %buildroot/%{_includedir}/
%__mkdir -p %buildroot/%{_libdir}/
%__mkdir -p %buildroot/%{_datadir}/
%__mkdir -p %buildroot/%{_sysconfdir}

cp -a usr/bin/* %buildroot/%{_bindir}/
cp -a usr/include/* %buildroot/%{_includedir}/
cp -a usr/lib/* %buildroot/%{_libdir}/
cp -a usr/share/* %buildroot/%{_datadir}/
cp -a etc/* %buildroot/%{_sysconfdir}


find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%post

if test -e /usr/include/linux/videodev.h; then
echo 'no necesario crear enlace simbolico'
else
cd /usr/include/linux/
ln -s videodev2.h videodev.h
fi


%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc %{_datadir}/doc/*
%doc %{_mandir}/man1/ffmpeg-kino.1*
%doc %{_mandir}/man1/kino.1*
%doc %{_mandir}/man1/kino2raw.1*
%{_sysconfdir}/udev/rules.d/kino.rules
%{_bindir}/ffmpeg-kino
%{_bindir}/kino.bin
%{_bindir}/kino
%{_bindir}/kino2raw
%{_datadir}/applications/Kino.desktop
%{_datadir}/kino/
%{_datadir}/mime/packages/kino.xml
%{_datadir}/pixmaps/kino.png
%{_datadir}/locale/*
%{_includedir}/kino/
%{_libdir}/kino-gtk2/*





%changelog
*Mon Jan 23 2012 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.3.4
- Initial rpm for new version
