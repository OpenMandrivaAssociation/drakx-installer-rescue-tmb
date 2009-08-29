%define base_name drakx-installer-rescue
%define name %{base_name}-tmb
%define version 1.14
%define release %mkrel 2

Summary: Rescue image adapted for kernel-tmb
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{base_name}-%{version}.tar.bz2
Patch0:  %{base_name}-reiser4.patch
Patch1:  %{base_name}-ext4.patch
Patch2:  %{base_name}-tmb.patch
License: GPL
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-XML-Parser squashfs3-tools mknod-m600
BuildRequires: ldetect-lst-devel
BuildRequires: hexedit grub telnet rsync openssh-clients ftp-client-krb5 kbd strace
BuildRequires: gpart parted partimage
BuildRequires: dump xfsdump eject testdisk extipl
BuildRequires: xfsprogs reiserfsprogs jfsprogs ntfsprogs dosfstools reiser4progs
BuildRequires: mdadm lvm2 dmraid
BuildRequires: setserial
BuildRequires: mt-st
BuildRequires: pciutils ldetect
BuildRequires: packdrake rpmtools
BuildRequires: vim-minimal
BuildRequires: drakx-installer-binaries-tmb drakxtools-backend drakx-kbd-mouse-x11
BuildRequires: bind-utils nfs-utils-clients wget
BuildRequires: ka-deploy-source-node
BuildRequires: cdialog
BuildRequires: ldetect-lst >= 0.1.222
BuildRequires: ntfs-3g
BuildRequires: cryptsetup photorec quota
BuildRequires: pv

%description
Rescue image based on kernel-tmb

%prep
%setup -q -n %{base_name}-%{version}
%patch0 -p1 -b .reiser4
%patch1 -p1 -b .ext4
%patch2 -p1 -b .tmb

%build
make -C rescue

%install
rm -rf $RPM_BUILD_ROOT

dest=$RPM_BUILD_ROOT%{_libdir}/%name
mkdir -p $dest
cp -r rescue/rescue.sqfs $dest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/%name
