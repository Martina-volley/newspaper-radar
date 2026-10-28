#!/usr/bin/env python3
"""Regenerate the publication catalog on the cover page (index.html) from docs/.

Usage:
    python3 scripts/update_index.py          # rewrite index.html if needed
    python3 scripts/update_index.py --check  # exit 1 if index.html is out of date

Only these parts of index.html are rewritten; everything else is left byte-for-byte:
  * each publication's month list, between <!-- CATALOG:<slug>:START --> and
    <!-- CATALOG:<slug>:END --> (publications and their order come from these markers);
  * the per-publication count  <p class="pub-meta">共 N 期 HTML ・ <code>docs/<slug>/</code></p>;
  * the overall count          <span class="section-count">P 份刊物 · N 期</span>;
  * the latest-issue links     .nav-link / .primary "閱讀最新一期" hrefs and the .hero-note label.

Issues are docs/<slug>/YYYY-MM/*.html files whose name contains YYYY-MM-DD (or only
YYYY-MM for a whole-month issue, shown as 全月). Files sharing a date form one issue;
-brief / -engineering files get the kind-brief / kind-engineering classes. Link labels
are the issue's <title> (or a filename-derived label in the page's existing style when
the file has no <title>). The latest issue is the newest date overall; ties go to the
publication listed first on the page.
"""

import argparse
import html
import os
import re
import sys
from urllib.parse import quote, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.html")

MONTH_DIR_RE = re.compile(r"^(\d{4})-(\d{2})$")
DATE_RE = re.compile(r"(?<!\d)(\d{4})-(\d{2})(?:-(\d{2}))?(?!\d)")
KIND_RE = re.compile(r"-(brief|engineering)\.html$")
KIND_ORDER = {"brief": 0, None: 1, "engineering": 2}
FALLBACK_KIND_LABEL = {"brief": "決策／入門版", "engineering": "工程技術版"}
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)
MARKER_RE = re.compile(
    r"(<!-- CATALOG:([a-z0-9-]+):START -->\n)(.*?)(<!-- CATALOG:\2:END -->)", re.S
)


class Issue:
    def __init__(self, slug, year, month, day):
        self.slug = slug
        self.year = year
        self.month = month
        self.day = day
        self.files = []  # (kind, relpath, label)

    @property
    def key(self):
        return (self.year, self.month, self.day or "")

    @property
    def datetime(self):
        return f"{self.year}-{self.month}" + (f"-{self.day}" if self.day else "")

    @property
    def dotted(self):
        return f"{self.year}.{self.month}" + (f".{self.day}" if self.day else "")


def read_title(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        m = TITLE_RE.search(f.read())
    if not m:
        return None
    title = " ".join(html.unescape(m.group(1)).split())
    return title or None


def fallback_label(slug, pub_name, issue, kind):
    if slug == "ai-radar":
        label = f"{pub_name}｜{issue.dotted}"
    elif slug == "si-ai-tools":
        label = f"{pub_name}｜{issue.datetime}（Asia/Taipei）"
    elif slug == "ai-security":
        label = f"AI 資安報｜{issue.datetime}"
    else:
        label = f"{pub_name}｜{issue.datetime}"
    if kind:
        label += " " + FALLBACK_KIND_LABEL[kind]
    return label


def scan(slug, pub_name):
    base = os.path.join(ROOT, "docs", slug)
    issues = {}
    if not os.path.isdir(base):
        return []
    for month_dir in sorted(os.listdir(base)):
        md = MONTH_DIR_RE.match(month_dir)
        month_path = os.path.join(base, month_dir)
        if not md or not os.path.isdir(month_path):
            continue
        for name in sorted(os.listdir(month_path)):
            path = os.path.join(month_path, name)
            if not name.endswith(".html") or not os.path.isfile(path):
                continue
            dm = DATE_RE.search(name)
            if not dm or (dm.group(1), dm.group(2)) != md.groups():
                print(f"略過（檔名無對應日期）：docs/{slug}/{month_dir}/{name}", file=sys.stderr)
                continue
            year, month, day = dm.groups()
            km = KIND_RE.search(name)
            kind = km.group(1) if km else None
            issue = issues.setdefault((year, month, day), Issue(slug, year, month, day))
            title = read_title(path)
            issue.files.append((kind, f"docs/{slug}/{month_dir}/{name}", title))
    result = sorted(issues.values(), key=lambda i: i.key, reverse=True)
    for issue in result:
        issue.files.sort(key=lambda f: (KIND_ORDER[f[0]], f[1]))
        issue.files = [
            (kind, rel, title or fallback_label(slug, pub_name, issue, kind))
            for kind, rel, title in issue.files
        ]
    return result


def esc(text):
    return html.escape(text, quote=False)


def href(rel):
    return html.escape(quote(rel, safe="/"), quote=True)


def render_issue(issue):
    time_text = f"{issue.month}/{issue.day}" if issue.day else "全月"
    links = "".join(
        f'<a href="{href(rel)}"' + (f' class="kind-{kind}"' if kind else "") + f">{esc(label)}</a>"
        for kind, rel, label in issue.files
    )
    return (
        f'<li><time datetime="{issue.datetime}">{time_text}</time>'
        f'<span class="links">{links}</span></li>\n'
    )


def render_months(issues):
    out = []
    months = []
    for issue in issues:
        ym = (issue.year, issue.month)
        if not months or months[-1][0] != ym:
            months.append((ym, []))
        months[-1][1].append(issue)
    for (year, month), items in months:
        out.append(
            f'<div class="month"><h4>{year} 年 {int(month)} 月<span>{len(items)} 期</span></h4>'
            f'<ul class="issues">\n'
        )
        out.extend(render_issue(i) for i in items)
        out.append("</ul></div>\n")
    return "".join(out)


def sub_once(pattern, repl, text, what):
    new, n = re.subn(pattern, repl, text, flags=re.S)
    if n != 1:
        raise SystemExit(f"錯誤：index.html 中找到 {n} 處「{what}」，預期恰好 1 處")
    return new


def build(page):
    slugs = [m.group(2) for m in MARKER_RE.finditer(page)]
    if not slugs:
        raise SystemExit("錯誤：index.html 缺少 <!-- CATALOG:<slug>:START/END --> 標記")
    if len(set(slugs)) != len(slugs):
        raise SystemExit("錯誤：index.html 有重複的 CATALOG 標記")

    pubs = []
    for slug in slugs:
        m = re.search(rf'<h3 id="h-{re.escape(slug)}">(.*?)</h3>', page, re.S)
        if not m:
            raise SystemExit(f'錯誤：找不到 <h3 id="h-{slug}">')
        name = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        pubs.append((slug, name, scan(slug, name)))

    blocks = {slug: render_months(issues) for slug, _, issues in pubs}
    page = MARKER_RE.sub(lambda m: m.group(1) + blocks[m.group(2)] + m.group(4), page)

    for slug, _, issues in pubs:
        page = sub_once(
            rf'(<p class="pub-meta">共 )\d+( 期 HTML ・ <code>docs/{re.escape(slug)}/</code></p>)',
            lambda m, n=len(issues): f"{m.group(1)}{n}{m.group(2)}",
            page,
            f"{slug} 期數",
        )

    total = sum(len(issues) for _, _, issues in pubs)
    page = sub_once(
        r'(<span class="section-count">)\d+ 份刊物 · \d+ 期(</span>)',
        lambda m: f"{m.group(1)}{len(pubs)} 份刊物 · {total} 期{m.group(2)}",
        page,
        "刊物總數",
    )

    latest = None
    for slug, name, issues in pubs:
        if issues and (latest is None or issues[0].key > latest[1].key):
            latest = (name, issues[0])
    if latest:
        name, issue = latest
        target = href(issue.files[0][1])
        for cls in ("nav-link", "primary"):
            page = sub_once(
                rf'(<a class="{cls}" href=")[^"]*(">閱讀最新一期)',
                lambda m: f"{m.group(1)}{target}{m.group(2)}",
                page,
                f"{cls} 最新一期連結",
            )
        page = sub_once(
            r'(<p class="hero-note">最新一期：)[^<]*(</p>)',
            lambda m: f"{m.group(1)}{esc(name)}・{issue.dotted}{m.group(2)}",
            page,
            "hero-note 最新一期說明",
        )
    return page, pubs, latest


def check_links(page):
    hrefs = sorted(set(re.findall(r'href="(docs/[^"#?]+)"', page)))
    missing = [
        h for h in hrefs
        if not os.path.isfile(os.path.join(ROOT, *unquote(html.unescape(h)).split("/")))
    ]
    return len(hrefs), missing


def main():
    parser = argparse.ArgumentParser(description="從 docs/ 重新產生 index.html 的刊物目錄")
    parser.add_argument("--check", action="store_true", help="只檢查；index.html 需要更新時以非零狀態結束")
    args = parser.parse_args()

    with open(INDEX, "rb") as f:
        original = f.read().decode("utf-8")
    page, pubs, latest = build(original)

    n_links, missing = check_links(page)
    for slug, name, issues in pubs:
        print(f"{name}（docs/{slug}/）：{len(issues)} 期")
    if latest:
        print(f"最新一期：{latest[0]}・{latest[1].dotted} → {latest[1].files[0][1]}")
    print(f"連結檢查：{n_links} 個 docs/ 連結，缺少 {len(missing)} 個")
    if missing:
        for h in missing:
            print(f"  缺少檔案：{h}", file=sys.stderr)
        return 2

    changed = page != original
    if args.check:
        print("index.html 需要更新" if changed else "index.html 已是最新")
        return 1 if changed else 0
    if changed:
        with open(INDEX, "wb") as f:
            f.write(page.encode("utf-8"))
        print("已更新 index.html")
    else:
        print("index.html 無變更")
    return 0


if __name__ == "__main__":
    sys.exit(main())
