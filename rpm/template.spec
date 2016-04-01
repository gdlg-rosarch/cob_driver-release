Name:           ros-indigo-cob-camera-sensors
Version:        0.6.6
Release:        0%{?dist}
Summary:        ROS cob_camera_sensors package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_camera_sensors
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       opencv-devel
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-cob-vision-utils
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-polled-camera
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
BuildRequires:  boost-devel
BuildRequires:  opencv-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-cob-vision-utils
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-polled-camera
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
For more information read the readme.htm file located in

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Apr 01 2016 Jan Fischer <jsf@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Jan Fischer <jsf@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Jan Fischer <jsf@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Jan Fischer <jsf@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Jan Fischer <jsf@ipa.fhg.de> - 0.5.7-0
- Autogenerated by Bloom

