# Script generated with Bloom
pkgdesc="ROS - This package contains classes that are able to control the platform of the Care-O-Bot. This means to establish a CAN communication to drive and steering motors of the platform and later send motion commands and receive motor information."
url='http://ros.org/wiki/cob_base_drive_chain'

pkgname='ros-kinetic-cob-base-drive-chain'
pkgver='0.6.11_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cob-canopen-motor'
'ros-kinetic-cob-generic-can'
'ros-kinetic-cob-utilities'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
)

depends=('ros-kinetic-cob-canopen-motor'
'ros-kinetic-cob-generic-can'
'ros-kinetic-cob-utilities'
'ros-kinetic-control-msgs'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
)

conflicts=()
replaces=()

_dir=cob_base_drive_chain
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_base_drive_chain $srcdir/cob_base_drive_chain
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

