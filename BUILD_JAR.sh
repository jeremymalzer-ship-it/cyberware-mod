#!/bin/bash

echo ""
echo "╔════════════════════════════════════════╗"
echo "║   CYBERWARE MOD - JAR BUILD SCRIPT     ║"
echo "║         (Linux/Mac)                    ║"
echo "╚════════════════════════════════════════╝"
echo ""

echo "[1/3] Generiere Assets..."
python3 generate_all_assets.py

if [ $? -ne 0 ]; then
    echo "❌ Asset-Generierung fehlgeschlagen!"
    echo "Stelle sicher, dass Python 3 installiert ist."
    exit 1
fi

echo "✓ Assets generiert!"
echo ""
echo "[2/3] Kompiliere JAR..."
chmod +x gradlew
./gradlew clean build

if [ $? -ne 0 ]; then
    echo "❌ Build fehlgeschlagen!"
    echo "Prüfe die Fehlermeldung oben."
    exit 1
fi

echo "✓ Build erfolgreich!"
echo ""
echo "[3/3] Zeige JAR-Datei..."
ls -lh build/libs/*.jar

echo ""
echo "╔════════════════════════════════════════╗"
echo "║  ✅ JAR ERFOLGREICH ERSTELLT!          ║"
echo "╚════════════════════════════════════════╝"
echo ""
echo "📍 Deine JAR-Datei:"
echo "   build/libs/cyberware-1.0.0.jar"
echo ""
echo "📋 Nächste Schritte:"
echo "    1. Kopiere die JAR-Datei"
echo "    2. Füge sie zu ~/.minecraft/mods/ hinzu"
echo "    3. Minecraft starten"
echo ""

