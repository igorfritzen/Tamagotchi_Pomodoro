[Setup]
AppId={{04720097-C12B-49C9-A8CC-4FDB8305E989}
AppName=Tamagotchi Pomodoro
AppVersion=0.1.0
AppPublisher=Igor Fritzen
AppPublisherURL=https://github.com/igorfritzen/Tamagotchi_Pomodoro
DefaultDirName={autopf}\Tamagotchi Pomodoro
DefaultGroupName=Tamagotchi Pomodoro
DisableProgramGroupPage=yes
OutputDir=installer_output
OutputBaseFilename=TamagotchiPomodoro-Setup-0.1.0
SetupIconFile=assets\icon.ico
UninstallDisplayIcon={app}\TamagotchiPomodoro.exe
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
WizardStyle=modern

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "Criar um atalho na área de trabalho"; GroupDescription: "Atalhos:"; Flags: unchecked

[Files]
Source: "dist\TamagotchiPomodoro\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\Tamagotchi Pomodoro"; Filename: "{app}\TamagotchiPomodoro.exe"
Name: "{autodesktop}\Tamagotchi Pomodoro"; Filename: "{app}\TamagotchiPomodoro.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\TamagotchiPomodoro.exe"; Description: "Abrir o Tamagotchi Pomodoro"; Flags: nowait postinstall skipifsilent
