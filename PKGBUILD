# Script generated with Bloom
pkgdesc="ROS - This package implements the Care-O-bot mimic"
url='http://ros.org/wiki/cob_mimic'

pkgname='ros-kinetic-cob-mimic'
pkgver='0.6.11_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('boost'
'ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'vlc'
)

depends=('boost'
'ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'vlc'
)

conflicts=()
replaces=()

_dir=cob_mimic
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_mimic $srcdir/cob_mimic
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

