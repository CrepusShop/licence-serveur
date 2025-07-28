# Serveur de Licence (Python + Flask)

## 📦 Fichiers
- `server.py` : serveur Flask qui gère les licences
- `licenses.json` : fichier contenant les clés et dates d'expiration
- `requirements.txt` : pour que Render installe Flask automatiquement

## 🚀 Déploiement sur Render.com
1. Crée un dépôt sur [github.com](https://github.com)
2. Ajoute les 3 fichiers (`server.py`, `licenses.json`, `requirements.txt`)
3. Va sur [render.com](https://render.com) > "New Web Service"
4. Connecte ton GitHub > choisis ton dépôt
5. Renseigne :
   - Build Command : `pip install -r requirements.txt`
   - Start Command : `python server.py`
6. Clique sur "Create Web Service"

✅ L’API sera en ligne sur une URL comme : `https://tonprojet.onrender.com/check`

## ✅ Test
POST `/check` avec un body JSON :
```json
{
  "key": "ABC123"
}
```