## Cursor Cloud specific instructions

This is a **Zola** static site blog ("OMG Debugging"). The only dependency is the Zola binary (v0.17.2).

### Key commands

| Action | Command |
|--------|---------|
| Build | `zola build` |
| Dev server | `zola serve --interface 0.0.0.0 --port 1111` |
| Check (build + link validation) | `zola check` |

### Important notes

- The `config.toml` uses Zola **0.17.x** syntax (`generate_feed`, `feed_filename`, `external_links_target_blank`, `render_emoji`). These fields were renamed/moved in 0.19+, so **do not upgrade Zola** without updating `config.toml`.
- `zola serve` starts a dev server with live reload on port 1111 (WebSocket on port 1024). There is no separate build step needed during development.
- There are no linters, test frameworks, or package managers in this project. `zola build` (exit code 0) and `zola check` are the primary validation commands.
- Content lives in `content/blog/` as Markdown files with TOML front matter (`+++`). Templates use Tera syntax in `templates/`.
