# Wanderoot Café — Menu, Reservation, Billing & Reviews

A standalone, artisanal web platform for **Menu Browsing**, **Interactive Table Reservations**, **Billing** and **Guest Reviews** for Wanderoot Café & Roastery, Landour, Mussoorie.

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

### 3. Our Story, Billing & Guest Reviews
- **Our Story (`about.html`)**: The founder's journey, architecture and the Winter Line sunset status.
- **Billing (`billing.html`)**: Order summary from your tray, customer details, payment method selection and confirmation.
- **Guest Reviews (`review.html`)**: Read guest stories and add your own star rating and review (saved in your browser).

### 4. Signature Brand Identity (identical on every page)
- **Vintage Moka-Pot Pour Animation**: Branded coffee-pouring loading animation on every page load (`assets/moka-pot-loader.png`).
- **Scroll Motion Blur**: A subtle, velocity-responsive blur on page content while scrolling (disabled for visitors who prefer reduced motion).
- **One Navigation & Footer**: Menu · About · Reservation · Billing · Reviews on every page.
- **Official Brand Typography**: Custom styling with `EB Garamond` serif and `Plus Jakarta Sans`.

---

## 📁 Repository Structure

```
.
├── assets/
│   ├── gabled-tin-roofs-stone-lintels.jpg
│   ├── moka-pot-loader.jpg
│   ├── moka-pot-loader.png
│   ├── mussoorie-dusk-horizon.jpg
│   └── wanderoot-cafe-logo.svg
├── index.html         # Main entry point (Artisan Menu)
├── menu.html          # Mirror of index.html (keep in sync)
├── about.html         # Our Story
├── reservation.html   # Interactive Table Reservation System
├── billing.html       # Billing & Payment
├── review.html        # Guest Reviews
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
