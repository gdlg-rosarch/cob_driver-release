Name:           ros-indigo-cob-base-drive-chain
Version:        0.6.1
Release:        0%{?dist}
Summary:        ROS cob_base_drive_chain package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_base_drive_chain
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-canopen-motor
Requires:       ros-indigo-cob-generic-can
Requires:       ros-indigo-cob-srvs
Requires:       ros-indigo-cob-utilities
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-libntcan
Requires:       ros-indigo-libpcan
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-canopen-motor
BuildRequires:  ros-indigo-cob-generic-can
BuildRequires:  ros-indigo-cob-srvs
BuildRequires:  ros-indigo-cob-utilities
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-libntcan
BuildRequires:  ros-indigo-libpcan
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
This package contains classes that are able to control the platform of the
Care-O-Bot. This means to establish a CAN communication to drive and steering
motors of the platform and later send motion commands and receive motor
information.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 17 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Matthias Gruhler <mig@ipa.fhg.de> - 0.5.7-0
- Autogenerated by Bloom

