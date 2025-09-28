Coding-Lessons/
├── .devcontainer/
│   ├── Dockerfile
│   ├── check_versions.sh
│   ├── devcontainer.json
│   └── environment.yml
├── .github/
│   └── workflows/
│       └── render.yml
├── content/
│   └── Lesson1/
│       └── website/
│           ├── content/
│           │   └── protected/           # Possibly restricted content (e.g., student-only material)
│           ├── scripts/
│           │   └── flask_server.py      # Flask backend logic
│           ├── templates/
│           │   └── login.html           # HTML templates for Flask (Jinja2)
│           ├── .env                     # Environment variables for Flask or other tools
│           ├── .gitignore               # Git ignore rules for this subproject
│           ├── README.md                # Website-specific documentation
│           ├── _quarto.yml              # Quarto project configuration
│           ├── analysis.qmd             # Analysis notebook/page
│           ├── data.qmd                 # Data description or exploration
│           ├── index.qmd                # Main entry page for Quarto site
│           └── reports.qmd              # Reports generated or included in the site
├── Lesson 1 Plan.md
├── Lesson-One-HW.qmd
├── README.md
└── Setup.txt
