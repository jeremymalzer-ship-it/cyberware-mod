# 🚀 INTEGRATION GUIDE - Version 2.0

## 📦 Übersicht der neuen Dateien

Diese Erweiterung fügt hinzu:
- ✅ **50+ Cyberware Items**
- ✅ **Slot-System mit 6 Kategorien**
- ✅ **Conversation-System mit 50+ Dialoge**
- ✅ **Erweiterte NPC-Entities**
- ✅ **GUI für Slot-Management**
- ✅ **Persistente Speicherung**

---

## 🔧 Installation (Schritt für Schritt)

### Phase 1: Alte Dateien ersetzen

| Alte Datei | Neue Datei | Pfad |
|-----------|-----------|------|
| ModItems.java | ModItems_Extended.java | src/main/java/com/cyberware/item/ |
| CyberwareCapability.java | CyberwareCapability_Extended.java | src/main/java/com/cyberware/capabilities/ |
| ModEntities.java (teil) | AdvancedEntities.java | src/main/java/com/cyberware/entity/ |

**Wie man ersetzt:**
```bash
# 1. Alte Datei löschen oder umbenennen
mv src/main/java/com/cyberware/item/ModItems.java ModItems_Backup.java

# 2. Neue Datei kopieren
cp ModItems_Extended.java src/main/java/com/cyberware/item/ModItems.java

# 3. In der neuen Datei:
#    - "ModItems_Extended" → "ModItems" umbenennen
#    - Class-Name anpassen
```

### Phase 2: Neue Dateien hinzufügen

Kopiere diese neuen Dateien:

```
NEUE DATEIEN:
├── src/main/java/com/cyberware/
│   ├── conversation/
│   │   └── ConversationManager.java          (NEU)
│   ├── gui/
│   │   └── CyberwareSlotScreen.java          (NEU)
│   └── entity/
│       └── AdvancedEntities.java             (NEU - ersetzt ModEntities)
│
└── src/main/resources/assets/cyberware/lang/
    ├── en_us_extended.json                   (NEU)
    └── de_de_extended.json                   (NEU)
```

### Phase 3: CyberwareMod.java updaten

**In CyberwareMod.java hinzufügen:**

```java
package com.cyberware;

import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.ModLoadingContext;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import com.cyberware.block.ModBlocks;
import com.cyberware.item.ModItems;
import com.cyberware.entity.ModEntities;
import com.cyberware.capabilities.CyberwareCapability;
import com.cyberware.network.PacketHandler;
import com.cyberware.conversation.ConversationManager;      // NEU
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

@Mod("cyberware")
public class CyberwareMod {
    public static final String MOD_ID = "cyberware";
    public static final Logger LOGGER = LogManager.getLogger();

    public CyberwareMod() {
        IEventBus modEventBus = net.minecraftforge.fml.javafxmod.FXModLanguageProvider.getFXEventBus();
        
        ModItems.register(modEventBus);
        ModBlocks.register(modEventBus);
        ModEntities.register(modEventBus);
        
        modEventBus.addListener(this::commonSetup);
        modEventBus.addListener(this::clientSetup);
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
        event.enqueueWork(() -> {
            PacketHandler.register();
            CyberwareCapability.register();
            // NEU: Lade Conversations
            ConversationManager.class.getName();
            LOGGER.info("Cyberware Mod Common Setup Complete");
        });
    }

    private void clientSetup(final FMLClientSetupEvent event) {
        LOGGER.info("Cyberware Mod Client Setup Complete");
    }
}
```

---

## 🎯 Wichtige Änderungen verstehen

### 1. ModItems → ModItems_Extended

**Was ändert sich:**
- ✅ 8 Items → 50+ Items
- ✅ Neue Categorization (operative, netrunning, etc.)
- ✅ Neue Crafting-Materials
- ✅ Soul Shards für Conversations

**Integration:**
```java
// Alte Code:
public static final RegistryObject<Item> SANDEVISTAN = ITEMS.register("sandevistan", ...)

// Neue Code (gleich):
public static final RegistryObject<Item> SANDEVISTAN = ITEMS.register("sandevistan", 
    () -> new CyberwareItem(new Item.Properties(), "sandevistan", "operative", "..."))
            //                                                                      ↑ Neue kategorie
```

### 2. CyberwareCapability → CyberwareCapability_Extended

**Was ändert sich:**
- ✅ Slot-System (statt einfache Liste)
- ✅ 6 Kategorien mit je eigenen Limits
- ✅ Chrome-Level Berechnung
- ✅ Bessere NBT-Speicherung

**Bestehender Code funktioniert noch:**
```java
// Alles kann man noch so nutzen:
cyberwareData.addCyberware("sandevistan");   // Funktioniert noch
cyberwareData.getChrome();                   // Funktioniert noch

// Neue Methoden:
cyberwareData.installCyberware("sandevistan", "operative");  // NEU
cyberwareData.canInstallType("operative");                    // NEU
cyberwareData.getMaxSlotsForType("operative");               // NEU
```

### 3. Neue ConversationManager.java

**Was ist neu:**
- ✅ Dialog-System mit Knoten
- ✅ Vordefinierte Conversations (Lucy, David, Smasher, MaxTac, Ripperdoc)
- ✅ Interactive Choice-System
- ✅ Story-Verzweigungen

**So nutzen:**
```java
// Conversation starten
ConversationManager.startConversation(player, "lucy_default");

// Wahlen treffen
conversation.selectChoice(player, 0);  // Choice 1
conversation.selectChoice(player, 1);  // Choice 2
```

### 4. Neue CyberwareSlotScreen.java

**Was ist neu:**
- ✅ Visuelles Slot-Management GUI
- ✅ Farbcodierte Kategorien
- ✅ Chrome-Level Anzeige
- ✅ Rechtsklick zum Installieren

**Integration:**
```java
// GUI öffnen (für NPC oder Command):
Minecraft.getInstance().setScreen(new CyberwareSlotScreen(player));
```

---

## 🔀 Datei-Abhängigkeiten

```
CyberwareMod.java
├── ModItems.java (50+ Items)
│   └── CyberwareItem.java (nutzt Aktivierungslogik)
├── CyberwareCapability.java (Slot-System)
│   └── NBT Serialisierung
├── ModEntities.java (8 NPCs)
│   └── Alle mit Dialog-Integration
├── ConversationManager.java (Dialog-System)
│   └── DialogueNode & Conversation
└── CyberwareSlotScreen.java (GUI)
    └── Client-Side nur
```

---

## 🛠️ Build & Compile

```bash
# 1. Alle Dateien kopiert? ✓
# 2. CyberwareMod.java aktualisiert? ✓
# 3. Dann:

gradle clean build

# Output:
# build/libs/cyberware-1.0.0.jar ← Diese ist fertig!
```

---

## ✅ Schritt-für-Schritt Checklist

### Datei-Integration:
- [ ] ModItems_Extended.java → ModItems.java (umbenannt)
- [ ] CyberwareCapability_Extended.java → CyberwareCapability.java (umbenannt)
- [ ] ConversationManager.java kopiert (neu)
- [ ] CyberwareSlotScreen.java kopiert (neu)
- [ ] AdvancedEntities.java kopiert (neu)

### Sprach-Dateien:
- [ ] en_us_extended.json kopiert
- [ ] de_de_extended.json kopiert
- [ ] Old lang files aktualisiert mit neuen Keys

### Konfiguration:
- [ ] CyberwareMod.java aktualisiert
- [ ] Alle Imports vorhanden
- [ ] gradle build erfolgreich

### Testing:
- [ ] Mod lädt ohne Fehler
- [ ] Alle 50+ Items sichtbar
- [ ] NPCs spawnen
- [ ] Dialoge funktionieren
- [ ] Slots speicherbar

---

## 🐛 Häufige Fehler beim Integration

### Fehler 1: "Class ModItems not found"
```
→ Datei nicht kopiert/umbenannt
→ Alte ModItems.java nicht gelöscht?
→ Import-Pfade korrekt?
```

### Fehler 2: "Conversation nicht gefunden"
```
→ ConversationManager.java nicht im Ordner
→ Package-Name korrekt?
→ Im CyberwareMod.java geladen?
```

### Fehler 3: "Slot-System funktioniert nicht"
```
→ CyberwareCapability_Extended.java nicht kopiert
→ Methoden-Namen vergessen?
→ Capability nicht registriert?
```

### Fehler 4: "NPC Dialoge nicht sichtbar"
```
→ ConversationManager.registerConversations() wird nicht aufgerufen
→ In CyberwareMod.java hinzufügen
→ Oder direkt in ConversationManager statischer Block
```

---

## 📊 Feature-Vergleich

### Vorher (v1.0):
```
Items:          8
Cyberware:      8
NPCs:           5
Conversations:  0
Slots:          Limitlos
Chrome-Level:   Einfach
GUI:            Keine
```

### Nachher (v2.0):
```
Items:          50+
Cyberware:      50+
NPCs:           8+ mit Dialogen
Conversations:  50+ Dialog-Knoten
Slots:          13 (kategorial)
Chrome-Level:   Psychose-System
GUI:            Slot-Screen
```

---

## 🎮 Im Spiel testen

```bash
# 1. Minecraft starten mit Forge
gradle runClient

# 2. Creative Mode
/gamemode creative

# 3. Items geben
/give @s cyberware:sandevistan
/give @s cyberware:berserk
/give @s cyberware:adam_smasher (NPC!)

# 4. Conversations testen
Rechtsklick auf NPC

# 5. Slot-GUI testen
/execute as @s run function cyberware:open_slots

# 6. Chrome-Level prüfen
/data get entity @s SelectedItem.tag.cyberware:chrome
```

---

## 📈 Nächste Verbesserungen (Optional)

- [ ] Custom Textures für alle 50 Items
- [ ] Armor Models für Cyberware
- [ ] 3D-Modelle der NPCs
- [ ] Voice-Lines (mit Resource Pack)
- [ ] Particle Effects bei Aktivierung
- [ ] Sound-Effekte
- [ ] Handels-System für Ripperdoc
- [ ] Quests mit Story

---

## 📞 Support

Falls etwas nicht funktioniert:

1. Logs prüfen: `run/logs/latest.log`
2. Alle Imports prüfen
3. Datei-Namen überprüfen (Case-sensitive!)
4. gradle clean probieren
5. Caches invalidieren

---

**Integration erfolgreich? Glückwunsch!** 🎉

Du hast jetzt eine komplette Cyberpunk 2077-Mod mit:
- 50+ Cyberware Items
- Slot-System
- NPC Conversations
- Chrome-Psychose Mechanic
- Persistente Speicherung

**Let's get this bread! 🤖⚡**

