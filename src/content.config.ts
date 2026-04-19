import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const collections = {
  excursions: defineCollection({
    loader: glob({ pattern: "**/*.md", base: "./src/content/excursions" }),
    schema: ({ image }) => z.object({
      title: z.string(),
      subtitle: z.string().optional(), // Подзаголовок (как "есть ранний выезд")
      category: z.string(),
      priceAdult: z.number(),
      priceChild: z.number().optional(), // Цена для ребенка
      childAge: z.string().optional(), // Возраст ребенка
      pricePrefix: z.string().optional(), // Префикс для цены (например, "от")
      badges: z.array(z.string()).optional(),
      city: z.string().optional(), // Город (например, "Phuket" или "Pattaya")
      cover: image().optional(), // Обложка теперь опциональна в каталоге
    })
  })
};