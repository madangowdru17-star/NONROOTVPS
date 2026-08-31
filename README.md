# NONROOTVPS - Railway.app Edition 🚀

Complete NoRoot Mod Proxy deployment package for Railway.app

## **Quick Start (2 Minutes)**

### Step 1: Create GitHub Repository

```bash
# Create GitHub repo (https://github.com/new)
# Name it: nonrootvps-railway

git clone https://github.com/YOUR_USERNAME/nonrootvps-railway.git
cd nonrootvps-railway
```

### Step 2: Copy This Project

Copy all files from this folder to your GitHub repo:
- `Dockerfile`
- `railway.json`
- `.gitignore`
- `NONROOTVPS/` (folder)
- `README.md`

### Step 3: Push to GitHub

```bash
git add .
git commit -m "Initial NONROOTVPS Railway deployment"
git push origin main
```

### Step 4: Deploy on Railway

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project"
4. Select "GitHub Repo"
5. Choose **nonrootvps-railway**
6. Click "Deploy"

**That's it! Railway auto-deploys in 2-5 minutes** ✨

---

## **Step 5: Configure Environment Variables**

In Railway Dashboard:

1. Click your project
2. Go to **Variables** tab
3. Add these (click "Add Variable"):

```
PORT = 8089
RAILWAY_HOST = 0.0.0.0
TELEGRAM_BOT_TOKEN = your_bot_token_here
TELEGRAM_ADMIN_ID = your_admin_id_here
```

Save and Railway auto-restarts your app.

---

## **Step 6: Access Your Service**

Railway gives you a public URL:

```
https://your-project-name.railway.app
```

Your mitmproxy listens on:
```
your-project-name.railway.app:8089
```

---

## **File Structure**

```
nonrootvps-railway/
├── Dockerfile                 # Container config for Railway
├── railway.json              # Railway deployment settings
├── .gitignore               # Keep secrets safe
├── README.md                # This file
├── NONROOTVPS/
│   ├── main.py              # Railway-ready entry point ✓
│   ├── requirements.txt
│   ├── ifix.config.json
│   ├── common/
│   ├── config/
│   ├── libs/
│   └── __pycache__/
```

---

## **What's Included**

✅ Python 3.11 slim image  
✅ All dependencies pre-configured  
✅ Auto-restart on crashes  
✅ Health checks enabled  
✅ Railway environment variables support  
✅ Persistent database volume  

---

## **Environment Variables Explained**

| Variable | Value | Purpose |
|----------|-------|---------|
| `PORT` | `8089` | Mitmproxy listen port |
| `RAILWAY_HOST` | `0.0.0.0` | Listen on all interfaces |
| `TELEGRAM_BOT_TOKEN` | Your token | Telegram bot auth |
| `TELEGRAM_ADMIN_ID` | Your ID | Admin user ID |
| `DB_PATH` | `/tmp/nonrootvps` | Database storage location |

---

## **Monitoring Your App**

### View Live Logs
```bash
railway logs
```

### Restart Service
Go to Railway Dashboard → Click "Restart"

### Check Status
```bash
railway status
```

### SSH Into Container
```bash
railway shell
```

---

## **Database Persistence**

### Option 1: Railway Volume (Recommended for SQLite)

In Railway Dashboard:
1. Go to **Volumes** tab
2. Click "Add Volume"
3. Set mount path: `/tmp/nonrootvps`
4. Set size: `1GB`

Your SQLite database will persist across restarts.

### Option 2: PostgreSQL (Production)

1. In Railway, click "Add Service"
2. Select **PostgreSQL**
3. Railway auto-creates `DATABASE_URL`
4. Modify `main.py` to use PostgreSQL

---

## **Customization**

### Change Mitmproxy Port
Edit `NONROOTVPS/main.py` line 94:
```python
'--set', 'listen_port=8089'  # Change this number
```

### Modify Game Mods
Edit `NONROOTVPS/ifix.config.json`:
```json
{
  "game_mod_features": {
    "auto_aim_assist_packet": {
      "enabled": true,
      "prediction_rate": "99.8%"
    }
  }
}
```

### Add Telegram Bot
Edit environment variables in Railway:
```
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklmnoPQRstuvWXYZ
TELEGRAM_ADMIN_ID=987654321
```

---

## **Troubleshooting**

### Build Fails: "mitmproxy not found"
✓ Already fixed in Dockerfile (installs `mitmproxy>=11.0.0`)

### App Crashes
Check Railway logs:
- Railway Dashboard → Logs tab
- Look for error messages
- Click restart if needed

### Port Already in Use
Port 8089 may conflict. Change in both:
1. `railway.json` → Change PORT value
2. `NONROOTVPS/ifix.config.json` → Change listen_port

### Database Not Persisting
Add Railway Volume (see "Database Persistence" above)

### Out of Memory
Upgrade Railway plan or optimize code
- Check current usage in Railway Dashboard → Metrics

---

## **Costs**

- **Free Plan**: $5/month credit (usually enough for testing)
- **Pro Plan**: $20/month (more resources)
- **Usage**: Includes CPU, RAM, bandwidth
- **Volume**: $5/month per 1GB storage

---

## **Auto-Deploy Updates**

Every time you push to GitHub:
```bash
git add .
git commit -m "Update"
git push origin main
```

Railway automatically rebuilds and deploys! 🚀

---

## **Deployment Checklist**

- [ ] GitHub repo created
- [ ] All files pushed to GitHub
- [ ] Railway project created
- [ ] Environment variables set
- [ ] App deployed successfully
- [ ] Can access service on port 8089
- [ ] Database volume added (if using SQLite)
- [ ] No errors in Railway logs

---

## **Support & Help**

- **Railway Docs**: https://docs.railway.app
- **Railway Discord**: https://railway.app/discord
- **GitHub Issues**: Create issue in your repo

---

## **Advanced: Custom Domain**

In Railway Dashboard:
1. Go to **Settings**
2. Click "Domains"
3. Add custom domain (requires DNS setup)

Example:
```
app.yourdomain.com:8089
```

---

**Ready? Push to GitHub and watch Railway deploy!** 🎯

Good luck bro! 💪
