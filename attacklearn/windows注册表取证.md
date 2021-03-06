

嘿嘿，跟进文章，找到了一个黑客训练营，比较喜欢其中的标语：  Fools talk;  The Wise listen.

转自：https://www.hackers-arise.com/single-post/2016/10/21/Digital-Forensics-Part-5-Analyzing-the-Windows-Registry-for-Evidence



# 数字取证：第五部分：分析取证windows注册表

虽然几乎所有的微软Windows用户都知道他们的系统有一个注册表，但很少有人了解它的功能，甚至更少的人知道如何操作它以达到他们的目的。作为一名法医分析师，注册管理机构可以作为证据证明系统发生什么，何处，何时以及如何发生的宝藏。

 在本文中，我想帮助您了解Windows注册表的工作原理以及在有人使用系统生病或生病时留下的证据。

## 什么是注册表：

注册表是存储有关Windows系统上的用户，硬件和软件的配置信息的数据库。尽管注册表旨在配置系统，但要这样做，它会跟踪有关用户活动，连接到系统的设备，使用什么软件以及何时等等的大量信息。所有这些都可用于法医鉴定调查员追踪法医调查的人员，地点，地点和时间。在分析取证方面可以进行行为分析。

## 注册表根键值说明：

在注册表中，有根文件夹。这些根文件夹被称为配置单元。有五（5）个注册表配置单元。

- HKEY_USERS：包含所有已加载的用户配置文件

- HKEYCURRENT_USER：当前登录用户的配置文件

- HKEYCLASSES_ROOT：用于打开文件的应用程序的配置信息

- HKEYCURRENT_CONFIG：启动时系统的硬件配置文件

- HKEYLOCAL_MACHINE：配置信息，包括硬件和软件设置

  

## 注册表结构

注册表的结构与Windows目录/子目录结构非常相似。您有五个根密钥或配置单元，然后是子密钥。在某些情况下，您有子子项。这些子键然后具有显示在内容窗格中的描述和值。通常情况下，这些值仅为0或1，表示打开或关闭，但也可以包含通常以十六进制显示的更复杂的信息。 

![QQ图片20180603105924](img-storage\QQ图片20180603105924.png)



## 查看注册表

在我们自己的系统上（而不是取证模式），我们可以使用Windows内置的regedit实用程序访问注册表。只需在搜索窗口中键入regedit，然后点击它打开注册表编辑器，如下所示：

![QQ图片20180603110136](img-storage\QQ图片20180603110136.png)





## 注册表中的取证点：



可以在注册表中找到的信息包括：

- 用户和他们上次使用该系统的时间
- 最近使用过的软件
- 安装到系统的任何设备，包括闪存驱动器，硬盘驱动器，电话，平板电脑等的唯一标识符
- 当系统连接到特定的无线接入点时
- 什么和何时访问文件
- 列出在系统上完成的任何搜索
- 还有更多



## 注册表中进行无线数据取证

许多黑客破解本地无线接入点并将其用于入侵。通过这种方式，如果IP地址被跟踪，它将回到邻居或其他无线AP，而不是它们。

 

例如，在2012年1月，匿名成员John Borrell III袭击了盐湖城警察局和犹他州警察总长的电脑系统。联邦调查局被要求进行调查，并将黑客追溯到俄亥俄州托莱多的圣体教堂Wi-Fi无线接入点的IP地址。黑客显然破解了教堂无线接入点的密码，并用它在互联网上“匿名”攻击。

最终，联邦调查局能够通过各种调查技术找到嫌疑犯，这些调查技术大多是低技术，彻底的侦探工作。这有助于John Borrell在Twitter上吹嘘自己作为黑客的成功。最终，博列尔先生被判有罪，并在联邦监狱被判处两年徒刑。

 

当FBI追查Borrell先生并扣押他的电脑时，他们可以通过检查他的注册表来证明他已经连接到教堂AP。法医调查员只需在此处查看注册表：

 

**HKEY_LOCAL_MACHINE \ SOFTWARE \ Microsoft \ Windows NT \ CurrentVersion \ NetworkList \ Profiles**

 

在那里，您将找到机器连接到的无线接入点的**GUID列表**。当您点击其中一个时，它将显示包含SSID名称和上次以十六进制连接的日期的信息。因此，虽然博雷尔先生最初否认他参与这次黑客行为，但这些证据是确凿的，他最终认罪。

 

您可以在下面的屏幕截图中看到2014年11月举报者已连接到“HolidayInnColumbia”SSID。

![QQ图片20180603111002](img-storage\QQ图片20180603111002.png)





## 根据文档KEY,查看最近打开的文件

Windows注册表跟踪有关用户活动的大量信息。在大多数情况下，这些注册表项旨在使Windows更高效，更流畅地运行。作为分析取证人员，这些密钥就像用户或攻击者活动的路线图。

 

其中一个键是“RecentDocs”键。它通过文件扩展名跟踪系统中使用或打开的最新文档。它可以在：

 

**HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs** 

 

因此，例如，最近使用的Word文档可以在.doc或.docx扩展名下找到，具体取决于它们在其中创建的Word版本（每个键最多可容纳最后10个文档）。如果我们转到.docx扩展名，我们会看到此密钥下列出的最后10个Word文档。

![QQ图片20180603111429](img-storage\QQ图片20180603111429.png)



当我们点击其中一个键时，它会显示有关文档的信息，如下所示。我们可以在左边的十六进制和右边的ASCII中查看文档数据。在这种情况下，它表明该文档是Metasploit课程大纲。 



![QQ图片20180603111530](img-storage\QQ图片20180603111530.png)



在某些情况下，攻击者将上传.tar文件，因此这是查找违规证据的好地方。一般来说，Windows机器上不会看到.tar文件扩展名，所以在这里出现的条目需要进一步调查。检查.tar键中的文件，看看他们可能会透露有关攻击或攻击者的内容。 



![QQ图片20180603111729](img-storage\QQ图片20180603111729.png)

在民事或政策违规调查中，可以在各种图形文件扩展名（如.jpg，.gif或.png）中找到证据。 



## TypedURLs Key （url访问）

当用户在Internet Explorer中键入URL时，该值存储在注册表中：

 

- **HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\TypedURLs** 

   

当我们在注册表中打开该密钥时，它会列出用户使用IE访问的最后一个URL。这可能会揭示违规中使用的恶意恶意软件的来源，或者违反民事或政策违规类型的调查，可能会揭示用户在寻找/查看的内容。

 



![QQ图片20180603112052](img-storage\QQ图片20180603112052.png)

 

 

这些值将从urI1（最近的）到urI25（最早的）运行。

 

#### IP地址

####  

注册表还跟踪用户界面的IP地址。请注意，可能有许多接口，并且此注册表项可以跟踪每个接口的IP地址和相关信息。



**HKEY_LOCAL_MACHINE\System\Services\CurrentControlSet\services\Tcpip\Parameters\Interfaces** 



如下所示，我们可以找到分配给接口的IP地址，子网掩码以及DHCP服务器租用IP的时间。通过这种方式，我们可以判断犯罪嫌疑人在入侵或犯罪时是否使用了该特定IP



![QQ图片20180603112246](img-storage\QQ图片20180603112246.png)



## 启动项在注册表中的取证

作为分析取证人员，我们经常需要找到在系统启动时要启动的应用程序或服务。每次系统重新启动以防止攻击者连接时，恶意软件通常会设置为启动。这些信息可以位于注册表中几十个位置。我们将只看几个最常用的键。

 

可能最常用的位置是：



**HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run** 



![QQ图片20180603112508](img-storage\QQ图片20180603112508.png)



每次系统启动时，这些子项中指定的任何软件/位置都将启动。Rootkit和其他恶意软件通常可以在这里找到，并且每次系统启动时都会启动。 



**RunOnce Startup  （一次性自启动）**



如果黑客只是想让软件在启动时运行一次，那么可以在这里设置子项。 



- **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce** 



## 自启动服务项：



下面的键列出了在系统启动时启动的所有服务。如果密钥设置为2，服务将自动启动; 如果设置为3，则必须手动启动服务; 并且如果该密钥设置为4，则该服务被禁用。 



**HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services** 



## Start Legacy Applications （低版本应用程序）

在运行遗留16位应用程序时，将运行所列出的程序。 



**HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\WOW** 



## 特殊用户登陆时启动

在下面的键中，当特定用户登录时，将运行这些值 





- **HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run** 



## 硬件注册表记录

通常，嫌疑人将使用闪存驱动器或硬盘驱动器进行恶意活动，然后将其删除，以免留下任何证据。然而，熟练的法医调查人员仍然可以在注册表内找到这些存储设备的证据痕迹，如果他们知道去哪里寻找。

 

Windows系统上的注册表在各个版本之间会有所不同。熟练的专业数字取证调查员需要能够使用几乎所有版本的Windows和其他操作系统。由于Windows 7仍然是使用最广泛的操作系统，迄今为止，我将在其上进行演示。请记住，不同版本之间会有所不同。



- ### USB设备

  想象一下，我们怀疑有人安装了键盘记录器或者使用USB驱动器删除了机密信息。我们如何找到USB存储设备插入和使用的证据？要找到USB存储设备的证据，我们希望看看下面的关键。 

  **HK_Local_Machine\System\ControlSet00x\Enum\USBSTOR** 

  在这个键中，我们会找到任何连接到此系统的USB存储设备的证据。展开USBSTOR以查看连接到此系统的每个USB存储设备的列表。 

  ![QQ图片20180603114026](img-storage\QQ图片20180603114026.png)

  在上面的屏幕截图中，我圈出了一个可疑的USB设备。当我们扩展它时，它会显示该设备的唯一标识符。通过点击这个标识符，我们可以找到关于该设备的更多信息。 

  

  ![QQ图片20180603114146](img-storage\QQ图片20180603114146.png)

  正如您在上面的屏幕截图中看到的那样，当我们单击USB存储标识符时，它会在右侧窗口中显示全局唯一标识符（GUID），友好名称和硬件ID等等。这可能正是我们需要将嫌疑人与他们在这个系统上的活动联系起来的证据！ 

  

  

  

#### 已安装的设备



如果嫌疑人使用任何必须安装的硬件设备读取或写入数据（CD-ROM，DVD，硬盘驱动器，闪存驱动器等），注册表将记录挂载的设备。这些信息存储在： 



**HKEY_LOCAL_MACHINE\System\MountedDevices** 



正如你在下面看到的，当我们点击这个键时，它为我们提供了在该机器上安装的每一个设备的长列表。 

![QQ图片20180603113800](img-storage\QQ图片20180603113800.png)

如果我们需要关于这些装载设备的更多信息，我们可以简单地点击它，它会打开一个小应用程序，使我们能够读取ASCII数据。如您所见，此设备是Teac制造的IDE CD-ROM。 



![QQ图片20180603115414](img-storage\QQ图片20180603115414.png)



如果系统中没有TEAC CD_ROM，法医调查人员现在知道他们需要找到这个硬件来寻找进一步的犯罪证据。

 

注册表是存储大量有关Windows系统上发生的事件的信息的存储库，通过学习我们的方式，我们可以重新构建它所用的犯罪要素。