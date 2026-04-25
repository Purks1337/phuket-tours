import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

import sitemap from '@astrojs/sitemap';
import remarkBreaks from 'remark-breaks';
import { remarkBullets, remarkBoldTimes } from './src/remark/markdown-helpers.js';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },

  markdown: {
    remarkPlugins: [remarkBreaks, remarkBullets, remarkBoldTimes],
  },

  integrations: [sitemap()],
});