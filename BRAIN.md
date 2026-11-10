# Project Brain

This file serves as the persistent, file-based memory layer and protocol entry point for this project. It stores durable knowledge, design decisions, and architecture details to ensure alignment across different AI coding agents and sessions.

## Cafe Identity
- **Name**: Wanderroot Cafe
- **Previous Name**: The Winter Line Cafe (renamed on 2026-09-09). The "Winter Line" natural phenomenon references in content should be preserved as-is — only the cafe *brand name* was changed.

## Architecture
- **Framework**: Pure static HTML/CSS. 
- **Origin**: This project uses a 1:1 raw HTML export from the Stitch project "The Winter Line Cafe" (Project ID: `15985674307391738768`), subsequently renamed to "Wanderroot Cafe", combined with the interactive artisan menu & table reservation system.
- **Styling**: Relies on pre-compiled CSS and Tailwind classes, plus custom `<style>` blocks in each page's `<head>` for the loading animation and scroll effects.

## Navigation & Routing Rules
- **Menu / Home**: All "Menu" and primary home navigation links point to `index.html`.
- **About**: All "About" / "Our Story" links MUST point to `about.html`.
- **Reservation**: All "Reservation" and table booking links MUST point to `reservation.html`.
- **Reviews**: All "Reviews" links point to `review.html`.

## Loading Animation (MANDATORY — DO NOT REMOVE)
Every page (`index.html`, `about.html`, `reservation.html`, `menu.html`, and any future pages) **MUST** include the **kettle-pouring coffee loading animation**. This is a core brand element of Wanderroot Cafe and must always be present on every page load. The animation consists of:

1. **A full-screen overlay** (`#coffee-loader`) with the cafe's warm background color (`#faf8f5`), fixed position, `z-index: 9999`.
2. **A supplied vintage moka-pot image** (`assets/moka-pot-loader.png`) — a transparent 32-bit PNG asset with clean alpha transparency around the kettle contour and handle opening, ensuring it blends seamlessly into the cafe's warm `#faf8f5` theme without any white box or unblended background artifacts. The asset is animated with the `mokaPour` keyframes to tip toward the cup.
3. **A pouring stream** (`.pour-stream`) — a CSS stream that animates vertically using `streamPour` keyframes with opacity and scale transforms.
4. **Rising coffee fill** (`.coffee-fill`) — the CSS cup fills from bottom to top using `fillCup` keyframes.
5. **Fade-out**: After ~2.1 seconds, the overlay fades to `opacity: 0` over 0.6s, then is removed from the DOM.

The CSS for this animation lives inside a `<style>` block in each page's `<head>`, and the JS that injects and removes the loader runs via a `<script>` block also in the `<head>` or at DOM load.

> **CRITICAL AGENT INSTRUCTION**: This moka-pot pour loading animation is a non-negotiable brand identity element that MUST be present on every page. Keep `assets/moka-pot-loader.png` (and backward-compatible `assets/moka-pot-loader.jpg`) with the project. If you create a new page, copy the loader CSS and JS from an existing page. DO NOT remove, replace, or reintroduce white background boxes to the animation.

## Scroll Motion Blur
A subtle motion blur effect is applied to the page body during scroll events:
- On `scroll`, the body receives `filter: blur(2px)` (or velocity-responsive blur up to 1px on main).
- After 100ms of no scrolling, the blur is cleared back to `blur(0px)`.
- The element has `transition: filter 0.15s ease-out` for smooth application and removal.

## Agent Protocol
- **Updating Memory**: Whenever you (an AI agent) make changes to the architecture, routing rules, or significant design elements, you MUST update this `BRAIN.md` file up to that change.
- **Consistency**: Do not introduce single-page application (SPA) patterns (like client-side routers or state managers) unless explicitly requested by the user, as the current architecture relies on static file navigation.
- **New Pages**: Any new page added to the project MUST include the kettle-pouring loading animation and scroll blur effect. Copy the `<style>` and `<script>` blocks from `index.html` or `about.html`.
- **Loading Animation Preservation**: The kettle-pour loading animation is a permanent brand requirement. Any agent working on this project must maintain this animation on all pages, regardless of other changes being made.

## Recent Changes
- **2026-11-10**: Cleaned up the navigation bar on `about.html`, removing redundant placeholder options ("Sensory Haven", "Gallery", and "Find Us") to keep the header focused cleanly on Menu, About, Reservation, and Reviews.
- **2026-11-10**: Added the dedicated About page (`about.html`) directly from the Wanderroot Cafe project without altering its rich storytelling content. Integrated the About navigation link alongside the Reservation option across the primary navigation bars and footers in `index.html`, `reservation.html`, `menu.html`, and `review.html`. Synchronized `assets/moka-pot-loader.png` across all pages for the transparent moka-pot loading animation.
- **2026-10-20**: Streamlined repository to focus purely on the dedicated **Artisan Menu & Interactive Table Reservation** system. Set `index.html` directly to the Menu experience, added cross-linking between Menu and Reservation with pre-order tray synchronizer, brand SVG logos in navbars, and preserved the signature moka-pot loading animation across both pages.
- **2026-09-10**: Replaced the Home gallery card labeled “Gabled Tin Roofs & Stone Lintels” with the user-supplied local image `assets/gabled-tin-roofs-stone-lintels.jpg`. Keep this card source local for reliable local-host rendering.
- **2026-09-10**: Replaced the Home gallery's remote “Mussoorie Dusk Horizon” image with the user-supplied local asset `assets/mussoorie-dusk-horizon.jpg`. The card must retain this local source so it reliably loads when the site is served locally.
- **2026-09-10**: Synced the updated Stitch brand treatment: both page headers now render the local `assets/wanderoot-cafe-logo.svg` wordmark (WANDEROOT / CAFE & ROASTERY) in place of the previous emblem-and-text lockup.
- **2026-09-09**: Initialized project by exporting the "Home" (`index.html`) and "Our Story" (`about.html`) screens from Stitch Project ID `15985674307391738768`.
- **2026-09-09**: Added minimalist coffee-pouring loading animation. Animation plays on every page load.
- **2026-09-09**: Added subtle scroll motion blur effect (2px blur during scroll, clears after 100ms idle).
- **2026-09-09**: Renamed cafe from "The Winter Line Cafe" to "Wanderroot Cafe" across all pages. Natural phenomenon references to the "Winter Line" sunset preserved.
- **2026-09-10**: Replaced the loader's geometric kettle with the supplied vintage moka-pot illustration, stored locally at `assets/moka-pot-loader.png` (with transparent background).

## Features Implemented
- **Artisan Menu (`index.html` & `menu.html`)**: Complete interactive artisan menu with multi-angle food photography explorer (Hero, Top-Down, Close-up, Plated), real-time search, category/dietary filters, quantity counters, live Order Tray drawer with WhatsApp checkout, and 1-click transition to table reservation with pre-selected dishes attached.
- **About / Our Story Page (`about.html`)**: Complete brand narrative chronicling the founder's journey, architectural heritage, deodar & stone craft, living hearth philosophy, chapter ribbon navigation, and interactive sunset status.
- **Table Reservation System (`reservation.html`)**: Interactive visual floor plan (Veranda, Indoor Lounge, Pine Garden), slot scheduler, guest counter, live pre-ordered tray items summary preview, instant booking pass generator, 1-click Google Calendar & Apple/Outlook .ICS download, and localStorage persistence.
- **Guest Reviews Page (`review.html`)**: Interactive guest stories, star rating submission, and review listings with localStorage persistence.
