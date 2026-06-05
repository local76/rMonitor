```text
         __  ___            _ __            
   _____/  |/  /___  ____  (_) /_____  _____
  / ___/ /|_/ / __ \/ __ \/ / __/ __ \/ ___/
 / /  / /  / / /_/ / / / / / /_/ /_/ / /    
/_/  /_/  /_/\____/_/ /_/_/\__/\____/_/     
```

### 2. Doctor Diagnostic System (`--doctor` / `doctor`)
Runs a quick health check of the monitoring environment, checking execution privilege levels, registry access permissions, GPU hardware paths, and connection interfaces:
```powershell
.\rmon.exe --doctor
```

### 3. Native Windows Installation (`--install` / `install`)
Registers `rMonitor` under the user's `App Paths` registry entry (enabling execution via `Win + R` as `rmon`) and creates a shortcut in the Windows Start Menu programs folder (making it instantly searchable/launchable via the Start Menu):
```powershell
.\rmon.exe --install
```

---

## 📝 Error Logging
All runtime activities, errors, and system crashes (including panics) are automatically captured and logged silently to:
`%APPDATA%\rmonitor\rmonitor.log` (typically `C:\Users\<User>\AppData\Roaming\rmonitor\rmonitor.log`)

---

## 🛠️ Building From Source
Ensure you have the Rust compiler toolchain installed on Windows.

1. Clone the repository and navigate to the folder:
    ```powershell
    cd rMonitor
    ```
2. Build the release binary:
    ```powershell
    .\build.bat
    ```
    This will generate an optimized executable with embedded application resource icons directly at the root (`rmon.exe`).
