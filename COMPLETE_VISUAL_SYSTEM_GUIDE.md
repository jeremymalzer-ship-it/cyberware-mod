# 🎨 COMPLETE VISUAL SYSTEM GUIDE

## 📊 ÜBERSICHT

Deine Mod hat jetzt:
- ✅ **50+ Item-Texturen** (automatisch generiert)
- ✅ **50+ JSON-Modelle** (automatisch generiert)
- ✅ **Player-Renderer-System** (zeigt Cyberware am Körper)
- ✅ **Armor-Layer-System** (visuelle Veränderungen)
- ✅ **Glow/Aura-Effekte** (bei hohem Chrome)
- ✅ **Eye-Rendering** (leuchtende Augen bei 100%)

---

## 🖼️ PART 1: ITEM-TEXTUREN

### Automatische Generierung

```bash
# 1. Python Script ausführen
python3 generate_all_assets.py

# ODER: Mit Start-Script
./RUN_ASSET_GENERATOR.sh

# Output:
# ✓ 50+ PNG-Texturen erstellt
# ✓ 50+ JSON-Modelle erstellt
```

### Was wird generiert?

#### Textur-Farben:

**Operative (Rot/Orange):**
- Sandevistan → Cyan (Zeit)
- Berserk → Rot (Aggression)
- Mantis Blades → Grün (Giftig)
- Gorilla Arms → Orange (Kraft)

**Netrunning (Blau):**
- Quickhacking → Blau
- Ping → Cyan
- Breach Protocol → Blau-Hell

**Stealth (Lila/Dunkel):**
- Optical Camo → Magenta
- Camouflage → Grau
- Silent Steps → Dunkelblau

**Defense (Grau/Silber):**
- Chrome Body → Grau/Silber
- Dermal Armor → Dunkelgrau
- Regeneration → Grün

**Sensory (Bunt):**
- Thermal Vision → Rot
- Tactical Scanner → Gelb
- Zoom Optics → Grün

**Iconic (Rainbow):**
- Smasher Overseer → Pink-Rot
- Edgerunner Custom → Regenbogen
- Lucy Netrunning → Blau-Pink-Cyan

**Soul Shards (Glühend):**
- Diamant-Form mit Glows
- Jede Soul Shard hat eigene Farbe

### Struktur der Texturen:

```
src/main/resources/assets/cyberware/textures/item/
├── sandevistan.png           (16x16 Cyan)
├── berserk.png               (16x16 Rot)
├── mantis_blades.png         (16x16 Grün)
├── gorilla_arms.png          (16x16 Orange)
├── quickhacking.png          (16x16 Blau)
├── ping.png                  (16x16 Cyan)
├── optical_camo.png          (16x16 Magenta)
├── chrome_body.png           (16x16 Grau)
...
└── (50+ insgesamt)
```

### Textur-Design:

```
┌─────────────────┐
│                 │   
│  ◆◆◆◆◆◆◆◆◆◆   │   Basis: Große Form in Primär-Farbe
│  ◆◆◆◆◆◆◆◆◆◆   │   Muster: Horizontale Linien
│  ◆◆◆     ◆◆◆   │   Highlight: Weiße Ecke (3D-Effekt)
│  ◆◆◆  ◆  ◆◆◆   │   Center: Sekundär-Farbe Punkt
│  ◆◆◆◆◆◆◆◆◆◆   │   
│  ◆◆◆◆◆◆◆◆◆◆   │
│                 │
└─────────────────┘
```

**Soul Shards:**
```
     ◆
    ◆◆◆
   ◆◆◆◆◆     Diamant-Form
    ◆◆◆◆     Mit innerer Glow
     ◆◆      Sehr glänzend
      ◆
```

---

## 👤 PART 2: PLAYER-VISUALS

### Was passiert wenn Cyberware installiert ist?

#### Chrome-Level 0-30%: **Subtil**
```
Spieler sieht normal aus
Nur kleine metallische Glanz
```

#### Chrome-Level 30-60%: **Sichtbar**
```
Körper: Metallischer Glanz
Arme: Sichtbar verstärkt
Augen: Leicht leuchtend
Effekt: Glow um Spieler
```

#### Chrome-Level 60-100%: **VOLLER CYBORG**
```
Augen: LEUCHTEN MAGENTA/NEON
Körper: Kompletter Metallglanz
Effekt: Starker Neon-Glow (Cyan/Magenta)
Bewegung: Rigider, mechanischer
Schatten: Metallisch glänzend
```

### Visuelle Veränderungen pro Slot-Typ:

**Operative (Rot) + Cyberware:**
- Rote Augen-Glow
- Aggressive Bewegungen
- Breite Schultern-Optik
- Blut-rote Aura

**Netrunning (Blau) + Cyberware:**
- Blaue Augen-Glow
- Schnelle, nervöse Bewegungen
- Blau-glühende Aura
- Digitale Effekte

**Stealth (Grau) + Cyberware:**
- Keine Glow (unsichtbar)
- Flüssige Bewegungen
- Kaum sichtbare Aura
- Shadow-Effekt

**Defense (Silber) + Cyberware:**
- Silberne Augen-Glow
- Robuste Bewegungen
- Helles Glänzen
- Silber-Aura

**Sensory (Bunt) + Cyberware:**
- Multi-Farb Glow
- Schnelle Kopfbewegungen
- Scanner-Effekt
- Rainbow-Aura

**Iconic (Legendär) + Cyberware:**
- EXTREME Glow
- Magenta/Pink Augen
- Beste Effekte
- Einzigartige Aura

---

## 🔧 TECHNISCHE DETAILS

### Player-Renderer Hook (in CyberwarePlayerRenderer.java):

```java
RenderPlayerEvent.Post
  ↓
getCyberwareData(player)
  ↓
if chrome > 0: renderCyberwareEffects()
  ├→ 30%: renderMetallicSheen()
  ├→ 60%: renderNeonGlow()
  └→ 100%: renderFullCyborgMode()
```

### Rendering-Pipeline:

```
1. PoseStack.pushPose()          // Speichere alte Position
2. Bestimme Farbe basierend auf Cyberware
3. Rendere Gloss-Effekt
4. Rendere Glow-Aura
5. Rendere Eye-Glow (bei 100%)
6. PoseStack.popPose()           // Stelle alte Position wieder her
```

### Farb-Bestimmung:

```java
if cyber.hasCyberware("operative") → 0xFF0000 (Rot)
if cyber.hasCyberware("netrunning") → 0x0000FF (Blau)
if cyber.hasCyberware("stealth") → 0x888888 (Grau)
if cyber.hasCyberware("defense") → 0xCCCCCC (Silber)
if cyber.hasCyberware("sensory") → 0xFFFF00 (Gelb)
if cyber.hasCyberware("iconic") → 0xFF00FF (Magenta)
```

---

## 📦 INSTALLATION (SCHRITT-FÜR-SCHRITT)

### Phase 1: Asset-Generierung

```bash
# 1. In Mod-Ordner gehen
cd cyberware-mod

# 2. Asset-Generator ausführen
python3 generate_all_assets.py

# ODER Windows:
python generate_all_assets.py

# Output:
# ✓ sandevistan.png
# ✓ sandevistan.json
# ✓ berserk.png
# ✓ berserk.json
# ... (50+ insgesamt)

# Zeit: ~5-10 Sekunden ⚡
```

### Phase 2: Code-Integration

```bash
# 1. CyberwarePlayerRenderer.java kopieren
cp src/main/java/com/cyberware/client/CyberwarePlayerRenderer.java \
   [DEIN_PROJEKT]/src/main/java/com/cyberware/client/

# 2. In CyberwareMod.java registrieren:
```

**In CyberwareMod.java hinzufügen:**
```java
import com.cyberware.client.CyberwarePlayerRenderer;

// In commonSetup oder clientSetup:
event.enqueueWork(() -> {
    // ... anderer Code
    // NEU:
    CyberwarePlayerRenderer.class.getName();
});
```

### Phase 3: Kompilieren

```bash
gradle clean build

# Wenn Fehler:
gradle --stop
gradle clean build
```

### Phase 4: Testen

```bash
gradle runClient

# Im Spiel:
/give @s cyberware:sandevistan
Rechtsklick mit Shift → Cyberware installieren
→ Spieler fängt zu glänzen an!
```

---

## ✨ VISUELLE EFFEKTE DETAILS

### Metallischer Glanz (Chrome 30%+)

**Was passiert:**
- Kopf: Kleine silberne Schicht
- Körper: Glänzender Effekt
- Arme: Sichtbar verstärkt
- Effekt: Subtil aber erkennbar

**Code:**
```java
renderGlassBox(
    -0.3f, 0.5f, -0.3f,    // Position: Kopf
    0.3f, 1.0f, 0.3f,      // Größe
    0x888888,               // Grau
    intensity               // Alpha
);
```

### Neon-Glow (Chrome 60%+)

**Was passiert:**
- Ganze Körper leuchtet
- Farbe: Basierend auf installierter Cyberware
- Intensität: Steigt mit Chrome
- Effekt: Sehr sichtbar

**Farben:**
- Operative → Rot glow
- Netrunning → Blau glow
- Stealth → Grau glow
- Defense → Silber glow
- Sensory → Gelb glow
- Iconic → Magenta glow

### Full Cyborg Mode (100% Chrome)

**Was passiert:**
- Augen LEUCHTEN in Neon-Farbe
- Whole body glowing
- Maximum visual impact
- Spieler sieht aus wie echter Cyborg!

**Eye-Rendering:**
```java
poseStack.translate(0, 1.7, 0);  // Kopf-Höhe
renderEyeGlow(poseStack, 0xFF00FF);  // Magenta
```

---

## 🎮 TEXTURE-PACK KOMPATIBILITÄT

Das System ist kompatibel mit:
- ✅ Custom Texture Packs (überschreiben PNG-Dateien)
- ✅ Resource Packs (ModifyTextures.zip)
- ✅ Shader-Mods (Enhanced Gloss)
- ✅ Mod-Kombinationen

**Für Custom Textures:**

```
dein-resource-pack/
└── assets/
    └── cyberware/
        └── textures/
            └── item/
                ├── sandevistan.png (deine Textur!)
                ├── berserk.png
                └── ...
```

---

## 🎨 TEXTUR-ANPASSUNG

Falls du die automatischen Texturen nicht magst:

### Option 1: Mit Paint.NET bearbeiten
```
1. generate_all_assets.py ausführen (Basis)
2. Jedes PNG in Paint.NET öffnen
3. Farben/Details anpassen
4. Speichern
```

### Option 2: Komplett neu zeichnen
```
1. 16x16 PNG erstellen
2. Cyberpunk-Style zeichnen
3. In textures/item/ speichern
4. JSON-Modell anpassen
5. Rebuild
```

### Option 3: AI-generiert
```
1. Midjourney/Stable Diffusion nutzen
   "cyberpunk sandevistan item minecraft 16x16"
2. Bild downloaden
3. Auf 16x16 zuschneiden
4. Als PNG speichern
```

---

## 📊 DATEI-STRUKTUR NACH GENERIERUNG

```
src/main/resources/assets/cyberware/
├── textures/item/
│   ├── sandevistan.png          ✓ AUTO
│   ├── berserk.png              ✓ AUTO
│   ├── mantis_blades.png        ✓ AUTO
│   └── (50+ insgesamt)          ✓ AUTO
│
└── models/item/
    ├── sandevistan.json         ✓ AUTO
    ├── berserk.json             ✓ AUTO
    ├── mantis_blades.json       ✓ AUTO
    └── (50+ insgesamt)          ✓ AUTO
```

---

## ✅ FINAL CHECKLIST

- [ ] `generate_all_assets.py` ausgeführt
- [ ] 50+ PNGs erstellt (textures/item/)
- [ ] 50+ JSONs erstellt (models/item/)
- [ ] CyberwarePlayerRenderer.java kopiert
- [ ] CyberwareMod.java aktualisiert
- [ ] `gradle clean build` erfolgreich
- [ ] Items im Inventar sichtbar
- [ ] Player-Glow funktioniert
- [ ] Augen leuchten bei 100% Chrome

---

## 🚀 PERFORMANCE-TIPPS

Falls Lags mit vielen Effekten:

```java
// In CyberwarePlayerRenderer.java:

// Option 1: Weniger häufig rendern
if(this.tickCount % 2 == 0) {
    renderCyberwareEffects(...);
}

// Option 2: Nur nahe Spieler rendern
if(player.distanceTo(viewer) < 64) {
    renderCyberwareEffects(...);
}

// Option 3: Details reduzieren bei vielen
if(player.level().getEntitiesOfClass(...).size() > 5) {
    skipDetailedRendering();
}
```

---

## 🎯 RESULT

Nach Installation siehst du:

```
Du gibst dir Sandevistan
    ↓
Shift+Rechtsklick
    ↓
✨ Spieler fängt an zu glänzen ✨
    ↓
Körper hat Metallglanz
Augen leuchten subtil
Aura erscheint
    ↓
Bei 100% Chrome:
    ↓
🤖 DU BIST EIN CYBORG! 🤖
Volle Neon-Glow
Leuchtende Augen
Vollständige Metallic-Textur
```

---

**Mit diesem System ist deine Mod KOMPLETT visuell!** 🎨✨

