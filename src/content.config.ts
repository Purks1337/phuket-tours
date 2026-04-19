import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

export const collections = {
  excursions: defineCollection({
    loader: glob({ pattern: "**/*.md", base: "./src/content/excursions" }),
    schema: ({ image }) => z.object({
      title: z.string(),
      subtitle: z.string().optional(),
      category: z.string(),
      priceAdult: z.number(),
      priceChild: z.number().optional(),
      childAge: z.string().optional(),
      pricePrefix: z.string().optional(),
      badges: z.array(z.string()).optional(),
      city: z.string().optional(),
      cover: image().optional(),
      packages: z.array(z.object({
        title: z.string(),
        priceAdult: z.number(),
        priceChild: z.number().optional(),
        childAge: z.string().optional(),
      })).optional()
    })
  })
};