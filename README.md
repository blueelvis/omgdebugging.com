# OMG Debugging

A personal blog about technology, coding, finance and life — built with [Hugo](https://gohugo.io/).

## Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) v0.147 or later

## Quick start

```bash
# Start the dev server with live reload
hugo server

# Build the static site into public/
hugo build
```

The dev server runs at `http://localhost:1313` by default.

## Project structure

```
├── hugo.toml                 # Site configuration
├── content/
│   ├── technology/           # Technology section posts
│   ├── coding/               # Coding section posts
│   ├── finance/              # Finance section posts
│   ├── life/                 # Life section posts
│   ├── about-me.md           # Standalone pages (rendered at /about-me/)
│   ├── contact.md
│   └── ...
├── layouts/
│   ├── _default/
│   │   ├── baseof.html       # Base template (head, body wrapper)
│   │   ├── list.html         # Section listing pages
│   │   └── single.html       # Individual post pages
│   ├── partials/
│   │   ├── header.html       # Site header with navigation
│   │   └── footer.html       # Site footer
│   ├── shortcodes/
│   │   ├── tweet.html        # Embedded tweets
│   │   └── mermaid.html      # Mermaid diagrams
│   ├── taxonomy/             # Tag list and tag term templates
│   ├── page/                 # Standalone page template
│   └── index.html            # Homepage
├── assets/
│   ├── css/main.css          # All styles (light + dark theme)
│   └── js/main.js            # Theme toggle, mobile nav, ToC tracking
├── static/
│   └── images/               # Static images
├── archetypes/
│   └── default.md            # Template for new posts
├── scripts/
│   └── ghost_to_hugo.py      # Ghost-to-Hugo import script (reference)
└── MEDIA_REPORT.md           # List of images needing manual placement
```

## Adding a new post

### 1. Create the file

Use Hugo's built-in scaffolding:

```bash
hugo new content technology/my-new-post.md
```

Replace `technology` with the target section (`coding`, `finance`, or `life`).

This creates a file from the archetype with pre-filled front matter.

### 2. Edit the front matter

Every post starts with YAML front matter between `---` markers:

```yaml
---
title: "My New Post Title"
date: 2026-05-16T12:00:00+00:00
draft: false
description: "Optional short summary for meta tags"
tags: ["Azure", "Docker", "DevOps"]
feature_image: "/images/2026/05/hero.png"
---
```

| Field           | Required | Description                                    |
|-----------------|----------|------------------------------------------------|
| `title`         | Yes      | Post title                                     |
| `date`          | Yes      | Publish date in ISO 8601 format                |
| `draft`         | No       | Set to `true` to hide from production builds   |
| `description`   | No       | Short excerpt for SEO meta tags                |
| `tags`          | No       | List of tags (appear on the post and tags page) |
| `feature_image` | No       | Hero image path (relative to `static/`)        |
| `lastmod`       | No       | Last modified date                             |

### 3. Write content

Write standard Markdown below the front matter. Hugo supports:

- **Headings** (`##`, `###`, `####`) — these auto-populate the Table of Contents sidebar
- **Fenced code blocks** with syntax highlighting:

  ````markdown
  ```python
  def hello():
      print("Hello, World!")
  ```
  ````

- **Images**: `![Alt text](/images/2026/05/screenshot.png)`
- **Links**, **bold**, *italic*, lists, tables, blockquotes — all standard Markdown

### 4. Set `draft: false` and rebuild

Remove `draft: true` (or set it to `false`) when the post is ready. Draft posts are only visible with `hugo server --buildDrafts`.

## Adding media (images)

Place images in `static/` and reference them with absolute paths from the site root:

```
static/
└── images/
    └── 2026/
        └── 05/
            └── screenshot.png
```

Reference in Markdown as:

```markdown
![Description](/images/2026/05/screenshot.png)
```

For the feature (hero) image, set it in front matter:

```yaml
feature_image: "/images/2026/05/hero.png"
```

### Migrated Ghost images

The Ghost export references images from the old hosting. `MEDIA_REPORT.md` lists all 86 references. To restore them:

1. Locate the image in your Ghost site backup (usually under `content/images/`)
2. Place it in `static/content/images/` preserving the original path
3. For example, Ghost path `/content/images/2024/02/screenshot.png` → `static/content/images/2024/02/screenshot.png`

## Embedding tweets

Use the `tweet` shortcode with a tweet ID:

```markdown
{{</* tweet 1234567890 */>}}
```

The tweet ID is the numeric part at the end of a tweet URL (e.g., `https://twitter.com/user/status/1234567890`).

## Mermaid diagrams

Wrap Mermaid syntax in the `mermaid` shortcode:

```markdown
{{</* mermaid */>}}
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action]
    B -->|No| D[End]
{{</* /mermaid */>}}
```

Mermaid JS is loaded only on pages that use the shortcode.

## Adding a standalone page

Create a Markdown file directly in `content/` (not inside a section folder):

```bash
hugo new content my-page.md
```

Add `type: "page"` and `layout: "single"` to the front matter:

```yaml
---
title: "My Page"
date: 2026-05-16T12:00:00+00:00
type: "page"
layout: "single"
---
```

Pages use a simpler template without the ToC sidebar or post navigation.

## Theme (day/night mode)

The site supports light and dark modes:

- Users toggle via the sun/moon button in the header
- Preference is saved in `localStorage` and persists across visits
- Falls back to the OS preference (`prefers-color-scheme`) on first visit

Theme colors are defined as CSS custom properties in `assets/css/main.css` under `:root` (light) and `[data-theme="dark"]` (dark). Edit these to change the color scheme.

## Tags

Tags are defined in post front matter and automatically generate:

- A tag cloud page at `/tags/`
- Individual tag pages at `/tags/<tag-name>/` listing all posts with that tag

## Configuration

All site settings live in `hugo.toml`. Key settings:

| Setting | Description |
|---------|-------------|
| `baseURL` | Production URL |
| `title` | Site name shown in header and meta |
| `params.description` | Site tagline |
| `params.mainSections` | Sections shown on the homepage |
| `params.dateFormat` | Go date format for displayed dates |
| `pagination.pagerSize` | Posts per page on list pages |
| `menu.main` | Navigation links in the header |

## Building for production

```bash
hugo build
```

Output goes to `public/`. Deploy the contents of `public/` to any static hosting service (Cloudflare Pages, Netlify, Vercel, GitHub Pages, S3, etc.).
