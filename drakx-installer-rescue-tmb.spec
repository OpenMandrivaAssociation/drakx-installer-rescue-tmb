%define name drakx-installer-rescue
%define version 1.12
%define release %mkrel 1

Summary: Rescue image
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-XML-Parser squashfs-tools mknod-m600
BuildRequires: ldetect-lst-devel
BuildRequires: hexedit grub telnet rsync openssh-clients ftp-client-krb5 kbd strace
BuildRequires: gpart parted partimage
BuildRequires: dump xfsdump eject testdisk extipl
BuildRequires: xfsprogs reiserfsprogs jfsprogs ntfsprogs dosfstools
BuildRequires: mdadm lvm2 dmraid
BuildRequires: setserial
BuildRequires: mt-st
BuildRequires: pciutils ldetect
BuildRequires: packdrake rpmtools
BuildRequires: vim-minimal
BuildRequires: drakx-installer-binaries drakxtools-backend drakx-kbd-mouse-x11
BuildRequires: bind-utils nfs-utils-clients wget
BuildRequires: ka-deploy-source-node
BuildRequires: cdialog
BuildRequires: ldetect-lst >= 0.1.222
BuildRequires: ntfs-3g

%description
rescue image

%prep
%setup -q

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
