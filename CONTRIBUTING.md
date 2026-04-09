# Contributing to SurvivalCalc

Thanks for considering a contribution to SurvivalCalc! 🎉

## Requirements

- Python 3.10+
- Git
- Basic knowledge of Tkinter (for UI changes)

## Getting Started

1. Fork & clone the repository:
   ```bash
   git clone https://git.survivalful.de/survivalful/survivalcalc.git
   cd survivalcalc
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

## Submitting Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/my-feature
   ```

2. Commit your changes:
   ```bash
   git commit -m "feat: short description of the change"
   ```

3. Push your branch and open a **Pull Request** on Gitea.

## Commit Format

We use conventional commits:

| Prefix | Meaning |
|--------|---------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `style:` | Formatting, no logic change |
| `refactor:` | Code restructure without new features |
| `chore:` | Build, dependencies, misc |

## Guidelines

- Code in English, comments in English or German
- No hardcoded paths – use the existing settings logic
- UI changes must work with both themes (Dark & Light)
- Always add new strings to both language files (`de` / `en`)

## Reporting Bugs

Please open an **Issue** on [git.survivalful.de](https://git.survivalful.de) and include:
- SurvivalCalc version
- OS & Python version
- Steps to reproduce
- Expected vs. actual behavior

## Contact

Questions? Reach out at [team@survivalful.de](mailto:team@survivalful.de)
