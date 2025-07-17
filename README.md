# 🧠 My Python Multi-Project Repo

This repository contains multiple Python projects, each in its own folder.  
Each project may include data encryption, saving JSON files, and other utilities.

---

## 📁 Project Structure

```
your-repo/
├── project1/
│   ├── main.py
│   └── save/            # Folder to store encrypted or JSON data
│       └── .gitkeep     # Keeps the folder tracked by Git
│
├── project2/
│   └── main.py
│
├── requirements.txt     # Dependencies for all projects
└── README.md
```

---

## 🛠 Setup

Install dependencies (once) using:

```bash
pip install -r requirements.txt
```

This installs:

- `cryptography` — used for Fernet encryption/decryption

---

## 🔐 About `.gitkeep`

Git does **not track empty folders** by default.  
We use `.gitkeep` inside each `save/` folder so Git knows to keep them.

You can replace `.gitkeep` with any dummy file if you want — it’s just a naming convention.

---

## 🚀 Running a Project

Example for `project1`:

```bash
cd project1
python main.py
```

Encrypted files will be saved in `project1/save/`.

---

## 📦 Dependencies

All required libraries are listed in `requirements.txt`.  
Make sure to run `pip install -r requirements.txt` before using any project.

---
