import { visit } from 'unist-util-visit';

/**
 * Turns paragraphs consisting only of bullet-like lines into real Markdown lists.
 * Supports:
 * - "• item"
 * - "- item" (when it was parsed as a paragraph, e.g. due to missing blank lines)
 */
export function remarkBullets() {
  return (tree) => {
    visit(tree, 'paragraph', (node, index, parent) => {
      if (!parent || typeof index !== 'number') return;
      if (!node.children || node.children.length !== 1) return;
      const only = node.children[0];
      if (!only || only.type !== 'text') return;

      const raw = only.value ?? '';
      const lines = raw
        .split(/\r?\n/)
        .map((l) => l.trimEnd())
        .filter((l) => l.trim().length > 0);
      if (lines.length < 1) return;

      const bulletMatch = (line) => {
        const trimmed = line.trimStart();
        // Accept both "• item" and "•item"
        if (trimmed.startsWith('•')) return { marker: '•', text: trimmed.slice(1).trimStart() };
        // Accept standard markdown list marker when it got parsed as paragraph
        if (trimmed.startsWith('-')) return { marker: '-', text: trimmed.slice(1).trimStart() };
        return null;
      };

      const parsed = lines.map(bulletMatch);
      if (parsed.some((x) => !x || !x.text.trim())) return;

      parent.children.splice(index, 1, {
        type: 'list',
        ordered: false,
        spread: false,
        children: parsed.map((b) => ({
          type: 'listItem',
          spread: false,
          children: [
            {
              type: 'paragraph',
              children: [{ type: 'text', value: b.text }],
            },
          ],
        })),
      });
    });
  };
}

/**
 * Automatically bolds times like "11:15" in normal text.
 * Skips inside inline code / code / links / existing strong.
 */
export function remarkBoldTimes() {
  const TIME_RE = /\b([01]?\d|2[0-3]):[0-5]\d\b/g;
  const SKIP_PARENTS = new Set(['inlineCode', 'code', 'link', 'linkReference', 'strong']);

  return (tree) => {
    visit(tree, 'text', (node, index, parent) => {
      if (!parent || typeof index !== 'number') return;
      if (SKIP_PARENTS.has(parent.type)) return;

      const value = node.value ?? '';
      TIME_RE.lastIndex = 0;
      if (!TIME_RE.test(value)) return;

      TIME_RE.lastIndex = 0;
      const out = [];
      let last = 0;
      let m;
      while ((m = TIME_RE.exec(value))) {
        const start = m.index;
        const end = start + m[0].length;
        if (start > last) out.push({ type: 'text', value: value.slice(last, start) });
        out.push({ type: 'strong', children: [{ type: 'text', value: m[0] }] });
        last = end;
      }
      if (last < value.length) out.push({ type: 'text', value: value.slice(last) });

      parent.children.splice(index, 1, ...out);
      return index + out.length;
    });
  };
}

