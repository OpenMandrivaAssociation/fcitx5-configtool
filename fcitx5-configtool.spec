Name:		fcitx5-configtool
Version:	5.1.8
Release:	3
Source0:	https://github.com/fcitx/fcitx5-configtool/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Configuration tool for FCITX based input methods
URL:		https://github.com/fcitx/fcitx5-configtool
License:	GPL
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Fcitx5Core)
BuildRequires:	cmake(Fcitx5Config)
BuildRequires:	cmake(Fcitx5Qt6DBusAddons)
BuildRequires:	cmake(Fcitx5Qt6WidgetsAddons)
BuildRequires:	cmake(Fcitx5Utils)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6Package)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(XKBCommon)
BuildRequires:	pkgconfig(xkeyboard-config)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(iso-codes)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Configuration tool for FCITX based input methods

%files -f %{name}.lang
%{_bindir}/fcitx5-config-qt
%{_bindir}/fcitx5-migrator
%{_bindir}/fcitx5-plasma-theme-generator
%{_bindir}/kbd-layout-viewer5
%{_libdir}/libFcitx5Migrator.so*
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_fcitx5.so
%{_datadir}/applications/kbd-layout-viewer5.desktop
%{_datadir}/applications/kcm_fcitx5.desktop
%{_datadir}/applications/org.fcitx.fcitx5-config-qt.desktop
%{_datadir}/applications/org.fcitx.fcitx5-migrator.desktop
