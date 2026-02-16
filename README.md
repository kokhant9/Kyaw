/* ၁။ တစ်ကိုယ်လုံးအတွက် အခြေခံ ဒီဇိုင်း */
body {
    margin: 0;
    padding: 0;
    font-family: 'Inter', sans-serif;
    background: radial-gradient(circle, #1a1f2b, #0b0e14);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
}

/* ၂။ အလယ်က ကတ်ပြား ဒီဇိုင်း */
.container {
    background: rgba(25, 30, 45, 0.8);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
}

/* ၃။ နာမည်ကို Glow ဖြစ်အောင် လုပ်မယ် */
.name {
    font-size: 2.5rem;
    margin: 0;
    color: #00d2ff;
    text-shadow: 0 0 10px #00d2ff88;
}

/* ၄။ Social Links တွေကို စီမယ် */
.social-links {
    margin: 25px 0;
}

.social-links a img {
    width: 30px;
    margin: 0 10px;
    filter: invert(1); /* Icon တွေကို အဖြူရောင်ပြောင်းတာ */
    transition: 0.3s transform;
}

.social-links a:hover img {
    transform: scale(1.2);
}

/* ၅။ Contact Button လှလှလေး */
.contact-btn {
    text-decoration: none;
    background: #e94560;
    color: white;
    padding: 12px 25px;
    border-radius: 50px;
    font-weight: bold;
    display: inline-block;
    transition: 0.3s;
}

.contact-btn:hover {
    background: #00d2ff;
    box-shadow: 0 0 20px #00d2ff;
}

