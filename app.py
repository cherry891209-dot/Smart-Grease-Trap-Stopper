from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


BASE_DIR = Path(__file__).parent
PROPOSAL_IMAGE = BASE_DIR / "proposal-cover.png"
RULES_IMAGE = BASE_DIR / "rules-cover.png"
MESSY_SINK_IMAGE = BASE_DIR / "assets" / "messy-sink.jpg"
DRAIN_IMAGE = BASE_DIR / "assets" / "drain-closeup.jpg"
APARTMENT_SINK_IMAGE = BASE_DIR / "assets" / "apartment-sink.jpg"
TEAM_ILLUSTRATION_IMAGE = BASE_DIR / "assets" / "team-illustration.png"
TEAM_MEMBERS_REDRAWN_IMAGE = BASE_DIR / "assets" / "team-members-redrawn.png"
RULES_PDF = BASE_DIR / "612483020334563589_Startup World Cup Pitch Deck Outline_ 2025.pdf"
PROPOSAL_PDF = BASE_DIR / "612513577919578249_Smart_Grease_Trap_Revolution_(4).pdf"


st.set_page_config(
    page_title="Smart Grease-Trap Stopper",
    layout="wide",
    initial_sidebar_state="expanded",
)


CUSTOM_CSS = """
<style>
    :root {
        --ink: #17211d;
        --muted: #59645f;
        --paper: #f8f5ee;
        --panel: #ffffff;
        --line: #d9dfd6;
        --moss: #496b58;
        --fern: #78a083;
        --clay: #c7653f;
        --amber: #f0b45c;
    }

    .stApp {
        background: var(--paper);
        color: var(--ink);
        font-family: "Noto Sans TC", "Inter", system-ui, sans-serif;
    }

    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] p {
        color: var(--ink);
    }

    h1, h2, h3 {
        letter-spacing: 0;
    }

    .hero {
        min-height: 520px;
        padding: clamp(28px, 5vw, 64px);
        border-radius: 8px;
        background:
            linear-gradient(90deg, rgba(23, 33, 29, .92), rgba(23, 33, 29, .52)),
            url("data:image/jpeg;base64,__HERO_PLACEHOLDER__");
        background-size: cover;
        background-position: center;
        color: white;
        display: grid;
        align-content: end;
        box-shadow: 0 26px 80px rgba(23, 33, 29, .18);
    }

    .hero h1 {
        max-width: 11ch;
        font-size: clamp(56px, 9vw, 124px);
        line-height: .9;
        margin: 0;
    }

    .hero .subtitle {
        font-size: clamp(24px, 3vw, 38px);
        font-weight: 900;
        margin-top: 18px;
    }

    .hero p {
        max-width: 720px;
        color: rgba(255,255,255,.82);
        font-size: 18px;
        line-height: 1.85;
    }

    .eyebrow {
        color: var(--clay);
        font-size: 13px;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .hero .eyebrow {
        color: var(--amber);
    }

    .card {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 14px 38px rgba(23, 33, 29, .07);
        height: 100%;
    }

    .number {
        color: var(--clay);
        font-weight: 900;
        font-size: 13px;
    }

    .muted {
        color: var(--muted);
        line-height: 1.8;
    }

    .big-number {
        color: var(--moss);
        font-size: clamp(38px, 6vw, 72px);
        line-height: 1;
        font-weight: 900;
    }

    .pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 18px;
    }

    .pill {
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 8px 13px;
        background: white;
        color: var(--muted);
        font-size: 14px;
        font-weight: 700;
    }

    .quote {
        border-left: 5px solid var(--clay);
        padding: 24px;
        font-size: clamp(24px, 4vw, 44px);
        line-height: 1.25;
        font-weight: 900;
    }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 16px 18px;
        box-shadow: 0 12px 28px rgba(23, 33, 29, .06);
    }

    .split-panel {
        display: grid;
        grid-template-columns: minmax(0, 1.1fr) minmax(280px, .9fr);
        gap: 18px;
        align-items: stretch;
    }

    .product-demo {
        position: relative;
        min-height: 430px;
        border: 1px solid var(--line);
        border-radius: 8px;
        background:
            linear-gradient(180deg, rgba(255,255,255,.78), rgba(214,226,228,.52)),
            #d8e6e6;
        overflow: hidden;
        box-shadow: 0 24px 70px rgba(23, 33, 29, .12);
    }

    .sink-rim {
        position: absolute;
        left: 8%;
        right: 8%;
        bottom: 64px;
        height: 235px;
        border: 18px solid #e5ebe7;
        border-top-width: 28px;
        border-radius: 8px 8px 54px 54px;
        background: rgba(255,255,255,.35);
    }

    .water-flow {
        position: absolute;
        top: 48px;
        left: 48%;
        width: 16px;
        height: 250px;
        border-radius: 999px;
        background: linear-gradient(180deg, rgba(85,160,185,.18), rgba(85,160,185,.88));
    }

    .stopper-demo {
        position: absolute;
        left: 50%;
        bottom: 145px;
        width: 130px;
        height: 130px;
        border-radius: 50%;
        transform: translateX(-50%);
        background: #2f4d40;
        box-shadow: inset 0 0 0 13px #d8e7da, inset 0 0 0 23px #78a083, 0 18px 34px rgba(47,77,64,.26);
    }

    .oil-dot {
        position: absolute;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: var(--amber);
        opacity: .9;
    }

    .oil-dot.one { top: 126px; left: 38%; }
    .oil-dot.two { top: 175px; left: 56%; }
    .oil-dot.three { top: 218px; left: 45%; }

    .collector-demo {
        position: absolute;
        right: 13%;
        bottom: 46px;
        width: 132px;
        height: 150px;
        border: 8px solid rgba(255,255,255,.82);
        border-radius: 8px 8px 34px 34px;
        background: rgba(255,255,255,.52);
        overflow: hidden;
    }

    .collector-oil {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 54px;
        height: 52px;
        background: rgba(240,180,92,.9);
    }

    .collector-water {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        height: 54px;
        background: rgba(85,160,185,.62);
    }

    .roadmap {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 14px;
    }

    .roadmap .step {
        background: white;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 18px;
        min-height: 170px;
    }

    .persona {
        border: 1px solid var(--line);
        border-radius: 8px;
        background: white;
        padding: 22px;
        height: 100%;
        box-shadow: 0 14px 38px rgba(23, 33, 29, .07);
    }

    .persona strong {
        display: block;
        font-size: 22px;
        margin-bottom: 8px;
    }

    .matrix {
        width: 100%;
        border-collapse: collapse;
        background: white;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 14px 38px rgba(23, 33, 29, .07);
    }

    .matrix th,
    .matrix td {
        border-bottom: 1px solid var(--line);
        padding: 14px 16px;
        text-align: left;
        vertical-align: top;
    }

    .matrix th {
        background: #eef4ec;
    }

    .hero {
        position: relative;
        overflow: hidden;
        isolation: isolate;
        animation: heroReveal 900ms ease-out both;
    }

    .hero::before {
        content: "";
        position: absolute;
        inset: -40%;
        z-index: -1;
        background:
            radial-gradient(circle at 24% 30%, rgba(240,180,92,.28), transparent 28%),
            radial-gradient(circle at 74% 62%, rgba(120,160,131,.22), transparent 30%);
        animation: ambientDrift 9s ease-in-out infinite alternate;
    }

    .hero::after {
        content: "";
        position: absolute;
        inset: 0;
        z-index: -1;
        background: linear-gradient(110deg, transparent 0 34%, rgba(255,255,255,.18) 46%, transparent 58% 100%);
        transform: translateX(-115%);
        animation: heroSweep 5.8s ease-in-out infinite;
    }

    .hero h1 { animation: slideUp 760ms 120ms ease-out both; }
    .hero .subtitle { animation: slideUp 760ms 220ms ease-out both; }
    .hero p { animation: slideUp 760ms 320ms ease-out both; }

    .card,
    .persona,
    .roadmap .step,
    .matrix,
    div[data-testid="stMetric"],
    .product-demo {
        animation: cardRise 680ms ease-out both;
        transition: transform 260ms ease, box-shadow 260ms ease, border-color 260ms ease;
    }

    .card,
    .persona,
    .roadmap .step {
        position: relative;
        overflow: hidden;
    }

    .card::after,
    .persona::after,
    .roadmap .step::after {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(115deg, transparent 0 38%, rgba(255,255,255,.58) 48%, transparent 58% 100%);
        transform: translateX(-125%);
        animation: surfaceSweep 6.2s ease-in-out infinite;
        pointer-events: none;
    }

    .card:hover,
    .persona:hover,
    .roadmap .step:hover,
    div[data-testid="stMetric"]:hover {
        transform: translateY(-6px);
        box-shadow: 0 24px 58px rgba(23, 33, 29, .13);
        border-color: rgba(73,107,88,.38);
    }

    .big-number {
        animation: numberPulse 2.8s ease-in-out infinite;
    }

    .water-flow {
        animation: waterStream 1.4s ease-in-out infinite;
    }

    .stopper-demo {
        animation: stopperPulse 2.1s ease-in-out infinite;
    }

    .oil-dot {
        animation: oilTravel 3.4s ease-in-out infinite;
    }

    .oil-dot.one { animation-delay: 0s; }
    .oil-dot.two { animation-delay: .55s; }
    .oil-dot.three { animation-delay: 1.1s; }

    .collector-oil {
        animation: oilLevel 3.8s ease-in-out infinite;
    }

    .collector-water {
        animation: waterLevel 3.8s ease-in-out infinite;
    }

    .photo-grid {
        display: grid;
        grid-template-columns: 1.2fr .8fr;
        gap: 16px;
        margin: 20px 0;
    }

    .photo-tile {
        position: relative;
        min-height: 280px;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid var(--line);
        box-shadow: 0 18px 48px rgba(23, 33, 29, .12);
        animation: cardRise 760ms ease-out both;
    }

    .photo-tile img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transform: scale(1.06);
        animation: kenBurns 13s ease-in-out infinite alternate;
    }

    .photo-tile.small {
        min-height: 132px;
    }

    .photo-stack {
        display: grid;
        gap: 16px;
    }

    .photo-caption {
        position: absolute;
        left: 14px;
        right: 14px;
        bottom: 14px;
        padding: 12px 14px;
        border-radius: 8px;
        background: rgba(23,33,29,.74);
        color: white;
        backdrop-filter: blur(12px);
        font-weight: 800;
    }

    .animated-strip {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 12px;
        margin: 18px 0;
    }

    .signal {
        position: relative;
        min-height: 112px;
        border-radius: 8px;
        background: #1f2d27;
        color: white;
        padding: 18px;
        overflow: hidden;
        animation: cardRise 680ms ease-out both;
    }

    .signal::before {
        content: "";
        position: absolute;
        width: 90px;
        height: 90px;
        right: -30px;
        top: -30px;
        border-radius: 50%;
        background: rgba(240,180,92,.32);
        animation: blobPulse 3s ease-in-out infinite;
    }

    .signal strong {
        display: block;
        font-size: 28px;
        line-height: 1;
        margin-bottom: 8px;
    }

    .motion-visual {
        position: relative;
        min-height: 330px;
        border-radius: 8px;
        border: 1px solid var(--line);
        background:
            radial-gradient(circle at 25% 20%, rgba(240,180,92,.18), transparent 28%),
            linear-gradient(135deg, #ffffff, #eef4ec);
        overflow: hidden;
        box-shadow: 0 22px 64px rgba(23,33,29,.12);
        animation: cardRise 760ms ease-out both;
        margin: 18px 0;
    }

    .pipe-line {
        position: absolute;
        left: 8%;
        right: 8%;
        top: 47%;
        height: 48px;
        border-radius: 999px;
        background: #536a7c;
        box-shadow: inset 0 0 0 10px rgba(255,255,255,.24);
    }

    .pipe-bend {
        position: absolute;
        right: 12%;
        top: 36%;
        width: 140px;
        height: 140px;
        border: 46px solid #536a7c;
        border-left: 0;
        border-bottom: 0;
        border-radius: 0 90px 0 0;
    }

    .grease-flow {
        position: absolute;
        left: 10%;
        top: calc(47% + 12px);
        width: 24px;
        height: 24px;
        border-radius: 50%;
        background: var(--amber);
        animation: clogMove 3.8s ease-in-out infinite;
        box-shadow: 0 0 0 8px rgba(240,180,92,.18);
    }

    .clog {
        position: absolute;
        right: 16%;
        top: calc(47% + 4px);
        width: 62px;
        height: 40px;
        border-radius: 999px;
        background: #c7653f;
        animation: clogPulse 2.6s ease-in-out infinite;
    }

    .motion-label {
        position: absolute;
        left: 24px;
        bottom: 22px;
        max-width: 380px;
        color: var(--ink);
        font-weight: 900;
        font-size: clamp(24px, 4vw, 42px);
        line-height: 1.08;
    }

    .parts-orbit {
        position: absolute;
        inset: 0;
    }

    .part {
        position: absolute;
        display: grid;
        place-items: center;
        width: 96px;
        height: 96px;
        border-radius: 50%;
        color: white;
        font-weight: 900;
        background: #2f4d40;
        box-shadow: 0 18px 38px rgba(23,33,29,.18);
        animation: partFloat 3.8s ease-in-out infinite;
    }

    .part.one { left: 14%; top: 18%; background: #496b58; }
    .part.two { left: 42%; top: 10%; background: #78a083; animation-delay: .4s; }
    .part.three { right: 18%; top: 26%; background: #c7653f; animation-delay: .8s; }
    .part.four { left: 34%; bottom: 16%; background: #536a7c; animation-delay: 1.2s; }

    .market-rings {
        position: absolute;
        inset: 0;
        display: grid;
        place-items: center;
    }

    .ring {
        position: absolute;
        border: 2px solid rgba(73,107,88,.22);
        border-radius: 50%;
        animation: ringPulse 3.6s ease-in-out infinite;
    }

    .ring.one { width: 90px; height: 90px; }
    .ring.two { width: 180px; height: 180px; animation-delay: .4s; }
    .ring.three { width: 290px; height: 290px; animation-delay: .8s; }
    .ring.four { width: 430px; height: 430px; animation-delay: 1.2s; }

    .cash-bars {
        position: absolute;
        left: 10%;
        right: 10%;
        bottom: 76px;
        display: flex;
        align-items: end;
        gap: 18px;
        height: 190px;
    }

    .cash-bar {
        flex: 1;
        border-radius: 8px 8px 0 0;
        background: linear-gradient(180deg, var(--fern), var(--moss));
        animation: barGrow 2.8s ease-in-out infinite alternate;
    }

    .cash-bar:nth-child(2) { height: 56%; animation-delay: .2s; }
    .cash-bar:nth-child(3) { height: 74%; animation-delay: .4s; }
    .cash-bar:nth-child(4) { height: 92%; animation-delay: .6s; }
    .cash-bar:nth-child(1) { height: 38%; }

    .route-line {
        position: absolute;
        left: 10%;
        right: 10%;
        top: 45%;
        height: 4px;
        background: linear-gradient(90deg, var(--moss), var(--amber), var(--clay));
    }

    .route-dot {
        position: absolute;
        top: calc(45% - 18px);
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: white;
        border: 8px solid var(--moss);
        animation: dotPulse 2.4s ease-in-out infinite;
    }

    .route-dot.one { left: 10%; }
    .route-dot.two { left: 36%; animation-delay: .35s; }
    .route-dot.three { left: 62%; animation-delay: .7s; }
    .route-dot.four { right: 10%; animation-delay: 1.05s; }

    .radar {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 230px;
        height: 230px;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        background:
            conic-gradient(from 20deg, rgba(73,107,88,.72), rgba(240,180,92,.78), rgba(199,101,63,.62), rgba(73,107,88,.72));
        clip-path: polygon(50% 0, 92% 26%, 78% 84%, 25% 90%, 6% 35%);
        animation: radarMorph 4.8s ease-in-out infinite;
    }

    .radar-grid {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 310px;
        height: 310px;
        transform: translate(-50%, -50%);
        border: 1px solid rgba(73,107,88,.22);
        border-radius: 50%;
        box-shadow: inset 0 0 0 52px rgba(73,107,88,.06), inset 0 0 0 104px rgba(73,107,88,.05);
    }

    .image-marquee {
        position: relative;
        overflow: hidden;
        border-radius: 8px;
        border: 1px solid var(--line);
        background: #111a16;
        box-shadow: 0 22px 64px rgba(23, 33, 29, .18);
        margin: 20px 0;
    }

    .image-marquee::before,
    .image-marquee::after {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        z-index: 2;
        width: 120px;
        pointer-events: none;
    }

    .image-marquee::before {
        left: 0;
        background: linear-gradient(90deg, #111a16, transparent);
    }

    .image-marquee::after {
        right: 0;
        background: linear-gradient(270deg, #111a16, transparent);
    }

    .marquee-track {
        display: flex;
        width: max-content;
        gap: 16px;
        padding: 16px;
        animation: marqueeSlide 28s linear infinite;
    }

    .image-marquee:hover .marquee-track {
        animation-play-state: paused;
    }

    .marquee-item {
        position: relative;
        flex: 0 0 360px;
        height: 230px;
        overflow: hidden;
        border-radius: 8px;
        background: #26362f;
        box-shadow: 0 18px 42px rgba(0,0,0,.24);
    }

    .marquee-item img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transform: scale(1.06);
        animation: kenBurns 10s ease-in-out infinite alternate;
    }

    .marquee-item span {
        position: absolute;
        left: 12px;
        right: 12px;
        bottom: 12px;
        padding: 10px 12px;
        border-radius: 8px;
        background: rgba(23,33,29,.76);
        color: white;
        font-size: 14px;
        font-weight: 800;
        backdrop-filter: blur(10px);
    }

    @keyframes heroReveal {
        from { opacity: 0; transform: translateY(18px) scale(.985); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(24px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes cardRise {
        from { opacity: 0; transform: translateY(18px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes ambientDrift {
        from { transform: translate3d(-3%, -2%, 0) rotate(0deg); }
        to { transform: translate3d(4%, 3%, 0) rotate(7deg); }
    }

    @keyframes heroSweep {
        0%, 48% { transform: translateX(-115%); }
        62%, 100% { transform: translateX(115%); }
    }

    @keyframes surfaceSweep {
        0%, 58% { transform: translateX(-125%); }
        75%, 100% { transform: translateX(125%); }
    }

    @keyframes waterStream {
        0%, 100% { transform: scaleY(.86); opacity: .72; }
        50% { transform: scaleY(1.08); opacity: 1; }
    }

    @keyframes stopperPulse {
        0%, 100% { transform: translateX(-50%) scale(1); }
        50% { transform: translateX(-50%) scale(1.045); }
    }

    @keyframes oilTravel {
        0% { transform: translate3d(-18px, -32px, 0) scale(.72); opacity: 0; }
        18% { opacity: .95; }
        68% { transform: translate3d(26px, 36px, 0) scale(1.08); opacity: .95; }
        100% { transform: translate3d(84px, 120px, 0) scale(.62); opacity: 0; }
    }

    @keyframes oilLevel {
        0%, 100% { height: 36px; }
        50% { height: 64px; }
    }

    @keyframes waterLevel {
        0%, 100% { height: 62px; }
        50% { height: 48px; }
    }

    @keyframes kenBurns {
        from { transform: scale(1.05) translate3d(-1%, -1%, 0); }
        to { transform: scale(1.16) translate3d(2%, 1.5%, 0); }
    }

    @keyframes numberPulse {
        0%, 100% { transform: scale(1); filter: saturate(1); }
        50% { transform: scale(1.035); filter: saturate(1.18); }
    }

    @keyframes blobPulse {
        0%, 100% { transform: scale(1); opacity: .56; }
        50% { transform: scale(1.32); opacity: .88; }
    }

    @keyframes clogMove {
        0% { transform: translateX(0) scale(.8); opacity: .2; }
        35% { opacity: 1; }
        72% { transform: translateX(64vw) scale(1.05); opacity: .95; }
        100% { transform: translateX(64vw) scale(.2); opacity: 0; }
    }

    @keyframes clogPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.18); }
    }

    @keyframes partFloat {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-16px) rotate(5deg); }
    }

    @keyframes ringPulse {
        0%, 100% { transform: scale(.94); opacity: .48; }
        50% { transform: scale(1.04); opacity: 1; }
    }

    @keyframes barGrow {
        from { transform: scaleY(.72); filter: saturate(.9); }
        to { transform: scaleY(1); filter: saturate(1.2); }
    }

    @keyframes dotPulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(73,107,88,.22); }
        50% { transform: scale(1.16); box-shadow: 0 0 0 14px rgba(73,107,88,0); }
    }

    @keyframes radarMorph {
        0%, 100% { clip-path: polygon(50% 0, 92% 26%, 78% 84%, 25% 90%, 6% 35%); transform: translate(-50%, -50%) rotate(0deg); }
        50% { clip-path: polygon(50% 8%, 84% 18%, 88% 76%, 32% 84%, 12% 42%); transform: translate(-50%, -50%) rotate(4deg); }
    }

    @keyframes marqueeSlide {
        from { transform: translateX(0); }
        to { transform: translateX(calc(-50% - 8px)); }
    }

    /* Product-site polish: consistent 8px spacing scale, type hierarchy, and component density. */
    :root {
        --space-1: 4px;
        --space-2: 8px;
        --space-3: 12px;
        --space-4: 16px;
        --space-5: 24px;
        --space-6: 32px;
        --space-7: 48px;
        --radius: 8px;
        --shadow-sm: 0 8px 20px rgba(23, 33, 29, .06);
        --shadow-md: 0 18px 44px rgba(23, 33, 29, .10);
    }

    html,
    body,
    .stApp,
    [data-testid="stMarkdownContainer"],
    button,
    input,
    textarea {
        font-family: -apple-system, BlinkMacSystemFont, "Inter", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
        letter-spacing: 0;
    }

    .block-container {
        max-width: 1160px;
        padding-top: 64px;
        padding-bottom: 80px;
    }

    h1,
    h2,
    h3,
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3 {
        color: var(--ink);
        letter-spacing: 0;
        font-weight: 800;
    }

    h1,
    [data-testid="stMarkdownContainer"] h1 {
        font-size: 48px;
        line-height: 1.12;
        margin: 0 0 var(--space-5);
    }

    h2,
    [data-testid="stMarkdownContainer"] h2 {
        font-size: 30px;
        line-height: 1.25;
        margin: var(--space-6) 0 var(--space-4);
    }

    h3,
    [data-testid="stMarkdownContainer"] h3 {
        font-size: 22px;
        line-height: 1.32;
        margin: var(--space-2) 0 var(--space-3);
    }

    .stMarkdown p,
    [data-testid="stMarkdownContainer"] p,
    .muted {
        font-size: 16px;
        line-height: 1.72;
        color: var(--muted);
        margin-bottom: var(--space-4);
    }

    .eyebrow {
        display: inline-flex;
        align-items: center;
        height: 24px;
        margin-bottom: var(--space-3);
        color: var(--clay);
        font-size: 12px;
        line-height: 1;
        font-weight: 800;
        letter-spacing: .04em;
        text-transform: uppercase;
    }

    .hero {
        min-height: 560px;
        padding: 56px;
        border-radius: var(--radius);
        box-shadow: var(--shadow-md);
    }

    .hero h1 {
        max-width: 720px;
        font-size: 72px;
        line-height: .96;
        font-weight: 850;
    }

    .hero .subtitle {
        margin-top: var(--space-4);
        font-size: 28px;
        line-height: 1.25;
        font-weight: 800;
    }

    .hero p {
        max-width: 680px;
        margin-top: var(--space-4);
        color: rgba(255,255,255,.82);
        font-size: 17px;
        line-height: 1.75;
    }

    .card,
    .persona,
    .roadmap .step,
    div[data-testid="stMetric"] {
        border-radius: var(--radius);
        border: 1px solid var(--line);
        background: var(--panel);
        box-shadow: var(--shadow-sm);
    }

    .card {
        display: flex;
        flex-direction: column;
        min-height: 212px;
        padding: var(--space-5);
    }

    .card h3 {
        min-height: 58px;
        margin: var(--space-2) 0 var(--space-3);
        font-size: 23px;
        line-height: 1.28;
    }

    .card .muted {
        margin: 0;
        font-size: 16px;
    }

    .number {
        font-size: 12px;
        line-height: 1;
        font-weight: 800;
        letter-spacing: .04em;
    }

    .persona {
        min-height: 210px;
        padding: var(--space-5);
    }

    .persona strong {
        font-size: 22px;
        line-height: 1.32;
        margin-bottom: var(--space-3);
    }

    .roadmap {
        gap: var(--space-4);
    }

    .roadmap .step {
        min-height: 192px;
        padding: var(--space-5);
    }

    div[data-testid="stMetric"] {
        padding: var(--space-4);
        min-height: 118px;
    }

    div[data-testid="stMetric"] label,
    div[data-testid="stMetricLabel"] {
        font-size: 13px;
        color: var(--muted);
        font-weight: 700;
    }

    div[data-testid="stMetricValue"] {
        font-size: 30px;
        line-height: 1.15;
        font-weight: 800;
        color: var(--ink);
    }

    .pill-row,
    .animated-strip {
        gap: var(--space-3);
        margin: var(--space-5) 0;
    }

    .pill {
        padding: 7px 12px;
        font-size: 13px;
        font-weight: 700;
    }

    .signal {
        min-height: 126px;
        padding: var(--space-5);
    }

    .signal strong {
        font-size: 24px;
        line-height: 1.08;
        margin-bottom: var(--space-3);
    }

    .signal span {
        display: block;
        font-size: 15px;
        line-height: 1.55;
        color: rgba(255,255,255,.78);
    }

    .quote {
        margin: var(--space-5) 0;
        padding: var(--space-5);
        border-left-width: 4px;
        background: rgba(255,255,255,.58);
        border-radius: 0 var(--radius) var(--radius) 0;
        font-size: 28px;
        line-height: 1.35;
        font-weight: 800;
    }

    .big-number {
        font-size: 56px;
        line-height: 1;
        font-weight: 850;
    }

    .card:has(.matrix) {
        min-height: auto;
        padding: var(--space-5);
    }

    .card:has(.matrix) h3 {
        min-height: auto;
        margin-bottom: var(--space-4);
        font-size: 24px;
    }

    .matrix {
        box-shadow: var(--shadow-sm);
        font-size: 15px;
    }

    .matrix th,
    .matrix td {
        padding: var(--space-4);
        line-height: 1.62;
    }

    .matrix th {
        font-size: 14px;
        font-weight: 800;
    }

    .image-marquee,
    .photo-tile {
        border-radius: var(--radius);
        box-shadow: var(--shadow-md);
    }

    .team-identity-card {
        min-height: 100%;
        justify-content: center;
    }

    .team-identity-card h3 {
        min-height: auto;
        font-size: 28px;
        line-height: 1.25;
    }

    div[data-testid="stImage"] img {
        border-radius: var(--radius);
        border: 1px solid var(--line);
        box-shadow: var(--shadow-md);
    }

    .photo-caption,
    .marquee-item span {
        font-size: 13px;
        line-height: 1.45;
        font-weight: 700;
    }

    .card::after,
    .persona::after,
    .roadmap .step::after {
        display: none;
    }

    .card,
    .persona,
    .roadmap .step,
    .matrix,
    div[data-testid="stMetric"],
    .product-demo {
        animation: cardRise 420ms ease-out both;
    }

    .card:hover,
    .persona:hover,
    .roadmap .step:hover,
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }

    [data-testid="stSidebar"] {
        font-size: 15px;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        font-size: 15px;
        line-height: 1.68;
    }

    div[data-testid="stCaptionContainer"] {
        margin: 6px 0 var(--space-5);
        color: var(--muted);
        font-size: 14px;
        line-height: 1.55;
    }

    .stButton > button,
    div[data-testid="stFormSubmitButton"] button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 44px;
        padding: 0 var(--space-4);
        border-radius: var(--radius);
        font-size: 15px;
        line-height: 1.3;
        font-weight: 800;
        font-family: "Noto Sans TC", "Inter", system-ui, sans-serif;
        letter-spacing: 0.02em;
    }

    div[data-baseweb="input"] input,
    textarea,
    div[data-baseweb="select"] {
        font-size: 15px;
    }

    @media (max-width: 900px) {
        .block-container {
            padding-top: 40px;
        }

        h1,
        [data-testid="stMarkdownContainer"] h1 {
            font-size: 38px;
        }

        h2,
        [data-testid="stMarkdownContainer"] h2 {
            font-size: 26px;
        }

        .hero {
            min-height: 500px;
            padding: 32px;
        }

        .hero h1 {
            font-size: 48px;
        }

        .hero .subtitle {
            font-size: 24px;
        }

        .card,
        .persona,
        .roadmap .step {
            min-height: auto;
        }

        .card h3 {
            min-height: auto;
        }

        .split-panel,
        .roadmap,
        .photo-grid,
        .animated-strip {
            grid-template-columns: 1fr;
        }

        .marquee-item {
            flex-basis: 280px;
            height: 190px;
        }
    }
</style>
"""


def image_to_base64(path: Path) -> str:
    import base64

    if not path.exists():
        return ""
    return base64.b64encode(path.read_bytes()).decode("ascii")


def render_css() -> None:
    hero_b64 = image_to_base64(APARTMENT_SINK_IMAGE if APARTMENT_SINK_IMAGE.exists() else PROPOSAL_IMAGE)
    st.markdown(CUSTOM_CSS.replace("__HERO_PLACEHOLDER__", hero_b64), unsafe_allow_html=True)


def section_label(text: str) -> None:
    st.markdown(f'<div class="eyebrow">{text}</div>', unsafe_allow_html=True)


def card(number: str, title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="card">
            <div class="number">{number}</div>
            <h3>{title}</h3>
            <p class="muted">{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_product_demo() -> None:
    render_anim_component("solution", "30 秒替換水槽塞，油脂留在透明收集倉，清水繼續排出。")


def render_motion_visual(kind: str, label: str) -> None:
    render_anim_component(kind, label)


def render_anim_component(kind: str, label: str) -> None:
    team_b64 = image_to_base64(TEAM_MEMBERS_REDRAWN_IMAGE)
    titles = {
        "problem": "油脂阻塞形成路徑",
        "solution": "換上水槽塞後的油水分流",
        "product": "產品零件爆炸圖",
        "market": "校園通路擴散模型",
        "finance": "硬體銷售 + 濾芯回購",
        "pilot": "90 天校園試點流程",
        "radar": "評審問答防守儀表板",
        "team": "清大計財碩一團隊分工",
        "deck": "簡報轉成互動網站",
    }
    scenes = {
        "problem": """
          <div class="sink-cabinet"><div class="tiny-sink"></div><div class="dirty-pan"></div></div>
          <div class="pipe-main"></div><div class="pipe-turn"></div><div class="pipe-shadow"></div>
          <div class="grease-dot g1"></div><div class="grease-dot g2"></div><div class="grease-dot g3"></div><div class="grease-dot g4"></div>
          <div class="sticky-layer l1"></div><div class="sticky-layer l2"></div><div class="sticky-layer l3"></div>
          <div class="bug-risk">異味上升</div><div class="steam-wave w1"></div><div class="steam-wave w2"></div>
          <div class="scene-note n-left">油膩湯汁倒入</div><div class="scene-note n-mid">油脂冷卻附著</div><div class="scene-note n-right">排水變慢</div>
        """,
        "solution": """
          <div class="install-rail"></div>
          <div class="old-stopper">舊塞</div><div class="swap-arrow"></div><div class="new-stopper">Smart<br>Stopper</div>
          <div class="sink-bowl"></div><div class="cutaway-pipe"></div><div class="flow-vortex"></div>
          <div class="collector-tank"><div class="tank-oil"></div><div class="tank-water"></div><span>透明收集倉</span></div>
          <div class="water-exit"></div><div class="drop dx1"></div><div class="drop dx2"></div><div class="drop dx3"></div>
          <div class="step-chip c1">1 取下舊塞</div><div class="step-chip c2">2 壓入新塞</div><div class="step-chip c3">3 油水分流</div><div class="step-chip c4">4 倒掉收集倉</div>
        """,
        "product": """
          <div class="exploded-axis"></div>
          <div class="product-shell"></div><div class="product-lip"></div><div class="product-core"></div>
          <div class="gasket-ring"></div><div class="vane-wheel"><i></i><b></b><em></em></div>
          <div class="clear-chamber"><div class="chamber-oil"></div><div class="chamber-water"></div></div>
          <div class="filter-pack"><span></span></div>
          <div class="callout co1">A 密封圈：貼合落水頭</div><div class="callout co2">B 導流片：延長停留</div><div class="callout co3">C 收集倉：看得見油脂</div><div class="callout co4">D 濾芯：低額回購</div>
        """,
        "market": """
          <div class="campus-map"></div><div class="campus-hub">清大</div>
          <div class="market-path p-a"></div><div class="market-path p-b"></div><div class="market-path p-c"></div><div class="market-path p-d"></div>
          <div class="market-node dorm">第一站<br>外宿生</div><div class="market-node shop">購買點<br>五金/百貨</div><div class="market-node pack">開學季<br>新生租屋包</div><div class="market-node sub">每月<br>濾芯回購</div>
          <div class="packet pk1"></div><div class="packet pk2"></div><div class="packet pk3"></div>
        """,
        "finance": """
          <div class="money-flow">
            <div class="money-box box-price"><strong>硬體售價</strong><span>NT$150</span></div>
            <div class="flow-arrow a1"></div>
            <div class="money-box box-cost"><strong>扣除成本</strong><span>製造 + 包裝 + 通路</span></div>
            <div class="flow-arrow a2"></div>
            <div class="money-box box-profit"><strong>硬體毛利</strong><span>可支撐校園試點</span></div>
          </div>
          <div class="sub-flow">
            <div class="sub-card"><strong>每月濾芯</strong><span>低額回購</span></div>
            <div class="sub-arrow"></div>
            <div class="sub-card"><strong>LTV 增加</strong><span>不是只賣一次</span></div>
          </div>
          <div class="finance-bars"><div></div><div></div><div></div><div></div></div>
        """,
        "pilot": """
          <div class="calendar-grid"></div><div class="pilot-road"></div><div class="pilot-runner"></div>
          <div class="milestone m1"><strong>D1-15</strong><span>訪談</span></div>
          <div class="milestone m2"><strong>D16-35</strong><span>打樣</span></div>
          <div class="milestone m3"><strong>D36-65</strong><span>試用</span></div>
          <div class="milestone m4"><strong>D66-90</strong><span>開賣</span></div>
          <div class="kpi k1">適配率</div><div class="kpi k2">攔截量</div><div class="kpi k3">回購率</div>
        """,
        "radar": """
          <div class="judge-table">
            <div class="judge-row"><strong>1 痛點</strong><span>房東壓力 / 通管費 / 臭味</span></div>
            <div class="judge-row"><strong>2 解方</strong><span>不改管線，只換水槽塞</span></div>
            <div class="judge-row"><strong>3 商業</strong><span>NT$150 低門檻 + 濾芯回購</span></div>
            <div class="judge-row"><strong>4 執行</strong><span>清大周邊 90 天試點</span></div>
          </div>
          <div class="judge-score">
            <div class="score-axis x"></div><div class="score-axis y"></div>
            <div class="score-card p">痛點</div><div class="score-card s">解方</div><div class="score-card b">商業</div><div class="score-card e">執行</div>
            <div class="score-core">守住<br>四題</div>
          </div>
        """,
        "team": """
          <div class="team-board">
            <div class="member-card liao">
              <div class="portrait liao-photo"></div>
              <strong>廖怡絜</strong><span>成本、損益、定價</span>
            </div>
            <div class="member-card tseng">
              <div class="portrait tseng-photo"></div>
              <strong>曾楷芸</strong><span>市場、通路、訪談</span>
            </div>
            <div class="member-card chiou">
              <div class="portrait chiou-photo"></div>
              <strong>邱芷凡</strong><span>產品、規格、試點</span>
            </div>
          </div>
          <div class="team-output">共同產出：產品設計 + 財務模型 + 校園試點策略</div>
          <div class="team-line l1"></div><div class="team-line l2"></div><div class="team-line l3"></div>
        """,
        "deck": """
          <div class="deck-stack">
            <div class="slide-card s1">問題</div><div class="slide-card s2">解方</div>
            <div class="slide-card s3">市場</div><div class="slide-card s4">財務</div>
          </div>
          <div class="convert-arrow"></div><div class="browser-mock"><div class="browser-top"></div><div class="browser-hero"></div><div class="browser-row"></div><div class="browser-row short"></div></div>
          <div class="rule-badge">SWC</div><div class="rule-badge b2">Pitch</div>
        """,
    }
    html = """
    <style>
      body { margin:0; background:transparent; font-family:-apple-system,BlinkMacSystemFont,"Noto Sans TC","Segoe UI",sans-serif; }
      .scene { position:relative; height:360px; border:1px solid #d9dfd6; border-radius:8px; overflow:hidden; background:radial-gradient(circle at 18% 18%, rgba(240,180,92,.22), transparent 30%), linear-gradient(135deg,#fff,#eef4ec); box-shadow:0 22px 64px rgba(23,33,29,.12); color:#17211d; }
      .scene.team { height:520px; }
      .scene-title { position:absolute; left:22px; top:18px; z-index:30; padding:8px 12px; border-radius:999px; background:#17211d; color:white; font-size:15px; font-weight:900; letter-spacing:0; box-shadow:0 10px 22px rgba(23,33,29,.18); }
      .problem .sink-cabinet{position:absolute;left:8%;top:46px;width:180px;height:154px;border-radius:8px;background:#e5ebe7;box-shadow:inset 0 -36px #cbd6ce}.tiny-sink{position:absolute;left:24px;top:24px;width:132px;height:52px;border:10px solid #fff;border-radius:8px 8px 28px 28px;background:#dfe9e7}.dirty-pan{position:absolute;right:18px;top:30px;width:62px;height:34px;border-radius:50%;background:#536a7c;transform:rotate(-16deg);box-shadow:-34px 32px 0 -8px #f0b45c}
      .pipe-main{position:absolute;left:18%;right:13%;top:51%;height:52px;border-radius:999px;background:#536a7c;box-shadow:inset 0 0 0 12px rgba(255,255,255,.22)}.pipe-turn{position:absolute;right:8%;top:40%;width:130px;height:130px;border:44px solid #536a7c;border-left:0;border-bottom:0;border-radius:0 88px 0 0}.pipe-shadow{position:absolute;left:24%;right:20%;top:calc(51% + 15px);height:19px;border-radius:999px;background:rgba(23,33,29,.24)}
      .grease-dot{position:absolute;top:calc(51% + 14px);width:22px;height:22px;border-radius:50%;background:#f0b45c;box-shadow:0 0 0 9px rgba(240,180,92,.16);animation:oilTravel 4.2s infinite}.g1{left:22%}.g2{left:28%;animation-delay:.5s}.g3{left:34%;animation-delay:1s}.g4{left:40%;animation-delay:1.5s}.sticky-layer{position:absolute;top:calc(51% + 8px);height:36px;border-radius:999px;background:#c7653f;animation:sticky 3.6s infinite}.l1{right:30%;width:70px}.l2{right:23%;width:44px;animation-delay:.5s}.l3{right:16%;width:88px;animation-delay:1s}.bug-risk{position:absolute;right:16%;top:92px;padding:12px 16px;border-radius:999px;background:#17211d;color:white;font-weight:900;animation:float 2.6s infinite}.steam-wave{position:absolute;right:19%;top:124px;width:58px;height:90px;border-left:5px solid rgba(199,101,63,.5);border-radius:50%;animation:steam 3s infinite}.w2{right:25%;animation-delay:.7s}.scene-note{position:absolute;padding:8px 11px;border-radius:999px;background:white;border:1px solid #d9dfd6;font-weight:900;font-size:14px;box-shadow:0 8px 18px rgba(23,33,29,.1)}.n-left{left:8%;top:224px}.n-mid{left:44%;top:246px}.n-right{right:10%;top:260px}
      .install-rail{position:absolute;left:9%;right:9%;top:78px;height:8px;border-radius:999px;background:linear-gradient(90deg,#536a7c,#f0b45c,#78a083)}.old-stopper,.new-stopper{position:absolute;top:34px;width:94px;height:94px;border-radius:50%;display:grid;place-items:center;text-align:center;font-weight:900;box-shadow:0 18px 40px rgba(23,33,29,.18)}.old-stopper{left:12%;background:#cbd6ce;color:#59645f;animation:removeOld 5s infinite}.new-stopper{left:38%;background:#17211d;color:white;animation:insertNew 5s infinite}.swap-arrow{position:absolute;left:26%;top:76px;width:90px;height:12px;border-radius:999px;background:#c7653f;animation:arrowPush 2s infinite}.swap-arrow:after{content:"";position:absolute;right:-18px;top:-10px;border-left:25px solid #c7653f;border-top:16px solid transparent;border-bottom:16px solid transparent}
      .sink-bowl{position:absolute;left:20%;right:18%;bottom:94px;height:150px;border:18px solid #e5ebe7;border-top-width:26px;border-radius:8px 8px 54px 54px;background:rgba(255,255,255,.48)}.cutaway-pipe{position:absolute;left:45%;bottom:70px;width:90px;height:104px;border-radius:0 0 38px 38px;background:#536a7c}.flow-vortex{position:absolute;left:47%;bottom:148px;width:72px;height:72px;border-radius:50%;border:10px dashed #78a083;animation:spin 2.2s linear infinite}
      .collector-tank{position:absolute;right:14%;bottom:76px;width:120px;height:140px;border:8px solid rgba(255,255,255,.9);border-radius:8px 8px 34px 34px;background:rgba(255,255,255,.55);overflow:hidden;box-shadow:0 18px 38px rgba(23,33,29,.16)}.collector-tank span{position:absolute;left:9px;right:9px;top:8px;font-size:12px;font-weight:900;color:#496b58;text-align:center}.tank-oil,.tank-water{position:absolute;left:0;right:0;bottom:0}.tank-oil{bottom:48px;height:54px;background:rgba(240,180,92,.88);animation:tankOil 3s infinite}.tank-water{height:48px;background:rgba(85,160,185,.62);animation:tankWater 3s infinite}.water-exit{position:absolute;right:4%;bottom:132px;width:100px;height:16px;border-radius:999px;background:#4e9ab2;animation:waterPulse 1.4s infinite}
      .drop{position:absolute;width:16px;height:16px;border-radius:50%;background:#f0b45c;animation:dropArc 3.2s infinite}.dx1{left:39%;top:150px}.dx2{left:48%;top:190px;animation-delay:.45s}.dx3{left:56%;top:214px;animation-delay:.9s}.step-chip{position:absolute;padding:8px 11px;border-radius:999px;background:white;border:1px solid #d9dfd6;font-weight:900;font-size:13px;box-shadow:0 10px 24px rgba(23,33,29,.12);animation:chip 4s infinite}.solution .c1{left:8%;top:144px}.solution .c2{left:32%;top:144px;animation-delay:.4s}.solution .c3{right:30%;top:116px;animation-delay:.8s}.solution .c4{right:8%;top:236px;animation-delay:1.2s}
      .exploded-axis{position:absolute;left:12%;right:10%;top:202px;height:5px;border-radius:999px;background:linear-gradient(90deg,#496b58,#78a083,#f0b45c,#c7653f)}.product-shell{position:absolute;left:34%;top:94px;width:170px;height:198px;border-radius:78px 78px 36px 36px;background:linear-gradient(180deg,#f7faf8,#dfe9e7);box-shadow:inset 0 0 0 13px #fff,0 22px 48px rgba(23,33,29,.15)}.product-lip{position:absolute;left:30%;top:84px;width:230px;height:42px;border-radius:999px;background:#496b58;box-shadow:0 14px 28px rgba(23,33,29,.16);animation:pulse 2.4s infinite}.product-core{position:absolute;left:40%;top:138px;width:98px;height:98px;border-radius:50%;background:#17211d;box-shadow:inset 0 0 0 12px #78a083;animation:coreBeat 2s infinite}.gasket-ring{position:absolute;left:15%;top:132px;width:112px;height:112px;border-radius:50%;border:16px solid #496b58;box-shadow:inset 0 0 0 14px rgba(120,160,131,.28);animation:gasket 3s infinite}.vane-wheel{position:absolute;left:43%;top:162px;width:48px;height:48px;border-radius:50%;background:#f0b45c;animation:spin 1.8s linear infinite;z-index:4}.vane-wheel i,.vane-wheel b,.vane-wheel em{position:absolute;left:20px;top:-16px;width:9px;height:80px;border-radius:999px;background:#f0b45c;content:""}.vane-wheel b{transform:rotate(60deg)}.vane-wheel em{transform:rotate(120deg)}.clear-chamber{position:absolute;right:22%;top:136px;width:110px;height:144px;border-radius:12px 12px 32px 32px;border:8px solid rgba(255,255,255,.9);background:rgba(255,255,255,.55);overflow:hidden;animation:float 3.4s infinite}.chamber-oil{position:absolute;left:0;right:0;bottom:50px;height:50px;background:#f0b45c}.chamber-water{position:absolute;left:0;right:0;bottom:0;height:50px;background:#75aebe}.filter-pack{position:absolute;right:7%;top:158px;width:82px;height:110px;border-radius:10px;background:repeating-linear-gradient(45deg,#fff 0 8px,#e5ebe7 8px 16px);border:1px solid #d9dfd6;box-shadow:0 18px 34px rgba(23,33,29,.14);animation:filterSlide 3.2s infinite}.filter-pack span{position:absolute;inset:18px;border-radius:8px;background:rgba(199,101,63,.18)}.callout{position:absolute;padding:8px 10px;border-radius:999px;background:#17211d;color:white;font-weight:900;font-size:12px;white-space:nowrap}.co1{left:8%;top:260px}.co2{left:38%;top:52px}.co3{right:17%;top:286px}.co4{right:3%;top:118px}
      .campus-map{position:absolute;left:9%;right:9%;top:44px;bottom:54px;background:linear-gradient(90deg,rgba(73,107,88,.08) 1px,transparent 1px),linear-gradient(rgba(73,107,88,.08) 1px,transparent 1px);background-size:44px 44px;border-radius:8px}.campus-hub{position:absolute;left:50%;top:49%;transform:translate(-50%,-50%);width:102px;height:102px;border-radius:50%;background:#17211d;color:white;display:grid;place-items:center;font-weight:900;z-index:4;box-shadow:0 18px 42px rgba(23,33,29,.22)}.market-path{position:absolute;height:5px;border-radius:999px;background:#78a083;transform-origin:left;animation:pathPulse 2.8s infinite}.p-a{left:25%;top:39%;width:260px;transform:rotate(18deg)}.p-b{left:50%;top:50%;width:260px;transform:rotate(-22deg)}.p-c{left:36%;top:60%;width:240px;transform:rotate(145deg)}.p-d{left:50%;top:51%;width:250px;transform:rotate(42deg)}.market-node{position:absolute;padding:14px 16px;border-radius:8px;background:white;border:1px solid #d9dfd6;font-weight:900;box-shadow:0 16px 34px rgba(23,33,29,.12);animation:float 3.2s infinite}.dorm{left:12%;top:22%}.shop{right:12%;top:22%;animation-delay:.4s}.pack{left:16%;bottom:22%;animation-delay:.8s}.sub{right:15%;bottom:20%;animation-delay:1.2s}.packet{position:absolute;width:28px;height:22px;border-radius:5px;background:#f0b45c;box-shadow:inset 0 -6px rgba(199,101,63,.3);animation:packetRun 4.5s infinite}.pk1{left:31%;top:42%}.pk2{left:55%;top:34%;animation-delay:.9s}.pk3{left:56%;top:63%;animation-delay:1.8s}
      .money-flow{position:absolute;left:8%;right:8%;top:96px;display:grid;grid-template-columns:1fr 74px 1fr 74px 1fr;align-items:center;gap:12px}.money-box{height:112px;border-radius:8px;background:white;border:1px solid #d9dfd6;display:grid;place-items:center;text-align:center;box-shadow:0 16px 34px rgba(23,33,29,.12);animation:float 3.2s infinite}.money-box strong{font-size:19px}.money-box span{color:#c7653f;font-weight:900}.flow-arrow{height:8px;border-radius:999px;background:#c7653f;position:relative;animation:arrowPush 2.2s infinite}.flow-arrow:after{content:"";position:absolute;right:-12px;top:-8px;border-left:18px solid #c7653f;border-top:12px solid transparent;border-bottom:12px solid transparent}.a2{animation-delay:.5s}.sub-flow{position:absolute;left:23%;right:23%;bottom:44px;display:grid;grid-template-columns:1fr 80px 1fr;align-items:center;gap:12px}.sub-card{height:74px;border-radius:8px;background:#17211d;color:white;display:grid;place-items:center;text-align:center;font-weight:900;box-shadow:0 16px 34px rgba(23,33,29,.15)}.sub-card span{color:#f0b45c}.sub-arrow{height:6px;border-radius:999px;background:#78a083;position:relative}.sub-arrow:after{content:"";position:absolute;right:-10px;top:-7px;border-left:16px solid #78a083;border-top:10px solid transparent;border-bottom:10px solid transparent}.finance-bars{position:absolute;right:8%;bottom:42px;display:flex;align-items:end;gap:8px;height:78px;opacity:.32}.finance-bars div{width:28px;border-radius:7px 7px 0 0;background:#496b58;animation:barGrow 2s infinite alternate}.finance-bars div:nth-child(1){height:28px}.finance-bars div:nth-child(2){height:44px;animation-delay:.2s}.finance-bars div:nth-child(3){height:62px;animation-delay:.4s}.finance-bars div:nth-child(4){height:78px;animation-delay:.6s}
      .calendar-grid{position:absolute;inset:44px 9% 50px;border-radius:8px;background:linear-gradient(90deg,rgba(73,107,88,.08) 1px,transparent 1px);background-size:12.5% 100%;border:1px solid #d9dfd6}.pilot-road{position:absolute;left:12%;right:12%;top:51%;height:8px;border-radius:999px;background:linear-gradient(90deg,#496b58,#78a083,#f0b45c,#c7653f)}.pilot-runner{position:absolute;top:calc(51% - 14px);left:12%;width:34px;height:34px;border-radius:50%;background:#c7653f;box-shadow:0 0 0 10px rgba(199,101,63,.16);animation:runner 6s infinite}.milestone{position:absolute;width:120px;height:78px;border-radius:8px;background:white;border:1px solid #d9dfd6;display:grid;place-items:center;text-align:center;box-shadow:0 14px 30px rgba(23,33,29,.12);animation:float 3.2s infinite}.milestone strong{color:#c7653f}.milestone span{font-weight:900}.pilot .m1{left:8%;top:82px}.pilot .m2{left:31%;bottom:86px;animation-delay:.4s}.pilot .m3{left:55%;top:82px;animation-delay:.8s}.pilot .m4{right:7%;bottom:86px;animation-delay:1.2s}.kpi{position:absolute;padding:9px 12px;border-radius:999px;background:#17211d;color:white;font-weight:900;animation:chip 3s infinite}.k1{left:22%;top:42px}.k2{left:49%;top:42px;animation-delay:.5s}.k3{right:18%;top:42px;animation-delay:1s}
      .judge-table{position:absolute;left:8%;top:72px;width:430px;display:grid;gap:10px}.judge-row{height:52px;border-radius:8px;background:white;border:1px solid #d9dfd6;display:flex;align-items:center;gap:14px;padding:0 16px;box-shadow:0 12px 24px rgba(23,33,29,.1);animation:float 3.2s infinite}.judge-row:nth-child(2){animation-delay:.25s}.judge-row:nth-child(3){animation-delay:.5s}.judge-row:nth-child(4){animation-delay:.75s}.judge-row strong{min-width:72px;color:#c7653f}.judge-row span{font-weight:850;color:#17211d}.judge-score{position:absolute;right:8%;top:72px;width:280px;height:236px}.score-axis{position:absolute;background:#d9dfd6}.score-axis.x{left:20px;right:20px;top:50%;height:4px}.score-axis.y{top:20px;bottom:20px;left:50%;width:4px}.score-card{position:absolute;width:82px;height:54px;border-radius:8px;background:#17211d;color:white;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1;font-weight:900;padding:0 2px;box-shadow:0 14px 30px rgba(23,33,29,.16)}.score-card.p{left:99px;top:0}.score-card.s{right:0;top:91px;background:#496b58}.score-card.b{left:99px;bottom:0;background:#c7653f}.score-card.e{left:0;top:91px;background:#f0b45c;color:#17211d}.score-core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:92px;height:92px;border-radius:50%;background:white;border:8px solid #78a083;display:grid;place-items:center;text-align:center;font-weight:900;line-height:1.2;animation:pulse 2.6s infinite}
      .team-board{position:absolute;left:5%;right:5%;top:72px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;z-index:4}.member-card{height:342px;border-radius:8px;background:white;border:1px solid #d9dfd6;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center;gap:7px;padding:16px 14px 18px;box-shadow:0 16px 34px rgba(23,33,29,.12);animation:float 3.4s infinite}.member-card strong{font-size:24px;line-height:1.15;margin-top:6px}.member-card span{color:#c7653f;font-weight:900;font-size:16px;line-height:1.25;min-height:22px;display:flex;align-items:center;justify-content:center}.tseng{animation-delay:.35s}.chiou{animation-delay:.7s}.portrait{width:100%;max-width:220px;height:238px;border-radius:8px;background-image:url("data:image/png;base64,__TEAM_IMAGE__");background-size:660px auto;background-repeat:no-repeat;background-color:#f7f4ec;border:1px solid #d9dfd6;box-shadow:0 12px 24px rgba(23,33,29,.12);animation:portraitFloat 3.6s ease-in-out infinite}.liao-photo{background-position:0% 0%}.tseng-photo{background-position:50% 0%;animation-delay:.3s}.chiou-photo{background-position:100% 0%;animation-delay:.6s}.team-output{position:absolute;left:18%;right:18%;bottom:32px;height:58px;border-radius:8px;background:#17211d;color:white;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:900;font-size:18px;line-height:1.35;padding:0 18px;box-shadow:0 18px 38px rgba(23,33,29,.18);z-index:5}.team-line{position:absolute;height:4px;border-radius:999px;background:#f0b45c;transform-origin:center;z-index:2;opacity:.75}.team-line.l1{left:25%;top:428px;width:145px;transform:rotate(12deg)}.team-line.l2{left:45%;top:426px;width:140px}.team-line.l3{right:25%;top:428px;width:145px;transform:rotate(-12deg)}
      .deck-stack{position:absolute;left:10%;top:76px;width:300px;height:210px}.slide-card{position:absolute;width:136px;height:88px;border-radius:8px;background:white;border:1px solid #d9dfd6;display:grid;place-items:center;text-align:center;font-weight:900;box-shadow:0 14px 30px rgba(23,33,29,.12);animation:flipSlide 4s infinite}.deck .s1{left:0;top:0}.deck .s2{left:90px;top:36px;animation-delay:.35s}.deck .s3{left:178px;top:74px;animation-delay:.7s}.deck .s4{left:64px;top:132px;animation-delay:1.05s}.convert-arrow{position:absolute;left:44%;top:46%;width:118px;height:16px;border-radius:999px;background:#c7653f;animation:arrowPush 2.4s infinite}.convert-arrow:after{content:"";position:absolute;right:-18px;top:-12px;border-left:28px solid #c7653f;border-top:20px solid transparent;border-bottom:20px solid transparent}.browser-mock{position:absolute;right:10%;top:74px;width:292px;height:210px;border-radius:8px;background:#17211d;box-shadow:0 18px 42px rgba(23,33,29,.22);overflow:hidden}.browser-top{height:32px;background:#536a7c}.browser-hero{position:absolute;left:24px;right:24px;top:58px;height:62px;border-radius:8px;background:#78a083;animation:pulse 2.8s infinite}.browser-row{position:absolute;left:24px;right:24px;top:142px;height:14px;border-radius:999px;background:#f0b45c;animation:screenLine 2.8s infinite}.browser-row.short{top:172px;width:140px;background:#fff}.rule-badge{position:absolute;right:29%;bottom:66px;padding:11px 14px;border-radius:999px;background:#f0b45c;font-weight:900;animation:chip 3s infinite}.rule-badge.b2{right:11%;bottom:48px;background:white;border:1px solid #d9dfd6;animation-delay:.6s}
      @keyframes oilTravel{0%{transform:translateX(0);opacity:.2}55%{opacity:1}100%{transform:translateX(46vw);opacity:0}} @keyframes sticky{50%{transform:scaleX(1.28);filter:saturate(1.3)}} @keyframes steam{0%{transform:translateY(18px);opacity:0}50%{opacity:1}100%{transform:translateY(-42px);opacity:0}} @keyframes float{50%{transform:translateY(-13px)}} @keyframes portraitFloat{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-5px) scale(1.02)}} @keyframes removeOld{50%{transform:translate(-24px,-18px) rotate(-15deg);opacity:.45}} @keyframes insertNew{50%{transform:translate(0,122px) scale(.92)}} @keyframes arrowPush{50%{transform:translateX(18px);opacity:.72}} @keyframes spin{to{transform:rotate(360deg)}} @keyframes tankOil{50%{height:72px}} @keyframes tankWater{50%{height:38px}} @keyframes waterPulse{50%{transform:scaleX(1.18);opacity:.72}} @keyframes dropArc{0%{transform:translate(-44px,-44px);opacity:0}50%{opacity:1}100%{transform:translate(108px,96px);opacity:0}} @keyframes chip{50%{transform:translateY(-10px);filter:saturate(1.22)}} @keyframes pulse{50%{transform:scale(1.05)}} @keyframes coreBeat{50%{box-shadow:inset 0 0 0 20px #78a083;transform:scale(1.06)}} @keyframes gasket{50%{transform:scale(.9);border-color:#78a083}} @keyframes filterSlide{50%{transform:translateX(-20px)}} @keyframes pathPulse{50%{opacity:.45;filter:saturate(1.4)}} @keyframes packetRun{50%{transform:translate(160px,70px) rotate(12deg)}} @keyframes costOut{50%{transform:translateX(48px);opacity:.55}} @keyframes meter{50%{height:78%}} @keyframes coinFall{50%{transform:translateY(118px) rotate(180deg)}} @keyframes barGrow{from{transform:scaleY(.68)}to{transform:scaleY(1)}} @keyframes runner{0%{left:12%}100%{left:84%}} @keyframes screenLine{50%{width:82px;opacity:.55}} @keyframes radar{50%{clip-path:polygon(50% 8%,84% 18%,88% 76%,32% 84%,12% 42%);transform:translate(-50%,-50%) rotate(5deg)}} @keyframes sweep{to{transform:rotate(360deg)}} @keyframes flipSlide{50%{transform:translateY(-10px) rotateX(18deg)}}
    </style>
    <div class="scene __KIND__"><div class="scene-title">__TITLE__</div>__SCENE__</div>
    """
    html = (
        html.replace("__KIND__", kind)
        .replace("__TITLE__", titles[kind])
        .replace("__SCENE__", scenes[kind])
        .replace("__TEAM_IMAGE__", team_b64)
        .replace("__LABEL__", label)
    )
    components.html(html, height=540 if kind == "team" else 380, scrolling=False)
    st.caption(label)


def render_lab_visual(weekly_oil: float, captured: float, fill_ratio: float, capture_rate: int, clean_days: int) -> None:
    fill_percent = max(6, min(92, int(fill_ratio * 100)))
    html = f"""
    <style>
      body {{ margin:0; background:transparent; font-family:-apple-system,BlinkMacSystemFont,"Noto Sans TC","Segoe UI",sans-serif; }}
      .lab {{ position:relative; height:430px; border:1px solid #d9dfd6; border-radius:8px; overflow:hidden; background:radial-gradient(circle at 80% 20%, rgba(125,181,199,.22), transparent 29%), linear-gradient(135deg,#fff,#eef4ec); box-shadow:0 22px 64px rgba(23,33,29,.12); color:#17211d; }}
      .title {{ position:absolute; left:22px; top:18px; z-index:8; padding:8px 12px; border-radius:999px; background:#17211d; color:white; font-size:15px; font-weight:900; box-shadow:0 10px 22px rgba(23,33,29,.18); }}
      .bench {{ position:absolute; left:7%; right:7%; bottom:86px; height:28px; border-radius:999px; background:#536a7c; }}
      .reservoir {{ position:absolute; left:10%; top:92px; width:156px; height:176px; border-radius:12px 12px 36px 36px; border:8px solid rgba(255,255,255,.9); background:rgba(255,255,255,.58); overflow:hidden; box-shadow:0 18px 38px rgba(23,33,29,.14); }}
      .reservoir .oil {{ position:absolute; left:0; right:0; bottom:74px; height:{min(86, max(24, weekly_oil / 2)):.0f}px; background:#f0b45c; animation:oilPulse 2.6s infinite; }}
      .reservoir .water {{ position:absolute; left:0; right:0; bottom:0; height:74px; background:#75aebe; }}
      .tube {{ position:absolute; left:25%; top:176px; width:290px; height:18px; border-radius:999px; background:linear-gradient(90deg,#f0b45c,#78a083,#75aebe); animation:tubeFlow 1.6s infinite; }}
      .filter-unit {{ position:absolute; left:49%; top:118px; width:128px; height:150px; border-radius:16px; background:#17211d; box-shadow:0 20px 42px rgba(23,33,29,.24); }}
      .filter-unit:before {{ content:""; position:absolute; left:31px; top:28px; width:66px; height:66px; border-radius:50%; border:10px dashed #78a083; animation:spin 2s linear infinite; }}
      .collector {{ position:absolute; right:14%; top:98px; width:144px; height:190px; border:8px solid rgba(255,255,255,.9); border-radius:12px 12px 38px 38px; background:rgba(255,255,255,.6); overflow:hidden; box-shadow:0 18px 38px rgba(23,33,29,.14); }}
      .captured {{ position:absolute; left:0; right:0; bottom:0; height:{fill_percent}%; background:linear-gradient(180deg,#f0b45c,#c7653f); animation:fillWobble 3s infinite; }}
      .clean-water {{ position:absolute; right:4%; top:198px; width:106px; height:16px; border-radius:999px; background:#4e9ab2; animation:waterOut 1.4s infinite; }}
      .badge {{ position:absolute; padding:8px 11px; border-radius:999px; background:white; border:1px solid #d9dfd6; box-shadow:0 12px 26px rgba(23,33,29,.12); font-weight:900; font-size:13px; }}
      .b1 {{ left:8%; top:58px; }} .b2 {{ left:44%; top:58px; }} .b3 {{ right:10%; top:58px; }}
      .stage-label {{ position:absolute; padding:8px 10px; border-radius:999px; background:#17211d; color:white; font-weight:900; font-size:12px; }}
      .sl1 {{ left:12%; top:282px; }} .sl2 {{ left:49%; top:282px; }} .sl3 {{ right:13%; top:302px; }}
      .readout {{ position:absolute; left:18px; right:18px; bottom:14px; min-height:48px; display:flex; align-items:center; padding:10px 14px; border-radius:8px; background:rgba(255,255,255,.92); border:1px solid rgba(217,223,214,.95); z-index:4; font-size:18px; line-height:1.35; font-weight:850; box-shadow:0 12px 28px rgba(23,33,29,.12); }}
      .readout small {{ display:block; margin-left:10px; color:#59645f; font-size:13px; font-weight:800; }}
      @keyframes oilPulse {{ 50% {{ transform:scaleY(1.16); filter:saturate(1.25); }} }}
      @keyframes tubeFlow {{ 50% {{ opacity:.58; transform:scaleX(.95); }} }}
      @keyframes spin {{ to {{ transform:rotate(360deg); }} }}
      @keyframes fillWobble {{ 50% {{ transform:translateY(-8px); filter:saturate(1.2); }} }}
      @keyframes waterOut {{ 50% {{ transform:scaleX(1.18); opacity:.7; }} }}
    </style>
    <div class="lab">
      <div class="title">互動實驗室：即時油脂攔截模擬</div>
      <div class="badge b1">每週油脂 {weekly_oil:.0f} ml</div>
      <div class="badge b2">攔截效率 {capture_rate}%</div>
      <div class="badge b3">{clean_days} 天清理一次</div>
      <div class="reservoir"><div class="oil"></div><div class="water"></div></div>
      <div class="tube"></div><div class="filter-unit"></div>
      <div class="collector"><div class="captured"></div></div><div class="clean-water"></div><div class="bench"></div>
      <div class="stage-label sl1">倒入油水</div><div class="stage-label sl2">旋流分離</div><div class="stage-label sl3">收集油脂</div>
      <div class="readout">本月約攔截 {captured * 4:.0f} ml 油脂<small>左：倒入油水｜中：分流｜右：收集倉填滿程度</small></div>
    </div>
    """
    components.html(html, height=450, scrolling=False)


def render_photo_grid() -> None:
    messy = image_to_base64(MESSY_SINK_IMAGE)
    drain = image_to_base64(DRAIN_IMAGE)
    apartment = image_to_base64(APARTMENT_SINK_IMAGE)
    st.markdown(
        f"""
        <div class="photo-grid">
            <div class="photo-tile">
                <img src="data:image/jpeg;base64,{messy}" alt="messy kitchen sink with dishes">
                <div class="photo-caption">真實生活感：晚餐後的油膩碗盤與狹小水槽</div>
            </div>
            <div class="photo-stack">
                <div class="photo-tile small">
                    <img src="data:image/jpeg;base64,{drain}" alt="kitchen sink drain close up">
                    <div class="photo-caption">風險入口：油脂最後都會進到這裡</div>
                </div>
                <div class="photo-tile small">
                    <img src="data:image/jpeg;base64,{apartment}" alt="small apartment kitchen sink">
                    <div class="photo-caption">租屋場景：小套房、低預算、難施工</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_signal_strip() -> None:
    st.markdown(
        """
        <div class="animated-strip">
            <div class="signal"><strong>Oil</strong><span>殘油進入水槽前先被導流</span></div>
            <div class="signal"><strong>Trap</strong><span>油脂浮起，停留在透明收集倉</span></div>
            <div class="signal"><strong>Clean</strong><span>清水繼續排出，降低管壁累積</span></div>
            <div class="signal"><strong>Repeat</strong><span>可分解濾芯帶動低額回購</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_image_marquee() -> None:
    items = [
        (BASE_DIR / "assets" / "marquee-01-apartment-sink.jpg", "小套房水槽：空間小、難施工"),
        (BASE_DIR / "assets" / "marquee-02-messy-window-sink.jpg", "晚餐後水槽：髒碗盤與殘湯"),
        (BASE_DIR / "assets" / "marquee-03-drain-closeup.jpg", "排水口近照：油脂累積入口"),
        (BASE_DIR / "assets" / "marquee-04-dark-dirty-sink.jpg", "暗光廚房：真實生活的清潔拖延"),
        (BASE_DIR / "assets" / "marquee-05-stainless-drain.jpg", "金屬落水頭：租屋水槽常見規格"),
        (BASE_DIR / "assets" / "marquee-06-water-drain.jpg", "水流進排水孔：油脂跟著水走"),
        (BASE_DIR / "assets" / "marquee-07-running-faucet.jpg", "水龍頭沖洗：日常洗碗高頻場景"),
        (BASE_DIR / "assets" / "marquee-08-greasy-dishes.jpg", "油膩鍋具：最容易堵住管線的殘油"),
        (BASE_DIR / "assets" / "marquee-09-person-cleaning.jpg", "洗碗動作：學生不想碰油污"),
        (BASE_DIR / "assets" / "marquee-10-soapy-sink.jpg", "泡沫水槽：清潔後仍有殘留風險"),
    ]
    rendered = []
    for path, caption in items * 2:
        mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        rendered.append(
            f"""
            <div class="marquee-item">
                <img src="data:{mime};base64,{image_to_base64(path)}" alt="{caption}">
                <span>{caption}</span>
            </div>
            """
        )

    components.html(
        f"""
        <style>
            body {{
                margin: 0;
                background: transparent;
                font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "Segoe UI", sans-serif;
            }}
            .image-marquee {{
                position: relative;
                overflow: hidden;
                border-radius: 8px;
                border: 1px solid #d9dfd6;
                background: #111a16;
                box-shadow: 0 22px 64px rgba(23, 33, 29, .18);
            }}
            .image-marquee::before,
            .image-marquee::after {{
                content: "";
                position: absolute;
                top: 0;
                bottom: 0;
                z-index: 2;
                width: 120px;
                pointer-events: none;
            }}
            .image-marquee::before {{
                left: 0;
                background: linear-gradient(90deg, #111a16, transparent);
            }}
            .image-marquee::after {{
                right: 0;
                background: linear-gradient(270deg, #111a16, transparent);
            }}
            .marquee-track {{
                display: flex;
                width: max-content;
                gap: 16px;
                padding: 16px;
                animation: marqueeSlide 26s linear infinite;
            }}
            .image-marquee:hover .marquee-track {{
                animation-play-state: paused;
            }}
            .marquee-item {{
                position: relative;
                flex: 0 0 360px;
                height: 230px;
                overflow: hidden;
                border-radius: 8px;
                background: #26362f;
                box-shadow: 0 18px 42px rgba(0,0,0,.24);
            }}
            .marquee-item img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                transform: scale(1.06);
                animation: kenBurns 10s ease-in-out infinite alternate;
            }}
            .marquee-item span {{
                position: absolute;
                left: 12px;
                right: 12px;
                bottom: 12px;
                padding: 10px 12px;
                border-radius: 8px;
                background: rgba(23,33,29,.76);
                color: white;
                font-size: 14px;
                font-weight: 800;
                backdrop-filter: blur(10px);
            }}
            @keyframes marqueeSlide {{
                from {{ transform: translateX(0); }}
                to {{ transform: translateX(calc(-50% - 8px)); }}
            }}
            @keyframes kenBurns {{
                from {{ transform: scale(1.05) translate3d(-1%, -1%, 0); }}
                to {{ transform: scale(1.16) translate3d(2%, 1.5%, 0); }}
            }}
            @media (max-width: 720px) {{
                .marquee-item {{
                    flex-basis: 280px;
                    height: 190px;
                }}
            }}
        </style>
        <div class="image-marquee">
            <div class="marquee-track">
                {''.join(rendered)}
            </div>
        </div>
        """,
        height=270,
        scrolling=False,
    )


def render_deep_table(title: str, rows: list[tuple[str, str, str]]) -> None:
    body = "\n".join(
        f"""
        <tr>
            <td><strong>{name}</strong></td>
            <td>{detail}</td>
            <td>{why}</td>
        </tr>
        """
        for name, detail, why in rows
    )
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <table class="matrix">
                <thead>
                    <tr>
                        <th>項目</th>
                        <th>內容</th>
                        <th>說服力</th>
                    </tr>
                </thead>
                <tbody>{body}</tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_personas() -> None:
    personas = [
        ("宵夜型學生", "一週 4 次外食，常倒麵湯和火鍋湯。需要的是不改變習慣的預防。"),
        ("老屋套房族", "屋齡 20 年以上，水槽小、排水慢、怕房東扣押金。願意買低價保險。"),
        ("共用廚房宿舍", "多人使用、責任分散，最需要可視化收集倉提醒大家清理。"),
    ]
    cols = st.columns(3)
    for col, (name, body) in zip(cols, personas):
        with col:
            st.markdown(
                f"""
                <div class="persona">
                    <strong>{name}</strong>
                    <p class="muted">{body}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_roadmap() -> None:
    st.markdown(
        """
        <div class="roadmap">
            <div class="step">
                <div class="number">Week 1-2</div>
                <h3>校園訪談</h3>
                <p class="muted">訪談 30 位外宿學生，驗證倒油頻率、異味和通管成本痛點。</p>
            </div>
            <div class="step">
                <div class="number">Week 3-5</div>
                <h3>3D 打樣</h3>
                <p class="muted">測試密封圈尺寸、收集倉容量與拆洗手感，找出可量產結構。</p>
            </div>
            <div class="step">
                <div class="number">Week 6-8</div>
                <h3>宿舍試點</h3>
                <p class="muted">在清大周邊 20 個水槽試用，追蹤排水速度、異味與清理頻率。</p>
            </div>
            <div class="step">
                <div class="number">Month 3</div>
                <h3>開學季販售</h3>
                <p class="muted">與生活百貨、新生租屋包合作，推出水槽塞加濾芯入門組。</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_competitor_matrix() -> None:
    st.markdown(
        """
        <table class="matrix">
            <thead>
                <tr>
                    <th>方案</th>
                    <th>學生接受度</th>
                    <th>限制</th>
                    <th>我們的切入</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>傳統濾網</td>
                    <td>高，便宜且常見</td>
                    <td>攔截固體，不處理油脂與異味</td>
                    <td>補足油脂攔截與可視化收集</td>
                </tr>
                <tr>
                    <td>化學通管劑</td>
                    <td>中，堵塞後才會買</td>
                    <td>刺激性、對老舊管線有疑慮</td>
                    <td>從事後處理改為日常預防</td>
                </tr>
                <tr>
                    <td>大型油脂截留器</td>
                    <td>低，不適合小套房</td>
                    <td>安裝成本高、占空間</td>
                    <td>縮小成水槽塞規格，免施工</td>
                </tr>
            </tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )


def init_state() -> None:
    defaults = {
        "show_checkup": False,
        "checkup_done": False,
        "checkup_score": 0,
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def start_checkup() -> None:
    st.session_state.show_checkup = True


def score_level(score: int) -> tuple[str, str]:
    if score >= 14:
        return "高風險", "你的排水情境很適合用預防型油脂攔截裝置，尤其是老舊套房、小水槽和常倒湯汁的使用者。"
    if score >= 8:
        return "中風險", "目前已有阻塞和異味的前兆。建議先從水槽塞、濾網和每週清理開始，降低管線累積油脂。"
    return "低風險", "你的使用習慣相對安全，但若住處屋齡高或共用廚房頻率增加，仍建議備一個低成本預防工具。"


def render_checkup_form() -> None:
    st.subheader("租屋排水風險自我檢測")
    st.caption("6 題快速判斷你的水槽是否正走向阻塞、異味或蟲害風險。")

    questions = [
        (
            "你一週會把火鍋湯、乾麵醬汁、炸物油水倒進水槽幾次？",
            {"0 次": 0, "1-2 次": 1, "3-5 次": 3, "幾乎每天": 4},
        ),
        (
            "水槽排水速度最近是否變慢？",
            {"沒有": 0, "偶爾": 1, "明顯變慢": 3, "常常積水": 4},
        ),
        (
            "廚房或浴室排水口是否有異味？",
            {"沒有": 0, "偶爾有": 1, "每天都聞得到": 3, "異味會擴散到房間": 4},
        ),
        (
            "租屋處屋齡或管線狀態？",
            {"新屋或剛換管線": 0, "不確定": 1, "屋齡 20 年以上": 3, "曾經堵塞或漏水": 4},
        ),
        (
            "你願意每週拆洗水槽濾網或存水彎嗎？",
            {"願意而且會做": 0, "偶爾會": 1, "很少做": 3, "完全不想碰": 4},
        ),
        (
            "你能接受一次通管維修約 1500 元嗎？",
            {"可以接受": 0, "有點心痛": 1, "希望盡量避免": 3, "完全不能接受": 4},
        ),
    ]

    with st.form("risk_checkup"):
        total = 0
        for index, (question, options) in enumerate(questions, start=1):
            choice = st.radio(
                f"{index}. {question}",
                list(options.keys()),
                horizontal=True,
                key=f"risk_q{index}",
            )
            total += options[choice]

        submitted = st.form_submit_button("查看檢測結果", use_container_width=True)

    if submitted:
        st.session_state.checkup_done = True
        st.session_state.checkup_score = total

    if st.session_state.checkup_done:
        score = st.session_state.checkup_score
        level, advice = score_level(score)
        st.progress(score / 24)
        left, right = st.columns([1, 2])
        left.metric("風險分數", f"{score}/24", level, border=True)
        with right:
            st.markdown(
                f"""
                <div class="card">
                    <h3>{level}</h3>
                    <p class="muted">{advice}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def page_demo_lab() -> None:
    render_css()
    section_label("Interactive Demo Lab")
    st.title("油脂攔截互動實驗室")
    st.markdown(
        """
        評審通常會問：這個東西到底怎麼工作？這頁把抽象技術變成可操作的 demo。
        調整倒油頻率、用水量和清理頻率，就能看到估計攔截量和維護提醒。
        """
    )
    render_signal_strip()

    left, right = st.columns([1.05, 1])
    with right:
        meals = st.slider("每週油膩餐點次數", 0, 14, 6)
        oil_per_meal = st.slider("每餐平均油脂殘留量 ml", 2, 40, 14)
        capture_rate = st.slider("目標攔截效率", 40, 90, 72, format="%d%%")
        clean_days = st.slider("幾天清理一次收集倉", 1, 14, 7)

        weekly_oil = meals * oil_per_meal
        captured = weekly_oil * capture_rate / 100
        monthly_captured = captured * 4
        collector_capacity = 120
        fill_ratio = min(1.0, (captured / 7 * clean_days) / collector_capacity)

        st.metric("每週進入水槽油脂", f"{weekly_oil:.0f} ml", border=True)
        st.metric("每月預估攔截", f"{monthly_captured:.0f} ml", f"{capture_rate}% 效率", border=True)
        st.progress(fill_ratio)
        if fill_ratio >= 0.85:
            st.warning("收集倉接近滿載，建議縮短清理週期。")
        elif fill_ratio >= 0.5:
            st.info("目前清理週期可行，但開學季或共用廚房建議更勤清理。")
        else:
            st.success("目前清理週期舒適，適合懶人使用情境。")
    with left:
        render_lab_visual(weekly_oil, captured, fill_ratio, capture_rate, clean_days)

    st.divider()
    section_label("User Personas")
    st.header("三個最容易買單的使用者")
    render_personas()

    st.divider()
    section_label("Scenario Presets")
    st.header("三種常見租屋情境的建議設定")
    cols = st.columns(3)
    with cols[0]:
        card("Light", "偶爾開伙", "每週 1-2 次油膩餐點，建議 10-14 天清理一次，適合低風險用戶。")
    with cols[1]:
        card("Student", "外食高頻", "每週 5-8 次油膩餐點，建議每週清理一次，濾芯月更換。")
    with cols[2]:
        card("Shared", "共用廚房", "多人倒湯且責任分散，建議 3-5 天清理一次，搭配可視提醒。")

    render_deep_table(
        "Demo 數字如何解讀",
        [
            ("每週油脂 ml", "油膩餐點次數乘以每餐殘油", "讓使用者理解日常累積速度。"),
            ("攔截效率", "用 40%-90% 作為可調假設", "比賽時可根據實測更新。"),
            ("收集倉滿載", "清理週期與容量換算", "直接回答會不會溢出的疑問。"),
            ("每月攔截量", "把小油滴放大成月度數字", "讓產品價值更可視化。"),
        ],
    )


def page_financials() -> None:
    render_css()
    section_label("Financial Model")
    st.title("價格、毛利與校園試點試算")
    render_motion_visual("finance", "低價硬體打開入口，濾芯回購拉高生命週期價值。")
    st.markdown(
        "這頁讓提案從產品創意走向商業可行性。數字是可調模型，方便你比賽前練習回答成本與損益問題。"
    )

    st.subheader("單位經濟模型")
    col1, col2, col3, col4 = st.columns(4)
    price = col1.number_input("單入售價 NT$", min_value=80, max_value=400, value=150, step=10)
    unit_cost = col2.number_input("單入製造成本 NT$", min_value=20, max_value=220, value=58, step=5)
    channel_fee = col3.number_input("通路/包裝成本 NT$", min_value=0, max_value=120, value=28, step=5)
    filter_margin = col4.number_input("每月濾芯毛利 NT$", min_value=0, max_value=80, value=12, step=2)

    gross_profit = price - unit_cost - channel_fee
    gross_margin = gross_profit / price if price else 0
    payback_months = price / max(filter_margin, 1)

    metrics = st.columns(4)
    metrics[0].metric("單入毛利", f"NT${gross_profit:.0f}", border=True)
    metrics[1].metric("硬體毛利率", f"{gross_margin:.0%}", border=True)
    metrics[2].metric("濾芯年毛利", f"NT${filter_margin * 12:.0f}", border=True)
    metrics[3].metric("通管費可買", f"{1500 // max(price, 1):.0f} 個", "以 NT$1500 估", border=True)

    st.divider()
    st.subheader("校園市場滲透試算")
    left, right = st.columns([1, 1])
    with left:
        target_students = st.slider("第一波可觸及外宿學生", 500, 30000, 6000, step=500)
        adoption = st.slider("首年購買率", 1, 35, 8, format="%d%%")
        subscription = st.slider("濾芯訂閱轉換率", 0, 80, 30, format="%d%%")
    with right:
        units = target_students * adoption / 100
        hardware_revenue = units * price
        hardware_profit = units * gross_profit
        annual_filter_profit = units * subscription / 100 * filter_margin * 12
        total_profit = hardware_profit + annual_filter_profit

        st.metric("首年銷量", f"{units:,.0f} 個", border=True)
        st.metric("硬體營收", f"NT${hardware_revenue:,.0f}", border=True)
        st.metric("首年總毛利", f"NT${total_profit:,.0f}", "含濾芯", border=True)

    st.caption("註：以上為 pitch 用模型，用來展示商業邏輯；實際數字仍需依打樣報價和通路條件修正。")

    st.divider()
    section_label("Sensitivity")
    st.header("評審可能追問的財務敏感度")
    render_deep_table(
        "三個會影響毛利的關鍵槓桿",
        [
            ("製造成本", "若從 NT$58 升到 NT$80，硬體毛利會明顯壓縮", "需要用設計簡化和模具攤提控制成本。"),
            ("通路抽成", "校園店與百貨通路條件不同", "早期可用直售與租屋包合作保留毛利。"),
            ("濾芯轉換", "訂閱率從 15% 到 40% 會改變 LTV", "透明收集倉和異味改善是推動回購的關鍵。"),
            ("售價帶", "NT$129-199 是學生可接受區間", "比一次通管費低很多，心理上像買保險。"),
        ],
    )

    st.subheader("可以帶到台上的一句財務說法")
    st.info("我們不追求高單價硬體，而是用 NT$150 的低門檻進入學生租屋場景，再用濾芯和開學季組合包提高生命週期價值。")


def page_pilot_strategy() -> None:
    render_css()
    section_label("Pilot Strategy")
    st.title("從清大周邊開始的試點計畫")
    render_motion_visual("pilot", "訪談、打樣、試點、開學季販售，90 天形成可驗證節奏。")
    st.markdown(
        """
        競賽網站要讓評審相信你知道下一步怎麼做。這裡把產品驗證、校園通路和開學季銷售排成
        90 天行動節奏。
        """
    )

    render_roadmap()

    st.divider()
    section_label("Channel Playbook")
    st.header("通路打法")
    cols = st.columns(3)
    with cols[0]:
        card("01", "五金與百貨", "先讓產品出現在學生真的會買水管用品、衣架、延長線的地方。")
    with cols[1]:
        card("02", "租屋包合作", "和床墊、垃圾桶、曬衣架一起進入新生開學採買清單。")
    with cols[2]:
        card("03", "宿舍共用廚房", "用多人場景快速累積油脂攔截案例，變成社群素材。")

    st.divider()
    section_label("Competitor Matrix")
    st.header("競品與替代方案比較")
    render_competitor_matrix()

    st.divider()
    section_label("Pilot KPI")
    st.header("試點要收集的 8 個指標")
    render_deep_table(
        "從試用回饋走向量產決策",
        [
            ("適配率", "不同租屋水槽能否安裝", "低於 80% 就需要重新設計密封圈。"),
            ("漏水率", "邊緣是否有水流繞過產品", "直接影響使用者信任。"),
            ("每週攔截量", "透明收集倉實際累積油脂 ml", "證明產品不是心理安慰。"),
            ("清理完成率", "使用者是否願意定期倒掉收集倉", "決定長期留存。"),
            ("異味改善", "使用前後主觀評分", "是最容易被學生感受到的價值。"),
            ("排水速度", "安裝後是否影響正常排水", "不能因為攔截油脂而造成新麻煩。"),
            ("購買意願", "試用後願意支付價格", "驗證 NT$150 定價。"),
            ("推薦意願", "是否願意推薦室友或同學", "決定校園口碑能否擴散。"),
        ],
    )


def page_judge_room() -> None:
    render_css()
    section_label("Judge Room")
    st.title("評審問答備戰室")
    render_motion_visual("radar", "把問題、解法、商業、執行四個評分面向守住。")
    st.markdown("把最可能被問到的問題先放進網站，讓提案看起來更成熟。")

    faqs = [
        (
            "為什麼學生會願意買？",
            "因為它把一次 NT$1500 左右的通管焦慮，變成 NT$150 的預防型保險。學生不一定愛清潔，但很怕房東、押金和臭味。",
        ),
        (
            "跟一般濾網差在哪？",
            "濾網主要攔固體，油脂仍會隨水流進管線。這個產品把油脂導入透明收集倉，讓油脂被看見、被清掉。",
        ),
        (
            "會不會很難清？",
            "產品設計重點是可抽取收集盒，清理方式接近倒垃圾；如果清理仍太麻煩，學生就不會持續使用。",
        ),
        (
            "技術門檻在哪？",
            "核心不是電子技術，而是小體積內的油水分流、密封適配、容量與清理手感。這些會決定能否真的進入租屋日常。",
        ),
        (
            "下一步驗證什麼？",
            "先驗證三件事：不同落水頭適配率、實際油脂攔截量、學生清理意願。這三個數據會決定量產版本。",
        ),
    ]

    for question, answer in faqs:
        with st.expander(question):
            st.write(answer)

    st.divider()
    section_label("Pitch Timer")
    st.header("60 秒電梯簡報")
    script = """
    外宿學生最怕的不是做家事，而是水管堵住後的房東壓力、通管費和整間房間的臭味。
    Smart Grease-Trap Stopper 是一個專為學生租屋設計的油脂攔截水槽塞。
    它不需要插電、不需要改管線，也不要求學生改變飲食，只要換上水槽塞，
    就能把油脂留在透明收集倉，讓乾淨水流走。
    我們用 NT$150 的低門檻，取代一次 NT$1500 的事後維修；
    再透過校園五金、開學租屋包和濾芯訂閱建立回購。
    這不是一個水槽小物，而是外宿生活品質的低成本防線。
    """
    st.text_area("可直接練習的口說稿", script.strip(), height=190)

    st.divider()
    section_label("Scoring Rubric")
    st.header("回答時要守住的四條主線")
    cols = st.columns(4)
    with cols[0]:
        card("P", "痛點清楚", "不要只說堵塞，要說房東壓力、通管費、臭味和蟲害。")
    with cols[1]:
        card("S", "解法簡單", "不改習慣、不改管線、不插電，只換水槽塞。")
    with cols[2]:
        card("B", "商業低門檻", "NT$150 買排水保險，濾芯帶回購。")
    with cols[3]:
        card("E", "執行可驗證", "用 90 天試點拿適配率、攔截量、購買意願。")

    render_deep_table(
        "評審尖銳問題與防守方向",
        [
            ("油脂真的能攔多少？", "承認需要試點實測，先用 demo 模型展示假設", "誠實且有實驗計畫，比硬說有效更可信。"),
            ("學生會清理嗎？", "透明收集倉加低沾手拆卸，並測清理完成率", "把行為問題變成產品設計問題。"),
            ("會不會太小眾？", "從清大外宿生切入，再擴到青年租屋、小套房、共用廚房", "小場景可以是進入大市場的 wedge。"),
            ("競品會不會很容易做？", "重點在通用適配、清理體驗、通路組合和濾芯回購", "不只是一個塑膠件，而是完整使用情境。"),
        ],
    )


def page_home() -> None:
    render_css()
    init_state()

    render_image_marquee()

    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">Startup World Cup Pitch</div>
            <h1>Smart Grease-Trap Stopper</h1>
            <div class="subtitle">外宿族的排水守護者</div>
            <p>
                用一個可替換的水槽塞，在學生倒湯、洗鍋、清廚餘的日常瞬間，
                自動攔截油脂、減少惡臭，讓老舊租屋管線少一點崩潰。
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    metric_cols = st.columns(3)
    metric_cols[0].metric("目標入手價", "NT$150", "比一次通管低很多", border=True)
    metric_cols[1].metric("電費與電池", "0", "純物理分流", border=True)
    metric_cols[2].metric("清理時間", "3 min", "像倒垃圾一樣", border=True)
    render_signal_strip()

    st.markdown(
        """
        <div class="pill-row">
            <span class="pill">租屋水槽</span>
            <span class="pill">開學季剛需</span>
            <span class="pill">低價硬體</span>
            <span class="pill">可回購濾芯</span>
            <span class="pill">免施工</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    section_label("Self Check")
    left, right = st.columns([1.1, 1])
    with left:
        st.header("先測你是不是高風險租屋水槽")
        st.markdown(
            """
            這個網站不只展示產品，也讓評審一開始就能進入使用情境。
            自我檢測會把「油膩外食、老舊管線、異味、維修成本」轉成可視化分數，
            讓痛點更直覺。
            """
        )
        st.markdown(
            """
            - 6 題快速判斷你的水槽是否已經開始積油
            - 從日常倒湯、清理習慣到維修成本承受度
            - 回答後立即得到「低 / 中 / 高風險」與行動建議
            """
        )
        st.button(
            "開始自我檢測",
            type="primary",
            on_click=start_checkup,
            use_container_width=True,
            key="start_checkup_button",
        )
        st.info("點擊後會展開題目表單，回答完就能看到即時風險評分與建議。", icon="⚡")

    with right:
        st.markdown(
            """
            <div class="card">
                <h3>檢測設計</h3>
                <p class="muted">
                    題目聚焦於倒油頻率、排水速度、異味、屋齡、清理意願與維修成本承受度。
                    結果分成低、中、高風險，最後導回產品價值。
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if st.session_state.show_checkup:
        st.divider()
        render_checkup_form()

    st.divider()
    section_label("Pitch Map")
    st.header("評審進站後 90 秒會看到什麼")
    cols = st.columns(4)
    with cols[0]:
        card("1", "痛點立即共鳴", "先用自我檢測讓評審進入租屋水槽情境。")
    with cols[1]:
        card("2", "產品可視化", "用互動 demo 展示油脂如何被攔截。")
    with cols[2]:
        card("3", "商業可試算", "價格、成本、滲透率都能調整，直接回答毛利問題。")
    with cols[3]:
        card("4", "落地有路線", "試點計畫、通路打法、評審 FAQ 全部放入網站。")

    st.divider()
    section_label("Why Now")
    st.header("為什麼現在適合做這個產品")
    cols = st.columns(3)
    with cols[0]:
        card("A", "外食日常化", "學生生活高度依賴外食與外送，油膩湯汁和醬料成為水槽的日常負擔。")
    with cols[1]:
        card("B", "租屋成本壓力", "房租、押金與維修費讓學生更願意接受低價預防型工具，而不是事後補救。")
    with cols[2]:
        card("C", "開學季採購窗口", "新生搬家時會一次購買生活用品，是水槽塞進入租屋包的最佳時點。")

    render_deep_table(
        "網站如何對應 SWC Pitch 評分邏輯",
        [
            ("Problem", "自我檢測、情境圖、痛點卡片", "讓評審快速感到這是真實日常，不是硬湊題目。"),
            ("Solution", "產品 demo、油脂流向、使用前後差異", "把看不見的油脂攔截變成可理解的互動體驗。"),
            ("Business", "財務試算、通路打法、訂閱濾芯", "讓產品從小物件變成可規模化的商業模型。"),
            ("Execution", "90 天試點、KPI、FAQ", "預先回答評審最在意的落地與風險問題。"),
        ],
    )


def page_problem() -> None:
    render_css()
    section_label("Problem")
    st.title("學生租屋最尷尬的維修問題")
    st.markdown(
        "外宿學生不是不知道油會堵管線，而是租屋生活太小、太趕、太不想碰油污。"
    )
    render_motion_visual("problem", "油脂進入管線，冷卻、附著，最後變成阻塞與異味。")

    cols = st.columns(3)
    with cols[0]:
        card("01", "外食油膩", "火鍋、乾麵、炸物便當的殘餘湯汁直接進水槽，油脂冷卻後黏附管壁。")
    with cols[1]:
        card("02", "修繕困難", "老舊套房管線窄、轉角多，一旦堵住就要面對房東、室友與通管費。")
    with cols[2]:
        card("03", "衛生失控", "狹小空間裡，水管惡臭會迅速佔滿生活環境，並提高蟲害風險。")

    st.write("")
    st.markdown(
        """
        <div class="quote">
            真正的問題不是水槽堵住，而是學生沒有一個便宜、直覺、願意每天用的預防工具。
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    section_label("Oil Journey")
    st.header("一碗火鍋湯進水槽後會發生什麼")
    cols = st.columns(4)
    with cols[0]:
        card("1", "熱湯倒入", "油脂在高溫下跟水一起流動，學生通常看不出立即風險。")
    with cols[1]:
        card("2", "管線冷卻", "油脂溫度下降後變黏，開始附著在管壁、轉角與毛髮殘渣上。")
    with cols[2]:
        card("3", "流速下降", "殘渣堆積讓排水慢，異味開始從排水口反上來。")
    with cols[3]:
        card("4", "事後維修", "真正堵住後只能通管、聯絡房東或自行使用刺激性清潔劑。")

    render_deep_table(
        "利害關係人痛點",
        [
            ("學生", "臭味、蟲害、通管費、押金壓力", "使用者願意為低價預防付費。"),
            ("房東", "維修溝通成本、老舊管線損耗", "可作為入住配件降低日後糾紛。"),
            ("室友/共用廚房", "責任分散，沒人想清油污", "透明收集倉讓問題可見，促進共同清理。"),
            ("校園周邊店家", "開學季生活用品需求集中", "容易和現有商品組合銷售。"),
        ],
    )


def page_solution() -> None:
    render_css()
    section_label("Solution")
    st.title("懶人式油脂攔截系統")
    st.markdown(
        "不改管線、不插電、不要求學生先分類湯汁。只要更換水槽塞，就能把油脂導入透明收集倉。"
    )
    render_signal_strip()

    left, right = st.columns([1, 1])
    with left:
        render_product_demo()
    with right:
        st.subheader("核心流程")
        st.markdown(
            """
            1. 倒入含油湯汁或清洗油膩碗盤  
            2. 導流結構延長油水停留時間  
            3. 油脂留在透明收集倉，水流繼續排出  
            4. 收集盒取出後直接清理，不徒手接觸油污
            """
        )
        st.info("Pitch 重點：我們不是改變學生飲食，而是降低學生做對事情的門檻。")

        st.subheader("使用前後差異")
        st.markdown(
            """
            | 情境 | 沒有產品 | 使用後 |
            |---|---|---|
            | 倒火鍋湯 | 油脂進管線冷卻黏附 | 油脂停留在收集倉 |
            | 排水變慢 | 只能等堵塞後通管 | 先把累積源頭減少 |
            | 惡臭 | 住處小，臭味擴散快 | 降低油脂腐敗殘留 |
            """
        )

    st.divider()
    section_label("Install Flow")
    st.header("30 秒安裝流程")
    cols = st.columns(4)
    with cols[0]:
        card("01", "取下原水槽塞", "不需要工具，不拆管線，只處理水槽上方可接觸部位。")
    with cols[1]:
        card("02", "壓入密封圈", "彈性密封圈貼合常見落水頭，避免水流從邊緣漏過。")
    with cols[2]:
        card("03", "扣上收集倉", "透明盒朝向使用者，讓油脂累積狀態可被看見。")
    with cols[3]:
        card("04", "倒掉收集物", "收集倉滿了就拆下清理，濾芯可每月更換。")

    render_deep_table(
        "產品設計要處理的真實情境",
        [
            ("熱湯", "耐熱 PP 與可替換濾芯需承受短時間高溫", "避免學生倒火鍋湯時變形或異味。"),
            ("小水槽", "本體高度不能影響洗碗和放鍋", "租屋處空間很小，產品不能變成阻礙。"),
            ("懶人清理", "收集盒要可單手取出、少沾手", "清理門檻決定留存率。"),
            ("尺寸差異", "密封圈需涵蓋常見廉價落水頭", "通用性決定第一波校園通路是否能賣。"),
        ],
    )


def page_product() -> None:
    render_css()
    section_label("Product")
    st.title("為學生優化的實體構造")
    render_motion_visual("product", "四個核心零件：密封、導流、收集、濾芯。")

    cols = st.columns(3)
    with cols[0]:
        card("A", "通用接口", "彈性密封圈適配租屋處常見廉價落水頭，不需改裝原有設備。")
    with cols[1]:
        card("B", "透明收集倉", "看得見油脂被攔截，降低忘記清理的機率，也讓效果一眼可懂。")
    with cols[2]:
        card("C", "簡易清理", "收集盒可快速取出，像倒垃圾一樣處理，不需要徒手接觸油污。")

    st.divider()
    section_label("Underlying Magic")
    st.header("純物理分流，零電費、低故障率")

    cols = st.columns(3)
    cols[0].metric("Gravity", "油水比重差", "自然分層", border=True)
    cols[1].metric("Centrifugal Flow", "導流停留", "提高攔截", border=True)
    cols[2].metric("Industrial PP", "耐熱耐酸鹼", "量產友善", border=True)

    st.markdown(
        """
        <div class="pill-row">
            <span class="pill">零電費</span>
            <span class="pill">零電池</span>
            <span class="pill">低故障率</span>
            <span class="pill">目標售價 NT$150</span>
            <span class="pill">可搭配可分解濾芯</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    section_label("Design Details")
    st.header("量產前要驗證的 4 個設計參數")
    cols = st.columns(4)
    cols[0].metric("密封圈外徑", "32-45 mm", "租屋落水頭", border=True)
    cols[1].metric("收集倉容量", "80-120 ml", "一週清理", border=True)
    cols[2].metric("耐熱溫度", "90°C", "熱湯情境", border=True)
    cols[3].metric("拆洗動作", "< 3 min", "降低抗拒", border=True)

    st.divider()
    section_label("BOM Concept")
    st.header("初版量產構成")
    render_deep_table(
        "BOM 與設計理由",
        [
            ("上蓋濾網", "攔截固體菜渣、麵條、飯粒", "避免固體物進入分流倉，降低卡住風險。"),
            ("導流葉片", "讓含油水流形成旋轉與停留", "增加油水分離時間，是核心物理設計。"),
            ("透明收集倉", "可視化油脂累積，可拆卸", "讓效果可被看見，也提醒使用者清理。"),
            ("矽膠密封圈", "彈性適配不同落水頭", "解決租屋處設備規格不一致。"),
            ("濾芯包", "可分解油脂吸附材料", "建立每月低價回購與清新維護。"),
        ],
    )

    st.subheader("MVP 測試版本")
    cols = st.columns(3)
    with cols[0]:
        card("V1", "3D 列印外殼", "快速驗證尺寸、清理手感和水流方向。")
    with cols[1]:
        card("V2", "矽膠圈套件", "測試不同水槽落水頭的適配率與漏水問題。")
    with cols[2]:
        card("V3", "小批量射出", "進入 20-50 組校園試點，收集真實油脂量。")


def page_market() -> None:
    render_css()
    section_label("Market Opportunity")
    st.title("百萬外宿學生與青年，都需要一份排水保險")
    render_motion_visual("market", "從清大周邊外宿生開始，向青年租屋與共用廚房擴散。")

    left, right = st.columns([1.1, 1])
    with left:
        st.markdown(
            """
            在老舊建築、低預算租屋與高頻率外食交會的場景中，
            Smart Grease-Trap Stopper 把昂貴維修變成低價預防。
            """
        )
        st.markdown(
            """
            <div class="card">
                <div class="big-number">10x</div>
                <p class="muted">一次通管費約等於十個預防型水槽塞。學生更願意花 NT$150 買一份排水保險。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.metric("潛在客群", "100萬+", "外宿學生與青年", border=True)
        st.metric("常見租屋屋齡", "20年+", "管線老化風險", border=True)
        st.metric("濾芯訂閱", "< NT$20/月", "提高回購", border=True)

    st.divider()
    section_label("Business Model")
    st.header("從開學季切入，讓耗材帶動回購")
    cols = st.columns(3)
    with cols[0]:
        card("Launch", "校園周邊通路", "五金行、文具店、小北百貨與宿舍生活用品店。")
    with cols[1]:
        card("Bundle", "新生租屋包", "與床墊、衣架、延長線一起成為入住第一批採買。")
    with cols[2]:
        card("Recurring", "訂閱濾芯", "可分解油脂吸附包，每月不到 20 元維持清新。")

    st.divider()
    section_label("Go-To-Market Detail")
    st.header("三階段上市打法")
    render_deep_table(
        "通路與轉換策略",
        [
            ("校園驗證", "清大周邊租屋學生、宿舍共用廚房、小套房", "先在最熟悉的場景拿到案例與推薦。"),
            ("開學套組", "與床墊、衣架、延長線、垃圾桶一起包裝", "搬家時學生最願意一次買齊生活用品。"),
            ("生活百貨", "五金行、小北百貨、校園附近文具生活店", "產品不需教育太久，適合衝動型低價購買。"),
            ("濾芯回購", "QR code 導到月配濾芯或校園店取貨", "讓低價硬體連到持續收益。"),
        ],
    )

    st.divider()
    section_label("Adoption Funnel")
    st.header("從看見臭味問題到回購濾芯")
    funnel_cols = st.columns(5)
    funnel_cols[0].metric("觸及", "校園社群", "短影音/租屋包", border=True)
    funnel_cols[1].metric("理解", "自我檢測", "痛點量化", border=True)
    funnel_cols[2].metric("購買", "NT$150", "低決策成本", border=True)
    funnel_cols[3].metric("持續", "透明收集", "提醒清理", border=True)
    funnel_cols[4].metric("回購", "濾芯", "每月低額", border=True)


def page_team_pitch() -> None:
    render_css()
    section_label("Team")
    st.title("清大計財碩一團隊")

    identity_options = {
        "正式 Pitch": {
            "tagline": "用財務邏輯與學生洞察做硬體產品。",
            "focus": "適合放在比賽現場或對外提案，呈現專業、穩定、可信任的團隊形象。",
            "badges": ["成本模型", "商業簡報", "產品驗證"],
        },
        "校園訪談": {
            "tagline": "從清大周邊租屋現場找痛點。",
            "focus": "強調我們真的理解外宿族日常，能把訪談、使用情境和通路假設連起來。",
            "badges": ["外宿洞察", "使用者訪談", "開學季通路"],
        },
        "產品實驗": {
            "tagline": "把水槽阻塞問題變成可測的產品假設。",
            "focus": "適合說明打樣、適配率、清理手感與油脂攔截量，讓評審看到執行路線。",
            "badges": ["MVP 打樣", "油脂攔截", "90 天試點"],
        },
        "財務分析": {
            "tagline": "用計財背景守住定價、毛利與回購。",
            "focus": "凸顯團隊能把 NT$150 低價硬體做成可持續商業模型，而不是只停在創意。",
            "badges": ["單位經濟", "濾芯回購", "損益平衡"],
        },
    }
    selected_identity = st.segmented_control(
        "切換團隊形象",
        list(identity_options.keys()),
        default="正式 Pitch",
        label_visibility="collapsed",
    )
    identity = identity_options[selected_identity]

    left, right = st.columns([1.05, 1])
    with left:
        st.image(
            TEAM_ILLUSTRATION_IMAGE,
            caption="團隊形象插畫：廖怡絜、曾楷芸、邱芷凡",
            use_container_width=True,
        )
    with right:
        st.markdown(
            f"""
            <div class="card team-identity-card">
                <div class="number">{selected_identity}</div>
                <h3>{identity["tagline"]}</h3>
                <p class="muted">{identity["focus"]}</p>
                <div class="pill-row">
                    {"".join(f'<span class="pill">{badge}</span>' for badge in identity["badges"])}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_motion_visual("team", f"廖怡絜、曾楷芸、邱芷凡：{identity['tagline']}")
    st.markdown(
        """
        我們是清大計財碩一學生：廖怡絜、曾楷芸、邱芷凡。團隊把外宿生活的真實痛點，
        轉成可以被驗證的產品設計、成本模型與校園試點策略。
        """
    )

    st.markdown(
        """
        <div class="quote">
            我們不只是在賣一個水槽塞，我們是在保護學生的居住人權與生活品質。
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    section_label("Speaking Notes")
    st.header("30 秒結尾口說")
    st.markdown(
        """
        大家好，我們是清大計財碩一團隊，成員是廖怡絜、曾楷芸、邱芷凡。
        外宿生活裡，水管阻塞和惡臭不是小事，
        它會直接影響學生的房間、預算與居住尊嚴。
        Smart Grease-Trap Stopper 用一個低成本、零電力、容易清理的水槽塞，
        把昂貴的事後維修變成日常預防。讓我們一起用科技，
        讓外宿生活不再有負擔。
        """
    )

    st.divider()
    section_label("Team Advantage")
    st.header("團隊優勢怎麼講")
    render_deep_table(
        "把背景轉成執行力",
        [
            ("廖怡絜", "成本、損益、定價與 pitch 財務模型", "把 NT$150 的低價產品講成可持續的商業模型。"),
            ("曾楷芸", "校園通路、外宿族訪談與市場切入", "讓產品從清大周邊開始驗證，而不是空泛談大市場。"),
            ("邱芷凡", "使用者情境、產品規格與試點回饋", "把清理手感、密封尺寸、濾芯回購變成可測 KPI。"),
            ("計財背景", "用數據、成本與風險思維管理硬體試點", "避免只停留在創意，能往量產與銷售推進。"),
        ],
    )

    st.subheader("15 秒團隊介紹")
    st.success("我們是清大計財碩一廖怡絜、曾楷芸、邱芷凡。外宿生活讓我們看見水槽阻塞的真實痛點，計財訓練則讓我們能用成本、毛利與試點數據判斷這個產品能不能真的活下來。")


def page_deck() -> None:
    render_css()
    section_label("Reference Deck")
    st.title("競賽規則與原始提案簡報")
    render_motion_visual("deck", "把原始簡報轉成可互動、可展示、可試算的網站版本。")

    left, right = st.columns(2)
    with left:
        st.image(RULES_IMAGE, caption="Startup World Cup Pitch Deck Outline 2025")
        if RULES_PDF.exists():
            st.download_button(
                "下載 SWC 規則 PDF",
                data=RULES_PDF.read_bytes(),
                file_name=RULES_PDF.name,
                mime="application/pdf",
                use_container_width=True,
            )
    with right:
        st.image(PROPOSAL_IMAGE, caption="Smart Grease Trap Revolution")
        if PROPOSAL_PDF.exists():
            st.download_button(
                "下載原始提案 PDF",
                data=PROPOSAL_PDF.read_bytes(),
                file_name=PROPOSAL_PDF.name,
                mime="application/pdf",
                use_container_width=True,
            )

    st.divider()
    section_label("Image Credits")
    st.header("網站使用的網路圖片來源")
    st.markdown(
        """
        - 小套房水槽情境圖：Pexels，Max Vakhtbovycn，Kitchen counter with sink in small apartment
        - 髒碗水槽情境圖：Unsplash，Devon MacKay，A kitchen sink filled with dishes next to a window
        - 排水口近照：Unsplash，Daniel Dan，A close up of a metal sink drain
        """
    )


def sidebar_intro() -> None:
    st.sidebar.markdown("## Smart Grease-Trap Stopper")
    st.sidebar.caption("外宿族的排水守護者")
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        **網站目錄**

        左側可切換各分頁；首頁提供自我檢測，其他頁面對應 SWC pitch deck 的關鍵章節。
        """
    )


sidebar_intro()

pages = {
    "Pitch Website": [
        st.Page(page_home, title="首頁與自我檢測", url_path="", default=True),
        st.Page(page_problem, title="問題", url_path="problem"),
        st.Page(page_solution, title="解決方案", url_path="solution"),
        st.Page(page_product, title="產品與技術", url_path="product"),
        st.Page(page_demo_lab, title="互動實驗室", url_path="demo-lab"),
        st.Page(page_market, title="市場與商業模式", url_path="market"),
        st.Page(page_financials, title="財務試算", url_path="financials"),
        st.Page(page_pilot_strategy, title="試點策略", url_path="pilot"),
        st.Page(page_team_pitch, title="團隊與結語", url_path="team"),
        st.Page(page_judge_room, title="評審問答", url_path="judge-room"),
        st.Page(page_deck, title="原始簡報與規則", url_path="deck"),
        st.Page(page_problem, title="問題", url_path="page_problem", visibility="hidden"),
        st.Page(page_solution, title="解決方案", url_path="page_solution", visibility="hidden"),
        st.Page(page_product, title="產品與技術", url_path="page_product", visibility="hidden"),
        st.Page(page_demo_lab, title="互動實驗室", url_path="page_demo_lab", visibility="hidden"),
        st.Page(page_market, title="市場與商業模式", url_path="page_market", visibility="hidden"),
        st.Page(page_financials, title="財務試算", url_path="page_financials", visibility="hidden"),
        st.Page(page_pilot_strategy, title="試點策略", url_path="page_pilot_strategy", visibility="hidden"),
        st.Page(page_team_pitch, title="團隊與結語", url_path="page_team_pitch", visibility="hidden"),
        st.Page(page_judge_room, title="評審問答", url_path="page_judge_room", visibility="hidden"),
        st.Page(page_deck, title="原始簡報與規則", url_path="page_deck", visibility="hidden"),
    ]
}

current_page = st.navigation(pages, position="sidebar", expanded=True)
current_page.run()
