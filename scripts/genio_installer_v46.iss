; [INSTALLER] GENIO LLM v46.0 - SOTA VIP
; Inno Setup Script

[Setup]
AppName=Genio LLM Sovereign AI
AppVersion=46.0
DefaultDirName={autopf}\GenioLLM
DefaultGroupName=Genio LLM
OutputBaseFilename=GenioLLM_SOTA_VIP_Install
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin

[Files]
Source: ".\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs
; Exclude .panda and private docs in real distribution via Flags

[Icons]
Name: "{group}\Genio LLM Launcher"; Filename: "{app}\genio_launcher_GL.py"; IconFilename: "{app}\icon.ico"
Name: "{commondesktop}\Genio LLM"; Filename: "{app}\genio_launcher_GL.py"; IconFilename: "{app}\icon.ico"

[Run]
Filename: "{app}\scripts\wizard_config_v46.py"; Description: "Optimizing for your hardware..."; Flags: postinstall runascurrentuser
Filename: "{app}\genio_launcher_GL.py"; Description: "Launch Genio LLM"; Flags: postinstall nowait
