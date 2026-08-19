<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Luna.AI - Premium Assistant</title>
  
  <!-- Modern Font Imports -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-dark: #05070e;
      --panel-bg: rgba(13, 17, 28, 0.65);
      --panel-border: rgba(255, 255, 255, 0.08);
      --accent-pink: #f43f5e;
      --accent-purple: #a855f7;
      --accent-cyan: #06b6d4;
      --accent-gold: #fbbf24;
      --text-primary: #f8fafc;
      --text-muted: #94a3b8;
      --input-bg: rgba(21, 26, 42, 0.7);
      --glass-glow: rgba(244, 63, 94, 0.15);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-primary);
      display: flex;
      height: 100vh;
      overflow: hidden;
      position: relative;
    }

    /* Ambient Background Glow Orbs */
    .ambient-bg {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 0;
      pointer-events: none;
      overflow: hidden;
    }

    .orb {
      position: absolute;
      border-radius: 50%;
      filter: blur(120px);
      opacity: 0.35;
      animation: floatOrb 18s ease-in-out infinite alternate;
    }

    .orb-1 {
      top: -10%;
      left: 20%;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, var(--accent-pink), transparent 70%);
    }

    .orb-2 {
      bottom: -15%;
      right: 10%;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, var(--accent-purple), transparent 70%);
      animation-delay: -5s;
    }

    .orb-3 {
      top: 40%;
      left: -10%;
      width: 450px;
      height: 450px;
      background: radial-gradient(circle, var(--accent-cyan), transparent 70%);
      animation-delay: -10s;
    }

    @keyframes floatOrb {
      0% { transform: translate(0, 0) scale(1); }
      50% { transform: translate(60px, 40px) scale(1.1); }
      100% { transform: translate(-40px, -60px) scale(0.95); }
    }

    /* App Loader */
    #app-loader {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: var(--bg-dark);
      display: flex; flex-direction: column; justify-content: center; align-items: center;
      z-index: 999;
      transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .loader-orb-wrapper {
      position: relative; width: 100px; height: 100px;
      display: flex; justify-content: center; align-items: center;
      margin-bottom: 24px;
    }

    .loader-orb {
      position: absolute; width: 100%; height: 100%; border-radius: 50%;
      border: 3px solid transparent; 
      border-top-color: var(--accent-pink); 
      border-right-color: var(--accent-purple);
      animation: spin 1.2s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
    }

    .loader-orb-inner {
      position: absolute; width: 70%; height: 70%; border-radius: 50%;
      border: 3px solid transparent; 
      border-bottom-color: var(--accent-cyan); 
      border-left-color: var(--accent-pink);
      animation: spinReverse 0.9s linear infinite;
    }

    .loader-text {
      font-size: 13px; font-weight: 800; color: var(--text-primary);
      letter-spacing: 4px; text-transform: uppercase;
      background: linear-gradient(90deg, var(--accent-pink), var(--accent-purple), var(--accent-cyan));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      animation: pulseGlow 2s infinite alternate;
    }

    /* Sidebar Styling */
    .sidebar {
      width: 290px;
      background: var(--panel-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      display: flex; flex-direction: column; justify-content: space-between;
      padding: 24px 18px;
      border-right: 1px solid var(--panel-border);
      z-index: 10;
      box-shadow: 10px 0 30px rgba(0, 0, 0, 0.3);
    }

    .brand-container {
      display: flex; align-items: center; gap: 12px; margin-bottom: 24px; cursor: pointer;
      padding: 6px 8px; border-radius: 12px; transition: background 0.3s;
    }
    .brand-container:hover { background: rgba(255, 255, 255, 0.04); }

    .brand-logo-wrapper {
      width: 42px; height: 42px; border-radius: 14px;
      background: linear-gradient(135deg, var(--accent-pink), var(--accent-purple));
      display: flex; justify-content: center; align-items: center;
      box-shadow: 0 0 20px rgba(244, 63, 94, 0.4);
      overflow: hidden; position: relative;
      animation: logoGlow 4s ease-in-out infinite alternate;
    }

    @keyframes logoGlow {
      0% { box-shadow: 0 0 15px rgba(244, 63, 94, 0.3); }
      100% { box-shadow: 0 0 30px rgba(168, 85, 247, 0.6), 0 0 10px rgba(6, 182, 212, 0.4); }
    }

    .brand-logo-img { width: 100%; height: 100%; object-fit: cover; }
    .brand-name {
      font-size: 1.35rem; font-weight: 800; letter-spacing: -0.5px;
      background: linear-gradient(135deg, #fff 30%, var(--accent-pink));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    .vip-badge {
      font-size: 10px; font-weight: 800;
      background: linear-gradient(135deg, var(--accent-gold), #f59e0b);
      color: #000; padding: 3px 7px; border-radius: 8px; letter-spacing: 1px; margin-left: auto;
      box-shadow: 0 0 12px rgba(251, 191, 36, 0.3);
    }

    .new-chat-btn {
      display: flex; align-items: center; justify-content: center; gap: 10px;
      padding: 14px; border-radius: 14px; color: #fff; font-weight: 700;
      background: linear-gradient(135deg, var(--accent-pink), var(--accent-purple));
      border: none; cursor: pointer; font-size: 14px; width: 100%; margin-bottom: 24px;
      box-shadow: 0 4px 20px rgba(244, 63, 94, 0.35);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative; overflow: hidden;
    }

    .new-chat-btn::before {
      content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
      transition: left 0.5s;
    }

    .new-chat-btn:hover::before { left: 100%; }
    .new-chat-btn:hover { transform: translateY(-2px) scale(1.01); box-shadow: 0 8px 30px rgba(244, 63, 94, 0.5); }
    .new-chat-btn:active { transform: translateY(0) scale(0.98); }

    .recents-label {
      font-size: 11px; font-weight: 800; color: var(--text-muted);
      margin: 0 0 12px 6px; text-transform: uppercase; letter-spacing: 1.2px;
    }

    .recents-list { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; padding-right: 4px; }
    .recents-list::-webkit-scrollbar { width: 4px; }
    .recents-list::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 4px; }

    .recent-item-container {
      display: flex; align-items: center; justify-content: space-between;
      border-radius: 12px; padding: 4px; transition: all 0.25s ease;
      border: 1px solid transparent;
    }
    .recent-item-container:hover { background: rgba(255, 255, 255, 0.04); border-color: var(--panel-border); }
    .recent-item-container.active { background: rgba(244, 63, 94, 0.12); border-color: rgba(244, 63, 94, 0.3); }

    .recent-item {
      display: flex; align-items: center; gap: 10px; padding: 8px;
      color: var(--text-primary); background: transparent; border: none;
      cursor: pointer; font-size: 13.5px; flex: 1; text-align: left; font-weight: 500;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }

    .sidebar-action-btn {
      background: transparent; border: none; color: var(--text-muted);
      cursor: pointer; opacity: 0; transition: all 0.2s;
      display: flex; align-items: center; justify-content: center; padding: 6px; border-radius: 6px;
    }
    .recent-item-container:hover .sidebar-action-btn { opacity: 1; }
    .sidebar-action-btn:hover { color: var(--accent-pink); background: rgba(244, 63, 94, 0.15); }

    .profile-section {
      display: flex; align-items: center; justify-content: space-between;
      padding-top: 18px; border-top: 1px solid var(--panel-border); margin-top: auto;
    }
    .profile-img { width: 38px; height: 38px; border-radius: 50%; border: 2px solid var(--accent-pink); box-shadow: 0 0 10px rgba(244, 63, 94, 0.3); }

    /* Main Section Styling */
    .main-content {
      flex: 1; display: flex; flex-direction: column;
      justify-content: space-between; align-items: center;
      padding: 40px 24px 28px; position: relative; z-index: 5;
    }

    /* Hero Section */
    .hero-container {
      display: flex; flex-direction: column; align-items: center;
      margin-top: auto; margin-bottom: auto; text-align: center;
      animation: fadeInScale 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes fadeInScale {
      from { opacity: 0; transform: scale(0.92) translateY(20px); }
      to { opacity: 1; transform: scale(1) translateY(0); }
    }

    .glowing-ring-container {
      position: relative; width: 140px; height: 140px;
      display: flex; justify-content: center; align-items: center; margin-bottom: 32px;
    }

    .glowing-ring {
      position: absolute; width: 100%; height: 100%; border-radius: 50%;
      border: 3px solid transparent; 
      border-top-color: var(--accent-pink); 
      border-right-color: var(--accent-purple);
      box-shadow: 0 0 40px rgba(244, 63, 94, 0.4);
      animation: spin 6s linear infinite;
    }

    .glowing-ring-inner {
      position: absolute; width: 75%; height: 75%; border-radius: 50%;
      border: 3px solid transparent; 
      border-bottom-color: var(--accent-cyan); 
      border-left-color: var(--accent-pink);
      animation: spinReverse 4s linear infinite;
    }

    .core-orb {
      width: 50%; height: 50%; border-radius: 50%;
      background: radial-gradient(circle, var(--accent-pink), var(--accent-purple));
      box-shadow: 0 0 35px var(--accent-pink);
      animation: pulseCore 2.5s ease-in-out infinite alternate;
    }

    @keyframes pulseCore {
      0% { transform: scale(0.85); opacity: 0.8; }
      100% { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 15px var(--accent-purple)); }
    }

    @keyframes spin { 100% { transform: rotate(360deg); } }
    @keyframes spinReverse { 100% { transform: rotate(-360deg); } }

    .hero-title { font-size: 2.6rem; font-weight: 800; margin-bottom: 28px; letter-spacing: -1px; }
    .hero-title span {
      background: linear-gradient(135deg, var(--accent-pink), var(--accent-purple), var(--accent-cyan));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    .suggestion-container { display: flex; gap: 14px; flex-wrap: wrap; justify-content: center; max-width: 650px; }
    .chip {
      background: rgba(255, 255, 255, 0.03); 
      border: 1px solid var(--panel-border);
      backdrop-filter: blur(10px);
      padding: 12px 22px; border-radius: 30px; font-size: 13.5px; font-weight: 500;
      color: var(--text-muted); cursor: pointer; 
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      animation: floatChip 4s ease-in-out infinite alternate;
    }
    .chip:nth-child(2) { animation-delay: 0.7s; }
    .chip:nth-child(3) { animation-delay: 1.4s; }

    @keyframes floatChip { 0% { transform: translateY(0); } 100% { transform: translateY(-8px); } }
    
    .chip:hover {
      background: rgba(244, 63, 94, 0.12); border-color: rgba(244, 63, 94, 0.4); color: #fff;
      transform: translateY(-4px) scale(1.02);
      box-shadow: 0 10px 25px rgba(244, 63, 94, 0.25);
    }

    /* Chat Stream */
    .chat-stream {
      width: 100%; max-width: 850px; flex: 1; overflow-y: auto;
      display: flex; flex-direction: column; gap: 20px; margin-bottom: 24px; padding-right: 12px;
      scroll-behavior: smooth;
    }

    .chat-stream::-webkit-scrollbar { width: 6px; }
    .chat-stream::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 6px; }

    .msg-wrapper {
      display: flex; flex-direction: column; max-width: 82%; position: relative;
      animation: msgSlideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes msgSlideIn {
      from { opacity: 0; transform: translateY(18px) scale(0.96); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .msg-wrapper.user { align-self: flex-end; }
    .msg-wrapper.luna { align-self: flex-start; }

    .msg {
      padding: 16px 24px; border-radius: 22px; font-size: 15px; line-height: 1.6; font-weight: 400;
      backdrop-filter: blur(12px);
    }

    .user .msg {
      background: linear-gradient(135deg, rgba(244, 63, 94, 0.28), rgba(168, 85, 247, 0.2));
      border: 1px solid rgba(244, 63, 94, 0.35); border-bottom-right-radius: 6px;
      color: #fff; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
    }

    .luna .msg {
      background: var(--panel-bg); 
      border: 1px solid var(--panel-border);
      border-bottom-left-radius: 6px;
      color: var(--text-primary);
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3), 0 0 15px rgba(168, 85, 247, 0.1);
    }

    .typing-orb-indicator {
      display: inline-flex; align-items: center; gap: 6px; padding: 4px 8px;
    }

    .typing-dot {
      width: 8px; height: 8px; border-radius: 50%; background: var(--accent-pink);
      animation: dotPulse 1.4s infinite ease-in-out;
    }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; background: var(--accent-purple); }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; background: var(--accent-cyan); }

    @keyframes dotPulse {
      0%, 100% { transform: scale(0.6); opacity: 0.4; }
      50% { transform: scale(1.2); opacity: 1; }
    }

    .msg-actions { display: flex; gap: 8px; margin-top: 6px; opacity: 0; transition: opacity 0.2s; }
    .msg-wrapper:hover .msg-actions { opacity: 1; }
    .user .msg-actions { justify-content: flex-end; }

    .action-btn {
      background: rgba(255, 255, 255, 0.05); border: 1px solid var(--panel-border);
      color: var(--text-muted); cursor: pointer; font-size: 11px; font-weight: 600;
      padding: 5px 12px; border-radius: 8px; display: inline-flex; align-items: center; gap: 6px;
      transition: all 0.2s ease; backdrop-filter: blur(8px);
    }
    .action-btn:hover { color: #fff; background: rgba(255, 255, 255, 0.12); border-color: rgba(255, 255, 255, 0.25); }
    .action-btn svg { width: 13px; height: 13px; fill: currentColor; }

    /* Input Bar */
    .input-container {
      width: 100%; max-width: 850px; background: var(--input-bg);
      border: 1px solid rgba(244, 63, 94, 0.25); border-radius: 35px;
      padding: 10px 18px 10px 24px; display: flex; align-items: center; gap: 14px;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5), 0 0 20px rgba(244, 63, 94, 0.12);
      backdrop-filter: blur(20px);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .input-container:focus-within {
      border-color: var(--accent-pink);
      box-shadow: 0 14px 45px rgba(0, 0, 0, 0.6), 0 0 28px rgba(244, 63, 94, 0.3);
      transform: translateY(-2px);
    }

    .input-container.disabled { opacity: 0.5; pointer-events: none; }

    .input-container input {
      flex: 1; background: transparent; border: none; outline: none; color: #fff; font-size: 15.5px;
      font-weight: 400;
    }

    .input-container input::placeholder { color: var(--text-muted); opacity: 0.7; }

    .icon-btn {
      background: transparent; border: none; color: var(--text-muted);
      cursor: pointer; padding: 10px; border-radius: 50%; transition: all 0.25s;
      display: flex; align-items: center; justify-content: center;
    }
    .icon-btn svg { width: 20px; height: 20px; fill: currentColor; }
    .icon-btn:hover { color: var(--accent-pink); background: rgba(244, 63, 94, 0.12); transform: scale(1.1); }
    .mic-active { color: var(--accent-pink) !important; animation: pulseMic 1.2s ease-in-out infinite alternate; }

    @keyframes pulseMic { 
      from { transform: scale(1); filter: drop-shadow(0 0 2px var(--accent-pink)); } 
      to { transform: scale(1.2); filter: drop-shadow(0 0 12px var(--accent-pink)); } 
    }

    .disclaimer { font-size: 11.5px; color: var(--text-muted); margin-top: 14px; letter-spacing: 0.2px; opacity: 0.8; }
    #logo-input { display: none; }
  </style>
</head>
<body>

  <!-- Ambient Glow Canvas -->
  <div class="ambient-bg">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
  </div>

  <!-- Animated Loading Screen -->
  <div id="app-loader">
    <div class="loader-orb-wrapper">
      <div class="loader-orb"></div>
      <div class="loader-orb-inner"></div>
    </div>
    <div class="loader-text">Luna AI Engine</div>
  </div>

  <!-- Sidebar -->
  <div class="sidebar">
    <div>
      <div class="brand-container" onclick="document.getElementById('logo-input').click()" title="Click to Upload Custom Logo">
        <div class="brand-logo-wrapper">
          <img id="brand-logo" class="brand-logo-img" src="{{ url_for('static', filename='logo.png') }}" alt="Logo" onerror="this.style.display='none'">
        </div>
        <span class="brand-name">Luna.AI</span>
        <span class="vip-badge">PRO</span>
      </div>
      <input type="file" id="logo-input" accept="image/*" onchange="uploadCustomLogo(event)">

      <button class="new-chat-btn" id="newChatBtn" onclick="createNewChat()">
        <svg viewBox="0 0 24 24" style="width:18px; height:18px; fill:currentColor;"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
        New Session
      </button>

      <div class="recents-label">Recent Conversations</div>
      <div class="recents-list" id="recents-list"></div>
    </div>

    <div class="profile-section">
      <div style="display: flex; align-items: center; gap: 12px;">
        <img class="profile-img" src="{{ url_for('static', filename='logo.png') }}" alt="User" onerror="this.src='https://api.dicebear.com/7.x/bottts/svg?seed=Luna'">
        <div>
          <div style="font-size: 14px; font-weight: 700; color: #fff;">Luna Core</div>
          <div style="font-size: 11px; color: var(--accent-pink); font-weight: 600;">v2.5 Flash</div>
        </div>
      </div>
      <div style="display: flex; gap: 4px;">
        <button class="icon-btn" id="muteBtn" onclick="toggleMute()" title="Mute/Unmute Audio">
          <svg id="muteIcon" viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
        </button>
        <button class="icon-btn" onclick="createNewChat()" title="Reset Chat">
          <svg viewBox="0 0 24 24"><path d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/></svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Main View -->
  <div class="main-content">
    <div class="hero-container" id="hero">
      <div class="glowing-ring-container">
        <div class="glowing-ring"></div>
        <div class="glowing-ring-inner"></div>
        <div class="core-orb"></div>
      </div>
      <div class="hero-title">How can <span>Luna</span> assist today?</div>
      
      <div class="suggestion-container">
        <div class="chip" onclick="useChip('Tell me something inspiring!')">✨ Inspiring Thought</div>
        <div class="chip" onclick="useChip('Who created you?')">⚡ Who Created You?</div>
        <div class="chip" onclick="useChip('Mujhe ek choti kahani sunao')">📖 Hindi Story</div>
      </div>
    </div>

    <div class="chat-stream" id="chat" style="display: none;"></div>

    <div style="width: 100%; display: flex; flex-direction: column; align-items: center;">
      <div class="input-container" id="inputContainer">
        <input type="text" id="userInput" placeholder="Ask Luna anything..." onkeydown="if(event.key === 'Enter') sendText()">
        <button class="icon-btn" id="micBtn" onclick="startVoice()" title="Speak">
          <svg viewBox="0 0 24 24"><path d="M12 14c1.66 0 2.99-1.34 2.99-3L15 5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5.3-3c0 3-2.54 5.1-5.3 5.1S6.7 14 6.7 11H5c0 3.41 2.72 6.23 6 6.72V21h2v-3.28c3.28-.48 6-3.3 6-6.72h-1.7z"/></svg>
        </button>
        <button class="icon-btn" id="sendBtn" onclick="sendText()" style="color: var(--accent-pink);" title="Send">
          <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
        </button>
      </div>
      <div class="disclaimer">Luna.AI is powered by Gemini 2.5 Flash for ultra-fast generation.</div>
    </div>
  </div>

  <script>
    let isListening = false;
    let isMuted = false;
    let isReplying = false;
    let sessions = [];
    let currentSessionId = null;
    let speechRecognitionInstance = null;

    const SVG_ICONS = {
      chat: `<svg viewBox="0 0 24 24" style="width:14px; height:14px; fill:currentColor;"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 5H6v-2h8v2zm4-6H6V6h12v2z"/></svg>`,
      trash: `<svg viewBox="0 0 24 24" style="width:14px; height:14px; fill:currentColor;"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/></svg>`,
      copy: `<svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>`,
      edit: `<svg viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>`,
      check: `<svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>`,
      soundOn: `<path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>`,
      soundOff: `<path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>`
    };

    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    function playBeep(freq = 440, type = 'sine', duration = 0.1) {
      if (isMuted) return;
      try {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      } catch (e) {}
    }

    window.addEventListener('load', () => {
      setTimeout(() => {
        const loader = document.getElementById('app-loader');
        loader.style.opacity = '0';
        setTimeout(() => loader.style.display = 'none', 600);
      }, 700);

      const savedLogo = localStorage.getItem('luna_custom_logo');
      if (savedLogo) {
        document.getElementById('brand-logo').src = savedLogo;
      }
    });

    function setInputCooldown(state) {
      isReplying = state;
      const inputContainer = document.getElementById('inputContainer');
      const input = document.getElementById('userInput');
      const sendBtn = document.getElementById('sendBtn');
      const micBtn = document.getElementById('micBtn');

      if (state) {
        inputContainer.classList.add('disabled');
        input.disabled = true;
        sendBtn.disabled = true;
        micBtn.disabled = true;
      } else {
        inputContainer.classList.remove('disabled');
        input.disabled = false;
        sendBtn.disabled = false;
        micBtn.disabled = false;
        input.focus();
      }
    }

    function toggleMute() {
      isMuted = !isMuted;
      document.getElementById('muteIcon').innerHTML = isMuted ? SVG_ICONS.soundOff : SVG_ICONS.soundOn;
      if (isMuted && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
    }

    function uploadCustomLogo(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
          const logoUrl = e.target.result;
          document.getElementById('brand-logo').src = logoUrl;
          document.getElementById('brand-logo').style.display = 'block';
          localStorage.setItem('luna_custom_logo', logoUrl);
        };
        reader.readAsDataURL(file);
      }
    }

    function createNewChat() {
      if (isReplying) return;
      playBeep(500, 'sine', 0.1);
      fetch('/reset', { method: 'POST' }).catch(() => {});
      currentSessionId = null;
      document.getElementById('chat').innerHTML = '';
      document.getElementById('chat').style.display = 'none';
      document.getElementById('hero').style.display = 'flex';
      renderRecents();
    }

    function renameSession(id, event) {
      event.stopPropagation();
      const session = sessions.find(s => s.id === id);
      if (!session) return;

      const newTitle = prompt("Enter new title for this chat:", session.title);
      if (newTitle && newTitle.trim() !== "") {
        session.title = newTitle.trim();
        renderRecents();
      }
    }

    function deleteSession(id, event) {
      event.stopPropagation();
      sessions = sessions.filter(s => s.id !== id);
      if (currentSessionId === id) {
        createNewChat();
      } else {
        renderRecents();
      }
    }

    function renderRecents() {
      const list = document.getElementById('recents-list');
      list.innerHTML = '';
      sessions.forEach(session => {
        const container = document.createElement('div');
        container.className = `recent-item-container ${session.id === currentSessionId ? 'active' : ''}`;
        
        const btn = document.createElement('button');
        btn.className = 'recent-item';
        btn.innerHTML = `${SVG_ICONS.chat} <span>${session.title}</span>`;
        btn.onclick = () => loadSession(session.id);

        const renameBtn = document.createElement('button');
        renameBtn.className = 'sidebar-action-btn';
        renameBtn.innerHTML = SVG_ICONS.edit;
        renameBtn.title = 'Rename Chat';
        renameBtn.onclick = (e) => renameSession(session.id, e);

        const delBtn = document.createElement('button');
        delBtn.className = 'sidebar-action-btn';
        delBtn.innerHTML = SVG_ICONS.trash;
        delBtn.title = 'Delete Chat';
        delBtn.onclick = (e) => deleteSession(session.id, e);

        container.appendChild(btn);
        container.appendChild(renameBtn);
        container.appendChild(delBtn);
        list.appendChild(container);
      });
    }

    function loadSession(id) {
      if (isReplying) return;
      const session = sessions.find(s => s.id === id);
      if (!session) return;

      currentSessionId = id;
      document.getElementById('hero').style.display = 'none';
      const chat = document.getElementById('chat');
      chat.style.display = 'flex';
      chat.innerHTML = '';

      let lastUserIndex = -1;
      for (let i = session.messages.length - 1; i >= 0; i--) {
        if (session.messages[i].sender === 'user') {
          lastUserIndex = i;
          break;
        }
      }

      session.messages.forEach((m, idx) => {
        const isLatestUserMessage = (m.sender === 'user' && idx === lastUserIndex);
        renderMessageBubble(m.text, m.sender, idx, false, isLatestUserMessage);
      });
      renderRecents();
    }

    function useChip(text) {
      if (isReplying) return;
      document.getElementById('userInput').value = text;
      sendText();
    }

    async function sendText() {
      if (isReplying) return;
      const input = document.getElementById('userInput');
      const text = input.value.trim();
      if (!text) return;

      setInputCooldown(true);
      playBeep(600, 'sine', 0.08);

      document.getElementById('hero').style.display = 'none';
      const chat = document.getElementById('chat');
      chat.style.display = 'flex';

      if (!currentSessionId) {
        currentSessionId = Date.now();
        sessions.unshift({
          id: currentSessionId,
          title: text.length > 22 ? text.substring(0, 22) + '...' : text,
          messages: []
        });
      }

      const sess = sessions.find(s => s.id === currentSessionId);
      sess.messages.push({ text, sender: 'user' });

      renderMessageBubble(text, 'user', sess.messages.length - 1, false, true);
      input.value = '';
      renderRecents();

      const typingIndicator = showTypingIndicator();

      try {
        const res = await fetch('/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: text })
        });
        const data = await res.json();

        typingIndicator.remove();

        const replyText = (data && data.success && data.reply) ? data.reply : "I am experiencing connection issues. Please try again! 🌸";

        playBeep(880, 'sine', 0.12);
        sess.messages.push({ text: replyText, sender: 'luna' });
        renderMessageBubble(replyText, 'luna', sess.messages.length - 1, true, false);
        speakOutLoud(replyText);

      } catch (err) {
        typingIndicator.remove();
        const fallbackReply = "Sorry, I couldn't connect to the server right now. 😔";
        sess.messages.push({ text: fallbackReply, sender: 'luna' });
        renderMessageBubble(fallbackReply, 'luna', sess.messages.length - 1, true, false);
      }
    }

    function renderMessageBubble(text, sender, index, animateTyping = false, isLatestUser = false) {
      const chat = document.getElementById('chat');
      const wrapper = document.createElement('div');
      wrapper.className = `msg-wrapper ${sender}`;

      const msgDiv = document.createElement('div');
      msgDiv.className = 'msg';

      const actionsDiv = document.createElement('div');
      actionsDiv.className = 'msg-actions';

      const copyBtn = document.createElement('button');
      copyBtn.className = 'action-btn';
      copyBtn.innerHTML = `${SVG_ICONS.copy} Copy`;
      copyBtn.onclick = () => {
        navigator.clipboard.writeText(text);
        copyBtn.innerHTML = `${SVG_ICONS.check} Copied`;
        setTimeout(() => copyBtn.innerHTML = `${SVG_ICONS.copy} Copy`, 1500);
      };
      actionsDiv.appendChild(copyBtn);

      if (sender === 'user' && isLatestUser && index !== -1) {
        const editBtn = document.createElement('button');
        editBtn.className = 'action-btn';
        editBtn.innerHTML = `${SVG_ICONS.edit} Edit`;
        editBtn.onclick = () => editMessage(index);
        actionsDiv.appendChild(editBtn);
      }

      wrapper.appendChild(msgDiv);
      wrapper.appendChild(actionsDiv);
      chat.appendChild(wrapper);

      if (animateTyping && sender === 'luna') {
        let i = 0;
        const speed = 15;

        function type() {
          if (i < text.length) {
            msgDiv.innerText = text.substring(0, i + 1);
            i++;
            chat.scrollTop = chat.scrollHeight;
            setTimeout(type, speed);
          } else {
            setInputCooldown(false);
          }
        }
        type();
      } else {
        msgDiv.innerText = text;
        chat.scrollTop = chat.scrollHeight;
        if (sender === 'luna') setInputCooldown(false);
      }
    }

    function editMessage(index) {
      if (isReplying) return;
      const sess = sessions.find(s => s.id === currentSessionId);
      if (!sess || !sess.messages[index]) return;

      const oldText = sess.messages[index].text;
      const newText = prompt("Edit your message:", oldText);

      if (newText && newText.trim() !== "") {
        sess.messages[index].text = newText.trim();
        loadSession(currentSessionId);
      }
    }

    function startVoice() {
      if (isListening || isReplying) return;

      const micBtn = document.getElementById('micBtn');
      const input = document.getElementById('userInput');
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

      if (!SpeechRecognition) {
        alert("Voice input is not supported by your browser.");
        return;
      }

      speechRecognitionInstance = new SpeechRecognition();
      speechRecognitionInstance.continuous = false;
      speechRecognitionInstance.interimResults = true;

      speechRecognitionInstance.onstart = () => {
        isListening = true;
        playBeep(520, 'triangle', 0.15);
        micBtn.classList.add('mic-active');
        input.placeholder = "Listening...";
      };

      speechRecognitionInstance.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
          transcript += event.results[i][0].transcript;
        }
        input.value = transcript;
      };

      speechRecognitionInstance.onerror = () => {
        micBtn.classList.remove('mic-active');
        input.placeholder = "Ask Luna anything...";
        isListening = false;
      };

      speechRecognitionInstance.onend = () => {
        micBtn.classList.remove('mic-active');
        input.placeholder = "Ask Luna anything...";
        isListening = false;
        if (input.value.trim() !== '') sendText();
      };

      speechRecognitionInstance.start();
    }

    function showTypingIndicator() {
      const chat = document.getElementById('chat');
      const wrapper = document.createElement('div');
      wrapper.className = `msg-wrapper luna`;
      const div = document.createElement('div');
      div.className = 'msg';
      div.innerHTML = `
        <div class="typing-orb-indicator">
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
        </div>
      `;
      wrapper.appendChild(div);
      chat.appendChild(wrapper);
      chat.scrollTop = chat.scrollHeight;
      return wrapper;
    }

    function speakOutLoud(text) {
      if (isMuted || !('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();

      let cleanText = text.replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{2600}-\u{26FF}]/gu, '').trim();
      if (!cleanText) return;

      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.rate = 1.05;
      utterance.pitch = 1.1;

      const isHindiScript = /[\u0900-\u097F]/.test(cleanText);
      utterance.lang = isHindiScript ? 'hi-IN' : 'en-US';

      window.speechSynthesis.speak(utterance);
    }
  </script>
</body>
</html>
