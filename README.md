<div align="middle">
<img height="200" src= "https://i.postimg.cc/3R2m4Vjq/s-Block-4.png"/>
</div>
<div align="left"> <h3>Description</h3></div>
<h><p align="left"> 

*sFirewall* is a Python-based application built using the Tkinter library, designed to enhance the security of computer systems or networks. With an intuitive graphical user interface (GUI), this app empowers users to configure and manage firewall rules seamlessly.</p></h>
<div align="left"> <h3>Use Case</h3></div>

⦁ **Network Security**: Protects networks from unauthorized access and malicious activity.<br>
⦁ **System Administration**: Helps system administrators manage network traffic and security.<br>
⦁ **Active Connections**: Displays real-time network activity and connection details.<br>

<div align="left"> <h3>Features</h3></div>

**Domain Blocking**: Prevent access to specific domains known for malicious content or phishing attempts.<br>

This section allows users to block or unblock specific domain names.<br>

Input Field:<br>
⦁ Label: Domain Name<br>
⦁ Purpose: Enter the domain to be blocked or unblocked (e.g., example.com)<br>

Buttons:<br>
⦁ Block Domain: Initiates blocking of the entered domain<br>
⦁ Unblock Domain: Removes the domain from the block list<br>
##
**IP Address Filtering**: Restrict inbound or outbound traffic from certain IP addresses to safeguard against cyberattacks.<br>

Used to block or unblock specific IP addresses and ports.<br>

⦁ Input Fields:<br>
⦁ IP Address: Enter the target IP (e.g., 192.168.1.1)<br>
⦁ Port: Specify the port number (e.g., 443)<br>

Dropdown Menu:<br>
⦁ Label: Protocol<br>
⦁ Options: TCP is selected; may include UDP or others<br>

Buttons:<br>
⦁ Block IP: Blocks the specified IP and port using the selected protocol<br>
⦁ Unblock IP: Removes the IP from the block list<br>
##
**Application Control**: Disable specific applications that pose security risks, such as untrusted or outdated software.<br>

Allows blocking of specific applications by their file path.<br>

⦁ Input Field:<br>
⦁ Label: Application Path<br>
⦁ Purpose: Enter the full path to the executable (e.g., C:\Program Files\App\App.exe)<br>

Buttons:<br>
⦁ Block App: Prevents the app from accessing the network<br>
⦁ Unblock App: Restores network access for the app<br>
##
**Active Connections Section**: Displays real-time network activity and connection details.

Large Text Area: Shows a list of active connections with the following attributes:<br>

⦁ Local Address & Port: IP and port on the user's machine<br>
⦁ Remote Address & Port: IP and port of the external connection<br>
⦁ Status: Connection state (e.g., ESTABLISHED, TIME_WAIT)<br>
⦁ Process Name: Executable using the connection (e.g., svchost.exe, msedge.exe, MSTeams.exe)<br>
⦁ Protocol: Typically TCP<br>

Examples from the list:<br>

⦁ svchost.exe — common Windows service host<br>
⦁ msedge.exe — Microsoft Edge browser<br>
⦁ MsEdgeWebView2.exe — WebView component used by Edge-based apps<br>
⦁ MSTeams.exe — Microsoft Teams<br>
⦁ CentralService.exe — possibly a custom or third-party service<br>

*The Active Connections panel is especially useful for monitoring suspicious or unknown processes in real time.*<br>
*The interface is functional and minimalistic, likely built for utility rather than aesthetics.*<br>
<div align="left"> <h3>Preview</h3></div>

![Screenshot](https://i.postimg.cc/SNfvMWzt/Screenshot-2025-04-24-101602.png)

<div align="left"> <h3>Installation</h3></div>

Install the **.exe** file from the release section.<br>

Install using **Winget** Command.<br>
```
winget install --id=SwastikSagar.sFirewall.PreRelease -e
```

<div align="left"> <h3>Requirements</h3></div>

- *Python 3.12+*
- *Windows OS*
