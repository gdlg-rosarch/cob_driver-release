# Script generated with Bloom
pkgdesc="ROS - The package cob_canopen_motor implements a controller-drive component which is connected to a can-bus and works with a canopen-interface. &quot;CanDriveItf&quot; provides a - more or less - generic interface to the controller-drive components. &quot;CanDrvie...&quot; then implements a specific setup, e.g. an ELMO Harmonica Controller in case of the &quot;CanDriveHarmonica&quot;."
url='http://ros.org/wiki/cob_canopen_motor'

pkgname='ros-kinetic-cob-canopen-motor'
pkgver='0.6.11_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cob-generic-can'
'ros-kinetic-cob-utilities'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-cob-generic-can'
'ros-kinetic-cob-utilities'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=cob_canopen_motor
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_canopen_motor $srcdir/cob_canopen_motor
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

