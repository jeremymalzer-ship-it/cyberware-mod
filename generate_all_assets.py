#!/usr/bin/env python3
"""
Cyberware Mod - Automatische Textur-Generierung (v2.0)
Erzeugt 50+ 16x16 Texturen für alle Cyberware Items
"""

from PIL import Image, ImageDraw
import os
import json

# Farbschema (Cyberpunk 2077 Style)
ITEM_COLORS = {
    # Operative (Rot/Orange)
    'sandevistan': ('#00FFFF', '#0088FF', '#000033'),      # Cyan - Zeit
    'berserk': ('#FF0000', '#880000', '#330000'),           # Rot - Aggression
    'mantis_blades': ('#00FF00', '#00AA00', '#003300'),     # Grün - Gift
    'gorilla_arms': ('#FFA500', '#AA6600', '#553300'),      # Orange - Kraft
    'monowire': ('#FFFF00', '#CCAA00', '#664400'),          # Gelb - Draht
    'tesla_coils': ('#FF00FF', '#AA00AA', '#330033'),       # Magenta - Blitz
    'projectile_launcher': ('#FFAA00', '#CC6600', '#664400'), # Orange-Rot
    'kerenzikov': ('#00FFFF', '#0099FF', '#003366'),        # Cyan - Reaktion

    # Netrunning (Blau)
    'quickhacking': ('#0000FF', '#0000AA', '#000033'),      # Blau
    'breach_protocol': ('#0000FF', '#0066FF', '#003366'),   # Blau-Hell
    'ping': ('#00FFFF', '#00AA88', '#003344'),              # Cyan
    'vulnerability_scanner': ('#0099FF', '#0066FF', '#003366'), # Blau
    'ping_quickhack': ('#0000FF', '#0088FF', '#004488'),    # Blau-Cyan
    'breach_and_hack': ('#0088FF', '#0055FF', '#002288'),   # Blau

    # Stealth (Lila/Dunkel)
    'optical_camo': ('#FF00FF', '#AA00AA', '#330033'),      # Magenta
    'camouflage': ('#888888', '#555555', '#222222'),        # Grau
    'silent_steps': ('#4444FF', '#3333AA', '#111133'),      # Dunkelblau
    'shadow_cloak': ('#220033', '#110011', '#000000'),      # Dunkel-Magenta

    # Defense (Grau/Silber)
    'chrome_body': ('#CCCCCC', '#999999', '#333333'),       # Grau
    'dermal_armor': ('#AAAAAA', '#888888', '#444444'),      # Grau-Dunkel
    'kinetic_dampening': ('#BBBBBB', '#888888', '#555555'), # Grau-Silber
    'regeneration_system': ('#00FF00', '#00AA00', '#004400'), # Grün
    'quickdodge': ('#FFFF00', '#CCCC00', '#666600'),        # Gelb
    'fortified_skeleton': ('#666666', '#333333', '#000000'), # Schwarz-Grau

    # Sensory (Mehrfarbig)
    'tactical_scanner': ('#FFFF00', '#CCCC00', '#666600'),  # Gelb
    'thermal_vision': ('#FF0000', '#AA0000', '#440000'),    # Rot
    'zoom_optics': ('#00FF00', '#00AA00', '#003300'),       # Grün
    'expanded_lungs': ('#00CCFF', '#0099FF', '#003366'),    # Cyan
    'reinforced_legs': ('#FFAA00', '#CC6600', '#664400'),   # Orange

    # Iconic (Rainbow/Spezial)
    'smasher_overseer': ('#FF00FF', '#FF0088', '#880044'),  # Pink-Rot
    'edgerunner_custom': ('#00FFFF', '#FF00FF', '#FFFF00'), # Rainbow
    'lucy_netrunning': ('#0000FF', '#FF00FF', '#00FFFF'),   # Blue-Pink-Cyan
    'maxtac_combat': ('#FF0000', '#0000FF', '#000000'),     # Rot-Blau
    'corpo_elite': ('#FFD700', '#AA8800', '#554400'),       # Gold
    'fixer_package': ('#00FF00', '#FF00FF', '#0000FF'),     # RGB

    # Crafting Materials
    'cyberware_chip': ('#FF00FF', '#AA00AA', '#330033'),    # Magenta
    'military_grade_chipset': ('#FFD700', '#AA8800', '#554400'), # Gold
    'neural_interface': ('#00FFFF', '#0088FF', '#003366'),  # Cyan
    'quickhacking_protocol': ('#00FF00', '#00AA00', '#003300'), # Grün
    'titanium_housing': ('#888888', '#666666', '#222222'),  # Grau
    'synthetic_muscle': ('#FF0000', '#AA0000', '#330000'),  # Rot
    'optical_lens': ('#00FFFF', '#0099FF', '#003366'),      # Cyan
    'neural_connector': ('#FF00FF', '#FF0088', '#880044'),  # Pink
    'quantum_processor': ('#FF00FF', '#FF0088', '#660044'), # Pink
    'edgerunner_shard': ('#FF00FF', '#FF0088', '#660044'),  # Pink

    # Soul Shards
    'lucy_soul_shard': ('#0000FF', '#0088FF', '#003366'),   # Blau
    'david_soul_shard': ('#FF0000', '#AA0000', '#440000'),  # Rot
    'smasher_soul_shard': ('#FF00FF', '#FF0088', '#880044'), # Pink
    'maxtac_soul_shard': ('#FF0000', '#0000FF', '#000000'), # Rot-Blau
}

def create_cyberpunk_item(name, colors, size=16):
    """Erstellt ein 16x16 Cyberpunk-Style Item"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    primary, secondary, dark = colors
    primary_rgb = tuple(int(primary[i:i+2], 16) for i in (1, 3, 5))
    secondary_rgb = tuple(int(secondary[i:i+2], 16) for i in (1, 3, 5))
    dark_rgb = tuple(int(dark[i:i+2], 16) for i in (1, 3, 5))
    
    # Base: Großes Rechteck
    draw.rectangle([1, 1, size-2, size-2], fill=primary_rgb, outline=dark_rgb)
    
    # Inner Pattern
    for i in range(2, size-2, 4):
        draw.line([(2, i), (size-3, i)], fill=secondary_rgb, width=1)
    
    # Corner Highlights (3D-Effekt)
    draw.rectangle([1, 1, 3, 3], fill=(255, 255, 255, 128))
    
    # Center Accent
    center = size // 2
    draw.ellipse([center-2, center-2, center+2, center+2], fill=secondary_rgb)
    draw.ellipse([center-1, center-1, center+1, center+1], fill=(255, 255, 255, 200))
    
    return img

def create_soul_shard_texture(name, colors):
    """Erstellt ein Soul Shard Texture (glühend)"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    primary, secondary, dark = colors
    primary_rgb = tuple(int(primary[i:i+2], 16) for i in (1, 3, 5))
    secondary_rgb = tuple(int(secondary[i:i+2], 16) for i in (1, 3, 5))
    
    # Soul Shard = Diamant-Form
    points = [(8, 2), (14, 8), (8, 14), (2, 8)]
    draw.polygon(points, fill=primary_rgb, outline=secondary_rgb)
    
    # Glowing center
    draw.ellipse([5, 5, 11, 11], fill=secondary_rgb)
    draw.ellipse([6, 6, 10, 10], fill=(255, 255, 255, 150))
    
    return img

def create_all_textures():
    """Erstellt alle 50+ Texturen"""
    output_dir = 'src/main/resources/assets/cyberware/textures/item'
    os.makedirs(output_dir, exist_ok=True)
    
    print("🎨 Erstelle Cyberware Item-Texturen...\n")
    
    for name, colors in ITEM_COLORS.items():
        # Soul Shards haben speziales Design
        if 'soul_shard' in name:
            img = create_soul_shard_texture(name, colors)
        else:
            img = create_cyberpunk_item(name, colors)
        
        filepath = f'{output_dir}/{name}.png'
        img.save(filepath)
        print(f'✓ {name}.png erstellt')
    
    print(f"\n✅ {len(ITEM_COLORS)} Texturen erfolgreich erstellt!")
    print(f"   Ordner: {output_dir}")

def create_item_models():
    """Erstellt JSON-Modelle für alle Items"""
    output_dir = 'src/main/resources/assets/cyberware/models/item'
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n📋 Erstelle Item-Modelle...\n")
    
    for name in ITEM_COLORS.keys():
        model = {
            "parent": "item/handheld",
            "textures": {
                "layer0": f"cyberware:item/{name}"
            },
            "display": {
                "thirdperson_righthand": {
                    "rotation": [0, 0, 0],
                    "translation": [0, 2, 0],
                    "scale": [0.85, 0.85, 0.85]
                },
                "firstperson_righthand": {
                    "rotation": [0, -90, 25],
                    "translation": [1.13, 3.2, 1.13],
                    "scale": [0.68, 0.68, 0.68]
                },
                "gui": {
                    "rotation": [30, 225, 0],
                    "translation": [0, 0, 0],
                    "scale": [0.625, 0.625, 0.625]
                }
            }
        }
        
        filepath = f'{output_dir}/{name}.json'
        with open(filepath, 'w') as f:
            json.dump(model, f, indent=2)
        
        print(f'✓ {name}.json erstellt')
    
    print(f"\n✅ {len(ITEM_COLORS)} Item-Modelle erstellt!")

def main():
    """Hauptfunktion"""
    print("=" * 50)
    print("🤖 CYBERWARE MOD - ASSET GENERATOR")
    print("=" * 50)
    
    create_all_textures()
    create_item_models()
    
    print("\n" + "=" * 50)
    print("✨ ALLE ASSETS ERSTELLT!")
    print("=" * 50)
    print("\n📝 Nächste Schritte:")
    print("1. gradle build ausführen")
    print("2. Items im Inventar überprüfen")
    print("3. Weitere Texturen anpassen wenn nötig")
    print("\n🎮 Viel Spaß mit der Mod!")

if __name__ == '__main__':
    main()
