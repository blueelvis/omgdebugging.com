## Cursor Cloud specific instructions

This is a **Hugo** static site blog ("OMG Debugging") with sections for Technology, Coding, Finance, and Life.

### Key commands

| Action | Command |
|--------|---------|
| Build | `hugo build` |
| Dev server | `hugo server --bind 0.0.0.0 --port 1313` |

### Important notes

- Hugo extended edition is required (v0.147.x+). The update script installs it automatically.
- Content is organized into sections: `content/technology/`, `content/coding/`, `content/finance/`, `content/life/`. Standalone pages live in `content/` root.
- `hugo.toml` is the config file. `markup.goldmark.renderer.unsafe = true` is enabled because imported Ghost content contains raw HTML.
- Shortcodes available: `{{</* mermaid */>}}` for diagrams, `{{</* tweet <id> */>}}` for embedded tweets.
- Day/night theme toggle is handled by `assets/js/main.js` with CSS custom properties in `assets/css/main.css`.
- The `scripts/ghost_to_hugo.py` converter was used to import posts from a Ghost JSON export. It is kept for reference but not needed for ongoing development.
