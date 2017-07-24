Name:           ros-kinetic-cob-sick-s300
Version:        0.6.10
Release:        0%{?dist}
Summary:        ROS cob_sick_s300 package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_sick_s300
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs

%description
This package published a laser scan message out of a Sick S300 laser scanner.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jul 24 2017 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

