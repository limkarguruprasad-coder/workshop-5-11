---
name: DevPulse Event Engine
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#464555'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#855300'
  on-secondary: '#ffffff'
  secondary-container: '#fea619'
  on-secondary-container: '#684000'
  tertiary: '#00505f'
  on-tertiary: '#ffffff'
  tertiary-container: '#006a7c'
  on-tertiary-container: '#93e8ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#ffddb8'
  secondary-fixed-dim: '#ffb95f'
  on-secondary-fixed: '#2a1700'
  on-secondary-fixed-variant: '#653e00'
  tertiary-fixed: '#acedff'
  tertiary-fixed-dim: '#4cd7f6'
  on-tertiary-fixed: '#001f26'
  on-tertiary-fixed-variant: '#004e5c'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '800'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '800'
    lineHeight: 34px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  label-code-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: -0.01em
  label-code-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
  label-code-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.04em
  label-ui:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.25rem
  gutter-mobile: 0.75rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.875rem
  space-lg: 1.5rem
  space-xl: 2.25rem
---

## Brand & Style
The design system establishes a hyper-focused, precision-engineered developer platform and technical event orchestrator. Engineered for software architects, API engineers, and tech event organizers, the interface marries crisp technical utility with vibrant, modern digital craft.

The aesthetic fuses **Corporate / Modern** precision with high-density developer ergonomics. Micro-borders, monospaced endpoint paths, high-visibility HTTP method badges, and glowing accent states build an environment that feels simultaneously robust and lightning-fast. It evokes absolute operational clarity, technical trust, and modern developer joy.

## Colors
The color architecture delivers unambiguous typographic clarity alongside vivid contextual indicators:

- **Primary (`#4F46E5` - Indigo Royal):** Anchors core actions, navigation headers, active interactive states, and HTTP `GET` badge highlights. Supported by ultra-soft tinted surface fills (`#EEF2FF`) for table rows and endpoint groupings.
- **Secondary (`#F59E0B` - Soft Amber / Orange):** Used for code parameters, parameterized routes (`{id}`), warning notices, authentication callouts, and high-visibility status states. Backed by warm alert container washes (`#FFFBEB`).
- **Tertiary (`#06B6D4` - Electric Cyan):** Used for supplementary telemetry metrics, payload schema links, and real-time event listener indicators.
- **Neutral (`#0F172A` - Slate Obsidian):** Deep slate provides crisp typography against chalk-white canvases (`#FFFFFF`) and container borders (`#E2E8F0`). Dark code blocks use a grounded neutral base (`#0B0F19`) with high-contrast syntax tokens.

## Typography
Typographic rhythm relies on a deliberate separation of roles:
- **Display & Headings (Plus Jakarta Sans):** Geometric, warm, yet strictly authoritative for dashboard section titles and modal headers.
- **Interface & Prose (Inter):** Highly legible, neutral workhorse for standard table descriptions, user guidance, and configuration forms.
- **Technical & Code (JetBrains Mono):** Dedicated to REST endpoints (`/api/events`), HTTP methods (`GET`, `POST`), payload tokens, and response status codes. Tabular numbers ensure character-aligned endpoints across stacked rows.

## Layout & Spacing
The layout follows a responsive 12-column fluid structure paired with an 8-point base spatial grid:
- **Desktop (1024px+):** 12 columns, `margin: 2rem`, `gutter: 1.25rem`. Two-pane layouts place API specification tables and live response runners side-by-side.
- **Tablet (768px - 1023px):** 8 columns, content collapses to stacked inspection panels with retained horizontal padding.
- **Mobile (< 768px):** 4 columns, `margin-mobile: 1rem`. Data tables switch to card-based horizontal endpoint strips with method chips stacked above path declarations.

## Elevation & Depth
Depth is created through structured tonal layering and crisp micro-borders rather than aggressive drop shadows:

- **Level 0 (Canvas):** `#F8FAFC` base surface for background contexts.
- **Level 1 (Cards & Tables):** Pure `#FFFFFF` surface container with a sharp `1px solid #E2E8F0` border and a delicate ambient shadow (`0 1px 3px 0 rgba(15, 23, 42, 0.04), 0 1px 2px -1px rgba(15, 23, 42, 0.02)`).
- **Level 2 (Dropdowns, Flyouts & Modals):** `#FFFFFF` with `0 10px 15px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04)` and border `#CBD5E1`.
- **Level 3 (Dark Code Execution Panels):** `#0B0F19` with a subtle inner edge highlight (`inset 0 1px 0 0 rgba(255, 255, 255, 0.08)`) and border `1px solid #1E293B`.

## Shapes
A unified rounded shape language (`roundedness: 2`) balances clean software engineering precision with contemporary approachable software ergonomics:
- Standard buttons, input bars, code blocks, and data cards utilize `0.5rem` (8px).
- Badges, method pills, and authentication banners apply `rounded-md` (6px) or fully rounded pill styles where tag containment is necessary.
- Major table wrappers and dashboard summary cards use `rounded-lg` (1rem).

## Components

### API Contract Data Tables
- **Header Row:** Rendered on a soft tinted indigo ground (`#F1F5F9` or `#EEF2FF`) with uppercase medium-weight labels in `label-ui`.
- **Method Pill:** Bold monospace badge. `GET` uses `#4F46E5` on `#EEF2FF`, `POST` uses `#0D9488` on `#CCFBF1`, `DELETE` uses `#E11D48` on `#FFE4E6`.
- **Endpoint Cell:** High-visibility monospace string (`label-code-md`). Static paths in bold slate `#0F172A`, parameter segments (e.g., `{id}`) highlighted in amber `#D97706`.
- **Row Styling:** Alternating subtle hover state (`#F8FAFC`), segmented by crisp `#F1F5F9` horizontal rules.

### Code Blocks & JSON Viewers
- High-contrast dark container (`#0B0F19`) featuring subtle syntax highlighting (keys in `#93C5FD`, strings in `#86EFAC`, integers in `#FDE047`).
- Includes a floating copy-to-clipboard button and terminal prompt header.

### Authentication & Status Callouts
- Bounded container with a warm amber surface (`#FFFBEB`), amber-toned border (`#FDE68A`), and a prominent lock or security icon.
- Direct typographic pairing with bold lead text and regular supporting guidance.

### Buttons & Inputs
- **Primary Button:** `#4F46E5` solid background with pure white text, transitioning to `#4338CA` on hover.
- **Secondary / Ghost Button:** Transparent background, `1px solid #E2E8F0`, slate text with `#F8FAFC` hover fill.
- **Search & Filter Inputs:** Monospace or clean sans placeholder, leading search glyph, 40px default height, focused with a 2px `#4F46E5` ring.