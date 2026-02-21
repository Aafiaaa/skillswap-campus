# SkillSwap Campus 

---

## Basic Details

**Team Name:** CodeCraft

---

## Team Members

* **Member 1:** Aafia Gause– Muthoot Institute of Technology and Science
* **Member 2:** Pavithra V S – Muthoot Institute of Technology and Science

---

## Hosted Project Link

[Add your hosted link here – e.g., [https://skillswap-campus.onrender.com](https://skillswap-campus.onrender.com)]

---

# Project Description

SkillSwap Campus is a gamified peer-to-peer skill exchange platform designed for students.
It allows students to teach what they know and learn what they want — while earning XP, building streaks, and leveling up like a game.

---

# The Problem Statement

Students often:

* Want to learn new skills but can’t afford expensive courses
* Have valuable skills but no platform to teach
* Struggle to find like-minded peers within campus
* Lack motivation to consistently learn

There is no structured, engaging ecosystem for peer-to-peer skill exchange within campuses.

---

#  The Solution

SkillSwap Campus creates a gamified skill-exchange ecosystem where:

* Students register skills they can teach and skills they want to learn
* The platform automatically matches compatible users
* Students chat and arrange sessions
* Each exchange increases XP and unlocks progression

Learning becomes collaborative, competitive, and addictive.

---

# Technical Details

## For Software

### Languages Used

* Python
* HTML
* CSS
* JavaScript

### Frameworks Used

* Flask

### Libraries Used

* Werkzeug (Flask internal)

### Tools Used

* VS Code
* Git
* GitHub

---

# Features

### 🔹 Feature 1: Skill Matching System

Matches users based on teach ↔ learn compatibility.

### 🔹 Feature 2: In-App Chat Dashboard

Dynamic chat interface that loads conversations without page reload.

### 🔹 Feature 3: Gamified Landing Page

Retro game-inspired UI with animations, interactive modal, and pixel theme.

### 🔹 Feature 4: XP & Exchange Tracking

Users level up based on successful skill exchanges.

### 🔹 Feature 5: Modal-Based Registration

Blur background + centered pop-up registration form.

---

#  Implementation

## For Software

### Installation

```bash
git clone https://github.com/yourusername/skillswap-campus.git
cd skillswap-campus
pip install flask
```

---

### Run

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

# Project Documentation

## Screenshots

### Landing Page

![Screenshot1](![alt text](image-1.png))
Retro game-style animated homepage with PRESS START modal transition.

---

### Dashboard & Match View

![Screenshot2](![alt text](image-3.png))
Dynamic match list with real-time style chat interface.

---

### Registration Modal

![Screenshot3](![alt text](image-2.png))
Blur background + centered skill profile creation form.

---

# System Architecture

## Architecture Diagram

Frontend (HTML/CSS/JS)
⬇
Flask Backend (Python)
⬇
In-memory User Storage

* User submits registration
* Flask stores user in list
* Matching algorithm compares teach/learn fields
* Chat stored in dictionary-based structure

---

## Application Workflow

1. User lands on homepage
2. Press Start opens modal
3. User registers skill profile
4. Backend matches compatible users
5. Dashboard displays matches
6. Chat initiated
7. XP increases

---

# AI Tools Used (Transparency Bonus)

### Tool Used

ChatGPT

### Purpose

* UI design structuring
* CSS animation refinement
* Debugging Flask errors
* README documentation structuring

### Example Prompts Used

* “Create modal blur background effect”
* “Fix Flask KeyError email issue”
* “Create dashboard with same-page chat loading”

### Percentage of AI-Generated Code

Approximately 20–30% (UI structuring assistance)

### Human Contributions

* Core architecture
* Matching logic
* Chat logic
* UI design decisions
* System integration
* Testing & debugging

---

# Team Contributions

**Aafia Gause:**

* Backend development (Flask routes, matching logic)
* Chat system implementation
* Gamification structure
* UI styling and theme integration

**Pavithra V S:**

* Frontend UI enhancement
* Modal integration
* Design alignment
* Testing & debugging

---

# Hackathon Vision

SkillSwap Campus is designed not just as a project, but as a scalable campus startup model.

It encourages:

* Collaborative learning
* Gamified skill progression
* Peer-driven knowledge exchange

With further development, it can become a full campus-wide learning ecosystem.

---