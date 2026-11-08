# Project Brain

This file serves as the persistent, file-based memory layer and protocol entry point for this project. It stores durable knowledge, design decisions, and architecture details to ensure alignment across different AI coding agents and sessions.

## Cafe Identity
- **Name**: Wanderroot Cafe
- **Previous Name**: The Winter Line Cafe (renamed on 2026-09-09). The "Winter Line" natural phenomenon references in content should be preserved as-is — only the cafe *brand name* was changed.

## Architecture
- **Framework**: Pure static HTML/CSS. 
- **Origin**: This project uses a 1:1 raw HTML export from the Stitch project "The Winter Line Cafe" (Project ID: `15985674307391738768`), subsequently renamed to "Wanderroot Cafe".
- **Styling**: Relies entirely on the pre-compiled CSS classes embedded within the Stitch HTML export, plus custom `<style>` blocks in each page's `<head>` for the loading animation and scroll effects.

## Navigation & Routing Rules
- **Home**: All "Home" links MUST point to `index.html`.
- **Our Story**: All "Our Story" links MUST point to `about.html`.
- **Menu**: The Menu page is actively being developed by a separate AI agent team. Therefore, all "Menu" links, "Discover Our Menu" buttons, and Shopping Cart icons MUST point to `javascript:void(0)`. They should NOT use anchor links like `#menu` to ensure they don't scroll the current page.

## Loading Animation (MANDATORY — DO NOT REMOVE)
Every page (`index.html`, `about.html`, and any future pages) **MUST** include the **kettle-pouring coffee loading animation**. This is a core brand element of Wanderroot Cafe and must always be present on every page load. The animation consists of:

1. **A full-screen overlay** (`#coffee-loader`) with the cafe's warm background color (`#faf8f5`), fixed position, `z-index: 9999`.
2. **A supplied vintage moka-pot image** (`assets/moka-pot-loader.jpg`) — the local asset is animated with the `mokaPour` keyframes to tip toward the cup.
3. **A pouring stream** (`.pour-stream`) — a CSS stream that animates vertically using `streamPour` keyframes with opacity and scale transforms.
4. **Rising coffee fill** (`.coffee-fill`) — the CSS cup fills from bottom to top using `fillCup` keyframes.
5. **Fade-out**: After ~2.1 seconds, the overlay fades to `opacity: 0` over 0.6s, then is removed from the DOM.

The CSS for this animation lives inside a `<style>` block in each page's `<head>`, and the JS that injects and removes the loader runs via a `<script>` block also in the `<head>`.

> **CRITICAL AGENT INSTRUCTION**: This moka-pot pour loading animation is a non-negotiable brand identity element that MUST be present on every page. Keep `assets/moka-pot-loader.jpg` with the project. If you create a new page, copy the loader CSS and JS from an existing page. DO NOT remove, replace, or significantly modify the animation or its local asset without explicit user approval.

## Scroll Motion Blur
A subtle motion blur effect is applied to the page body during scroll events:
- On `scroll`, the body receives `filter: blur(2px)`.
- After 100ms of no scrolling, the blur is cleared back to `blur(0px)`.
- The body has `transition: filter 0.15s ease-out` for smooth application and removal.
- This JS lives alongside the loader script in the `<head>` `<script>` block.

## Agent Protocol
- **Updating Memory**: Whenever you (an AI agent) make changes to the architecture, routing rules, or significant design elements, you MUST update this `BRAIN.md` file up to that change.
- **Consistency**: Do not introduce single-page application (SPA) patterns (like client-side routers or state managers) unless explicitly requested by the user, as the current architecture relies on static file navigation.
- **New Pages**: Any new page added to the project MUST include the kettle-pouring loading animation and scroll blur effect. Copy the `<style>` and `<script>` blocks from `index.html` or `about.html`.
- **Loading Animation Preservation**: The kettle-pour loading animation is a permanent brand requirement. Any agent working on this project must maintain this animation on all pages, regardless of other changes being made.

## Recent Changes
- **2026-09-10**: Replaced the Home gallery card labeled “Gabled Tin Roofs & Stone Lintels” with the user-supplied local image `assets/gabled-tin-roofs-stone-lintels.jpg`. Keep this card source local for reliable local-host rendering.
- **2026-09-10**: Replaced the Home gallery's remote “Mussoorie Dusk Horizon” image with the user-supplied local asset `assets/mussoorie-dusk-horizon.jpg`. The card must retain this local source so it reliably loads when the site is served locally.
- **2026-09-10**: Synced the updated Stitch brand treatment: both page headers now render the local `assets/wanderoot-cafe-logo.svg` wordmark (WANDEROOT / CAFE & ROASTERY) in place of the previous emblem-and-text lockup. Also synced the refreshed Himalayan veranda image on the Home page. The wordmark asset must remain local and be used for future page headers.
- **2026-09-10**: Audited the supplied Stitch export and confirmed that `index.html` retains the `home_the_winter_line_cafe_1` visual system and `about.html` retains the `our_story_the_winter_line_cafe_2` visual system, with Wanderroot branding and the existing routing rules preserved. Updated both pages' scroll motion to the newer Stitch velocity-responsive blur treatment (maximum 1px), scoped to `<main>` so the fixed navigation and controls remain sharp and functional. The permanent kettle-pour loader remains in place on both pages.
- **2026-09-09**: Initialized project by exporting the "Home" (`index.html`) and "Our Story" (`about.html`) screens from Stitch Project ID `15985674307391738768`.
- **2026-09-09**: Applied navigation routing rules to `index.html` and `about.html`, setting cross-links and converting Menu and Cart links to `javascript:void(0)`.
- **2026-09-09**: Added minimalist coffee-pouring loading animation to both `index.html` and `about.html`. Animation plays on every page load.
- **2026-09-09**: Added subtle scroll motion blur effect (2px blur during scroll, clears after 100ms idle).
- **2026-09-09**: Renamed cafe from "The Winter Line Cafe" to "Wanderroot Cafe" across all pages (header, hero, footer, copyright, social handle). Natural phenomenon references to the "Winter Line" sunset preserved.
- **2026-09-10**: Replaced the loader's geometric kettle with the supplied vintage moka-pot illustration, stored locally at `assets/moka-pot-loader.jpg`. Both pages animate the moka pot tipping, coffee stream, and cup fill before fading the overlay. The loader is scaled to 84% and has a slower 3.1-second presentation to keep the motion calm and unobtrusive. This local asset must be retained with the loader implementation.
- **2026-10-20**: Streamlined repository to focus purely on the dedicated **Artisan Menu & Interactive Table Reservation** system. Removed peripheral pages (`about.html`, `reviews.html`) and legacy Stitch scraper metadata. Set `index.html` directly to the Menu experience, added cross-linking between Menu and Reservation with pre-order tray synchronizer, brand SVG logos in navbars, and preserved the signature moka-pot loading animation across both pages.

## Features Implemented
- **Artisan Menu (`index.html` & `menu.html`)**: Complete interactive artisan menu with multi-angle food photography explorer (Hero, Top-Down, Close-up, Plated), real-time search, category/dietary filters, quantity counters, live Order Tray drawer with WhatsApp checkout, and 1-click transition to table reservation with pre-selected dishes attached.
- **Table Reservation System (`reservation.html`)**: Interactive visual floor plan (Veranda, Indoor Lounge, Pine Garden), slot scheduler, guest counter, live pre-ordered tray items summary preview, instant booking pass generator, 1-click Google Calendar & Apple/Outlook .ICS download, and localStorage persistence.
