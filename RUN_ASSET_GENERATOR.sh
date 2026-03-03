#!/bin/bash
echo "🎨 CYBERWARE MOD - ASSET GENERATOR"
echo "===================================="
echo ""
echo "Dieses Script erstellt automatisch:"
echo "✓ 50+ PNG-Texturen (16x16)"
echo "✓ 50+ JSON-Modelle"
echo "✓ Alle Item-Assets"
echo ""
echo "Anforderung: Python 3 + PIL"
echo ""

# Prüfe ob Python 3 installiert ist
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 nicht gefunden!"
    echo "Bitte installieren: sudo apt install python3 python3-pip"
    echo "Oder: https://www.python.org/downloads/"
    exit 1
fi

# Prüfe ob PIL installiert ist
python3 -c "from PIL import Image" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  PIL nicht gefunden, installiere..."
    pip3 install Pillow --break-system-packages
fi

echo ""
echo "▶️  Starte Asset-Generator..."
echo ""

cd "$(dirname "$0")"
python3 generate_all_assets.py

echo ""
echo "✅ Fertig!"
echo ""
echo "Nächste Schritte:"
echo "1. gradle clean build"
echo "2. gradle runClient"
echo "3. Items im Inventar überprüfen!"
echo ""
