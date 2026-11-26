# Project Brain

This file serves as the persistent, file-based memory layer and protocol entry point for this project. It stores durable knowledge, design decisions, and architecture details to ensure alignment across different AI coding agents and sessions.

## Cafe Identity
- **Name**: Wanderoot Café
- **Previous Name**: The Winter Line Cafe (renamed on 2026-09-09). A later typo "Wanderroot" was corrected on 2026-11-26 — do not reintroduce it. The "Winter Line" natural phenomenon references in content should be preserved as-is — only the cafe *brand name* was changed.

## Architecture
- **Framework**: Pure static HTML/CSS. 
- **Origin**: This project uses a 1:1 raw HTML export from the Stitch project "The Winter Line Cafe" (Project ID: `15985674307391738768`), subsequently renamed to "Wanderoot Café", combined with the interactive artisan menu & table reservation system.
- **Styling**: Relies on pre-compiled CSS and Tailwind classes, plus custom `<style>` blocks in each page's `<head>` for the loading animation and scroll effects.

## Navigation & Routing Rules
- **Menu / Home**: All "Menu" and primary home navigation links point to `index.html`. (`menu.html` is a byte-for-byte mirror of `index.html`; never link to it — always link to `index.html`, and keep both files in sync.)
- **About**: All "About" / "Our Story" links MUST point to `about.html`.
- **Reservation**: All "Reservation" and table booking links MUST point to `reservation.html`.
- **Billing**: All "Billing" / order-payment links MUST point to `billing.html`.
- **Reviews**: All "Reviews" links point to `review.html`.
- **Footer deep links**: `index.html#coffee` and `index.html#pastries` pre-select that menu category (handled in `index.html`).

## Shared Shell (identical on EVERY page — copy it, never restyle it per page)
Every page (`index.html`, `menu.html`, `about.html`, `reservation.html`, `billing.html`, `review.html`) uses the same:
- **Navigation bar** (sticky): logo → Menu, About, Reservation, Billing, Reviews, Tray, "Book Table". The current page's link carries `class="active"`. On Menu/Reservation the Tray button opens the order drawer; on other pages it links to `billing.html`. The badge reads `localStorage["wanderoot_cart"]`.
- **Footer** (`.site-footer`): same brand block, Navigation list (all five pages + category deep links), Hours & Contact, copyright line.
- **Design tokens** (`:root`): `--bg-creamy`, `--nav-bg`, `--brown-dark/-deep/-medium/-warm/-gold/-light/-border`, `--text-muted`, `--shadow-*`, `--radius-*`. Fonts: `EB Garamond` (headings) + `Plus Jakarta Sans` (body). Icons: Font Awesome 6.5.1.
- **Components**: `.hero` (dark-brown page header with `.small-heading`, `h1`, `p`), `.bottom-section` CTA band, `.toast` notifications (`showToast()`), pill buttons (25px radius). Use toasts instead of `alert()`.
- **Shell script**: one inline `<script>` placed immediately after `<body>` that injects the loader, runs the scroll blur, syncs `--nav-h`, and paints the Tray badge on pages without a drawer.
- **`<main>`**: all page content between the nav and the footer lives in a single `<main>` (that is what gets the scroll blur). Modals, drawers, floating buttons and toasts MUST stay outside `<main>` (a CSS `filter` would break their `position: fixed`).

## Loading Animation (MANDATORY — DO NOT REMOVE)
Every page (`index.html`, `about.html`, `reservation.html`, `menu.html`, and any future pages) **MUST** include the **kettle-pouring coffee loading animation**. This is a core brand element of Wanderoot Café and must always be present on every page load. The animation consists of:

1. **A full-screen overlay** (`#coffee-loader`) with the cafe's warm background color (`#faf8f5`), fixed position, `z-index: 9999`.
2. **A supplied vintage moka-pot image** (`assets/moka-pot-loader.png`) — a transparent 32-bit PNG asset with clean alpha transparency around the kettle contour and handle opening, ensuring it blends seamlessly into the cafe's warm `#faf8f5` theme without any white box or unblended background artifacts. The asset is animated with the `mokaPour` keyframes to tip toward the cup.
3. **A pouring stream** (`.pour-stream`) — a CSS stream that animates vertically using `streamPour` keyframes with opacity and scale transforms.
4. **Rising coffee fill** (`.coffee-fill`) — the CSS cup fills from bottom to top using `fillCup` keyframes.
5. **Fade-out**: After 2.1 seconds, the overlay fades to `opacity: 0` over 0.6s, then is removed from the DOM. (Same timing on every page.)

The CSS for this animation lives inside a `<style>` block in each page's `<head>`, and the JS that injects and removes the loader is the shared shell script at the very top of `<body>` (so there is no flash of un-loaded content).

> **CRITICAL AGENT INSTRUCTION**: This moka-pot pour loading animation is a non-negotiable brand identity element that MUST be present on every page. Keep `assets/moka-pot-loader.png` (and backward-compatible `assets/moka-pot-loader.jpg`) with the project. If you create a new page, copy the loader CSS and JS from an existing page. DO NOT remove, replace, or reintroduce white background boxes to the animation.

## Scroll Motion Blur
A subtle, velocity-responsive blur is applied to `<main>` while the page scrolls (never to the nav, drawers or modals):
- On `scroll`, `main` gets `filter: blur(Npx)` where N scales with scroll speed (max 1px).
- It eases back to `none` within a fraction of a second after scrolling stops (`transition: filter 0.15s ease-out`).
- Skipped entirely when the visitor has `prefers-reduced-motion: reduce`.
- Implemented once in the shared shell script — every page, including Billing and Reviews, gets it.

## Agent Protocol
- **Updating Memory**: Whenever you (an AI agent) make changes to the architecture, routing rules, or significant design elements, you MUST update this `BRAIN.md` file up to that change.
- **Consistency**: Do not introduce single-page application (SPA) patterns (like client-side routers or state managers) unless explicitly requested by the user, as the current architecture relies on static file navigation.
- **New Pages**: Any new page added to the project MUST include the kettle-pouring loading animation and scroll blur effect. Copy the shared shell (nav, footer, tokens, hero, shell `<script>`) from `billing.html` or `review.html`, which are the smallest pages.
- **Loading Animation Preservation**: The kettle-pour loading animation is a permanent brand requirement. Any agent working on this project must maintain this animation on all pages, regardless of other changes being made.

## Recent Changes
- **2026-11-26**: UI/UX consistency pass across all pages. (1) Brand name standardized to **Wanderoot Café** everywhere (fixed "Wanderroot cafe" in `about.html` header, body copy and footer). (2) `billing.html` and `review.html` now include the moka-pot loader and scroll blur; `reservation.html` gained the scroll blur it was missing (it had no `<main>`); loader timing unified at 2.1s (About used 3.1s, Menu/Reservation 1.8s). (3) One shared navigation bar and footer on every page, including Billing in all navs and Reviews in all footers; Billing's old "Home"/"Menu" duplicates and mobile-hidden links removed; `menu.html` links replaced by `index.html`; About's separate Tailwind header/footer replaced by the shared ones. (4) `billing.html` and `review.html` restyled onto the shared tokens/hero/cards/buttons; `alert()` popups replaced by the shared toast; Billing now refuses to confirm an empty tray. (5) Footer `#coffee` / `#pastries` links now actually filter the menu. (6) Page content wrapped in `<main>` on all pages; modals moved outside it.
- **2026-11-10**: Cleaned up the navigation bar on `about.html`, removing redundant placeholder options ("Sensory Haven", "Gallery", and "Find Us") to keep the header focused cleanly on Menu, About, Reservation, and Reviews.
- **2026-11-10**: Added the dedicated About page (`about.html`) directly from the Wanderoot Café project without altering its rich storytelling content. Integrated the About navigation link alongside the Reservation option across the primary navigation bars and footers in `index.html`, `reservation.html`, `menu.html`, and `review.html`. Synchronized `assets/moka-pot-loader.png` across all pages for the transparent moka-pot loading animation.
- **2026-10-20**: Streamlined repository to focus purely on the dedicated **Artisan Menu & Interactive Table Reservation** system. Set `index.html` directly to the Menu experience, added cross-linking between Menu and Reservation with pre-order tray synchronizer, brand SVG logos in navbars, and preserved the signature moka-pot loading animation across both pages.
- **2026-09-10**: Replaced the Home gallery card labeled “Gabled Tin Roofs & Stone Lintels” with the user-supplied local image `assets/gabled-tin-roofs-stone-lintels.jpg`. Keep this card source local for reliable local-host rendering.
- **2026-09-10**: Replaced the Home gallery's remote “Mussoorie Dusk Horizon” image with the user-supplied local asset `assets/mussoorie-dusk-horizon.jpg`. The card must retain this local source so it reliably loads when the site is served locally.
- **2026-09-10**: Synced the updated Stitch brand treatment: both page headers now render the local `assets/wanderoot-cafe-logo.svg` wordmark (WANDEROOT / CAFE & ROASTERY) in place of the previous emblem-and-text lockup.
- **2026-09-09**: Initialized project by exporting the "Home" (`index.html`) and "Our Story" (`about.html`) screens from Stitch Project ID `15985674307391738768`.
- **2026-09-09**: Added minimalist coffee-pouring loading animation. Animation plays on every page load.
- **2026-09-09**: Added subtle scroll motion blur effect (2px blur during scroll, clears after 100ms idle).
- **2026-09-09**: Renamed cafe from "The Winter Line Cafe" to "Wanderoot Café" across all pages. Natural phenomenon references to the "Winter Line" sunset preserved.
- **2026-09-10**: Replaced the loader's geometric kettle with the supplied vintage moka-pot illustration, stored locally at `assets/moka-pot-loader.png` (with transparent background).

## Features Implemented
- **Artisan Menu (`index.html` & `menu.html`)**: Complete interactive artisan menu with multi-angle food photography explorer (Hero, Top-Down, Close-up, Plated), real-time search, category/dietary filters, quantity counters, live Order Tray drawer with WhatsApp checkout, and 1-click transition to table reservation with pre-selected dishes attached.
- **About / Our Story Page (`about.html`)**: Complete brand narrative chronicling the founder's journey, architectural heritage, deodar & stone craft, living hearth philosophy, chapter ribbon navigation, and interactive sunset status.
- **Table Reservation System (`reservation.html`)**: Interactive visual floor plan (Veranda, Indoor Lounge, Pine Garden), slot scheduler, guest counter, live pre-ordered tray items summary preview, instant booking pass generator, 1-click Google Calendar & Apple/Outlook .ICS download, and localStorage persistence.
- **Guest Reviews Page (`review.html`)**: Interactive guest stories, accessible star rating submission, and review listings with localStorage persistence.
- **Billing Page (`billing.html`)**: Order summary read from the shared `wanderoot_cart`, customer details form with validation toasts, payment method selection, 5% tax calculation and order confirmation.
