# MOBILE_COMPATIBILITY.md

## v1.4.0 mobile viewport adaptation

The game keeps a 1280×720 logical playfield for identical aim/charge muscle memory, while the browser shell now adapts to the usable viewport instead of assuming desktop `100vh`.

### Implemented

- `viewport-fit=cover` + CSS safe-area insets for notch / Dynamic Island / punch-hole devices.
- `VisualViewport` based width/height syncing, including mobile browser toolbar expansion/collapse.
- `100dvw/100dvh` fallback when supported, classic viewport fallback otherwise.
- Landscape playfield is aspect-preserving; ultra-wide surplus area receives atmospheric side fill instead of stretching the game world.
- Portrait overlay also uses the live visual viewport and safe-area padding.
- Canvas pointer mapping remains based on the actual rendered bounding rectangle, so touch coordinates stay correct after scaling.
- Canvas UI hit regions receive an 14 logical-pixel touch slop to improve small landscape-phone usability without changing visuals.
- `index.html` is now a fully standalone build, so static hosting/GitHub Pages can open the game directly without a missing `/src/main.ts`.

### Target landscape viewport classes checked

| Class | Representative CSS viewport | Typical devices |
|---|---:|---|
| 16:9 compact | 640×360 / 720×405 | older Android / small phones |
| 16:9 / 16:9-ish | 667×375 / 736×414 | iPhone 6–8 class |
| 19.5:9 | 844×390 / 852×393 | iPhone 12–15 class |
| 20:9 | 800×360 / 915×412 | mainstream Android |
| wide flagship | 932×430 | Pro Max / large flagship class |
| tablet landscape | 1024×768 | iPad class (game remains landscape-contained) |

### Design choice

The game does **not stretch** the 16:9 playfield on 19.5:9/20:9 screens. Stretching would alter apparent throw distance and undermine the fixed charge-time-to-distance relationship. The extra width is treated as decorative bleed while gameplay and HUD remain inside a safe, consistent 16:9 field.
