import re
import os
import subprocess

def run_git(commit_msg):
    subprocess.run(["git", "add", "."], check=False)
    subprocess.run(["git", "commit", "-m", commit_msg], check=False)
    subprocess.run(["git", "push"], check=False)

def main():
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Step 3: Banner
    os.makedirs("assets", exist_ok=True)
    svg_banner = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ff7eb3;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff758c;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)" rx="15" ry="15" />
  <text x="50%" y="45%" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">Awesome-AI-Dating</text>
  <text x="50%" y="65%" font-family="Arial, sans-serif" font-size="20" fill="white" text-anchor="middle" dominant-baseline="middle">Top AI Dating &amp; Companion Apps</text>
  <circle cx="10%" cy="50%" r="20" fill="rgba(255,255,255,0.2)">
    <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="90%" cy="50%" r="20" fill="rgba(255,255,255,0.2)">
    <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" begin="1s"/>
  </circle>
</svg>'''
    with open("assets/banner.svg", "w", encoding="utf-8") as f:
        f.write(svg_banner)
    
    if "![Banner]" not in content:
        content = re.sub(r'# Awesome-AI-Dating', '# Awesome-AI-Dating\n\n![Banner](assets/banner.svg)', content)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        run_git("added banner")

    # Step 4: Emojis
    if '## Top AI Dating' in content and '## 💘 Top AI Dating' not in content:
        content = content.replace('## Top AI Dating', '## 💘 Top AI Dating')
        content = content.replace('## Table of Contents', '## 📋 Table of Contents')
        content = content.replace('## Introduction', '## 📖 Introduction')
        content = content.replace('## Proprietary / Hosted Platforms', '## 🏢 Proprietary / Hosted Platforms')
        content = content.replace('## Open-Source & Self-Hosted Alternatives', '## 🔓 Open-Source & Self-Hosted Alternatives')
        content = content.replace('## Comparison Table', '## 📊 Comparison Table')
        content = content.replace('## Getting Started with Open-Source', '## 🚀 Getting Started with Open-Source')
        content = content.replace('## Key Considerations', '## ⚖️ Key Considerations')
        content = content.replace('## Resources & Communities', '## 🌐 Resources & Communities')
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        run_git("added emojis")

    # Step 5: SEO
    if 'Keywords:' not in content:
        seo_text = "\\n<div align=\"center\">\\n  <p><strong>Keywords:</strong> AI Dating, AI Girlfriend, AI Boyfriend, Uncensored AI, NSFW AI Chat, Roleplay AI, Open Source AI Companions, Self-hosted AI Dating, Chatbots, Character AI Alternatives.</p>\\n</div>\\n"
        content = content.replace('## 📖 Introduction', seo_text + '\\n## 📖 Introduction')
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        run_git("seo optimised")

    # Step 6: Left Badges
    if 'alt="Discord"' not in content:
        left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
        content = content.replace('![Banner](assets/banner.svg)', f'![Banner](assets/banner.svg)\\n\\n<div align="center">\\n{left_badges}\\n</div>')
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        run_git("badges to left added")

    # Step 7: Right Badges
    if 'alt="GitHub followers"' not in content:
        right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
        content = content.replace('</div>', f'{right_badge}\\n</div>', 1)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        run_git("badges to right added")

    # Step 8: Star History
    if 'Star History Chart' not in content:
        star_history = """
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-AI-Dating&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-AI-Dating&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-AI-Dating&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-AI-Dating&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
        content += star_history
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        run_git("star history added")

    # Step 9: Fix chartrepos -> chart?repos
    if 'chartrepos' in content:
        content = content.replace('chartrepos', 'chart?repos')
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        run_git("fixed star plot")

    # Step 10: Replace awesome link
    if 'https://github.com/sindresorhus/awesome' in content:
        content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        run_git("invalid awesome link fixed")

if __name__ == "__main__":
    main()
