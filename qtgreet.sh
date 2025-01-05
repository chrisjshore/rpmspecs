#!/usr/bin/env bash

if ! rpm -qa | grep rpmdevtools ; then
	#assume fresh VM, install dependencies
	sudo dnf install rpmdevtools rpmlint git greetd meson ninja-build qt6-qtbase-devel qt6-qtbase-private-devel qt6-qtwayland-devel qwlroots-devel wayland-devel libpng-devel json-devel mpv-devel -y
fi

if [ ! -d ~/rpmbuild ]; then
  #assume subfolders doen't exist either
  rpmdev-setuptree
fi

cp *.spec ~/rpmbuild/SPECS/

curdir=$(pwd)
#library repos qtgreet is dependent on
#librepos=("ipc" "applications" "login1" "utils" "wayqt")
repos=("ipc" "applications" "login1" "utils" "wayqt" "qtgreet")

for repo in "${repos[@]}"; do
  #specname=libdfl-$repo-qt6
  specname=$(ls *$repo*.spec | cut -d "." -f1 )
  if [ "$repo" == "qtgreet" ]; then
    git clone https://gitlab.com/marcusbritanicus/$repo.git $specname
  else
    git clone https://gitlab.com/desktop-frameworks/$repo.git $specname
  fi
  cd $specname

  git checkout $(git describe --abbrev=0 --tags)
  tagver=$(git describe --abbrev=0 --tags | tr -d 'a-z')
  tagdir=$specname-$tagver
  #mkdir ../$libdir
  #mkdir ../libdfl-$repo-qt6-$tagver
  #cp -ra * !$
  cd ..
  mv $specname $tagdir

  tar -cvf $tagdir.tar.gz $tagdir
  #tar -cvf libdfl-$repo-qt6-$tagver.tar.gz libdfl-$repo-qt6-$tagver
  cp $tagdir.tar.gz ~/rpmbuild/SOURCES/
  #cp libdfl-$repo-qt6-$tagver.tar.gz ~/rpmbuild/SOURCES/
  cd ~

  sed -i "s/{{VERSION}}/$tagver/g" rpmbuild/SPECS/$specname.spec
  rpmbuild -ba rpmbuild/SPECS/$specname.spec
  sudo rpm -i rpmbuild/RPMS/x86_64/$tagdir-*.rpm
  cd $curdir
done

