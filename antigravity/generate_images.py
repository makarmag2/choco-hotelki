# -*- coding: utf-8 -*-
import os

img_dir = r"c:\Users\user\Downloads\antigravity\img"
os.makedirs(img_dir, exist_ok=True)

# 1. rod1.svg - Поплавочная удочка Золотой Карась
rod1_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bgLight" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#1c202d"/>
      <stop offset="60%" stop-color="#0c0e16"/>
      <stop offset="100%" stop-color="#06070a"/>
    </radialGradient>
    <linearGradient id="carbon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4a4d5a"/>
      <stop offset="25%" stop-color="#21232b"/>
      <stop offset="50%" stop-color="#14151a"/>
      <stop offset="75%" stop-color="#2d303b"/>
      <stop offset="100%" stop-color="#111216"/>
    </linearGradient>
    <linearGradient id="cork" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#dfbb89"/>
      <stop offset="30%" stop-color="#cda36e"/>
      <stop offset="70%" stop-color="#b68852"/>
      <stop offset="100%" stop-color="#936737"/>
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f5d799"/>
      <stop offset="50%" stop-color="#c9a96e"/>
      <stop offset="100%" stop-color="#8b6831"/>
    </linearGradient>
    <linearGradient id="floatRed" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff3b30"/>
      <stop offset="70%" stop-color="#c41c13"/>
      <stop offset="100%" stop-color="#800b05"/>
    </linearGradient>
    <linearGradient id="floatWhite" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#d0d5dd"/>
      <stop offset="100%" stop-color="#98a2b3"/>
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="castShadow" x="-10%" y="-10%" width="120%" height="150%">
      <feDropShadow dx="0" dy="15" stdDeviation="12" flood-color="#000000" flood-opacity="0.8"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="600" height="400" fill="url(#bgLight)"/>
  
  <!-- Subtle Studio Light Spot -->
  <ellipse cx="320" cy="210" rx="220" ry="90" fill="#c9a96e" opacity="0.06" filter="url(#softGlow)"/>
  <ellipse cx="280" cy="270" rx="240" ry="30" fill="#000000" opacity="0.6" filter="url(#softGlow)"/>

  <!-- Rod Reflection -->
  <path d="M 60 260 L 520 180" stroke="#c9a96e" stroke-width="6" opacity="0.1" filter="url(#softGlow)"/>

  <!-- Float (Поплавок) -->
  <g transform="translate(370, 240) rotate(-18)" filter="url(#castShadow)">
    <!-- Antenna -->
    <line x1="0" y1="-50" x2="0" y2="0" stroke="#ffe600" stroke-width="2.5" stroke-linecap="round"/>
    <circle cx="0" cy="-52" r="3.5" fill="#ff3b30" filter="url(#softGlow)"/>
    <!-- Body top red -->
    <ellipse cx="0" cy="10" rx="9" ry="16" fill="url(#floatRed)"/>
    <!-- Body bottom white -->
    <path d="M -9 10 Q 0 45 0 55 Q 0 45 9 10 Z" fill="url(#floatWhite)"/>
    <!-- Gold accent rings -->
    <rect x="-8.5" y="8" width="17" height="3" fill="url(#gold)"/>
    <!-- Stem -->
    <line x1="0" y1="55" x2="0" y2="90" stroke="#222" stroke-width="2"/>
    <circle cx="0" cy="90" r="1.5" fill="#888"/>
  </g>

  <!-- Main Rod Blank (Бланк удочки) -->
  <g filter="url(#castShadow)">
    <!-- Cork handle -->
    <path d="M 40 290 L 170 248" stroke="url(#cork)" stroke-width="17" stroke-linecap="round"/>
    <path d="M 40 290 L 170 248" stroke="#000" stroke-width="17" stroke-opacity="0.15" stroke-dasharray="2 6" stroke-linecap="round"/>
    <!-- Butt Cap & Reel Seat Gold Rings -->
    <path d="M 36 291 L 46 288" stroke="url(#gold)" stroke-width="19" stroke-linecap="round"/>
    <path d="M 125 262 L 145 256" stroke="url(#gold)" stroke-width="19"/>
    <path d="M 160 251 L 172 247" stroke="url(#gold)" stroke-width="18"/>

    <!-- Carbon blank tapering -->
    <path d="M 170 248 L 320 200" stroke="url(#carbon)" stroke-width="9" stroke-linecap="round"/>
    <path d="M 315 202 L 460 155" stroke="url(#carbon)" stroke-width="6" stroke-linecap="round"/>
    <path d="M 455 157 L 560 120" stroke="url(#carbon)" stroke-width="3" stroke-linecap="round"/>

    <!-- Gold Guide Rings (Пропускные кольца) -->
    <!-- Guide 1 -->
    <g transform="translate(240, 226) rotate(-17)">
      <path d="M 0 0 L 0 -18" stroke="url(#gold)" stroke-width="2"/>
      <ellipse cx="0" cy="-20" rx="6" ry="9" fill="none" stroke="url(#gold)" stroke-width="2.5"/>
      <ellipse cx="0" cy="-20" rx="4" ry="7" fill="none" stroke="#2b384e" stroke-width="1.8"/>
    </g>
    <!-- Guide 2 -->
    <g transform="translate(360, 187) rotate(-17)">
      <path d="M 0 0 L 0 -14" stroke="url(#gold)" stroke-width="1.8"/>
      <ellipse cx="0" cy="-16" rx="4.5" ry="7" fill="none" stroke="url(#gold)" stroke-width="2"/>
      <ellipse cx="0" cy="-16" rx="3" ry="5.5" fill="none" stroke="#2b384e" stroke-width="1.5"/>
    </g>
    <!-- Guide 3 -->
    <g transform="translate(470, 151) rotate(-17)">
      <path d="M 0 0 L 0 -10" stroke="url(#gold)" stroke-width="1.5"/>
      <ellipse cx="0" cy="-12" rx="3.5" ry="5" fill="none" stroke="url(#gold)" stroke-width="1.6"/>
      <ellipse cx="0" cy="-12" rx="2.2" ry="4" fill="none" stroke="#2b384e" stroke-width="1.2"/>
    </g>
    <!-- Tip Guide (Тюльпан) -->
    <g transform="translate(560, 120) rotate(-17)">
      <ellipse cx="0" cy="-6" rx="2.5" ry="3.5" fill="none" stroke="url(#gold)" stroke-width="1.5"/>
    </g>

    <!-- Monofilament Line glint (Леска) -->
    <path d="M 135 258 Q 280 260 370 240 Q 460 210 560 120" fill="none" stroke="#ffffff" stroke-width="0.8" opacity="0.6"/>
  </g>

  <!-- Realistic Water Droplets with highlights -->
  <circle cx="160" cy="242" r="3" fill="#ffffff" opacity="0.7" filter="url(#softGlow)"/>
  <circle cx="161" cy="241" r="1" fill="#fff"/>
  <circle cx="270" cy="214" r="2.5" fill="#ffffff" opacity="0.6"/>
  <circle cx="410" cy="172" r="2" fill="#ffffff" opacity="0.7"/>

  <!-- Badge label watermark -->
  <text x="50" y="360" font-family="'Montserrat', sans-serif" font-size="12" font-weight="700" letter-spacing="3" fill="#c9a96e" opacity="0.4">CARBON MATRIX 4.0M CLASSIC</text>
</svg>"""

# 2. rod2.svg - Спиннинг Щука Про
rod2_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bgPredator" cx="55%" cy="45%" r="70%">
      <stop offset="0%" stop-color="#15212b"/>
      <stop offset="50%" stop-color="#0c1218"/>
      <stop offset="100%" stop-color="#05080c"/>
    </radialGradient>
    <linearGradient id="metallicCarbon" x1="0%" y1="0%" x2="100%" y2="50%">
      <stop offset="0%" stop-color="#606775"/>
      <stop offset="25%" stop-color="#2a2e38"/>
      <stop offset="50%" stop-color="#101217"/>
      <stop offset="75%" stop-color="#3f4552"/>
      <stop offset="100%" stop-color="#14171d"/>
    </linearGradient>
    <linearGradient id="evaFoam" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#30333d"/>
      <stop offset="50%" stop-color="#1e2027"/>
      <stop offset="100%" stop-color="#111317"/>
    </linearGradient>
    <linearGradient id="reelTitanium" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a6b4c9"/>
      <stop offset="30%" stop-color="#5a6577"/>
      <stop offset="70%" stop-color="#2b323d"/>
      <stop offset="100%" stop-color="#151920"/>
    </linearGradient>
    <linearGradient id="braidLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00e5ff"/>
      <stop offset="50%" stop-color="#00b0ff"/>
      <stop offset="100%" stop-color="#0077c2"/>
    </linearGradient>
    <linearGradient id="goldAccent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffe082"/>
      <stop offset="50%" stop-color="#ffb300"/>
      <stop offset="100%" stop-color="#c67c00"/>
    </linearGradient>
    <filter id="softGlow2" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="castShadow2" x="-15%" y="-15%" width="130%" height="150%">
      <feDropShadow dx="2" dy="16" stdDeviation="14" flood-color="#000000" flood-opacity="0.9"/>
    </filter>
  </defs>

  <rect width="600" height="400" fill="url(#bgPredator)"/>
  
  <!-- Cool cyan/teal back ambient highlight -->
  <circle cx="340" cy="180" r="160" fill="#00b4d8" opacity="0.08" filter="url(#softGlow2)"/>
  <ellipse cx="280" cy="300" rx="250" ry="25" fill="#000" opacity="0.7" filter="url(#softGlow2)"/>

  <!-- Reel and Handle Group -->
  <g filter="url(#castShadow2)">
    <!-- Split EVA Grip Handle (Разнесенная рукоятка) -->
    <path d="M 50 310 L 95 292" stroke="url(#evaFoam)" stroke-width="22" stroke-linecap="round"/>
    <path d="M 45 312 L 52 309" stroke="url(#goldAccent)" stroke-width="23" stroke-linecap="round"/>
    <!-- Exposed blank section -->
    <path d="M 95 292 L 135 277" stroke="url(#metallicCarbon)" stroke-width="12"/>
    <path d="M 135 277 L 180 260" stroke="url(#evaFoam)" stroke-width="22" stroke-linecap="round"/>
    <!-- Reel seat lock nut -->
    <path d="M 165 266 L 176 262" stroke="url(#goldAccent)" stroke-width="24"/>

    <!-- Spinning Reel (Катушка) -->
    <g transform="translate(155, 268)">
      <!-- Reel stem (Лапка катушки) -->
      <path d="M 0 0 L 15 35 L 30 45" stroke="url(#reelTitanium)" stroke-width="10" stroke-linecap="round" fill="none"/>
      <!-- Reel Body (Корпус) -->
      <ellipse cx="38" cy="55" rx="26" ry="19" fill="url(#reelTitanium)"/>
      <circle cx="38" cy="55" r="12" fill="#111" stroke="url(#goldAccent)" stroke-width="2"/>
      
      <!-- Spool (Шпуля) -->
      <path d="M 15 35 L 48 22 L 60 52 L 27 65 Z" fill="url(#reelTitanium)"/>
      <!-- Braid line on spool (Плетеный шнур) -->
      <rect x="25" y="32" width="22" height="22" rx="4" transform="rotate(-23 36 43)" fill="url(#braidLine)"/>
      <!-- Rotor & Bail arm (Дужка лесоукладывателя) -->
      <path d="M 10 32 Q 35 10 58 28" fill="none" stroke="url(#goldAccent)" stroke-width="3.5"/>
      <circle cx="10" cy="32" r="3" fill="#fff"/>
      
      <!-- Reel Handle (Рукоять катушки с кнобом) -->
      <path d="M 38 55 L 48 85 L 68 95" fill="none" stroke="url(#reelTitanium)" stroke-width="6" stroke-linecap="round"/>
      <ellipse cx="74" cy="98" rx="8" ry="13" fill="url(#evaFoam)" stroke="#555" stroke-width="1"/>
    </g>

    <!-- Predator Carbon Blank (Сверхмощный бланк) -->
    <path d="M 180 260 L 340 195" stroke="url(#metallicCarbon)" stroke-width="10" stroke-linecap="round"/>
    <!-- Cross carbon fiber texture -->
    <path d="M 180 260 L 340 195" stroke="#fff" stroke-width="10" stroke-dasharray="1 8" stroke-opacity="0.15" stroke-linecap="round"/>
    <path d="M 335 197 L 470 142" stroke="url(#metallicCarbon)" stroke-width="6.5" stroke-linecap="round"/>
    <path d="M 465 144 L 565 102" stroke="url(#metallicCarbon)" stroke-width="3.5" stroke-linecap="round"/>

    <!-- High-frame SiC Guides (Титановые кольца SiC) -->
    <!-- Big Stripper Guide -->
    <g transform="translate(265, 226) rotate(-22)">
      <path d="M 0 0 L 6 -24 M -6 0 L 0 -24" stroke="url(#reelTitanium)" stroke-width="2.5" fill="none"/>
      <ellipse cx="2" cy="-28" rx="10" ry="14" fill="none" stroke="url(#reelTitanium)" stroke-width="3"/>
      <ellipse cx="2" cy="-28" rx="7.5" ry="11.5" fill="none" stroke="#0a0c10" stroke-width="2.5"/>
    </g>
    <!-- Middle Guide -->
    <g transform="translate(375, 181) rotate(-22)">
      <path d="M 0 0 L 3 -16 M -4 0 L 0 -16" stroke="url(#reelTitanium)" stroke-width="2" fill="none"/>
      <ellipse cx="1" cy="-19" rx="6" ry="9" fill="none" stroke="url(#reelTitanium)" stroke-width="2.5"/>
      <ellipse cx="1" cy="-19" rx="4.5" ry="7" fill="none" stroke="#0a0c10" stroke-width="2"/>
    </g>
    <!-- Small Guide -->
    <g transform="translate(480, 138) rotate(-22)">
      <path d="M 0 0 L 0 -10" stroke="url(#reelTitanium)" stroke-width="1.8"/>
      <ellipse cx="0" cy="-12" rx="4" ry="6" fill="none" stroke="url(#reelTitanium)" stroke-width="2"/>
    </g>
    <!-- Tip -->
    <circle cx="565" cy="102" r="3" fill="url(#goldAccent)"/>

    <!-- Bright Blue Braided Line tension (Шнур) -->
    <path d="M 180 300 Q 260 210 375 162 T 565 102" fill="none" stroke="#00d4ff" stroke-width="1.2" opacity="0.8" filter="url(#softGlow2)"/>
  </g>

  <!-- Lure (Блесна щучья на переднем плане) -->
  <g transform="translate(430, 275) rotate(15)" filter="url(#castShadow2)">
    <path d="M 0 0 Q 30 -15 65 0 Q 30 15 0 0 Z" fill="url(#goldAccent)" stroke="#fff" stroke-width="0.8"/>
    <circle cx="12" cy="0" r="3" fill="#ff3b30"/>
    <circle cx="12" cy="0" r="1.5" fill="#000"/>
    <!-- Scales texture -->
    <path d="M 22 -6 L 22 6 M 34 -8 L 34 8 M 46 -6 L 46 6" stroke="#9e6600" stroke-width="1.5"/>
    <!-- Treble hook -->
    <path d="M 65 0 L 80 0 M 76 -7 Q 82 0 76 7" stroke="#889" stroke-width="2" fill="none"/>
  </g>

  <text x="50" y="360" font-family="'Montserrat', sans-serif" font-size="12" font-weight="800" letter-spacing="3" fill="#00b4d8" opacity="0.5">FAST ACTION / 10-35G TITANIUM</text>
</svg>"""

# 3. rod3.svg - Детская удочка Малёк
rod3_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bgKids" cx="50%" cy="50%" r="65%">
      <stop offset="0%" stop-color="#1f242e"/>
      <stop offset="60%" stop-color="#101319"/>
      <stop offset="100%" stop-color="#08090d"/>
    </radialGradient>
    <linearGradient id="kidColor" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff7a00"/>
      <stop offset="50%" stop-color="#ff9e00"/>
      <stop offset="100%" stop-color="#00c4cc"/>
    </linearGradient>
    <linearGradient id="kidTeal" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#26d0ce"/>
      <stop offset="100%" stop-color="#1a2980"/>
    </linearGradient>
    <filter id="softGlow3" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="castShadow3" x="-15%" y="-15%" width="130%" height="150%">
      <feDropShadow dx="2" dy="14" stdDeviation="12" flood-color="#000000" flood-opacity="0.8"/>
    </filter>
  </defs>

  <rect width="600" height="400" fill="url(#bgKids)"/>
  
  <ellipse cx="300" cy="220" rx="190" ry="80" fill="#ff7a00" opacity="0.08" filter="url(#softGlow3)"/>
  <ellipse cx="280" cy="285" rx="220" ry="24" fill="#000" opacity="0.6" filter="url(#softGlow3)"/>

  <!-- Spincast Reel and Kid Rod -->
  <g filter="url(#castShadow3)">
    <!-- Foam bright handle -->
    <path d="M 70 280 L 175 240" stroke="url(#kidColor)" stroke-width="22" stroke-linecap="round"/>
    <!-- Black comfort ribs -->
    <path d="M 90 272 L 95 270" stroke="#111" stroke-width="24"/>
    <path d="M 115 263 L 120 261" stroke="#111" stroke-width="24"/>
    <path d="M 140 253 L 145 251" stroke="#111" stroke-width="24"/>

    <!-- Cute Compact Spincast Reel (Катушка с кнопкой) -->
    <g transform="translate(180, 248)">
      <rect x="-15" y="-12" width="40" height="24" rx="10" transform="rotate(-21)" fill="#ff7a00"/>
      <!-- Cone cover -->
      <ellipse cx="14" cy="2" rx="14" ry="18" fill="url(#kidTeal)"/>
      <circle cx="18" cy="2" r="4" fill="#111"/>
      <!-- Thumb push button -->
      <rect x="-16" y="-8" width="10" height="12" rx="3" fill="#ffffff"/>
      <!-- Handle -->
      <circle cx="0" cy="18" r="7" fill="#fff" stroke="#ff7a00" stroke-width="3"/>
    </g>

    <!-- Fiber Rod Blank -->
    <path d="M 195 233 L 360 170" stroke="url(#kidTeal)" stroke-width="11" stroke-linecap="round"/>
    <path d="M 355 172 L 530 105" stroke="#ffaa00" stroke-width="6" stroke-linecap="round"/>

    <!-- Colorful guides -->
    <g transform="translate(280, 200) rotate(-21)">
      <path d="M 0 0 L 0 -15" stroke="#fff" stroke-width="3"/>
      <ellipse cx="0" cy="-18" rx="8" ry="11" fill="none" stroke="#ff7a00" stroke-width="3.5"/>
    </g>
    <g transform="translate(410, 150) rotate(-21)">
      <path d="M 0 0 L 0 -11" stroke="#fff" stroke-width="2.5"/>
      <ellipse cx="0" cy="-14" rx="6" ry="8" fill="none" stroke="#26d0ce" stroke-width="3"/>
    </g>
    <g transform="translate(525, 107) rotate(-21)">
      <ellipse cx="0" cy="-8" rx="5" ry="7" fill="none" stroke="#ff7a00" stroke-width="3"/>
    </g>

    <!-- Fluorescent Round Bobber (Яркий круглый поплавок-шарик) -->
    <g transform="translate(380, 260)" filter="url(#softGlow3)">
      <!-- Ball top orange -->
      <path d="M -18 0 A 18 18 0 0 1 18 0 Z" fill="#ff3b30"/>
      <!-- Ball bottom white -->
      <path d="M -18 0 A 18 18 0 0 0 18 0 Z" fill="#ffffff"/>
      <rect x="-2" y="-24" width="4" height="48" rx="2" fill="#ffe600"/>
    </g>

    <!-- Cute Soft Fish Lure -->
    <g transform="translate(460, 255) rotate(20)">
      <ellipse cx="0" cy="0" rx="22" ry="11" fill="#00e5ff"/>
      <polygon points="18,0 32,-10 32,10" fill="#ff9100"/>
      <circle cx="-10" cy="-3" r="4" fill="#fff"/>
      <circle cx="-10" cy="-3" r="2" fill="#000"/>
    </g>
  </g>

  <text x="50" y="360" font-family="'Montserrat', sans-serif" font-size="12" font-weight="700" letter-spacing="3" fill="#ff9e00" opacity="0.6">EASY CATCH / SAFE &amp; DURABLE 2.0M</text>
</svg>"""

# 4. fan1.svg - Вентилятор ШокоБриз
fan1_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bgChoco" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#1f1816"/>
      <stop offset="50%" stop-color="#110d0c"/>
      <stop offset="100%" stop-color="#070505"/>
    </radialGradient>
    <linearGradient id="milkChoco" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7a4b33"/>
      <stop offset="35%" stop-color="#563020"/>
      <stop offset="70%" stop-color="#3c1e13"/>
      <stop offset="100%" stop-color="#241009"/>
    </linearGradient>
    <linearGradient id="chocoGloss" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#966144"/>
      <stop offset="50%" stop-color="#673924"/>
      <stop offset="100%" stop-color="#3b1d10"/>
    </linearGradient>
    <linearGradient id="brassGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fcedc7"/>
      <stop offset="40%" stop-color="#d4af6a"/>
      <stop offset="80%" stop-color="#9c7832"/>
      <stop offset="100%" stop-color="#5a4112"/>
    </linearGradient>
    <filter id="softGlowFan" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="12" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="castShadowFan" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="20" stdDeviation="18" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
  </defs>

  <rect width="600" height="400" fill="url(#bgChoco)"/>

  <!-- Warm chocolate aroma vapor waves -->
  <path d="M 140 180 Q 200 120 280 150 T 420 110" fill="none" stroke="#d4af6a" stroke-width="2" opacity="0.12" filter="url(#softGlowFan)"/>
  <path d="M 180 220 Q 260 160 340 190 T 480 140" fill="none" stroke="#d4af6a" stroke-width="3" opacity="0.08" filter="url(#softGlowFan)"/>

  <!-- Shadow on surface -->
  <ellipse cx="300" cy="340" rx="140" ry="24" fill="#000000" opacity="0.85" filter="url(#softGlowFan)"/>

  <!-- Desk Fan Assembly -->
  <g filter="url(#castShadowFan)">
    <!-- Base (Тяжелая круглая база цвета шоколада) -->
    <ellipse cx="300" cy="330" rx="90" ry="25" fill="url(#milkChoco)"/>
    <ellipse cx="300" cy="326" rx="84" ry="21" fill="url(#chocoGloss)"/>
    <!-- Gold Trim Base Ring -->
    <ellipse cx="300" cy="326" rx="84" ry="21" fill="none" stroke="url(#brassGold)" stroke-width="2"/>
    
    <!-- Rotary Switch / Buttons (Латунный регулятор скоростей) -->
    <ellipse cx="300" cy="325" rx="14" ry="7" fill="url(#brassGold)"/>
    <ellipse cx="300" cy="322" rx="11" ry="5" fill="#2d170f"/>
    <circle cx="300" cy="322" r="2" fill="#ffd580"/>

    <!-- Neck / Stand (Изящная латунная ножка) -->
    <path d="M 293 325 L 293 210 Q 293 190 300 190 Q 307 190 307 210 L 307 325 Z" fill="url(#brassGold)"/>
    <!-- Motor Housing (Корпус мотора сзади) -->
    <ellipse cx="300" cy="180" rx="35" ry="32" fill="url(#milkChoco)"/>

    <!-- Fan Outer Grille (Внешняя золоченая решетка) -->
    <circle cx="300" cy="180" r="105" fill="#140d0a" stroke="url(#brassGold)" stroke-width="6"/>
    <circle cx="300" cy="180" r="100" fill="none" stroke="url(#milkChoco)" stroke-width="4"/>
    <circle cx="300" cy="180" r="75" fill="none" stroke="url(#brassGold)" stroke-width="1.5" opacity="0.6"/>
    <circle cx="300" cy="180" r="50" fill="none" stroke="url(#brassGold)" stroke-width="1.5" opacity="0.6"/>

    <!-- Radial Grille Spokes (Спицы решетки) -->
    <g stroke="url(#brassGold)" stroke-width="1.2" opacity="0.5">
      <line x1="300" y1="75" x2="300" y2="285"/>
      <line x1="195" y1="180" x2="405" y2="180"/>
      <line x1="225" y1="105" x2="375" y2="255"/>
      <line x1="375" y1="105" x2="225" y2="255"/>
      <line x1="205" y1="140" x2="395" y2="220"/>
      <line x1="205" y1="220" x2="395" y2="140"/>
      <line x1="260" y1="80" x2="340" y2="280"/>
      <line x1="340" y1="80" x2="260" y2="280"/>
    </g>

    <!-- Glossy Chocolate Fan Blades (Шоколадные лопасти) -->
    <!-- Blade 1 -->
    <path d="M 300 180 Q 260 110 300 85 Q 330 95 305 175 Z" fill="url(#chocoGloss)" stroke="url(#brassGold)" stroke-width="1"/>
    <!-- Blade 2 -->
    <path d="M 300 180 Q 375 190 385 230 Q 360 250 305 185 Z" fill="url(#chocoGloss)" stroke="url(#brassGold)" stroke-width="1"/>
    <!-- Blade 3 -->
    <path d="M 300 180 Q 230 220 220 255 Q 205 230 295 178 Z" fill="url(#chocoGloss)" stroke="url(#brassGold)" stroke-width="1"/>

    <!-- Center Centerpiece Emblem (Эмблема по центру) -->
    <circle cx="300" cy="180" r="24" fill="url(#brassGold)"/>
    <circle cx="300" cy="180" r="20" fill="url(#milkChoco)"/>
    <!-- Cocoa Bean / Fan icon inside center -->
    <path d="M 293 174 Q 300 166 307 174 Q 314 186 300 190 Q 286 186 293 174 Z" fill="url(#brassGold)"/>
    <circle cx="300" cy="180" r="2" fill="#fff"/>
  </g>

  <text x="50" y="360" font-family="'Montserrat', sans-serif" font-size="12" font-weight="700" letter-spacing="3" fill="#d4af6a" opacity="0.6">CHOCO-DIFFUSER 3-SPEED / SILENT</text>
</svg>"""

# 5. fan2.svg - Напольный вентилятор Какао Торнадо
fan2_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bgDarkTornado" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#18131d"/>
      <stop offset="50%" stop-color="#0d0912"/>
      <stop offset="100%" stop-color="#040206"/>
    </radialGradient>
    <linearGradient id="darkChoco" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#402c25"/>
      <stop offset="30%" stop-color="#231713"/>
      <stop offset="70%" stop-color="#140c09"/>
      <stop offset="100%" stop-color="#2c1e19"/>
    </linearGradient>
    <linearGradient id="roseGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fcd3ba"/>
      <stop offset="45%" stop-color="#e09f7a"/>
      <stop offset="80%" stop-color="#a66240"/>
      <stop offset="100%" stop-color="#6b371e"/>
    </linearGradient>
    <filter id="softGlowTornado" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="14" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="castShadowTornado" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="24" stdDeviation="20" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
  </defs>

  <rect width="600" height="400" fill="url(#bgDarkTornado)"/>

  <!-- Ambient light pillar -->
  <ellipse cx="300" cy="200" rx="90" ry="170" fill="#e09f7a" opacity="0.06" filter="url(#softGlowTornado)"/>
  <ellipse cx="300" cy="355" rx="160" ry="24" fill="#000" opacity="0.9" filter="url(#softGlowTornado)"/>

  <!-- High-end Column / Stand Fan -->
  <g filter="url(#castShadowTornado)">
    <!-- Base -->
    <ellipse cx="300" cy="345" rx="110" ry="24" fill="url(#darkChoco)"/>
    <ellipse cx="300" cy="341" rx="104" ry="20" fill="#1c120e"/>
    <ellipse cx="300" cy="341" rx="104" ry="20" fill="none" stroke="url(#roseGold)" stroke-width="2.5"/>

    <!-- Telescopic Standing Pole (Телескопическая золоченая стойка) -->
    <rect x="292" y="160" width="16" height="182" fill="url(#darkChoco)"/>
    <!-- Gold joints & accent bands -->
    <rect x="290" y="270" width="20" height="8" rx="2" fill="url(#roseGold)"/>
    <rect x="290" y="200" width="20" height="8" rx="2" fill="url(#roseGold)"/>

    <!-- Large Sleek Modern Head (Большая голова вентилятора) -->
    <!-- Outer ring casing -->
    <circle cx="300" cy="120" r="85" fill="#110a08" stroke="url(#roseGold)" stroke-width="5"/>
    <circle cx="300" cy="120" r="78" fill="none" stroke="#2a1a14" stroke-width="3"/>
    
    <!-- Modern Minimalist Blade Mesh -->
    <g stroke="url(#roseGold)" stroke-width="1" opacity="0.4">
      <circle cx="300" cy="120" r="60" fill="none"/>
      <circle cx="300" cy="120" r="40" fill="none"/>
      <circle cx="300" cy="120" r="20" fill="none"/>
      <line x1="300" y1="35" x2="300" y2="205"/>
      <line x1="215" y1="120" x2="385" y2="120"/>
      <line x1="240" y1="60" x2="360" y2="180"/>
      <line x1="360" y1="60" x2="240" y2="180"/>
    </g>

    <!-- 5 Aerodynamic Dark Chocolate Blades (5 мощных тихих лопастей) -->
    <g transform="translate(300, 120)">
      <path d="M 0 0 Q -25 -55 0 -72 Q 20 -55 0 0 Z" fill="url(#darkChoco)" stroke="url(#roseGold)" stroke-width="0.8"/>
      <path d="M 0 0 Q -25 -55 0 -72 Q 20 -55 0 0 Z" transform="rotate(72)" fill="url(#darkChoco)" stroke="url(#roseGold)" stroke-width="0.8"/>
      <path d="M 0 0 Q -25 -55 0 -72 Q 20 -55 0 0 Z" transform="rotate(144)" fill="url(#darkChoco)" stroke="url(#roseGold)" stroke-width="0.8"/>
      <path d="M 0 0 Q -25 -55 0 -72 Q 20 -55 0 0 Z" transform="rotate(216)" fill="url(#darkChoco)" stroke="url(#roseGold)" stroke-width="0.8"/>
      <path d="M 0 0 Q -25 -55 0 -72 Q 20 -55 0 0 Z" transform="rotate(288)" fill="url(#darkChoco)" stroke="url(#roseGold)" stroke-width="0.8"/>
      <!-- Hub -->
      <circle cx="0" cy="0" r="18" fill="url(#roseGold)"/>
      <circle cx="0" cy="0" r="14" fill="#140c09"/>
    </g>

    <!-- Smart Digital Touch Panel (Сенсорный дисплей на стойке) -->
    <rect x="286" y="220" width="28" height="42" rx="4" fill="#090605" stroke="url(#roseGold)" stroke-width="1.2"/>
    <!-- LED indicators -->
    <text x="300" y="235" font-family="'Inter', sans-serif" font-size="7" font-weight="700" fill="#e09f7a" text-anchor="middle">21°C</text>
    <circle cx="294" cy="245" r="1.5" fill="#e09f7a"/>
    <circle cx="300" cy="245" r="1.5" fill="#e09f7a"/>
    <circle cx="306" cy="245" r="1.5" fill="#e09f7a"/>
    <path d="M 293 254 Q 300 250 307 254" stroke="#e09f7a" stroke-width="1" fill="none"/>
  </g>

  <!-- Remote control next to base (Пульт ДУ) -->
  <g transform="translate(420, 310) rotate(-12)" filter="url(#castShadowTornado)">
    <rect x="0" y="0" width="24" height="46" rx="5" fill="#1b120e" stroke="url(#roseGold)" stroke-width="1"/>
    <circle cx="12" cy="12" r="3.5" fill="url(#roseGold)"/>
    <circle cx="8" cy="24" r="2" fill="#555"/>
    <circle cx="16" cy="24" r="2" fill="#555"/>
    <circle cx="12" cy="34" r="2.5" fill="#ff7a00"/>
  </g>

  <text x="50" y="360" font-family="'Montserrat', sans-serif" font-size="12" font-weight="700" letter-spacing="3" fill="#e09f7a" opacity="0.6">3 AROMA MODES / BLDC MOTOR / REMOTE</text>
</svg>"""

# 6. fan3.svg - Портативный USB вентилятор Сладкий Ветерок
fan3_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <radialGradient id="bgUsb" cx="50%" cy="45%" r="65%">
      <stop offset="0%" stop-color="#241d1a"/>
      <stop offset="60%" stop-color="#120e0c"/>
      <stop offset="100%" stop-color="#060504"/>
    </radialGradient>
    <linearGradient id="chocBar" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#653f2c"/>
      <stop offset="40%" stop-color="#462719"/>
      <stop offset="100%" stop-color="#28130a"/>
    </linearGradient>
    <linearGradient id="softBlades" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#b0815e"/>
      <stop offset="50%" stop-color="#805335"/>
      <stop offset="100%" stop-color="#4e2c17"/>
    </linearGradient>
    <linearGradient id="goldUsb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffe8a3"/>
      <stop offset="50%" stop-color="#d4af6a"/>
      <stop offset="100%" stop-color="#8c6827"/>
    </linearGradient>
    <filter id="softGlowUsb" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <filter id="castShadowUsb" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="2" dy="18" stdDeviation="15" flood-color="#000000" flood-opacity="0.95"/>
    </filter>
  </defs>

  <rect width="600" height="400" fill="url(#bgUsb)"/>

  <ellipse cx="300" cy="330" rx="140" ry="22" fill="#000" opacity="0.8" filter="url(#softGlowUsb)"/>
  <circle cx="340" cy="160" r="120" fill="#d4af6a" opacity="0.08" filter="url(#softGlowUsb)"/>

  <!-- Portable Fan Gadget -->
  <g filter="url(#castShadowUsb)">
    <!-- Base shaped like a real chocolate bar segment (Плитка шоколада в основании) -->
    <g transform="translate(180, 275) rotate(-6)">
      <!-- Main chocolate base slab -->
      <rect x="0" y="0" width="130" height="55" rx="8" fill="url(#chocBar)" stroke="url(#goldUsb)" stroke-width="1.5"/>
      <!-- Segments / Choco squares -->
      <rect x="8" y="8" width="34" height="38" rx="4" fill="#351b11" stroke="#5a3321" stroke-width="1.5"/>
      <rect x="48" y="8" width="34" height="38" rx="4" fill="#351b11" stroke="#5a3321" stroke-width="1.5"/>
      <rect x="88" y="8" width="34" height="38" rx="4" fill="#351b11" stroke="#5a3321" stroke-width="1.5"/>
      <!-- Cocoa percentage engraving -->
      <text x="25" y="32" font-family="'Montserrat', sans-serif" font-size="10" font-weight="800" fill="#b0815e" text-anchor="middle">72%</text>
      <!-- USB-C Port with gold pins -->
      <rect x="128" y="22" width="6" height="12" rx="2" fill="#111" stroke="url(#goldUsb)" stroke-width="1"/>
      <circle cx="70" cy="48" r="2" fill="#00e5ff" filter="url(#softGlowUsb)"/>
    </g>

    <!-- Flexible Soft-touch Gooseneck (Гибкая силиконовая ножка) -->
    <path d="M 270 280 Q 250 200 320 170" fill="none" stroke="url(#chocBar)" stroke-width="14" stroke-linecap="round"/>
    <path d="M 270 280 Q 250 200 320 170" fill="none" stroke="url(#goldUsb)" stroke-width="2" stroke-dasharray="3 7" stroke-linecap="round"/>

    <!-- Fan Head (Голова вентилятора) -->
    <g transform="translate(325, 165)">
      <!-- Motor pod -->
      <ellipse cx="0" cy="0" rx="18" ry="18" fill="url(#chocBar)" stroke="url(#goldUsb)" stroke-width="2"/>
      
      <!-- Safe Soft Dual Blades (Силиконовые безопасные лопасти) -->
      <!-- Blade 1 -->
      <path d="M 0 0 Q -50 -55 0 -85 Q 35 -65 0 0 Z" fill="url(#softBlades)" stroke="url(#goldUsb)" stroke-width="1"/>
      <!-- Blade 2 -->
      <path d="M 0 0 Q 50 55 0 85 Q -35 65 0 0 Z" fill="url(#softBlades)" stroke="url(#goldUsb)" stroke-width="1"/>

      <!-- Center chocolate button -->
      <circle cx="0" cy="0" r="9" fill="url(#goldUsb)"/>
      <circle cx="0" cy="0" r="6" fill="#28130a"/>
    </g>
  </g>

  <!-- Gold USB cable loosely curled nearby -->
  <path d="M 330 330 Q 380 345 420 325 T 480 340" fill="none" stroke="url(#goldUsb)" stroke-width="3" stroke-linecap="round" opacity="0.7"/>
  <rect x="480" y="335" width="22" height="10" rx="2" fill="#222" stroke="url(#goldUsb)" stroke-width="1"/>

  <text x="50" y="360" font-family="'Montserrat', sans-serif" font-size="12" font-weight="700" letter-spacing="3" fill="#d4af6a" opacity="0.6">USB-C PORTABLE / 72% DARK CHOCO SCENT</text>
</svg>"""

files = {
    "rod1.svg": rod1_svg,
    "rod2.svg": rod2_svg,
    "rod3.svg": rod3_svg,
    "fan1.svg": fan1_svg,
    "fan2.svg": fan2_svg,
    "fan3.svg": fan3_svg
}

for name, content in files.items():
    path = os.path.join(img_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {name} ({len(content)} chars)")
