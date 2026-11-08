# Wanderoot Café — Menu & Table Reservation System

A standalone, artisanal web platform designed specifically for **Menu Browsing** and **Interactive Table Reservations** for Wanderoot Café & Roastery, Landour, Mussoorie.

---

## ☕ Key Features

### 1. Artisan Menu & Multi-Angle Food Explorer (`index.html` & `menu.html`)
- **Interactive Multi-Angle Inspector**: View dishes from 3 to 4 distinct angles (Hero Front, Overhead Top-Down, Close-up Froth/Crumb, Setting/Plated).
- **Category Filtering**: Easily toggle between:
  - Specialty Roasted Coffees & Brews
  - Fresh Butter Croissants & Viennoiserie
  - Artisan Layer Cakes, Tarts & Cheesecakes
  - Gourmet Savory & Brunch
  - Ceremonial Teas, Matcha & Coolers
- **Dietary Badges & Toggles**: Filter instantly by *Pure Vegetarian*, *Bestsellers*, or *Chef's Choice*.
- **Seamless Reservation Link**: Instant 1-click CTA on every dish to book a table to savor it in person.

### 2. Interactive Table Reservation System (`reservation.html`)
- **Interactive Visual Floor Plan**: Select between:
  - *The Veranda* (Scenic mountain valley window views)
  - *Indoor Fireplace Lounge* (Cozy hearth booths)
  - *Pine Garden Patio* (Open-air seating under deodar cedar trees)
- **Smart Booking Form**: Date picker, time slot selector, guest count sync, and occasion customization.
- **Digital Pass & Ticket Generator**: Generates instant confirmation pass reference codes (`WND-XXXXX`).
- **Calendar & Notification Sync**: 1-click export to **Google Calendar**, **Apple/Outlook (.ICS)**, and direct **WhatsApp** reservation notification.
- **Active Bookings Manager**: View and manage upcoming table reservations saved securely in browser storage.

### 3. Signature Brand Identity
- **Vintage Moka-Pot Pour Animation**: Branded kettle-pouring coffee loading animation on page load (`assets/moka-pot-loader.jpg`).
- **Official Brand Typography**: Custom styling with `EB Garamond` serif and `Plus Jakarta Sans`.

---

## 📁 Repository Structure

```
.
├── assets/
│   ├── gabled-tin-roofs-stone-lintels.jpg
│   ├── moka-pot-loader.jpg
│   ├── mussoorie-dusk-horizon.jpg
│   └── wanderoot-cafe-logo.svg
├── index.html         # Main entry point (Artisan Menu)
├── menu.html          # Synchronized Menu page
├── reservation.html   # Interactive Table Reservation System
├── BRAIN.md           # Project architecture and design memory
├── README.md          # Documentation
└── .gitignore
```

---

## 🚀 Running Locally

No build tools or Node.js dependencies are required. This is a pure static web platform.

1. Simply double-click `index.html` or run:
   ```bash
   open index.html
   ```
2. Or serve via any local HTTP server:
   ```bash
   python3 -m http.server 8080
   ```
   and visit `http://localhost:8080`.
