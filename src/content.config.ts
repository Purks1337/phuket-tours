import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const collections = {
  excursions: defineCollection({
    loader: glob({ pattern: "**/*.md", base: "./src/content/excursions" }),
    // Обрати внимание: мы получаем helper 'image'
    schema: ({ image }) => z.object({
      title: z.string(),
      category: z.string(),
      priceAdult: z.number(),
      badges: z.array(z.string()).optional(),
      cover: image(), // Валидация и оптимизация картинки
    })
  })
};