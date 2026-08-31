# NONROOTVPS - Railway ಲೋಂಚ್ ಗೈಡ್ 🚀

## **ತ್ವರಿತ ಸ್ಟಾರ್ಟ (2 ನಿಮಿಷ)**

### ಹಂತ 1: GitHub ರಿಪೋಜಿಟರಿ ರಚನೆ

```
https://github.com/new ಗೆ ಹೋಗಿ
Repository name: nonrootvps-railway
"Create repository" ಕ್ಲಿಕ್ ಮಾಡಿ
```

### ಹಂತ 2: ಫೈಲುಗಳನ್ನು ಪುಶ್ ಮಾಡಿ

```bash
git clone https://github.com/YOUR_USERNAME/nonrootvps-railway.git
cd nonrootvps-railway

# ಸಮಸ್ತ ಫೈಲುಗಳನ್ನು ಜೊತೆ ಆ ಫೋಲ್ಡರಿಗೆ ನಕಲಿ ಮಾಡಿ
# Dockerfile, railway.json, NONROOTVPS/, README.md, ಇತ್ಯಾದಿ

git add .
git commit -m "Initial NONROOTVPS Railway deployment"
git push origin main
```

### ಹಂತ 3: Railway ನಲ್ಲಿ ಡಿಪ್ಲಾಯ್ ಮಾಡಿ

1. https://railway.app ಗೆ ಹೋಗಿ
2. GitHub ನೊಂದಿಗೆ ಸೈನ್ ಅಪ್ ಮಾಡಿ
3. "New Project" ಕ್ಲಿಕ್ ಮಾಡಿ
4. "GitHub Repo" ಆಯ್ಕೆ ಮಾಡಿ
5. **nonrootvps-railway** ಆಯ್ಕೆ ಮಾಡಿ
6. "Deploy" ಕ್ಲಿಕ್ ಮಾಡಿ

**ಇದು ಅಷ್ಟೇ! Railway ಸ್ವಯಂಚಾಲಿತವಾಗಿ 2-5 ನಿಮಿಷಗಳಲ್ಲಿ ಡಿಪ್ಲಾಯ್ ಮಾಡುತ್ತದೆ** ✨

---

## **ಹಂತ 4: ಕಾನ್ಫಿಗರೇಶನ ಸೆಟ್ ಮಾಡಿ**

Railway ಡ್ಯಾಶ್ಬೋರ್ಡ್ ನಲ್ಲಿ:

1. **Variables** ಟ್ಯಾಬ್ ಗೆ ಹೋಗಿ
2. ಈ ಮೌಲ್ಯಗಳನ್ನು ಸೇರಿಸಿ:

```
PORT = 8089
RAILWAY_HOST = 0.0.0.0
TELEGRAM_BOT_TOKEN = ನಿಮ್ಮ_ಟೋಕನ್
TELEGRAM_ADMIN_ID = ನಿಮ್ಮ_ಐಡಿ
```

---

## **ಹಂತ 5: ಸೇವೆ ಪ್ರವೇಶಿಸಿ**

ನಿಮ್ಮ ಸೇವೆ ಈ ಠಿಕಾಣದಲ್ಲಿ ಲೈವ್ ಆಗಿರುತ್ತದೆ:

```
https://your-project-name.railway.app:8089
```

---

## **ಫೈಲ್ ರಚನೆ**

```
nonrootvps-railway/
├── Dockerfile              # Railway ಸಂರಚನೆ
├── railway.json           # ನಿಯೋಜನೆ ಸೆಟ್ಟಿಂಗ್
├── .gitignore            # ರಹಸ್ಯಗಳನ್ನು ಸುರಕ್ಷಿತ ರಾಖಿ
├── README.md             # ಸಂಪೂರ್ಣ ಗೈಡ್
├── DEPLOY.sh             # ಕ್ವಿಕ್ ಡಿಪ್ಲಾಯ್ ಸ್ಕ್ರಿಪ್ಟ್
└── NONROOTVPS/
    ├── main.py           # ಮುಖ್ಯ ಪ್ರವೇಶ ಬಿಂದು
    ├── ifix.config.json  # ಮಾಡ್ ಸಂರಚನೆ
    ├── common/
    ├── config/
    ├── libs/
    └── requirements.txt
```

---

## **ಪರಿಸರ ಲೂಪುಗಳು (Environment Variables)**

| ವೇರಿಯಬಲ್ | ಮೌಲ್ಯ | ಉದ್ದೇಶ |
|----------|--------|--------|
| `PORT` | `8089` | Mitmproxy ಪೋರ್ಟ್ |
| `RAILWAY_HOST` | `0.0.0.0` | ಎಲ್ಲಾ ಇಂಟರ್ಫೇಸ್ ಕೇಳಿ |
| `TELEGRAM_BOT_TOKEN` | ನಿಮ್ಮ ಟೋಕನ್ | ಟೆಲಿಗ್ರಾಮ್ ಬಾಟ್ |
| `TELEGRAM_ADMIN_ID` | ನಿಮ್ಮ ಐಡಿ | ಆಡ್ಮಿನ್ ಐಡಿ |

---

## **ತ್ರುಟಿ ನಿವಾರಣೆ**

### ನಿರ್ಮಾಣ ವಿಫಲವಾಗಿದೆ?
Railway ಲಾಗ್ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ:
- Dashboard → Logs tab

### ಅ್ಯಾಪ್ ಕ್ರ್ಯಾಶ್ ಆಗುತ್ತದೆ?
- Dashboard ನಲ್ಲಿ "Restart" ಕ್ಲಿಕ್ ಮಾಡಿ
- ತ್ರುಟಿ ಸಂದೇಶಗಳನ್ನು ಪರಿಶೀಲಿಸಿ

### ಡೇಟಾಬೇಸ್ ಪುನರಾವರ್ತಿತವಾಗಿಲ್ಲ?
- Railway Volume ಸೇರಿಸಿ (ಮಾದರಿ ಗೈಡ್ ನಲ್ಲಿ)

---

## **ಅ್ಯಾಪ್ ಅನುಸರಣೆ ಮಾಡಿ**

### ಲೈವ್ ಲಾಗ್ಸ್ ನೋಡಿ

```bash
railway logs
```

### ಸೇವೆಯನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ

Dashboard → "Restart" ಕ್ಲಿಕ್ ಮಾಡಿ

### ಕಂಟೇನರ್ ಗೆ ಆದ್ಯತೆ ನೀಡಿ

```bash
railway shell
```

---

## **ಸ್ವಯಂ-ನಿಯೋಜನೆ ಅಪ್ಡೇಟ್

GitHub ಗೆ ಪ್ರತಿ ಪ್ರಸ್ತುತಿ:

```bash
git add .
git commit -m "Update"
git push origin main
```

Railway ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಮರುನಿರ್ಮಾಣ ಮತ್ತು ನಿಯೋಜನೆ ಮಾಡುತ್ತದೆ! 🚀

---

## **ವೆಲಾಪನೆ ತಿರುಳಿ**

- **ಉಚಿತ ಯೋಜನೆ**: ಪ್ರತಿ ಮಾಸಕ್ಕೆ $5 ಕ್ರೆಡಿಟ್
- **ಪ್ರೋ ಯೋಜನೆ**: ಪ್ರತಿ ಮಾಸಕ್ಕೆ $20
- **ಸಂಗ್ರಹಣೆ**: ಪ್ರತಿ 1GB ಕ್ಕೆ ಪ್ರತಿ ಮಾಸಕ್ಕೆ $5

---

## **ಚೆಕ್ಲಿಸ್ಟ್**

- [ ] GitHub ರಿಪೋಜಿಟರಿ ರಚನೆ ಮಾಡಲಾಯಿತು
- [ ] ಸಮಸ್ತ ಫೈಲುಗಳನ್ನು ಪುಶ್ ಮಾಡಲಾಯಿತು
- [ ] Railway ಪರಿಕಲ್ಪನೆ ರಚನೆ ಮಾಡಲಾಯಿತು
- [ ] ಪರಿಸರ ಲೂಪುಗಳನ್ನು ಸೆಟ್ ಮಾಡಲಾಯಿತು
- [ ] ಅ್ಯಾಪ್ ನಿಯೋಜಿತವಾಗಿದೆ
- [ ] ಸೇವೆಯನ್ನು ಪ್ರವೇಶಿಸಬಹುದು

---

**GitHub ಗೆ ಪ್ರಸ್ತುತಿ ಮಾಡಿ ಮತ್ತು Railway ಡಿಪ್ಲಾಯ್ ನೋಡಿ!** 🎯

ಶುಭೋಪದೇಶಗಳು ಭಾಯ್ಯ! 💪
