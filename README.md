<style>
  * {
    margin: 0;
    padding: 0;
  }
  
  @keyframes gradient-shift {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }
  
  @keyframes slide-in {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @keyframes pulse-glow {
    0%, 100% {
      box-shadow: 0 0 10px rgba(102, 126, 234, 0.5);
    }
    50% {
      box-shadow: 0 0 30px rgba(102, 126, 234, 0.8);
    }
  }
  
  @keyframes float {
    0%, 100% {
      transform: translateY(0px);
    }
    50% {
      transform: translateY(-10px);
    }
  }
  
  @keyframes shimmer {
    0% {
      background-position: -1000px 0;
    }
    100% {
      background-position: 1000px 0;
    }
  }
  
  @keyframes bounce-in {
    0% {
      opacity: 0;
      transform: scale(0.8) rotateY(90deg);
    }
    100% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }
  }
  
  @keyframes neon-glow {
    0%, 100% {
      text-shadow: 0 0 10px #667eea, 0 0 20px #764ba2;
    }
    50% {
      text-shadow: 0 0 20px #667eea, 0 0 30px #764ba2, 0 0 40px #667eea;
    }
  }
  
  @keyframes spin-slow {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  
  @keyframes fade-in-up {
    from {
      opacity: 0;
      transform: translateY(50px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @keyframes wave {
    0%, 100% {
      transform: translateY(0px);
    }
    25% {
      transform: translateY(-10px);
    }
    75% {
      transform: translateY(10px);
    }
  }
  
  .animated-heading {
    animation: neon-glow 3s infinite;
    font-weight: bold;
    color: #667eea;
  }
  
  .gradient-text {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #667eea 100%);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradient-shift 4s ease infinite;
  }
  
  .card-animated {
    animation: slide-in 0.6s ease-out;
    animation-fill-mode: both;
  }
  
  .card-1 { animation-delay: 0.1s; }
  .card-2 { animation-delay: 0.2s; }
  .card-3 { animation-delay: 0.3s; }
  .card-4 { animation-delay: 0.4s; }
  
  .tech-badge {
    display: inline-block;
    animation: float 3s ease-in-out infinite;
  }
  
  .tech-badge:nth-child(2) { animation-delay: 0.2s; }
  .tech-badge:nth-child(3) { animation-delay: 0.4s; }
  .tech-badge:nth-child(4) { animation-delay: 0.6s; }
  .tech-badge:nth-child(5) { animation-delay: 0.8s; }
  
  .stat-box {
    animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    padding: 15px 20px;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    border-left: 4px solid #667eea;
    border-radius: 5px;
    margin: 10px 0;
  }
  
  .pulse-dot {
    display: inline-block;
    height: 12px;
    width: 12px;
    background-color: #667eea;
    border-radius: 50%;
    animation: pulse-glow 2s infinite;
    margin-right: 8px;
  }
  
  .footer-box {
    animation: pulse-glow 3s ease-in-out infinite;
    padding: 30px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    color: white;
    margin-top: 40px;
  }
  
  .highlight-section {
    border-radius: 10px;
    padding: 20px;
    margin: 15px auto;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15));
    border-left: 5px solid #667eea;
    animation: slide-in 0.8s ease-out;
    transition: all 0.3s ease;
  }
  
  .highlight-section:hover {
    transform: translateX(5px);
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.3);
  }
  
  table {
    animation: fade-in-up 1s ease-out;
  }
  
  .stagger-1 { animation-delay: 0s; }
  .stagger-2 { animation-delay: 0.2s; }
  .stagger-3 { animation-delay: 0.4s; }
  .stagger-4 { animation-delay: 0.6s; }
  .stagger-5 { animation-delay: 0.8s; }
</style>

<div align="center">
  <div style="margin-bottom: 30px; animation: fade-in-up 1s ease-out;">
    <img src="https://readme-typing-svg.herokuapp.com?font=Righteous&size=40&duration=3000&pause=1000&color=667EEA&center=true&vCenter=true&width=600&height=80&lines=Hi+There+👋;I'm+Aditya+Deore;Full-Stack+Developer;Building+Scalable+Apps;Passionate+Developer" alt="Typing SVG" />
  </div>
</div>

<div align="center" style="animation: fade-in-up 1.2s ease-out;">
  <p style="font-size: 17px; color: #666; margin: 30px 0; font-weight: 500;">
    <span class="pulse-dot"></span>Welcome to my GitHub! I'm passionate about building scalable applications and solving real-world problems through code.
  </p>
</div>

---

<div align="center" style="animation: fade-in-up 1.4s ease-out;">
  <h1 class="gradient-text" style="font-size: 28px; margin-bottom: 30px;">⚡ What Makes Me Tick ⚡</h1>
  
  <table style="margin: 0 auto; width: 100%; max-width: 800px;">
    <tr>
      <td width="50%">
        <div class="highlight-section card-animated card-1">
          <h3 style="color: #667eea; margin-bottom: 15px; animation: neon-glow 2s infinite;">💻 What I Do</h3>
          <ul style="list-style: none; line-height: 2; animation: fade-in-up 1.5s ease-out;">
            <li style="animation: fade-in-up 1.5s ease-out; animation-delay: 0.1s; opacity: 0; animation-fill-mode: forwards;">✨ Build full-stack applications</li>
            <li style="animation: fade-in-up 1.5s ease-out; animation-delay: 0.2s; opacity: 0; animation-fill-mode: forwards;">🔧 Create scalable backend systems</li>
            <li style="animation: fade-in-up 1.5s ease-out; animation-delay: 0.3s; opacity: 0; animation-fill-mode: forwards;">🎨 Design beautiful user interfaces</li>
            <li style="animation: fade-in-up 1.5s ease-out; animation-delay: 0.4s; opacity: 0; animation-fill-mode: forwards;">🚀 Ship production-ready code</li>
          </ul>
        </div>
      </td>
      <td width="50%">
        <div class="highlight-section card-animated card-2">
          <h3 style="color: #764ba2; margin-bottom: 15px; animation: neon-glow 2s infinite; animation-delay: 0.5s;">📚 What I Know</h3>
          <ul style="list-style: none; line-height: 2; animation: fade-in-up 1.5s ease-out; animation-delay: 0.5s;">
            <li style="animation: fade-in-up 1.5s ease-out; animation-delay: 0.6s; opacity: 0; animation-fill-mode: forwards;">🎓 B.Tech IT (PCCOE, Pune)</li>
            <li style="animation: fade-in-up 1.5s ease-out; animation-delay: 0.7s; opacity: 0; animation-fill-mode: forwards;">👥 Led teams at Wipro DICE</li>
            <li style="animation: fade-in-up 1.5s ease-out; animation-delay: 0.8s; opacity: 0; animation-fill-mode: forwards;">🌟 Hackathon organizer & contributor</li>
            <li style="animation: fade-in-up 1.5s ease-out; animation-delay: 0.9s; opacity: 0; animation-fill-mode: forwards;">💡 System design & architecture</li>
          </ul>
        </div>
      </td>
    </tr>
  </table>
</div>

---

<h2 align="center" class="animated-heading" style="animation: neon-glow 3s infinite;">🛠️ My Tech Arsenal 🛠️</h2>

<div align="center" style="animation: fade-in-up 1.6s ease-out;">
  
  <h3 style="color: #667eea; margin: 25px 0 15px 0; font-size: 18px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);">💬 Languages</h3>
  <div style="margin-bottom: 20px; animation: fade-in-up 1.8s ease-out;">
    <span class="tech-badge" style="animation-delay: 0s;">![JavaScript](https://img.shields.io/badge/JavaScript-%23F7DF1E.svg?style=flat-square&logo=javascript&logoColor=black)</span>
    <span class="tech-badge" style="animation-delay: 0.1s;">![TypeScript](https://img.shields.io/badge/TypeScript-%23007ACC.svg?style=flat-square&logo=typescript&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 0.2s;">![Python](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)</span>
    <span class="tech-badge" style="animation-delay: 0.3s;">![Java](https://img.shields.io/badge/Java-%23ED8B00.svg?style=flat-square&logo=openjdk&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 0.4s;">![C](https://img.shields.io/badge/C-%2300599C.svg?style=flat-square&logo=c&logoColor=white)</span>
  </div>
  
  <h3 style="color: #667eea; margin: 25px 0 15px 0; font-size: 18px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); animation-delay: 0.1s;">🎨 Frontend</h3>
  <div style="margin-bottom: 20px; animation: fade-in-up 1.8s ease-out; animation-delay: 0.2s;">
    <span class="tech-badge" style="animation-delay: 0.5s;">![React](https://img.shields.io/badge/React-%2361DAFB.svg?style=flat-square&logo=react&logoColor=black)</span>
    <span class="tech-badge" style="animation-delay: 0.6s;">![Next.js](https://img.shields.io/badge/Next.js-%23000000.svg?style=flat-square&logo=next.js&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 0.7s;">![Tailwind](https://img.shields.io/badge/Tailwind%20CSS-%2338B2AC.svg?style=flat-square&logo=tailwind-css&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 0.8s;">![HTML5](https://img.shields.io/badge/HTML5-%23E34C26.svg?style=flat-square&logo=html5&logoColor=white)</span>
  </div>
  
  <h3 style="color: #667eea; margin: 25px 0 15px 0; font-size: 18px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); animation-delay: 0.2s;">⚙️ Backend</h3>
  <div style="margin-bottom: 20px; animation: fade-in-up 1.8s ease-out; animation-delay: 0.4s;">
    <span class="tech-badge" style="animation-delay: 0.9s;">![Node.js](https://img.shields.io/badge/Node.js-6DA55F?style=flat-square&logo=node.js&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 1s;">![Express](https://img.shields.io/badge/Express.js-%23000000.svg?style=flat-square&logo=express&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 1.1s;">![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=flat-square&logo=mongodb&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 1.2s;">![MySQL](https://img.shields.io/badge/MySQL-4479A1.svg?style=flat-square&logo=mysql&logoColor=white)</span>
  </div>
  
  <h3 style="color: #667eea; margin: 25px 0 15px 0; font-size: 18px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); animation-delay: 0.3s;">🤖 AI/ML & Tools</h3>
  <div style="margin-bottom: 20px; animation: fade-in-up 1.8s ease-out; animation-delay: 0.6s;">
    <span class="tech-badge" style="animation-delay: 1.3s;">![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=flat-square&logo=TensorFlow&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 1.4s;">![Git](https://img.shields.io/badge/Git-%23F05033.svg?style=flat-square&logo=git&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 1.5s;">![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)</span>
    <span class="tech-badge" style="animation-delay: 1.6s;">![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat-square&logo=amazon-aws&logoColor=white)</span>
  </div>

</div>

---

<h2 align="center" class="animated-heading" style="animation: neon-glow 3s infinite; animation-delay: 1s;">🔥 Currently Building 🔥</h2>

<div align="center" style="animation: fade-in-up 2s ease-out;">
  <table style="margin: 0 auto; width: 100%; max-width: 900px;">
    <tr>
      <td align="center" style="padding: 20px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); animation-delay: 0s;">
        <div style="font-size: 35px; margin-bottom: 10px; animation: float 3s ease-in-out infinite;">🌐</div>
        <b style="color: #667eea; display: block; animation: fade-in-up 1.8s ease-out; animation-delay: 0.2s;">Full-Stack Apps</b><br>
        <span style="color: #666; font-size: 13px; animation: fade-in-up 1.8s ease-out; animation-delay: 0.3s; display: block;">React + Node.js + MongoDB</span>
      </td>
      <td align="center" style="padding: 20px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); animation-delay: 0.15s;">
        <div style="font-size: 35px; margin-bottom: 10px; animation: float 3s ease-in-out infinite; animation-delay: 0.2s;">💳</div>
        <b style="color: #667eea; display: block; animation: fade-in-up 1.8s ease-out; animation-delay: 0.4s;">Payment Gateway</b><br>
        <span style="color: #666; font-size: 13px; animation: fade-in-up 1.8s ease-out; animation-delay: 0.5s; display: block;">UPI Integration (GPay, PhonePe)</span>
      </td>
      <td align="center" style="padding: 20px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); animation-delay: 0.3s;">
        <div style="font-size: 35px; margin-bottom: 10px; animation: float 3s ease-in-out infinite; animation-delay: 0.4s;">🤖</div>
        <b style="color: #667eea; display: block; animation: fade-in-up 1.8s ease-out; animation-delay: 0.6s;">AI/ML Projects</b><br>
        <span style="color: #666; font-size: 13px; animation: fade-in-up 1.8s ease-out; animation-delay: 0.7s; display: block;">Python & TensorFlow</span>
      </td>
      <td align="center" style="padding: 20px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); animation-delay: 0.45s;">
        <div style="font-size: 35px; margin-bottom: 10px; animation: float 3s ease-in-out infinite; animation-delay: 0.6s;">📱</div>
        <b style="color: #667eea; display: block; animation: fade-in-up 1.8s ease-out; animation-delay: 0.8s;">Web Design</b><br>
        <span style="color: #666; font-size: 13px; animation: fade-in-up 1.8s ease-out; animation-delay: 0.9s; display: block;">Tailwind CSS & Responsive UI</span>
      </td>
    </tr>
  </table>
</div>

---

<h2 align="center" class="animated-heading" style="animation: neon-glow 3s infinite; animation-delay: 2s;">📊 GitHub Analytics 📊</h2>

<div align="center" style="animation: fade-in-up 2.2s ease-out;">
  <img width="48%" src="https://github-readme-stats.vercel.app/api?username=AdityaxDeore&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" />
  <img width="48%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AdityaxDeore&layout=compact&theme=tokyonight&hide_border=true" />
</div>

<div align="center" style="margin-top: 30px; animation: fade-in-up 2.4s ease-out;">
  <img width="100%" src="https://nirzak-streak-stats.vercel.app/?user=AdityaxDeore&theme=tokyonight&hide_border=true" />
</div>

---

<h2 align="center" class="animated-heading" style="animation: neon-glow 3s infinite; animation-delay: 3s;">🏆 Achievements & Trophies 🏆</h2>

<div align="center" style="animation: fade-in-up 2.6s ease-out;">
  <img src="https://github-profile-trophy.vercel.app/?username=AdityaxDeore&theme=tokyonight&no-frame=true&row=1&column=6" />
</div>

---

<h2 align="center" class="gradient-text" style="font-size: 24px; animation: fade-in-up 2.8s ease-out;">🌟 Quick Stats 🌟</h2>

<div align="center" style="animation: fade-in-up 3s ease-out; max-width: 700px; margin: 0 auto;">
  
| 🎯 | Metric | Value |
|:---:|--------|-------|
| 💬 | **Languages** | JavaScript, Python, Java, C, TypeScript |
| 🎯 | **Specialization** | Full-Stack Development |
| 🏢 | **Experience** | Wipro DICE, Multiple Projects |
| 🎓 | **Education** | B.Tech IT, PCCOE Pune |
| 🚀 | **Current Focus** | Scalable Backends & Payment APIs |

</div>

---

<h2 align="center" style="animation: fade-in-up 3.2s ease-out; margin-bottom: 30px;">🤝 Let's Connect & Collaborate</h2>

<div align="center" style="animation: fade-in-up 3.4s ease-out; margin-bottom: 40px;">
  
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aditya-deore-3a725a263/)
  [![GitHub](https://img.shields.io/badge/GitHub-%23181717.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AdityaxDeore)
  [![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aditya@example.com)
  [![Portfolio](https://img.shields.io/badge/Portfolio-%23FF6B6B.svg?style=for-the-badge&logo=firefox&logoColor=white)](https://your-portfolio.com)

</div>

<div class="footer-box" align="center" style="animation: fade-in-up 3.6s ease-out;">
  <h3 style="margin-bottom: 15px; font-size: 24px; animation: neon-glow 3s infinite;">✨ Let's Build Something Amazing Together! ✨</h3>
  <p style="margin: 15px 0; font-size: 16px; font-weight: 500; animation: fade-in-up 3.8s ease-out;">
    <i>Always learning. Always growing. Always coding.</i>
  </p>
  <div style="margin-top: 20px; font-size: 14px; border-top: 2px solid rgba(255,255,255,0.3); padding-top: 20px; animation: fade-in-up 4s ease-out;">
    <p>📊 Open for collaborations • 💼 Full-stack solutions • 🚀 Innovation-driven</p>
    <p style="margin-top: 10px; opacity: 0.9;">Feel free to reach out for projects, collaborations, or just to chat!</p>
  </div>
</div>

<div align="center" style="margin-top: 30px; animation: pulse-glow 3s ease-in-out infinite;">
  <p style="font-size: 12px; color: #999; margin-top: 20px; animation: fade-in-up 4.2s ease-out;">
    ⭐ If you find my work interesting, feel free to star my repositories! ⭐
  </p>
</div>
