import streamlit as st
import cv2
import time
import pythoncom
from handgesture import GestureController

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Milestone 2: Gesture Recognition & Volume Control",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>
.title {
    background-color:#263238;
    color:white;
    text-align:center;
    padding:15px;
    font-size:26px;
    font-weight:bold;
}
.panel {
    padding:15px;
    border-radius:10px;
}
.left { background:#e0f7fa; }
.center { background:black; }
.right { background:#fce4ec; }
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown(
    '<div class="title">MILESTONE 2</div>',
    unsafe_allow_html=True
)

# ================= SESSION STATE =================
if "run" not in st.session_state:
    st.session_state.run = False
if "fps" not in st.session_state:
    st.session_state.fps = 0
if "volume" not in st.session_state:
    st.session_state.volume = 0
if "latency" not in st.session_state:
    st.session_state.latency = 0

# ================= LAYOUT =================
left, center, right = st.columns([1.3, 3.5, 1.5])

# ================= LEFT PANEL =================
with left:
    st.markdown('<div class="panel left">', unsafe_allow_html=True)
    st.subheader("Status")

    cam_status = st.empty()
    hand_status = st.empty()
    gesture_status = st.empty()
    vol_status = st.empty()
    latency_status = st.empty()
    fps_status = st.empty()

    st.markdown("### Volume Level")
    vol_bar = st.progress(0)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= CENTER PANEL =================
with center:
    st.markdown('<div class="panel center">', unsafe_allow_html=True)
    video_placeholder = st.empty()
    st.markdown('</div>', unsafe_allow_html=True)

# ================= RIGHT PANEL =================
with right:
    st.markdown('<div class="panel right">', unsafe_allow_html=True)
    st.subheader("Controls")

    det_conf = st.slider("Detection Confidence", 0.5, 1.0, 0.8)
    trk_conf = st.slider("Tracking Confidence", 0.5, 1.0, 0.8)
    max_hands = st.slider("Max Hands", 1, 2, 1)

    c1, c2 = st.columns(2)
    start = c1.button("Start Camera")
    stop = c2.button("Stop Camera")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= BUTTON ACTIONS =================
if start:
    st.session_state.run = True
if stop:
    st.session_state.run = False

# ================= CAMERA LOOP =================
if st.session_state.run:
    pythoncom.CoInitialize()
    cap = cv2.VideoCapture(0)
    controller = GestureController(det_conf, trk_conf, max_hands)
    prev_time = 0

    while st.session_state.run:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_start = time.time()

        frame, distance, gesture, volume, hands = controller.process_frame(frame)

        st.session_state.latency = int(
            (time.time() - frame_start) * 1000
        )

        if volume is not None:
            st.session_state.volume = volume

        curr_time = time.time()
        st.session_state.fps = int(1 / (curr_time - prev_time + 0.0001))
        prev_time = curr_time

        cam_status.markdown("📷 Camera: **Active**")
        hand_status.markdown(f"✋ Hands Detected: **{hands}**")
        gesture_status.markdown(f"🖐 Gesture: **{gesture}**")

        if gesture == "Closed":
            vol_status.markdown("🔇 **Muted (Closed Gesture)**")
        else:
            vol_status.markdown(f"🔊 Volume: **{st.session_state.volume}%**")

        latency_status.markdown(
            f"⏱ Latency: **{st.session_state.latency} ms**"
        )
        fps_status.markdown(f"⚡ FPS: **{st.session_state.fps}**")

        vol_bar.progress(min(st.session_state.volume, 100) / 100)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(frame, use_container_width=True)

    cap.release()
    cam_status.markdown("📷 Camera: **Stopped**")
