#!/usr/bin/env bash

if ! rpm -qa | grep rpmdevtools ; then #assume fresh VM so install dependencies
  sudo dnf install rpmdevtools rpmlint git greetd meson ninja-build qt6-qtbase-devel qt6-qtbase-private-devel qt6-qtwayland-devel json-devel libpng-devel mpv-devel qwlroots-devel wayland-devel -y
fi

if [ ! -d ~/rpmbuild ]; then #assume subfolders doen't exist either
  rpmdev-setuptree
fi

cp *.spec ~/rpmbuild/SPECS/

repos=("ipc" "applications" "login1" "utils" "wayqt" "qtgreet")

curdir=$(pwd)
for repo in "${repos[@]}"; do
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
  cd ..
  mv $specname $tagdir

  tar -cvf $tagdir.tar.gz $tagdir
  cp $tagdir.tar.gz ~/rpmbuild/SOURCES/
  cd ~

  sed -i "s/{{VERSION}}/$tagver/g" rpmbuild/SPECS/$specname.spec
  rpmbuild -ba rpmbuild/SPECS/$specname.spec
  sudo rpm -i rpmbuild/RPMS/x86_64/$tagdir-*.rpm
  cd $curdir
done
