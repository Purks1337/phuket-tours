import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const collections = {
  excursions: defineCollection({
    // Загружаем все .md файлы из папки excursions
    loader: glob({ pattern: "**/*.md", base: "./src/content/excursions" }),
    // Описываем схему данных (Zod)
    schema: z.object({
      title: z.string(),
      category: z.string(),
      priceAdult: z.number(),
      badges: z.array(z.string()).optional() // optional означает, что бейджиков может и не быть
    })
  })
};