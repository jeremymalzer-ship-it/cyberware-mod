# 🤖 CYBERWARE MOD - INSTALLATION

## Schnell-Anleitung

1. Diesen Ordner in dein Minecraft-Mod-Development-Verzeichnis kopieren
2. Terminal öffnen und in den Ordner gehen:
   ```bash
   cd cyberware-mod-complete
   ```

3. Assets generieren:
   ```bash
   python3 generate_all_assets.py
   ```

4. Kompilieren:
   ```bash
   gradle clean build
   ```

5. Testen:
   ```bash
   gradle runClient
   ```

## ✅ Was ist dabei?

- ✓ 50+ Cyberware Items
- ✓ Slot-System (13 Slots)
- ✓ Conversation-System (50+ Dialoge)
- ✓ 8+ NPCs mit Dialogen
- ✓ Player-Rendering (Glow-Effekte)
- ✓ 50+ Auto-generierte Texturen
- ✓ 50+ JSON-Modelle
- ✓ Deutsche & Englische Lokalisierung
- ✓ Chrome-Level System
- ✓ Persistente Speicherung

## 📝 Anforderungen

- Java 17+
- Gradle
- Python 3 (für Asset-Generator)
- Minecraft 1.20.1 Forge

## 🎮 Im Spiel testen

```
/give @s cyberware:sandevistan
Shift+Rechtsklick → Installiert!
```

## 📚 Dokumentation

- **README_V3.md** - Komplette Übersicht
- **COMPLETE_VISUAL_SYSTEM_GUIDE.md** - Visual System
- **ADVANCED_FEATURES_GUIDE.md** - Features
- **INTEGRATION_GUIDE_V2.md** - Integration
- **docs/** - Weitere Guides

## 🆘 Probleme?

1. **Assets nicht generiert:**
   ```bash
   pip3 install Pillow
   python3 generate_all_assets.py
   ```

2. **Gradle Fehler:**
   ```bash
   gradlew --stop
   gradle clean build
   ```

3. **Items nicht sichtbar:**
   - Alle Dateien kopiert?
   - gradle clean build?
   - Minecraft neugestartet?

Viel Erfolg! 🤖⚡
