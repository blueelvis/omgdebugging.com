#!/usr/bin/env python3
"""Convert Ghost JSON export to Hugo markdown posts."""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
import html as html_module

def load_ghost_export(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data['db'][0]['data']

def build_tag_map(db):
    tags = {t['id']: t for t in db['tags']}
    post_tags = {}
    for pt in db['posts_tags']:
        pid = pt['post_id']
        tid = pt['tag_id']
        if pid not in post_tags:
            post_tags[pid] = []
        if tid in tags:
            post_tags[pid].append(tags[tid]['name'])
    return post_tags

def classify_section(post, tags):
    """Assign a post to the best section based on its tags and content."""
    tag_lower = [t.lower() for t in tags]
    title_lower = post['title'].lower()
    slug = post['slug'].lower()

    coding_tags = {'c#', 'powershell', 'php', 'python', 'javascript', 'git',
                   'functions', 'shell32', 'git bash', 'java', 'maven',
                   'terraform', 'meteor', 'npm', 'uv'}
    coding_keywords = ['code', 'programming', 'psobject', 'hashtable',
                       'logging', 'formatter', 'rebase', 'squash',
                       'npgsql', 'entity', 'dotnet', '.net', 'visual studio',
                       'maven', 'npm', 'commits', 'function']

    tech_tags = {'azure', 'web app for containers', 'cloudflare', 'hosting',
                 'new relic', 'devops', 'kudu', 'rsyslog', 'logrotate',
                 'cron', 'anacron', 'docker', 'nginx', 'jenkins', 'splunk',
                 'event grid', 'storage account', 'openssl', 'az-400',
                 'linux', 'red hat', 'bsod', 'debugging', 'whea', 'windows',
                 'process monitor', 'registry', 'tdr', 'disk', 'hyper-v',
                 'ram', 'resource monitor', 'task manager', 'virtual machine',
                 'malware', 'security', 'dlls', 'ftp', 'msinfo32',
                 'windows blue screen of death', 'edge swipes', 'synaptics',
                 'port', 'azure storage emulator', 'loopback', 'write barrier',
                 'sshpass', 'api', 'rest', 'http', 'microsoft', 'winpty',
                 'certbot', 'pi-hole', 'ubuntu', 'mysql', 'gnupg', 'cors',
                 'arm template', 'watermark', 'steam', 'spotify', 'monitor',
                 'process', 'sony', 'headset', 'windirstat'}

    life_keywords = ['fast food', 'bang for the buck', 'tips for getting',
                     'sleep button', 'night light', 'chrome extension',
                     'quickly']

    for kw in life_keywords:
        if kw in title_lower or kw in slug:
            return 'life'

    for t in tag_lower:
        if t in coding_tags:
            return 'coding'

    for kw in coding_keywords:
        if kw in title_lower:
            return 'coding'

    for t in tag_lower:
        if t in tech_tags:
            return 'technology'

    tech_title_keywords = ['azure', 'bsod', 'driver', 'windows', 'linux',
                           'ubuntu', 'nginx', 'docker', 'jenkins', 'splunk',
                           'certbot', 'pi-hole', 'terraform', 'cloudflare',
                           'container', 'deploy', 'server', 'usb', 'port',
                           'mysql', 'gnupg', 'cors', 'debug', 'arm template',
                           'watermark', 'steam', 'spotify', 'registry',
                           'endian', 'ftp', 'heroku', 'app service',
                           'storage emulator', 'dynamics', 'watermark',
                           'ghost', 'refreshing desktop', 'fix ', 'install',
                           'disable', 'enable', 'error', 'audio', 'sound']
    for kw in tech_title_keywords:
        if kw in title_lower:
            return 'technology'

    return 'technology'

def html_to_markdown(html_content):
    """Convert Ghost HTML to clean markdown."""
    if not html_content:
        return ''

    content = html_content

    # Remove Ghost card markers
    content = re.sub(r'<!--kg-card-begin: .*?-->', '', content)
    content = re.sub(r'<!--kg-card-end: .*?-->', '', content)

    # Handle code blocks: <pre><code class="language-xxx">
    def replace_code_block(m):
        lang = m.group(1) or ''
        code = m.group(2)
        code = html_module.unescape(code)
        code = code.replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
        code = re.sub(r'<[^>]+>', '', code)
        return f'\n```{lang}\n{code}\n```\n'

    content = re.sub(
        r'<pre><code(?:\s+class="language-(\w+)")?\s*>(.*?)</code></pre>',
        replace_code_block, content, flags=re.DOTALL
    )

    # Handle inline code
    content = re.sub(r'<code>(.*?)</code>', r'`\1`', content)

    # Handle headings
    for i in range(6, 0, -1):
        content = re.sub(
            rf'<h{i}[^>]*>(.*?)</h{i}>',
            lambda m, lvl=i: f'\n{"#" * lvl} {m.group(1).strip()}\n',
            content, flags=re.DOTALL
        )

    # Handle links
    content = re.sub(r'<a\s+href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)

    # Handle images
    content = re.sub(r'<img\s+src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?\s*>', r'![\2](\1)', content)
    content = re.sub(r'<img\s+src="([^"]*)"[^>]*/?\s*>', r'![](\1)', content)

    # Handle bold/italic
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)

    # Handle lists
    content = re.sub(r'<ul[^>]*>', '\n', content)
    content = re.sub(r'</ul>', '\n', content)
    content = re.sub(r'<ol[^>]*>', '\n', content)
    content = re.sub(r'</ol>', '\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)

    # Handle blockquotes
    content = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>',
                     lambda m: '\n> ' + re.sub(r'\s*<p>\s*', '\n> ', m.group(1)).strip() + '\n',
                     content, flags=re.DOTALL)

    # Handle paragraphs and breaks
    content = re.sub(r'<p[^>]*>', '\n\n', content)
    content = re.sub(r'</p>', '', content)
    content = re.sub(r'<br\s*/?\s*>', '\n', content)
    content = re.sub(r'<hr\s*/?\s*>', '\n---\n', content)

    # Handle figures
    content = re.sub(r'<figure[^>]*>(.*?)</figure>', r'\1', content, flags=re.DOTALL)
    content = re.sub(r'<figcaption[^>]*>(.*?)</figcaption>', r'*\1*', content, flags=re.DOTALL)

    # Handle divs, spans, sections
    content = re.sub(r'<div[^>]*>', '', content)
    content = re.sub(r'</div>', '', content)
    content = re.sub(r'<span[^>]*>', '', content)
    content = re.sub(r'</span>', '', content)
    content = re.sub(r'<section[^>]*>', '', content)
    content = re.sub(r'</section>', '', content)

    # Remove remaining script/style/iframe tags but keep iframes as links
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    def iframe_to_link(m):
        src_match = re.search(r'src="([^"]*)"', m.group(0))
        if src_match:
            return f'\n[Embedded content]({src_match.group(1)})\n'
        return ''
    content = re.sub(r'<iframe[^>]*>.*?</iframe>', iframe_to_link, content, flags=re.DOTALL)
    content = re.sub(r'<iframe[^>]*/>', iframe_to_link, content)

    # Remove CDATA
    content = re.sub(r'//<!\[CDATA\[', '', content)
    content = re.sub(r'//\]\]>', '', content)

    # Clean up remaining HTML tags
    content = re.sub(r'</?[^>]+>', '', content)

    # Unescape HTML entities
    content = html_module.unescape(content)

    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()

    return content

def find_media_references(html_content, slug):
    """Find all media URLs referenced in post content."""
    if not html_content:
        return []
    media = []
    patterns = [
        r'<img\s+src="([^"]*)"',
        r'!\[.*?\]\(([^)]*)\)',
        r'src="([^"]*\.(?:png|jpg|jpeg|gif|svg|webp|mp4|mp3|pdf))"',
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, html_content, re.IGNORECASE):
            url = match.group(1)
            if url and url not in media:
                media.append(url)
    return media

def sanitize_title(title):
    """Clean up title for YAML front matter."""
    title = title.replace('"', '\\"')
    return title

def convert_post(post, tags, section, output_dir):
    """Convert a single Ghost post to Hugo markdown."""
    slug = post['slug']
    title = sanitize_title(post['title'])
    date = post.get('published_at', post.get('created_at', ''))
    if date:
        date = date[:19].replace(' ', 'T')
        if not date.endswith('Z') and '+' not in date:
            date += '+00:00'

    html_content = post.get('html', '')
    markdown = html_to_markdown(html_content)

    is_page = post.get('type') == 'page'
    feature_image = post.get('feature_image', '')
    custom_excerpt = post.get('custom_excerpt', '')

    # Build front matter
    fm = ['---']
    fm.append(f'title: "{title}"')
    fm.append(f'date: {date}')
    if post.get('updated_at'):
        updated = post['updated_at'][:19].replace(' ', 'T') + '+00:00'
        fm.append(f'lastmod: {updated}')
    if post.get('status') == 'draft':
        fm.append('draft: true')
    if custom_excerpt:
        fm.append(f'description: "{sanitize_title(custom_excerpt)}"')
    if feature_image:
        fm.append(f'feature_image: "{feature_image}"')
    if tags:
        tags_yaml = ', '.join(f'"{t}"' for t in tags)
        fm.append(f'tags: [{tags_yaml}]')
    if is_page:
        fm.append('type: "page"')
        fm.append('layout: "single"')
    fm.append('---')

    content = '\n'.join(fm) + '\n\n' + markdown

    # Determine output path
    if is_page:
        out_dir = os.path.join(output_dir, 'pages')
    else:
        out_dir = os.path.join(output_dir, section)

    os.makedirs(out_dir, exist_ok=True)
    filepath = os.path.join(out_dir, f'{slug}.md')

    with open(filepath, 'w') as f:
        f.write(content)

    return filepath

def generate_media_report(db, post_tags_map, output_path):
    """Generate a report of all media references that need manual handling."""
    posts = db['posts']
    report = ['# Media Report', '',
              'Posts that reference media files (images, videos, etc.) that may need to be manually added.', '',
              '| # | Post | Section | Media URL | Type |',
              '|---|------|---------|-----------|------|']

    count = 0
    for post in posts:
        if post['status'] != 'published':
            continue

        tags = post_tags_map.get(post['id'], [])
        section = classify_section(post, tags)
        html_content = post.get('html', '')
        media = find_media_references(html_content, post['slug'])

        feature_img = post.get('feature_image', '')
        if feature_img and feature_img not in media:
            media.insert(0, feature_img)

        for url in media:
            count += 1
            ext = url.rsplit('.', 1)[-1].lower() if '.' in url else 'unknown'
            media_type = 'Image' if ext in ('png', 'jpg', 'jpeg', 'gif', 'svg', 'webp') else \
                         'Video' if ext in ('mp4', 'webm', 'mov') else \
                         'Document' if ext in ('pdf', 'doc', 'docx') else 'Other'
            report.append(f'| {count} | {post["title"][:50]} | {section} | `{url}` | {media_type} |')

    report.append('')
    report.append(f'**Total: {count} media references across published posts.**')
    report.append('')
    report.append('## How to add media')
    report.append('')
    report.append('1. Download the media from the Ghost site dump')
    report.append('2. Place them in `static/content/images/` preserving the path structure')
    report.append('3. For example, a Ghost image at `/content/images/2024/02/screenshot.png`')
    report.append('   should be placed at `static/content/images/2024/02/screenshot.png`')

    with open(output_path, 'w') as f:
        f.write('\n'.join(report))

    return count

def main():
    ghost_file = sys.argv[1] if len(sys.argv) > 1 else 'ghost-export.json'
    content_dir = sys.argv[2] if len(sys.argv) > 2 else 'content'

    db = load_ghost_export(ghost_file)
    post_tags_map = build_tag_map(db)

    posts = db['posts']
    published = [p for p in posts if p['status'] == 'published']

    stats = {'technology': 0, 'coding': 0, 'finance': 0, 'life': 0, 'pages': 0}

    for post in published:
        tags = post_tags_map.get(post['id'], [])
        is_page = post.get('type') == 'page'

        if is_page:
            section = 'pages'
        else:
            section = classify_section(post, tags)

        filepath = convert_post(post, tags, section, content_dir)

        if is_page:
            stats['pages'] += 1
        else:
            stats[section] = stats.get(section, 0) + 1

        print(f'  [{section}] {post["slug"]}')

    print(f'\nConverted {len(published)} published posts:')
    for k, v in stats.items():
        print(f'  {k}: {v}')

    # Generate media report
    media_count = generate_media_report(db, post_tags_map, 'MEDIA_REPORT.md')
    print(f'\nMedia report: {media_count} references found. See MEDIA_REPORT.md')

if __name__ == '__main__':
    main()
