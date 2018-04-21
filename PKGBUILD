# Script generated with Bloom
pkgdesc="ROS - The cob_driver stack includes packages that provide access to the Care-O-bot hardware through ROS messages, services and actions. E.g. for mobile base, arm, camera sensors, laser scanners, etc..."
url='http://ros.org/wiki/cob_driver'

pkgname='ros-kinetic-cob-driver'
pkgver='0.6.11_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-cob-base-drive-chain'
'ros-kinetic-cob-bms-driver'
'ros-kinetic-cob-camera-sensors'
'ros-kinetic-cob-canopen-motor'
'ros-kinetic-cob-elmo-homing'
'ros-kinetic-cob-generic-can'
'ros-kinetic-cob-light'
'ros-kinetic-cob-mimic'
'ros-kinetic-cob-phidgets'
'ros-kinetic-cob-relayboard'
'ros-kinetic-cob-scan-unifier'
'ros-kinetic-cob-sick-lms1xx'
'ros-kinetic-cob-sick-s300'
'ros-kinetic-cob-sound'
'ros-kinetic-cob-undercarriage-ctrl'
'ros-kinetic-cob-utilities'
'ros-kinetic-cob-voltage-control'
)

conflicts=()
replaces=()

_dir=cob_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_driver $srcdir/cob_driver
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

