# Quick Start Guide - Landing Page

## 🚀 Getting Started in 2 Minutes

### Option 1: Simple Web Server (Recommended for Development)

1. **Open Terminal in project directory**
   ```powershell
   # Navigate to your project folder
   cd d:\AI_Resume_Gap_Analyzer
   ```

2. **Start a simple web server**
   ```powershell
   # Python 3.x
   python -m http.server 8000
   ```

3. **Open in browser**
   ```
   http://localhost:8000
   ```

### Option 2: VS Code Live Server (Easiest)

1. **Install Live Server Extension:**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Live Server"
   - Install by Ritwick Dey

2. **Launch:**
   - Right-click `index.html`
   - Select "Open with Live Server"
   - Browser opens automatically

### Option 3: Direct Browser Opening

1. **Navigate to project folder**
2. **Double-click `index.html`**
3. Opens in default browser

---

## 🔗 Running Landing Page + Streamlit App Together

1. **Terminal 1 - Start Landing Page:**
   ```powershell
   cd d:\AI_Resume_Gap_Analyzer
   python -m http.server 8000
   ```

2. **Terminal 2 - Start Streamlit App:**
   ```powershell
   cd d:\AI_Resume_Gap_Analyzer
   streamlit run app.py
   ```

3. **Access both:**
   - Landing Page: `http://localhost:8000`
   - Streamlit App: `http://localhost:8501`

---

## 📋 File Structure

```
d:\AI_Resume_Gap_Analyzer\
├── index.html                 ← LANDING PAGE (start here!)
├── assets/
│   ├── styles.css            ← Page styling
│   └── script.js             ← Page interactions
├── app.py                    ← Streamlit application
├── README.md                 ← Project info
├── LANDING_PAGE.md           ← Detailed documentation
├── requirements.txt          ← Python dependencies
└── QUICK_START.md           ← This file!
```

---

## ✨ Features

### Landing Page Includes:
✅ Professional design  
✅ Responsive (mobile, tablet, desktop)  
✅ 6 animated feature cards  
✅ How-it-works section  
✅ Benefits showcase  
✅ Call-to-action buttons  
✅ Footer with social links  
✅ Demo modal  
✅ Smooth animations  
✅ Fully customizable  

---

## 🎨 Customization Quick Tips

### Change Colors
Edit `assets/styles.css` (top of file):
```css
:root {
    --primary-color: #6366f1;    /* Change this */
    --secondary-color: #ec4899;  /* Or this */
    --accent-color: #f59e0b;     /* Or this */
}
```

### Update Content
Edit `index.html`:
- Line 45: Change "Get Started" button text
- Line 60: Update hero headline
- Line 70: Update hero subtitle
- Line 160+: Edit feature cards
- Line 220+: Edit how-it-works steps

### Link to Your Streamlit App
Edit `assets/script.js` (line ~10):
```javascript
function launchApp() {
    window.location.href = 'http://localhost:8501'; // Change this URL
}
```

---

## 🐛 Troubleshooting

**Issue:** Pages shows "Cannot GET /"
- **Solution:** Make sure you're opening the right port (8000 for landing, 8501 for Streamlit)

**Issue:** Streamlit app not loading
- **Solution:** Run `pip install -r requirements.txt` first
- Then: `streamlit run app.py`

**Issue:** Styling not loading
- **Solution:** Clear browser cache (Ctrl+Shift+Delete) and refresh

**Issue:** Links don't work
- **Solution:** Make sure file paths in HTML match your folder structure

---

## 📚 Documentation

- **Detailed Guide:** See `LANDING_PAGE.md`
- **Project Info:** See `README.md`
- **Dependencies:** See `requirements.txt`

---

## 🎯 Next Steps

1. ✅ Open landing page in browser
2. ✅ Click "Launch App" to test Streamlit integration
3. ✅ Customize colors and content to match your brand
4. ✅ Deploy to your hosting platform

---

## 🚀 Deployment Checklist

- [ ] Update Streamlit app URL in `script.js`
- [ ] Customize colors in `styles.css`
- [ ] Update content/copy in `index.html`
- [ ] Add your logo/images
- [ ] Test all links work
- [ ] Check responsive design on mobile
- [ ] Deploy landing page
- [ ] Deploy Streamlit app
- [ ] Update DNS/domain settings
- [ ] Share with users!

---

**Ready to launch? Open `index.html` now! 🚀**
