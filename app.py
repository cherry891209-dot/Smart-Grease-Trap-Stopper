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
PRODUCT_ILLUSTRATION_IMAGE = BASE_DIR / "assets" / "product-illustration.png"
LIAO_IMAGE = BASE_DIR / "assets" / "team-liao.jpg"
TSENG_IMAGE = BASE_DIR / "assets" / "team-tseng.jpg"
CHIOU_IMAGE = BASE_DIR / "assets" / "team-chiou.jpg"
RULES_PDF = BASE_DIR / "612483020334563589_Startup World Cup Pitch Deck Outline_ 2025.pdf"
PROPOSAL_PDF = BASE_DIR / "612513577919578249_Smart_Grease_Trap_Revolution_(4).pdf"


st.set_page_config(
    page_title="Clario Living",
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
        background:
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='360' height='240' viewBox='0 0 360 240'%3E%3Cg fill='none' stroke='%2378a083' stroke-width='2' stroke-linecap='round' opacity='.16'%3E%3Cpath d='M24 38c38-28 86-20 121 4 47 32 83 31 128-5'/%3E%3Cpath d='M42 181c45 20 86 18 124-8 40-27 79-30 124-7'/%3E%3Cpath d='M298 61c20 15 21 42 1 56-17 12-41 3-46-17-6-24 21-49 45-39z'/%3E%3Cpath d='M80 91c11 8 12 23 1 31-10 7-24 2-27-10-3-13 12-27 26-21z'/%3E%3C/g%3E%3Cg fill='%23f0b45c' opacity='.18'%3E%3Ccircle cx='304' cy='181' r='5'/%3E%3Ccircle cx='53' cy='134' r='4'/%3E%3Ccircle cx='215' cy='54' r='3'/%3E%3C/g%3E%3C/svg%3E"),
            var(--paper);
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
        background: #fbfaf5;
        color: var(--ink);
        display: grid;
        grid-template-columns: minmax(0, .9fr) minmax(360px, 1.1fr);
        gap: clamp(24px, 4vw, 56px);
        align-content: center;
        align-items: center;
        box-shadow: 0 26px 80px rgba(23, 33, 29, .18);
    }

    .hero-text {
        max-width: 680px;
    }

    .hero-product {
        width: 100%;
        max-width: 760px;
        justify-self: end;
        border-radius: 8px;
        object-fit: contain;
        filter: drop-shadow(0 26px 38px rgba(23,33,29,.16));
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
        color: var(--muted);
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
        color: var(--clay);
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

    .hero > * {
        position: relative;
        z-index: 2;
    }

    .hero::before {
        content: "";
        position: absolute;
        right: 4%;
        top: 10%;
        width: 44%;
        height: 72%;
        z-index: 1;
        border: 2px dashed rgba(120,160,131,.42);
        border-radius: 52% 48% 58% 42% / 48% 56% 44% 52%;
        transform: rotate(-4deg);
        animation: ambientDrift 9s ease-in-out infinite alternate;
        pointer-events: none;
    }

    .hero::after {
        content: "";
        position: absolute;
        right: 2%;
        bottom: 8%;
        width: 30%;
        height: 32%;
        z-index: 1;
        background:
            radial-gradient(circle at 16% 32%, rgba(240,180,92,.46) 0 6px, transparent 7px),
            radial-gradient(circle at 52% 58%, rgba(120,160,131,.36) 0 5px, transparent 6px),
            radial-gradient(circle at 82% 28%, rgba(199,101,63,.22) 0 4px, transparent 5px);
        border-bottom: 3px solid rgba(120,160,131,.28);
        border-radius: 50%;
        transform: rotate(-8deg);
        pointer-events: none;
    }

    .hero h1 { animation: slideUp 760ms 120ms ease-out both; }
    .hero .subtitle { animation: slideUp 760ms 220ms ease-out both; }
    .hero p { animation: slideUp 760ms 320ms ease-out both; }
    .hero-product { animation: cardRise 760ms 260ms ease-out both; }

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
        color: var(--muted);
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

    div[data-testid="stSegmentedControl"] button {
        min-height: 52px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0 18px;
    }

    div[data-testid="stSegmentedControl"] button > div,
    div[data-testid="stSegmentedControl"] button [data-testid="stMarkdownContainer"] {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
        width: 100%;
    }

    div[data-testid="stSegmentedControl"] button p {
        margin: 0;
        line-height: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100%;
        transform: none;
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
            min-height: 620px;
            padding: 32px 28px 280px;
            grid-template-columns: 1fr;
            gap: 22px;
            align-content: start;
        }

        .hero-product {
            max-width: 100%;
            justify-self: center;
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


def image_data_uri(path: Path) -> str:
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{image_to_base64(path)}"


def render_css() -> None:
    hero_image = PRODUCT_ILLUSTRATION_IMAGE if PRODUCT_ILLUSTRATION_IMAGE.exists() else APARTMENT_SINK_IMAGE
    hero_mime = "png" if hero_image.suffix.lower() == ".png" else "jpeg"
    hero_b64 = image_to_base64(hero_image if hero_image.exists() else PROPOSAL_IMAGE)
    st.markdown(
        CUSTOM_CSS.replace("__HERO_PLACEHOLDER__", hero_b64).replace("__HERO_MIME__", hero_mime),
        unsafe_allow_html=True,
    )


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
    render_anim_component("solution", "Swap in the stopper in 30 seconds: oil stays in the clear chamber while water keeps draining.")


def render_motion_visual(kind: str, label: str) -> None:
    render_anim_component(kind, label)


def render_team_photo_grid() -> None:
    members = [
        ("Yi-Chieh Liao", "CEO", "Company strategy and product vision", LIAO_IMAGE),
        ("Kai-Yun Tseng", "CFO", "Financial planning and capital allocation", TSENG_IMAGE),
        ("Chih-Fan Chiou", "CMO", "Market positioning and brand growth", CHIOU_IMAGE),
    ]
    cards = "".join(
        f"""
        <article class="team-photo-card">
            <img src="{image_data_uri(path)}" alt="{name} team photo">
            <div>
                <span>{role}</span>
                <strong>{name}</strong>
                <p>{focus}</p>
            </div>
        </article>
        """
        for name, role, focus, path in members
    )
    st.markdown(
        f"""
        <style>
          .team-photo-grid {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 14px;
            margin: 0 0 18px;
          }}
          .team-photo-card {{
            background: white;
            border: 1px solid #d9dfd6;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 14px 38px rgba(23, 33, 29, .08);
          }}
          .team-photo-card img {{
            width: 100%;
            aspect-ratio: 1 / 1;
            object-fit: cover;
            display: block;
            background: #f8f5ee;
          }}
          .team-photo-card div {{
            padding: 15px 16px 17px;
          }}
          .team-photo-card span {{
            color: #c7653f;
            font-size: 13px;
            font-weight: 900;
          }}
          .team-photo-card strong {{
            display: block;
            margin-top: 4px;
            font-size: 22px;
            line-height: 1.15;
          }}
          .team-photo-card p {{
            margin: 7px 0 0;
            color: #59645f;
            font-weight: 750;
            line-height: 1.45;
          }}
          @media (max-width: 760px) {{
            .team-photo-grid {{ grid-template-columns: 1fr; }}
          }}
        </style>
        <div class="team-photo-grid">{cards}</div>
        """,
        unsafe_allow_html=True,
    )


def render_anim_component(kind: str, label: str) -> None:
    team_b64 = image_to_base64(TEAM_MEMBERS_REDRAWN_IMAGE)
    liao_b64 = image_to_base64(LIAO_IMAGE)
    tseng_b64 = image_to_base64(TSENG_IMAGE)
    chiou_b64 = image_to_base64(CHIOU_IMAGE)
    titles = {
        "problem": "How Grease Clogs Form",
        "solution": "Oil-Water Separation After Installation",
        "product": "Product Component View",
        "market": "Campus Launch Network",
        "finance": "Hardware Sales + Filter Refills",
        "pilot": "90-Day Campus Pilot",
        "radar": "Investor Q&A Defense Board",
        "team": "Clario Living Team Roles",
        "deck": "Deck to Interactive Website",
    }
    scenes = {
        "problem": """
          <div class="sink-cabinet"><div class="tiny-sink"></div><div class="dirty-pan"></div></div>
          <div class="pipe-main"></div><div class="pipe-turn"></div><div class="pipe-shadow"></div>
          <div class="grease-dot g1"></div><div class="grease-dot g2"></div><div class="grease-dot g3"></div><div class="grease-dot g4"></div>
          <div class="sticky-layer l1"></div><div class="sticky-layer l2"></div><div class="sticky-layer l3"></div>
          <div class="bug-risk">Odor Rising</div><div class="steam-wave w1"></div><div class="steam-wave w2"></div>
          <div class="scene-note n-left">Greasy Soup Poured In</div><div class="scene-note n-mid">Grease Cools and Sticks</div><div class="scene-note n-right">Slow Drainage</div>
        """,
        "solution": """
          <div class="install-rail"></div>
          <div class="old-stopper">Old Stopper</div><div class="swap-arrow"></div><div class="new-stopper">Smart<br>Stopper</div>
          <div class="sink-bowl"></div><div class="cutaway-pipe"></div><div class="flow-vortex"></div>
          <div class="collector-tank"><div class="tank-oil"></div><div class="tank-water"></div><span>Clear Collection Chamber</span></div>
          <div class="water-exit"></div><div class="drop dx1"></div><div class="drop dx2"></div><div class="drop dx3"></div>
          <div class="step-chip c1">1 Remove Old Stopper</div><div class="step-chip c2">2 Press In New Stopper</div><div class="step-chip c3">3 Separate Oil and Water</div><div class="step-chip c4">4 Empty Chamber</div>
        """,
        "product": """
          <div class="exploded-axis"></div>
          <div class="product-shell"></div><div class="product-lip"></div><div class="product-core"></div>
          <div class="gasket-ring"></div><div class="vane-wheel"><i></i><b></b><em></em></div>
          <div class="clear-chamber"><div class="chamber-oil"></div><div class="chamber-water"></div></div>
          <div class="filter-pack"><span></span></div>
          <div class="callout co1">A Seal Ring: Fits the Drain</div><div class="callout co2">B Flow Guide: Extends Dwell Time</div><div class="callout co3">C Chamber: Visible Grease Capture</div><div class="callout co4">D Filter: Low-Cost Refills</div>
        """,
        "market": """
          <div class="campus-map"></div><div class="campus-hub">NTHU</div>
          <div class="market-path p-a"></div><div class="market-path p-b"></div><div class="market-path p-c"></div><div class="market-path p-d"></div>
          <div class="market-node dorm">First Users<br>Renters</div><div class="market-node shop">Retail<br>Hardware Stores</div><div class="market-node pack">Move-In<br>Starter Kits</div><div class="market-node sub">Monthly<br>Refills</div>
          <div class="packet pk1"></div><div class="packet pk2"></div><div class="packet pk3"></div>
        """,
        "finance": """
          <div class="money-flow">
            <div class="money-box box-price"><strong>Hardware Price</strong><span>NT$150</span></div>
            <div class="flow-arrow a1"></div>
            <div class="money-box box-cost"><strong>Cost Base</strong><span>Manufacturing + Packaging + Retail</span></div>
            <div class="flow-arrow a2"></div>
            <div class="money-box box-profit"><strong>Hardware Margin</strong><span>Funds Campus Pilots</span></div>
          </div>
          <div class="sub-flow">
            <div class="sub-card"><strong>Monthly Filter</strong><span>Low-Cost Refills</span></div>
            <div class="sub-arrow"></div>
            <div class="sub-card"><strong>Higher LTV</strong><span>More Than One Sale</span></div>
          </div>
          <div class="finance-bars"><div></div><div></div><div></div><div></div></div>
        """,
        "pilot": """
          <div class="calendar-grid"></div><div class="pilot-road"></div><div class="pilot-runner"></div>
          <div class="milestone m1"><strong>D1-15</strong><span>Interviews</span></div>
          <div class="milestone m2"><strong>D16-35</strong><span>Prototype</span></div>
          <div class="milestone m3"><strong>D36-65</strong><span>Trial</span></div>
          <div class="milestone m4"><strong>D66-90</strong><span>Launch</span></div>
          <div class="kpi k1">Fit Rate</div><div class="kpi k2">Capture Volume</div><div class="kpi k3">Refill Rate</div>
        """,
        "radar": """
          <div class="judge-table">
            <div class="judge-row"><strong>1 Problem</strong><span>Landlord Pressure / Plumbing Cost / Odor</span></div>
            <div class="judge-row"><strong>2 Solution</strong><span>No Pipe Work, Just Swap the Stopper</span></div>
            <div class="judge-row"><strong>3 Business</strong><span>NT$150 Entry + Filter Refills</span></div>
            <div class="judge-row"><strong>4 Execution</strong><span>90-Day NTHU Area Pilot</span></div>
          </div>
          <div class="judge-score">
            <div class="score-axis x"></div><div class="score-axis y"></div>
            <div class="score-card p">Problem</div><div class="score-card s">Solution</div><div class="score-card b">Business</div><div class="score-card e">Execution</div>
            <div class="score-core">Defend<br>Four Themes</div>
          </div>
        """,
        "team": """
          <div class="team-board">
            <div class="member-card liao">
              <div class="portrait liao-photo"></div>
              <strong>Yi-Chieh Liao</strong><span>CEO<br>Company strategy and product vision</span>
            </div>
            <div class="member-card tseng">
              <div class="portrait tseng-photo"></div>
              <strong>Kai-Yun Tseng</strong><span>CFO<br>Financial planning and capital allocation</span>
            </div>
            <div class="member-card chiou">
              <div class="portrait chiou-photo"></div>
              <strong>Chih-Fan Chiou</strong><span>CMO<br>Market positioning and brand growth</span>
            </div>
          </div>
          <div class="team-output">Shared output: product vision + financial planning + market growth strategy</div>
          <div class="team-line l1"></div><div class="team-line l2"></div><div class="team-line l3"></div>
        """,
        "deck": """
          <div class="deck-stack">
            <div class="slide-card s1">Problem</div><div class="slide-card s2">Solution</div>
            <div class="slide-card s3">Market</div><div class="slide-card s4">Finance</div>
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
      .team-board{position:absolute;left:5%;right:5%;top:72px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;z-index:4}.member-card{height:342px;border-radius:8px;background:white;border:1px solid #d9dfd6;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center;gap:7px;padding:16px 14px 18px;box-shadow:0 16px 34px rgba(23,33,29,.12);animation:float 3.4s infinite}.member-card strong{font-size:24px;line-height:1.15;margin-top:6px}.member-card span{color:#c7653f;font-weight:900;font-size:15px;line-height:1.3;min-height:42px;display:flex;align-items:center;justify-content:center}.tseng{animation-delay:.35s}.chiou{animation-delay:.7s}.portrait{width:100%;max-width:220px;height:222px;border-radius:8px;background-size:cover;background-position:center;background-repeat:no-repeat;background-color:#f7f4ec;border:1px solid #d9dfd6;box-shadow:0 12px 24px rgba(23,33,29,.12);animation:portraitFloat 3.6s ease-in-out infinite}.liao-photo{background-image:url("data:image/jpeg;base64,__LIAO_IMAGE__")}.tseng-photo{background-image:url("data:image/jpeg;base64,__TSENG_IMAGE__");animation-delay:.3s}.chiou-photo{background-image:url("data:image/jpeg;base64,__CHIOU_IMAGE__");animation-delay:.6s}.team-output{position:absolute;left:18%;right:18%;bottom:32px;height:58px;border-radius:8px;background:#17211d;color:white;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:900;font-size:18px;line-height:1.35;padding:0 18px;box-shadow:0 18px 38px rgba(23,33,29,.18);z-index:5}.team-line{position:absolute;height:4px;border-radius:999px;background:#f0b45c;transform-origin:center;z-index:2;opacity:.75}.team-line.l1{left:25%;top:428px;width:145px;transform:rotate(12deg)}.team-line.l2{left:45%;top:426px;width:140px}.team-line.l3{right:25%;top:428px;width:145px;transform:rotate(-12deg)}
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
        .replace("__LIAO_IMAGE__", liao_b64)
        .replace("__TSENG_IMAGE__", tseng_b64)
        .replace("__CHIOU_IMAGE__", chiou_b64)
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
      <div class="title">Interactive Lab: Real-Time Grease Capture Simulation</div>
      <div class="badge b1">Weekly grease {weekly_oil:.0f} ml</div>
      <div class="badge b2">Capture rate {capture_rate}%</div>
      <div class="badge b3">{clean_days} days per cleaning</div>
      <div class="reservoir"><div class="oil"></div><div class="water"></div></div>
      <div class="tube"></div><div class="filter-unit"></div>
      <div class="collector"><div class="captured"></div></div><div class="clean-water"></div><div class="bench"></div>
      <div class="stage-label sl1">Pour Oil + Water</div><div class="stage-label sl2">Vortex Separation</div><div class="stage-label sl3">Grease Capture</div>
      <div class="readout">Estimated monthly capture {captured * 4:.0f} ml grease<small>Left: pour oil-water | Center: separate | Right: chamber fill level</small></div>
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
                <div class="photo-caption">Real-life context: greasy dishes and a cramped sink after dinner</div>
            </div>
            <div class="photo-stack">
                <div class="photo-tile small">
                    <img src="data:image/jpeg;base64,{drain}" alt="kitchen sink drain close up">
                    <div class="photo-caption">Risk entry point: grease eventually reaches the drain</div>
                </div>
                <div class="photo-tile small">
                    <img src="data:image/jpeg;base64,{apartment}" alt="small apartment kitchen sink">
                    <div class="photo-caption">Rental context: small studios, low budgets, no renovation</div>
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
            <div class="signal"><strong>Oil</strong><span>Residual oil is guided before it enters the drain</span></div>
            <div class="signal"><strong>Trap</strong><span>Grease floats and stays in the clear collection chamber</span></div>
            <div class="signal"><strong>Clean</strong><span>Water keeps draining, reducing buildup on pipe walls</span></div>
            <div class="signal"><strong>Repeat</strong><span>Compostable filters drive low-cost refills</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_image_marquee() -> None:
    items = [
        (BASE_DIR / "assets" / "marquee-01-apartment-sink.jpg", "Small rental sink: tight space, hard to renovate"),
        (BASE_DIR / "assets" / "marquee-02-messy-window-sink.jpg", "After-dinner sink: dirty dishes and leftover soup"),
        (BASE_DIR / "assets" / "marquee-03-drain-closeup.jpg", "Drain close-up: where grease buildup starts"),
        (BASE_DIR / "assets" / "marquee-04-dark-dirty-sink.jpg", "Dim kitchen: real-life cleaning procrastination"),
        (BASE_DIR / "assets" / "marquee-05-stainless-drain.jpg", "Metal drain: common rental sink hardware"),
        (BASE_DIR / "assets" / "marquee-06-water-drain.jpg", "Water entering drain: grease travels with it"),
        (BASE_DIR / "assets" / "marquee-07-running-faucet.jpg", "Running faucet: everyday dishwashing moment"),
        (BASE_DIR / "assets" / "marquee-08-greasy-dishes.jpg", "Greasy cookware: the residue most likely to clog pipes"),
        (BASE_DIR / "assets" / "marquee-09-person-cleaning.jpg", "Dishwashing: users do not want to touch grease"),
        (BASE_DIR / "assets" / "marquee-10-soapy-sink.jpg", "Soapy sink: residue risk remains after cleaning"),
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
                        <th>Item</th>
                        <th>Content</th>
                        <th>Why It Matters</th>
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
        ("Late-Night Eater", "Eats out four times a week and often dumps noodle or hot-pot soup. Needs prevention without behavior change."),
        ("Old-Studio Renter", "Lives in a 20+ year-old unit with a small slow sink and deposit anxiety. Will buy low-cost insurance."),
        ("Shared-Kitchen Dorm", "Many users, unclear responsibility, and a strong need for visible reminders to clean."),
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
                <h3>Campus Interviews</h3>
                <p class="muted">Interview 30 student renters to validate oil disposal frequency, odor, and plumbing-cost pain points.</p>
            </div>
            <div class="step">
                <div class="number">Week 3-5</div>
                <h3>3D Prototype</h3>
                <p class="muted">Test seal size, chamber capacity, and cleaning feel to define a manufacturable structure.</p>
            </div>
            <div class="step">
                <div class="number">Week 6-8</div>
                <h3>Dorm Pilot</h3>
                <p class="muted">Pilot in 20 sinks near NTHU and track drainage speed, odor, and cleaning frequency.</p>
            </div>
            <div class="step">
                <div class="number">Month 3</div>
                <h3>Move-In Season Launch</h3>
                <p class="muted">Partner with lifestyle retailers and renter starter kits to sell a stopper-plus-filter pack.</p>
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
                    <th>Alternative</th>
                    <th>Student Acceptance</th>
                    <th>Limitations</th>
                    <th>Our Opening</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Traditional Sink Strainer</td>
                    <td>High: cheap and familiar</td>
                    <td>Catches solids but not grease or odor</td>
                    <td>Add grease capture and visible collection</td>
                </tr>
                <tr>
                    <td>Chemical Drain Cleaner</td>
                    <td>Medium: bought after clogging</td>
                    <td>Harsh and risky for old pipes</td>
                    <td>Shift from reaction to daily prevention</td>
                </tr>
                <tr>
                    <td>Commercial Grease Trap</td>
                    <td>Low: unsuitable for studios</td>
                    <td>Expensive installation and space-consuming</td>
                    <td>Shrink the idea into a no-install stopper</td>
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
        return "High Risk", "Your sink routine is a strong fit for preventive grease capture, especially with old studios, small sinks, or frequent soup disposal."
    if score >= 8:
        return "Medium Risk", "You already show early signs of clogging and odor. Start with a stopper, strainer, and weekly cleaning to reduce pipe buildup."
    return "Low Risk", "Your habits are relatively safe, but old buildings or shared kitchens still justify a low-cost preventive tool."


def render_checkup_form() -> None:
    st.subheader("Rental Sink Risk Check")
    st.caption("Six quick questions to see whether your sink is trending toward clogs, odor, or pest risk.")

    questions = [
        (
            "How often do you pour hot-pot soup, noodle sauce, or oily food residue into the sink each week?",
            {"0 times": 0, "1-2 times": 1, "3-5 times": 3, "Almost daily": 4},
        ),
        (
            "Has your sink drainage slowed recently?",
            {"No": 0, "Sometimes": 1, "Clearly slower": 3, "Often standing water": 4},
        ),
        (
            "Does your kitchen or bathroom drain smell?",
            {"No": 0, "Sometimes": 1, "Every day": 3, "Odor spreads into the room": 4},
        ),
        (
            "Building age or pipe condition?",
            {"New unit or recently replaced pipes": 0, "Not sure": 1, "20+ years old": 3, "Has clogged or leaked before": 4},
        ),
        (
            "Would you clean the strainer or trap every week?",
            {"Yes, and I do it": 0, "Sometimes": 1, "Rarely": 3, "Absolutely not": 4},
        ),
        (
            "Can you accept a plumbing repair costing about NT$1,500?",
            {"Acceptable": 0, "Painful but possible": 1, "I would rather avoid it": 3, "Not acceptable": 4},
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

        submitted = st.form_submit_button("See Results", use_container_width=True)

    if submitted:
        st.session_state.checkup_done = True
        st.session_state.checkup_score = total

    if st.session_state.checkup_done:
        score = st.session_state.checkup_score
        level, advice = score_level(score)
        st.progress(score / 24)
        left, right = st.columns([1, 2])
        left.metric("Risk Score", f"{score}/24", level, border=True)
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
    st.title("Interactive Grease Capture Lab")
    st.markdown(
        """
        Investors will ask how this actually works. This page turns the mechanism into a usable demo.
        Adjust greasy-meal frequency, water volume, and cleaning cadence to see estimated capture and maintenance reminders.
        """
    )
    render_signal_strip()

    left, right = st.columns([1.05, 1])
    with right:
        meals = st.slider("Greasy meals per week", 0, 14, 6)
        oil_per_meal = st.slider("Average oil residue per meal (ml)", 2, 40, 14)
        capture_rate = st.slider("Target capture rate", 40, 90, 72, format="%d%%")
        clean_days = st.slider("Days between chamber cleanings", 1, 14, 7)

        weekly_oil = meals * oil_per_meal
        captured = weekly_oil * capture_rate / 100
        monthly_captured = captured * 4
        collector_capacity = 120
        fill_ratio = min(1.0, (captured / 7 * clean_days) / collector_capacity)

        st.metric("Weekly grease entering sink", f"{weekly_oil:.0f} ml", border=True)
        st.metric("Estimated monthly capture", f"{monthly_captured:.0f} ml", f"{capture_rate}% efficiency", border=True)
        st.progress(fill_ratio)
        if fill_ratio >= 0.85:
            st.warning("The chamber is close to full. Shorten the cleaning cycle.")
        elif fill_ratio >= 0.5:
            st.info("This cleaning cycle works, but move-in season or shared kitchens need more frequent cleaning.")
        else:
            st.success("This cadence is comfortable and fits low-effort use cases.")
    with left:
        render_lab_visual(weekly_oil, captured, fill_ratio, capture_rate, clean_days)

    st.divider()
    section_label("User Personas")
    st.header("Three Highest-Intent Users")
    render_personas()

    st.divider()
    section_label("Scenario Presets")
    st.header("Recommended Settings for Common Rental Scenarios")
    cols = st.columns(3)
    with cols[0]:
        card("Light", "Occasional Cooking", "One to two greasy meals per week; clean every 10-14 days. Best for low-risk users.")
    with cols[1]:
        card("Student", "Frequent Takeout", "Five to eight greasy meals per week; clean weekly and replace the filter monthly.")
    with cols[2]:
        card("Shared", "Shared Kitchen", "Many people dump soup and responsibility is diffuse; clean every 3-5 days with visible reminders.")

    render_deep_table(
        "How to Read the Demo Numbers",
        [
            ("Weekly grease ml", "Greasy meals multiplied by oil residue per meal", "Shows users how quickly daily residue accumulates."),
            ("Capture rate", "Uses 40%-90% as an adjustable assumption", "Can be updated with pilot data before competition."),
            ("Chamber fill level", "Calculated from cleaning cadence and chamber capacity", "Directly answers whether it will overflow."),
            ("Monthly capture", "Turns small droplets into monthly impact", "Makes product value visible."),
        ],
    )


def page_financials() -> None:
    render_css()
    section_label("Financial Model")
    st.title("Pricing, Margin, and Campus Pilot Calculator")
    render_motion_visual("finance", "A low-cost device opens the door; filter refills increase lifetime value.")
    st.markdown(
        "This page turns the product concept into a business model. The numbers are adjustable so the team can practice cost and margin questions."
    )

    st.subheader("Unit Economics Model")
    col1, col2, col3, col4 = st.columns(4)
    price = col1.number_input("Unit price NT$", min_value=80, max_value=400, value=150, step=10)
    unit_cost = col2.number_input("Unit manufacturing cost NT$", min_value=20, max_value=220, value=58, step=5)
    channel_fee = col3.number_input("Channel / packaging cost NT$", min_value=0, max_value=120, value=28, step=5)
    filter_margin = col4.number_input("Monthly filter margin NT$", min_value=0, max_value=80, value=12, step=2)

    gross_profit = price - unit_cost - channel_fee
    gross_margin = gross_profit / price if price else 0
    payback_months = price / max(filter_margin, 1)

    metrics = st.columns(4)
    metrics[0].metric("Unit gross profit", f"NT${gross_profit:.0f}", border=True)
    metrics[1].metric("Hardware margin", f"{gross_margin:.0%}", border=True)
    metrics[2].metric("Annual filter gross profit", f"NT${filter_margin * 12:.0f}", border=True)
    metrics[3].metric("Plumbing cost equals", f"{1500 // max(price, 1):.0f} units", "based on NT$1,500", border=True)

    st.divider()
    st.subheader("Campus Market Penetration Calculator")
    left, right = st.columns([1, 1])
    with left:
        target_students = st.slider("Reachable student renters in first wave", 500, 30000, 6000, step=500)
        adoption = st.slider("First-year purchase rate", 1, 35, 8, format="%d%%")
        subscription = st.slider("Filter subscription conversion", 0, 80, 30, format="%d%%")
    with right:
        units = target_students * adoption / 100
        hardware_revenue = units * price
        hardware_profit = units * gross_profit
        annual_filter_profit = units * subscription / 100 * filter_margin * 12
        total_profit = hardware_profit + annual_filter_profit

        st.metric("First-year units", f"{units:,.0f} units", border=True)
        st.metric("Hardware revenue", f"NT${hardware_revenue:,.0f}", border=True)
        st.metric("First-year gross profit", f"NT${total_profit:,.0f}", "including filters", border=True)

    st.caption("Note: this is a pitch model that shows business logic. Actual numbers should be updated with prototype quotes and channel terms.")

    st.divider()
    section_label("Sensitivity")
    st.header("Financial Sensitivity Investors May Ask About")
    render_deep_table(
        "Key Levers That Affect Margin",
        [
            ("Manufacturing Cost", "If cost rises from NT$58 to NT$80, hardware margin compresses quickly", "Design simplification and mold amortization are needed to control cost."),
            ("Channel Take Rate", "Campus shops and lifestyle retailers have different terms", "Early direct sales and starter-kit partnerships can preserve margin."),
            ("Filter Conversion", "A 15% to 40% subscription rate changes LTV", "The clear chamber and odor improvement drive repeat purchases."),
            ("Price Band", "NT$129-199 is a student-friendly range", "It feels like buying insurance because it is far cheaper than one plumbing repair."),
        ],
    )

    st.subheader("One Financial Line for the Stage")
    st.info("We are not chasing premium hardware pricing; we use an NT$150 entry point to enter student rentals, then increase lifetime value through filters and move-in bundles.")


def page_pilot_strategy() -> None:
    render_css()
    section_label("Pilot Strategy")
    st.title("Pilot Plan Starting Around NTHU")
    render_motion_visual("pilot", "Interviews, prototypes, pilot trials, and move-in launch create a testable 90-day rhythm.")
    st.markdown(
        """
        A company site should make investors believe the team knows what happens next. This section turns product validation, campus channels, and move-in season into a 90-day action plan.
        """
    )

    render_roadmap()

    st.divider()
    section_label("Channel Playbook")
    st.header("Channel Playbook")
    cols = st.columns(3)
    with cols[0]:
        card("01", "Hardware and Lifestyle Retail", "Place the product where students already buy drain supplies, hangers, and extension cords.")
    with cols[1]:
        card("02", "Rental Starter Kits", "Bundle it with mattresses, trash bins, and drying racks during move-in shopping.")
    with cols[2]:
        card("03", "Dorm Shared Kitchens", "Use multi-user kitchens to generate grease-capture cases and social proof.")

    st.divider()
    section_label("Competitor Matrix")
    st.header("Competitors and Alternatives")
    render_competitor_matrix()

    st.divider()
    section_label("Pilot KPI")
    st.header("Eight Pilot Metrics to Collect")
    render_deep_table(
        "From Trial Feedback to Production Decisions",
        [
            ("Fit Rate", "Whether it fits different rental sinks", "Below 80% means the seal needs redesign."),
            ("Leak Rate", "Whether water bypasses the product edge", "Directly affects user trust."),
            ("Weekly capture volume", "Actual grease accumulated in the clear chamber (ml)", "Proves the product is not just psychological comfort."),
            ("Cleaning Completion Rate", "Whether users will empty the chamber regularly", "Determines long-term retention."),
            ("Odor Improvement", "Before-and-after user rating", "The value students feel fastest."),
            ("Drainage Speed", "Whether normal drainage is affected after installation", "Grease capture cannot create a new hassle."),
            ("Purchase Intent", "Willingness to pay after trial", "Validates the NT$150 price point."),
            ("Referral Intent", "Whether users would recommend it to roommates or classmates", "Determines whether campus word-of-mouth can spread."),
        ],
    )


def page_judge_room() -> None:
    render_css()
    section_label("Judge Room")
    st.title("Investor Q&A Room")
    render_motion_visual("radar", "Defend the four scoring themes: problem, solution, business, and execution.")
    st.markdown("Putting likely questions on the site makes the company story feel more mature.")

    faqs = [
        (
            "Why would students buy it?",
            "Because it turns a roughly NT$1,500 plumbing anxiety into a NT$150 preventive insurance product. Students may not love cleaning, but they do fear landlords, deposits, and odor.",
        ),
        (
            "How is it different from a normal strainer?",
            "A normal strainer catches solids, while grease still flows into the pipe. This product guides grease into a clear chamber so it can be seen and removed.",
        ),
        (
            "Is it hard to clean?",
            "The design centers on a removable chamber that cleans like emptying trash. If cleaning feels hard, students will not keep using it.",
        ),
        (
            "What is the technical barrier?",
            "The core is not electronics; it is oil-water separation, seal fit, capacity, and cleaning feel in a small form factor. Those details decide whether it fits rental life.",
        ),
        (
            "What do you validate next?",
            "Validate three things first: drain fit rate, actual grease capture volume, and student willingness to clean. These data points define the production version.",
        ),
    ]

    for question, answer in faqs:
        with st.expander(question):
            st.write(answer)

    st.divider()
    section_label("Pitch Timer")
    st.header("60-Second Elevator Pitch")
    script = """
    Student renters are not afraid of chores as much as they are afraid of clogged pipes, landlord pressure, repair costs, and room-wide odor.
    Clario Living's Smart Grease-Trap Stopper is a sink stopper designed for rental kitchens.
    It requires no electricity, no pipe renovation, and no diet change: users simply swap the stopper.
    Grease stays in the clear chamber while clean water drains away.
    At an NT$150 entry price, we replace a painful NT$1,500 repair event with daily prevention.
    Campus retail, move-in bundles, and filter refills turn a simple device into a repeatable living-care business.
    """
    st.text_area("Practice Script", script.strip(), height=190)

    st.divider()
    section_label("Scoring Rubric")
    st.header("Four Themes to Defend")
    cols = st.columns(4)
    with cols[0]:
        card("P", "Clear Problem", "Do not just say clogging; talk about landlord pressure, plumbing cost, odor, and pests.")
    with cols[1]:
        card("S", "Simple Solution", "No behavior change, no pipe work, no electricity: just swap the stopper.")
    with cols[2]:
        card("B", "Low-Friction Business", "NT$150 buys drainage insurance; filters create repeat purchases.")
    with cols[3]:
        card("E", "Verifiable Execution", "Use a 90-day pilot to measure fit rate, capture volume, and purchase intent.")

    render_deep_table(
        "Hard Investor Questions and Defense Angles",
        [
            ("How much grease can it really capture?", "Acknowledge that pilot data is needed and use the demo model to show assumptions", "Honesty plus a test plan is more credible than overclaiming."),
            ("Will students clean it?", "Use a clear chamber, low-touch removal, and measure cleaning completion rate", "Turn a behavior problem into a product design problem."),
            ("Is the market too niche?", "Start with NTHU renters, then expand to young renters, studios, and shared kitchens", "A narrow use case can be the wedge into a larger market."),
            ("Could competitors copy this easily?", "The edge is universal fit, cleaning experience, channel bundling, and filter refills", "It is not just a plastic part; it is a full use case."),
        ],
    )


def page_home() -> None:
    render_css()
    init_state()

    render_image_marquee()

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-text">
                <div class="eyebrow">Startup World Cup Pitch</div>
                <h1>Clario Living</h1>
                <div class="subtitle">Drain Protection for Rental Living</div>
                <p>
                    A replaceable sink stopper that captures grease during everyday rental-life moments, reducing odor and protecting old pipes from breakdowns.
                </p>
            </div>
            <img class="hero-product" src="{image_data_uri(PRODUCT_ILLUSTRATION_IMAGE)}" alt="Clario Living hand-drawn product illustration">
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    metric_cols = st.columns(3)
    metric_cols[0].metric("Target Entry Price", "NT$150", "Far below one plumbing repair", border=True)
    metric_cols[1].metric("Power and Batteries", "0", "Pure physical separation", border=True)
    metric_cols[2].metric("Cleaning Time", "3 min", "As easy as emptying trash", border=True)
    render_signal_strip()

    st.markdown(
        """
        <div class="pill-row">
            <span class="pill">Rental Sinks</span>
            <span class="pill">Move-In Essential</span>
            <span class="pill">Low-Cost Hardware</span>
            <span class="pill">Refillable Filters</span>
            <span class="pill">No Installation</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    section_label("Self Check")
    left, right = st.columns([1.1, 1])
    with left:
        st.header("Check Whether Your Sink Is High Risk")
        st.markdown(
            """
            This site does more than show the product. The self-check turns greasy takeout, old pipes, odor, and repair cost into a visible risk score.
            """
        )
        st.markdown(
            """
            - Six quick questions to see whether your sink is already collecting grease
            - Covers soup disposal, cleaning habits, and repair-cost tolerance
            - Get low / medium / high risk feedback with practical next steps
            """
        )
        st.button(
            "Start Self-Check",
            type="primary",
            on_click=start_checkup,
            use_container_width=True,
            key="start_checkup_button",
        )
        st.info("Click to open the form and get an instant risk score with recommendations.", icon="⚡")

    with right:
        st.markdown(
            """
            <div class="card">
                <h3>Check Design</h3>
                <p class="muted">
                    Questions focus on oil disposal frequency, drainage speed, odor, building age, cleaning willingness, and repair-cost tolerance. Results map to low, medium, or high risk and connect back to product value.
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
    st.header("What Visitors See in the First 90 Seconds")
    cols = st.columns(4)
    with cols[0]:
        card("1", "Immediate Problem Resonance", "Use the self-check to bring visitors into the rental-sink context.")
    with cols[1]:
        card("2", "Visible Product Logic", "Use an interactive demo to show how grease is captured.")
    with cols[2]:
        card("3", "Editable Business Model", "Price, cost, and penetration rate are adjustable to answer margin questions.")
    with cols[3]:
        card("4", "Clear Execution Path", "Pilot plan, channel playbook, and FAQ are built into the site.")

    st.divider()
    section_label("Why Now")
    st.header("Why Now")
    cols = st.columns(3)
    with cols[0]:
        card("A", "Takeout Is Daily Life", "Student life relies heavily on takeout and delivery, making greasy soup and sauces a daily sink burden.")
    with cols[1]:
        card("B", "Rental Cost Pressure", "Rent, deposits, and repair fees make students more open to low-cost prevention than after-the-fact fixes.")
    with cols[2]:
        card("C", "Move-In Purchase Window", "When students move in, they buy household items together. That is the best time for a stopper to enter starter kits.")

    render_deep_table(
        "How the Site Maps to Pitch Scoring",
        [
            ("Problem", "self-check, context visuals, problem cards", "Make visitors feel this is a real daily problem, not a forced topic."),
            ("Solution", "product demo, grease flow, before-and-after comparison", "Turn invisible grease capture into an understandable interactive experience."),
            ("Business", "financial calculator, channel playbook, filter subscriptions", "Turn a small object into a scalable business model."),
            ("Execution", "90-day pilot, KPIs, FAQ", "Pre-answer the execution and risk questions visitors care about most."),
        ],
    )


def page_problem() -> None:
    render_css()
    section_label("Problem")
    st.title("The Rental Maintenance Problem Students Dread")
    st.markdown(
        "Student renters know grease can clog pipes; rental life is just small, rushed, and too unpleasant for greasy cleanup."
    )
    render_motion_visual("problem", "Grease enters the pipe, cools, sticks, and eventually becomes clogging and odor.")

    cols = st.columns(3)
    with cols[0]:
        card("01", "Greasy Takeout", "Hot-pot soup, noodle sauce, and fried-food residue go straight into the sink; once cooled, grease sticks to pipe walls.")
    with cols[1]:
        card("02", "Hard Repairs", "Old studio pipes are narrow and full of bends. Once clogged, students face landlords, roommates, and repair fees.")
    with cols[2]:
        card("03", "Hygiene Spillover", "In a small room, drain odor spreads quickly and increases pest risk.")

    st.write("")
    st.markdown(
        """
        <div class="quote">
            The real problem is not just a clogged sink; it is the lack of an affordable, intuitive prevention tool students will actually use every day.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    section_label("Oil Journey")
    st.header("What Happens After Hot-Pot Soup Enters the Sink")
    cols = st.columns(4)
    with cols[0]:
        card("1", "Hot Soup Poured In", "Grease flows with water while hot, so the risk is not immediately visible.")
    with cols[1]:
        card("2", "Pipe Cools Down", "As temperature drops, grease becomes sticky and adheres to walls, bends, and trapped debris.")
    with cols[2]:
        card("3", "Flow Slows", "Buildup slows drainage and odor starts coming back through the drain.")
    with cols[3]:
        card("4", "Reactive Repair", "After a real clog, the options are plumbing service, landlord negotiation, or harsh chemicals.")

    render_deep_table(
        "Stakeholder Pain Points",
        [
            ("Students", "odor, pests, plumbing fees, deposit pressure", "Users are willing to pay for low-cost prevention."),
            ("Landlords", "repair coordination cost and aging pipe damage", "Can be offered as a move-in accessory to reduce disputes."),
            ("Roommates / Shared Kitchens", "Diffuse responsibility; nobody wants to clean grease", "The clear chamber makes the problem visible and encourages shared cleaning."),
            ("Campus-Area Retailers", "High demand for household goods during move-in season", "Easy to bundle with existing products."),
        ],
    )


def page_solution() -> None:
    render_css()
    section_label("Solution")
    st.title("Low-Effort Grease Capture System")
    st.markdown(
        "No pipe work, no electricity, and no need to pre-sort soup. Swap the stopper and guide grease into a clear chamber."
    )
    render_signal_strip()

    left, right = st.columns([1, 1])
    with left:
        render_product_demo()
    with right:
        st.subheader("Core Flow")
        st.markdown(
            """
            1. Pour oily soup or wash greasy dishes  
            2. The guide structure extends oil-water dwell time  
            3. Grease stays in the clear chamber while water drains  
            4. Remove and empty the chamber without touching grease
            """
        )
        st.info("Key point: we are not changing student diets; we are lowering the effort required to do the right thing.")

        st.subheader("Before and After")
        st.markdown(
            """
            | Situation | Without Product | After Use |
            |---|---|---|
            | Hot-pot soup | Grease enters pipes, cools, and sticks | Grease stays in the chamber |
            | Slow Drainage | Users wait until clogging requires repair | Reduce buildup at the source |
            | Odor | Small rooms spread odor quickly | Reduce rancid grease residue |
            """
        )

    st.divider()
    section_label("Install Flow")
    st.header("30-Second Installation")
    cols = st.columns(4)
    with cols[0]:
        card("01", "Remove the Old Stopper", "No tools or pipe work; only touch the accessible top of the sink.")
    with cols[1]:
        card("02", "Press In the Seal Ring", "A flexible seal fits common drains and prevents bypass flow.")
    with cols[2]:
        card("03", "Attach the Chamber", "Face the clear chamber toward the user so grease buildup is visible.")
    with cols[3]:
        card("04", "Empty the Capture", "Detach and clean the chamber when full; filters can be replaced monthly.")

    render_deep_table(
        "Real Use Cases the Design Must Handle",
        [
            ("Hot Soup", "Heat-resistant PP and replaceable filters must tolerate short high-temperature exposure", "Prevents deformation or odor when students pour hot soup."),
            ("Small Sinks", "The body height cannot block dishwashing or cookware", "Rental kitchens are small; the product cannot become an obstacle."),
            ("Low-Effort Cleaning", "The chamber must be removable with one hand and minimal contact", "Cleaning friction determines retention."),
            ("Size Variation", "The seal must cover common low-cost drain sizes", "Universality determines whether the first campus channels can sell it."),
        ],
    )


def page_product() -> None:
    render_css()
    section_label("Product")
    st.title("Physical Design Optimized for Students")
    render_motion_visual("product", "Four core parts: seal, guide, chamber, and filter.")

    cols = st.columns(3)
    with cols[0]:
        card("A", "Universal Interface", "A flexible seal fits common rental drains without modifying existing hardware.")
    with cols[1]:
        card("B", "Clear Collection Chamber", "Visible grease capture reduces forgotten cleaning and makes the effect obvious.")
    with cols[2]:
        card("C", "Easy Cleaning", "The chamber can be removed quickly and emptied like trash, without touching grease.")

    st.divider()
    section_label("Underlying Magic")
    st.header("Pure Physical Separation, No Power, Low Failure Risk")

    cols = st.columns(3)
    cols[0].metric("Gravity", "Oil-water density difference", "natural layering", border=True)
    cols[1].metric("Centrifugal Flow", "guided dwell time", "improves capture", border=True)
    cols[2].metric("Industrial PP", "heat and chemical resistant", "manufacturing friendly", border=True)

    st.markdown(
        """
        <div class="pill-row">
            <span class="pill">No electricity</span>
            <span class="pill">No batteries</span>
            <span class="pill">Low failure risk</span>
            <span class="pill">Target price NT$150</span>
            <span class="pill">Compatible with compostable filters</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    section_label("Design Details")
    st.header("Four Design Parameters to Validate Before Production")
    cols = st.columns(4)
    cols[0].metric("Seal outer diameter", "32-45 mm", "rental drains", border=True)
    cols[1].metric("Chamber capacity", "80-120 ml", "weekly cleaning", border=True)
    cols[2].metric("Heat tolerance", "90°C", "hot soup use case", border=True)
    cols[3].metric("Cleaning motion", "< 3 min", "lower friction", border=True)

    st.divider()
    section_label("BOM Concept")
    st.header("First Production Configuration")
    render_deep_table(
        "BOM and Design Rationale",
        [
            ("Top Strainer", "Catches vegetable scraps, noodles, and rice", "Keeps solids out of the separation chamber and reduces jamming."),
            ("Flow Guide Vanes", "Creates rotation and dwell time in oily water", "Increases oil-water separation time, the core physical mechanism."),
            ("Clear Collection Chamber", "Visual grease buildup, removable", "Makes the effect visible and reminds users to clean."),
            ("Silicone Seal Ring", "Flexibly fits different drain heads", "Solves inconsistent rental sink hardware."),
            ("Filter Pack", "Compostable grease-absorbing material", "Creates monthly low-cost refills and freshness maintenance."),
        ],
    )

    st.subheader("MVP Test Versions")
    cols = st.columns(3)
    with cols[0]:
        card("V1", "3D-Printed Shell", "Quickly validates dimensions, cleaning feel, and flow direction.")
    with cols[1]:
        card("V2", "Silicone Ring Kit", "Tests fit rate and leakage across different sink drains.")
    with cols[2]:
        card("V3", "Small-Batch Injection", "Enters a 20-50 unit campus pilot and collects real grease data.")


def page_market() -> None:
    render_css()
    section_label("Market Opportunity")
    st.title("Millions of Student and Young Renters Need Drainage Insurance")
    render_motion_visual("market", "Start with NTHU-area renters, then expand to young renters and shared kitchens.")

    left, right = st.columns([1.1, 1])
    with left:
        st.markdown(
            """
            In older buildings, low-budget rentals, and high-takeout routines, Clario Living turns expensive repairs into low-cost prevention.
            """
        )
        st.markdown(
            """
            <div class="card">
                <div class="big-number">10x</div>
                <p class="muted">One plumbing repair costs about ten preventive stoppers. Students are more willing to spend NT$150 on drainage insurance.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.metric("Potential Audience", "1M+", "student and young renters", border=True)
        st.metric("Common rental age", "20+ years", "aging-pipe risk", border=True)
        st.metric("Filter subscription", "< NT$20/month", "repeat purchase driver", border=True)

    st.divider()
    section_label("Business Model")
    st.header("Enter Through Move-In Season, Then Drive Refills")
    cols = st.columns(3)
    with cols[0]:
        card("Launch", "Campus-Area Retail", "Hardware stores, stationery shops, lifestyle retailers, and dorm supply stores.")
    with cols[1]:
        card("Bundle", "Student Renter Starter Kit", "Bundled with mattresses, hangers, and extension cords in the first move-in purchase.")
    with cols[2]:
        card("Recurring", "Filter Subscription", "Compostable grease-absorbing packs keep the sink fresh for under NT$20 per month.")

    st.divider()
    section_label("Go-To-Market Detail")
    st.header("Three-Stage Go-To-Market")
    render_deep_table(
        "Channel and Conversion Strategy",
        [
            ("Campus Validation", "NTHU-area student rentals, dorm shared kitchens, and small studios", "Start in the most familiar context to collect cases and referrals."),
            ("Move-In Kit", "Bundle with mattresses, hangers, extension cords, and trash bins", "Students are most willing to buy household essentials during move-in."),
            ("Lifestyle Retail", "Hardware stores, lifestyle retailers, and campus-area stationery shops", "The product is easy to understand and fits impulse low-price purchases."),
            ("Filter Refill", "QR code leads to monthly filter delivery or campus pickup", "Connects low-cost hardware to recurring revenue."),
        ],
    )

    st.divider()
    section_label("Adoption Funnel")
    st.header("From Odor Awareness to Filter Refills")
    funnel_cols = st.columns(5)
    funnel_cols[0].metric("Reach", "Campus social", "short videos / starter kits", border=True)
    funnel_cols[1].metric("Understand", "self-check", "quantified pain", border=True)
    funnel_cols[2].metric("Purchase", "NT$150", "low decision cost", border=True)
    funnel_cols[3].metric("Continue", "visible capture", "cleaning reminder", border=True)
    funnel_cols[4].metric("Refill", "filters", "low monthly cost", border=True)


def page_team_pitch() -> None:
    render_css()
    section_label("Team")
    st.title("Clario Living Team")

    identity_options = {
        "Formal Pitch": {
            "tagline": "Building hardware with financial discipline and student insight.",
            "focus": "Best for investor-facing moments: professional, stable, and credible.",
            "badges": ["Cost Model", "Business Story", "Product Validation"],
        },
        "Campus Interviews": {
            "tagline": "Finding the problem in real NTHU-area rental kitchens.",
            "focus": "Shows that the team understands rental life and can connect interviews, use cases, and channel assumptions.",
            "badges": ["Renter Insight", "User Interviews", "Move-In Channel"],
        },
        "Product Experiment": {
            "tagline": "Turning sink clogging into testable product assumptions.",
            "focus": "Best for discussing prototypes, fit rate, cleaning feel, and grease capture volume.",
            "badges": ["MVP Prototype", "Grease Capture", "90-Day Pilot"],
        },
        "Financial Analysis": {
            "tagline": "Using finance training to defend pricing, margin, and refills.",
            "focus": "Shows the team can turn NT$150 low-cost hardware into a sustainable business model.",
            "badges": ["Unit Economics", "Filter Refill", "Break-Even"],
        },
    }
    selected_identity = st.segmented_control(
        "Switch team angle",
        list(identity_options.keys()),
        default="Formal Pitch",
        label_visibility="collapsed",
    )
    identity = identity_options[selected_identity]

    left, right = st.columns([1.05, 1])
    with left:
        st.image(
            TEAM_ILLUSTRATION_IMAGE,
            caption="Team illustration: Yi-Chieh Liao, Kai-Yun Tseng, Chih-Fan Chiou",
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

    render_motion_visual("team", "Core Team: CEO / CFO / CMO Roles")
    st.markdown(
        """
        We are an NTHU finance team: Yi-Chieh Liao, Kai-Yun Tseng, and Chih-Fan Chiou. We turn the real pain of rental living into product design, cost models, and campus pilot strategy.
        """
    )

    st.markdown(
        """
        <div class="quote">
            We are not just selling a sink stopper; we are protecting dignity and quality of life in rental living.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    section_label("Speaking Notes")
    st.header("30-Second Closing Script")
    st.markdown(
        """
        We are Clario Living, an NTHU student-founded team by Yi-Chieh Liao, Kai-Yun Tseng, and Chih-Fan Chiou. In rental life, clogged pipes and odor are not small problems; they affect a student’s room, budget, and dignity. Our low-cost, zero-power, easy-clean stopper turns expensive reactive repair into everyday prevention.
        """
    )

    st.divider()
    section_label("Team Advantage")
    st.header("How to Explain the Team Advantage")
    render_deep_table(
        "Turning Background Into Execution",
        [
            ("Yi-Chieh Liao", "CEO: Company strategy and product vision", "Leads supply-chain integration and production planning."),
            ("Kai-Yun Tseng", "CFO: Financial planning and capital allocation", "Owns the 18-month break-even plan."),
            ("Chih-Fan Chiou", "CMO: Market positioning and brand growth", "Leads B2B property partnerships and B2C brand growth through a painless-upgrade strategy."),
            ("Finance Background", "Uses data, cost, and risk thinking to manage a hardware pilot", "Keeps the project moving beyond an idea toward production and sales."),
        ],
    )

    st.subheader("15-Second Team Intro")
    st.success("We are Yi-Chieh Liao, Kai-Yun Tseng, and Chih-Fan Chiou from NTHU finance. Rental living showed us the real sink-clogging problem, and our finance training helps us judge whether this product can survive through cost, margin, and pilot data.")


def page_deck() -> None:
    render_css()
    section_label("Reference Deck")
    st.title("Reference Deck and Competition Rules")
    render_motion_visual("deck", "Turning the original deck into an interactive, demo-ready, calculator-enabled site.")

    left, right = st.columns(2)
    with left:
        st.image(RULES_IMAGE, caption="Startup World Cup Pitch Deck Outline 2025")
        if RULES_PDF.exists():
            st.download_button(
                "Download SWC Rules PDF",
                data=RULES_PDF.read_bytes(),
                file_name=RULES_PDF.name,
                mime="application/pdf",
                use_container_width=True,
            )
    with right:
        st.image(PROPOSAL_IMAGE, caption="Smart Grease Trap Revolution")
        if PROPOSAL_PDF.exists():
            st.download_button(
                "Download Original Proposal PDF",
                data=PROPOSAL_PDF.read_bytes(),
                file_name=PROPOSAL_PDF.name,
                mime="application/pdf",
                use_container_width=True,
            )

    st.divider()
    section_label("Image Credits")
    st.header("Web Image Sources Used on This Site")
    st.markdown(
        """
        - Small studio sink context image:Pexels, Max Vakhtbovycn, Kitchen counter with sink in small apartment
        - Dirty dish sink context image:Unsplash, Devon MacKay, A kitchen sink filled with dishes next to a window
        - Drain close-up:Unsplash, Daniel Dan, A close up of a metal sink drain
        """
    )


def sidebar_intro() -> None:
    st.sidebar.markdown("## Clario Living")
    st.sidebar.caption("Drain Protection for Rental Living")
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        **Site Menu**

        Use the left navigation to switch pages. The homepage includes a self-check; the other pages map to key pitch-deck sections.
        """
    )


sidebar_intro()

pages = {
    "Clario Living": [
        st.Page(page_home, title="Home and Self-Check", url_path="", default=True),
        st.Page(page_problem, title="Problem", url_path="problem"),
        st.Page(page_solution, title="Solution", url_path="solution"),
        st.Page(page_product, title="Product and Technology", url_path="product"),
        st.Page(page_demo_lab, title="Interactive Lab", url_path="demo-lab"),
        st.Page(page_market, title="Market and Business Model", url_path="market"),
        st.Page(page_financials, title="Financial Calculator", url_path="financials"),
        st.Page(page_pilot_strategy, title="Pilot Strategy", url_path="pilot"),
        st.Page(page_team_pitch, title="Team and Closing", url_path="team"),
        st.Page(page_problem, title="Problem", url_path="page_problem", visibility="hidden"),
        st.Page(page_solution, title="Solution", url_path="page_solution", visibility="hidden"),
        st.Page(page_product, title="Product and Technology", url_path="page_product", visibility="hidden"),
        st.Page(page_demo_lab, title="Interactive Lab", url_path="page_demo_lab", visibility="hidden"),
        st.Page(page_market, title="Market and Business Model", url_path="page_market", visibility="hidden"),
        st.Page(page_financials, title="Financial Calculator", url_path="page_financials", visibility="hidden"),
        st.Page(page_pilot_strategy, title="Pilot Strategy", url_path="page_pilot_strategy", visibility="hidden"),
        st.Page(page_team_pitch, title="Team and Closing", url_path="page_team_pitch", visibility="hidden"),
        st.Page(page_judge_room, title="Investor Q&A", url_path="page_judge_room", visibility="hidden"),
        st.Page(page_deck, title="Deck and Rules", url_path="page_deck", visibility="hidden"),
    ]
}

current_page = st.navigation(pages, position="sidebar", expanded=True)
current_page.run()
