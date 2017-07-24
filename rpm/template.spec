Name:           ros-indigo-cob-sound
Version:        0.6.10
Release:        0%{?dist}
Summary:        ROS cob_sound package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_sound
Source0:        %{name}-%{version}.tar.gz

Requires:       alsa-oss
Requires:       libvlc-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-cob-srvs
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-visualization-msgs
Requires:       vlc
BuildRequires:  libvlc-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-srvs
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-visualization-msgs
BuildRequires:  vlc

%description
This package implements a sound play module using text2wave and aplay through
python.

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
* Mon Jul 24 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.8-0
- Autogenerated by Bloom

* Sat Apr 02 2016 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

