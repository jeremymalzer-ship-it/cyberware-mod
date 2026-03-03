@echo off
color 0A
echo.
echo ╔════════════════════════════════════════╗
echo ║   CYBERWARE MOD - JAR BUILD SCRIPT     ║
echo ║           (Windows)                    ║
echo ╚════════════════════════════════════════╝
echo.

echo [1/3] Generiere Assets...
python generate_all_assets.py

if %ERRORLEVEL% neq 0 (
    echo ❌ Asset-Generierung fehlgeschlagen!
    echo Stelle sicher, dass Python 3 installiert ist.
    pause
    exit /b 1
)

echo ✓ Assets generiert!
echo.
echo [2/3] Kompiliere JAR...
call gradlew clean build

if %ERRORLEVEL% neq 0 (
    echo ❌ Build fehlgeschlagen!
    echo Prüfe die Fehlermeldung oben.
    pause
    exit /b 1
)

echo ✓ Build erfolgreich!
echo.
echo [3/3] Zeige JAR-Datei...
dir build\libs\*.jar

echo.
echo ╔════════════════════════════════════════╗
echo ║  ✅ JAR ERFOLGREICH ERSTELLT!          ║
echo ╚════════════════════════════════════════╝
echo.
echo 📍 Deine JAR-Datei:
echo    build\libs\cyberware-1.0.0.jar
echo.
echo 📋 Nächste Schritte:
echo    1. Kopiere die JAR-Datei
echo    2. Füge sie zu .minecraft\mods\ hinzu
echo    3. Minecraft starten
echo.
pause
