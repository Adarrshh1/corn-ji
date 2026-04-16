"""
CornScan AI · ui/components.py
Reusable HTML/JS components: confidence ring, voice summary button.
"""

import math


def conf_ring(conf: float, color: str) -> str:
    """SVG confidence ring with animated stroke-dashoffset."""
    R = 38
    C = 2 * math.pi * R
    offset = C * (1 - conf)
    return f"""
<div class="ring-wrap">
  <div style="position:relative;width:94px;height:94px;">
    <svg class="ring-svg" width="94" height="94" viewBox="0 0 94 94">
      <circle class="ring-track" cx="47" cy="47" r="{R}"/>
      <circle class="ring-fill" cx="47" cy="47" r="{R}"
        stroke="{color}"
        stroke-dasharray="{C:.2f}"
        stroke-dashoffset="{offset:.2f}"/>
    </svg>
    <div class="ring-label">
      <div class="ring-pct">{conf * 100:.0f}%</div>
      <div class="ring-sub-l">conf</div>
    </div>
  </div>
  <div class="ring-foot">Confidence</div>
</div>"""


def voice_summary_js(text: str) -> str:
    """Inline HTML button that triggers Web Speech API voice playback."""
    safe = text.replace("'", "\\'").replace("\n", " ")
    return f"""
<button class="voice-btn" onclick="
  if(window.speechSynthesis.speaking){{
    window.speechSynthesis.cancel();
    this.textContent='🔊 Voice Summary';
    return;
  }}
  var u = new SpeechSynthesisUtterance('{safe}');
  u.rate = 0.92; u.pitch = 1;
  this.textContent = '⏹ Stop';
  u.onend = () => {{ this.textContent = '🔊 Voice Summary'; }};
  window.speechSynthesis.speak(u);
" id="voice-btn-el">🔊 Voice Summary</button>"""
