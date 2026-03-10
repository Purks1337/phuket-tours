# Структура проекта

```
📄 .gitignore
📄 README.md
📄 astro.config.mjs
📄 package.json
📄 tsconfig.json
📁 src/
│   📁 assets/
│   📁 components/
│   📁 content/
│   📁 layouts/
│   📁 pages/
│   📁 styles/
│   📄 content.config.ts
    │   📁 images/
        │   📄 bond.jpg
        │   📄 bounty-logo.svg
        │   📄 elephants.jpg
        │   📄 hanuman.jpg
        │   📄 phiphi.jpg
        │   📄 similan.jpg
    │   📄 BookingForm.astro
    │   📄 CategorySection.astro
    │   📄 Footer.astro
    │   📄 Header.astro
    │   📄 TourRow.astro
    │   📁 excursions/
        │   📄 elephants.md
        │   📄 hanuman.md
        │   📄 james-bond.md
        │   📄 phi-phi.md
        │   📄 similan.md
    │   📄 Layout.astro
    │   📁 excursions/
    │   📄 index.astro
        │   📄 [id].astro
    │   📄 global.css
📁 public/
│   📄 favicon.svg
```

# Содержимое файлов


---

## ` .gitignore `

```
# build output
dist/
# generated types
.astro/

# dependencies
node_modules/

# logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*


# environment variables
.env
.env.production

# macOS-specific files
.DS_Store

# jetbrains setting folder
.idea/

```


---

## ` README.md `

```md
# Astro Starter Kit: Minimal

```sh
npm create astro@latest -- --template minimal
```

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
├── src/
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).

```


---

## ` astro.config.mjs `

```mjs
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },
});
```


---

## ` package.json `

```json
{
  "name": "phuket-tours",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@tailwindcss/vite": "^4.2.1",
    "astro": "^5.17.1",
    "tailwindcss": "^4.2.1"
  }
}

```


---

## ` tsconfig.json `

```json
{
  "extends": "astro/tsconfigs/strict",
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist"]
}

```


---

## ` src/content.config.ts `

```ts
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
```


---

## ` src/content/excursions/elephants.md `

```md
---
title: "Треккинг на слонах"
category: "Сухопутные"
priceAdult: 800
badges: ["Для детей", "Джунгли"]
cover: "../../assets/images/elephants.jpg"
---

Незабываемая прогулка верхом на слонах по настоящим джунглям Пхукета. Вы сможете покормить животных и сделать отличные фото.

Программа занимает около 45 минут. Трансфер включен.
```


---

## ` src/content/excursions/hanuman.md `

```md
---
title: "Hanuman World (Зиплайн)"
category: "Сухопутные"
priceAdult: 1900
badges: ["Экстрим", "Адреналин"]
cover: "../../assets/images/hanuman.jpg"
---

Парк приключений в джунглях. Полеты на тросах между деревьями, подвесные мосты и скоростные спуски.

Безопасность на высшем уровне. Подходит как для новичков, так и для любителей экстрима.
```


---

## ` src/content/excursions/james-bond.md `

```md
---
title: "Остров Джеймса Бонда"
category: "Морские"
priceAdult: 1700
badges: ["Каноэ", "Пещеры"]
cover: "../../assets/images/bond.jpg"
---

Увлекательное путешествие по заливу Пханг Нга. Вы увидите знаменитую скалу Тапу, где снимали фильм "Человек с золотым пистолетом".

**Особенности:**
*   Катание на каноэ по пещерам
*   Деревня морских цыган на воде
*   Храм с обезьянами
```


---

## ` src/content/excursions/phi-phi.md `

```md
---
title: "Острова Пхи-Пхи"
category: "Морские"
priceAdult: 1500
badges: ["Хит продаж", "Русский гид"]
cover: "../../assets/images/phiphi.jpg"
---

Кристально чистая вода, снорклинг, обезьяны и знаменитая бухта Майя Бэй, где снимали фильм "Пляж" с Леонардо Ди Каприо!
```


---

## ` src/content/excursions/similan.md `

```md
---
title: "Симиланские острова"
category: "Морские"
priceAdult: 2300
badges: ["Must See", "Белый песок"]
cover: "../../assets/images/similan.jpg"
---

Симиланские острова — это национальный парк, входящий в десятку самых красивых мест на планете. Белоснежный песок, лазурная вода и огромные черепахи.

**В программу входит:**
*   Снорклинг в кристальной воде
*   Посещение скалы "Парус"
*   Обед в национальном парке
*   Отдых на пляже
```


---

## ` src/styles/global.css `

```css
@import "tailwindcss";
```


---

## ` src/components/BookingForm.astro `

```astro
---
interface Props {
  tourTitle: string;
}

const { tourTitle } = Astro.props;
---

<form id="telegram-form" class="space-y-4">
  <!-- Скрытое поле с названием экскурсии -->
  <input type="hidden" name="tour" value={tourTitle} />

  <div>
    <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Ваше имя</label>
    <input 
      type="text" 
      id="name" 
      name="name" 
      required 
      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
      placeholder="Иван Иванов"
    />
  </div>

  <div>
    <label for="contact" class="block text-sm font-medium text-gray-700 mb-1">Telegram / WhatsApp</label>
    <input 
      type="text" 
      id="contact" 
      name="contact" 
      required 
      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
      placeholder="@username или номер телефона"
    />
  </div>

  <div>
    <label for="date" class="block text-sm font-medium text-gray-700 mb-1">Желаемая дата</label>
    <input 
      type="date" 
      id="date" 
      name="date" 
      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
    />
  </div>

  <button 
    type="submit" 
    class="w-full bg-blue-600 text-white font-bold py-3 px-6 rounded-lg hover:bg-blue-700 transition duration-300 ease-in-out transform hover:-translate-y-1"
  >
    Отправить заявку
  </button>

  <div id="form-status" class="hidden mt-4 p-4 rounded-lg text-center text-sm font-medium"></div>
</form>

<script>
  // Astro/Vite автоматически заменят эти переменные на значения из файла .env
  const BOT_TOKEN = import.meta.env.PUBLIC_TELEGRAM_BOT_TOKEN;
  const CHAT_ID = import.meta.env.PUBLIC_TELEGRAM_CHAT_ID;

  const form = document.getElementById('telegram-form') as HTMLFormElement;
  const statusDiv = document.getElementById('form-status');

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const formData = new FormData(form);
      const tour = formData.get('tour');
      const name = formData.get('name');
      const contact = formData.get('contact');
      const date = formData.get('date');

      const text = `
🚀 *Новая заявка на экскурсию!*
🏝 *Тур:* ${tour}
👤 *Имя:* ${name}
📱 *Контакты:* ${contact}
📅 *Дата:* ${date || 'Не указана'}
      `;

      if (statusDiv) {
        statusDiv.classList.remove('hidden', 'bg-green-100', 'text-green-700', 'bg-red-100', 'text-red-700');
        statusDiv.classList.add('bg-gray-100', 'text-gray-700');
        statusDiv.textContent = 'Отправка...';
        statusDiv.style.display = 'block';
      }

      try {
        const response = await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            chat_id: CHAT_ID,
            text: text,
            parse_mode: 'Markdown',
          }),
        });

        if (response.ok) {
          if (statusDiv) {
            statusDiv.classList.remove('bg-gray-100', 'text-gray-700');
            statusDiv.classList.add('bg-green-100', 'text-green-700');
            statusDiv.textContent = 'Спасибо! Мы свяжемся с вами в ближайшее время.';
          }
          form.reset();
        } else {
          throw new Error('Ошибка Telegram API');
        }
      } catch (error) {
        console.error(error);
        if (statusDiv) {
          statusDiv.classList.remove('bg-gray-100', 'text-gray-700');
          statusDiv.classList.add('bg-red-100', 'text-red-700');
          statusDiv.textContent = 'Произошла ошибка. Проверьте консоль.';
        }
      }
    });
  }
</script>
```


---

## ` src/components/CategorySection.astro `

```astro
---
interface Props {
  title: string;
}

const { title } = Astro.props;
---
<section class="mb-10">
  <div class="border-b-2 border-black mb-6 pb-2">
    <h2 class="text-2xl font-black uppercase tracking-wider">{title}</h2>
  </div>
  <div class="flex flex-col gap-3">
    <slot />
  </div>
</section>
```


---

## ` src/components/Footer.astro `

```astro
---
---
<footer id="contacts" class="bg-gray-900 text-white mt-12 py-10">
    <div class="max-w-4xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-6">
      <div class="text-center md:text-left">
        <h3 class="text-xl font-bold mb-1 uppercase tracking-wider">Bounty Tours</h3>
        <p class="text-gray-400 text-sm">Лучшие экскурсии на Пхукете</p>
      </div>
      <div class="text-sm text-gray-400 text-center md:text-right">
        <p class="font-bold text-white mb-1">Свяжитесь с нами:</p>
        <p>Telegram: @bountytours</p>
        <p>WhatsApp: +66 000 000 000</p>
      </div>
    </div>
  </footer>
```


---

## ` src/components/Header.astro `

```astro
---
import { Image } from 'astro:assets';
// Импортируем логотип. Убедись, что файл называется именно так и лежит в этой папке
import logo from '../assets/images/bounty-logo.svg';
---
<header class="bg-white shadow-sm sticky top-0 z-50">
  <div class="max-w-4xl mx-auto px-4 py-3 flex justify-between items-center">
    <a href="/" class="block hover:opacity-80 transition">
      <!-- h-12 задает высоту, ширина подстроится автоматически (w-auto) -->
      <Image src={logo} alt="Bounty Tours" class="h-12 w-auto object-contain" loading="eager" />
    </a>
    <a href="#contacts" class="bg-blue-600 text-white px-5 py-2 rounded-full text-sm font-bold hover:bg-blue-700 transition">
      Telegram
    </a>
  </div>
</header>
```


---

## ` src/components/TourRow.astro `

```astro
---
import { Image } from 'astro:assets';

interface Props {
  id: string;
  title: string;
  priceAdult: number;
  badges?: string[];
  cover: ImageMetadata; // Тип для картинки Astro
}

const { id, title, priceAdult, badges = [], cover } = Astro.props;
---
<div class="bg-white rounded-xl shadow-sm hover:shadow-md transition-shadow p-4 flex flex-col md:flex-row items-start md:items-center justify-between border border-gray-100 gap-4">
  
  <!-- Картинка -->
  <div class="shrink-0 w-full md:w-32 h-32 md:h-24 bg-gray-100 rounded-lg overflow-hidden relative">
    <Image 
      src={cover} 
      alt={title} 
      class="w-full h-full object-cover" 
      width={300} 
      height={300}
    />
  </div>

  <div class="flex flex-col flex-1">
    {badges.length > 0 && (
      <div class="flex flex-wrap gap-2 mb-2">
        {badges.map((badge) => (
          <span class="bg-red-500 text-white text-[10px] font-bold px-2 py-1 rounded uppercase tracking-wider">
            {badge}
          </span>
        ))}
      </div>
    )}
    <h3 class="text-lg font-bold text-gray-900 mb-1 leading-tight">{title}</h3>
    <a href={`/excursions/${id}`} class="text-blue-500 text-sm font-medium hover:underline inline-flex items-center gap-1">
      Читать описание <span class="text-lg leading-none">→</span>
    </a>
  </div>

  <div class="flex flex-col items-end shrink-0 bg-[#f7f7f7] p-3 rounded-lg w-full md:w-auto min-w-[140px] text-right">
    <span class="text-[11px] text-gray-500 uppercase tracking-wider font-semibold mb-1">Взрослый</span>
    <span class="text-xl font-black text-gray-900">{priceAdult} ฿</span>
  </div>
</div>
```


---

## ` src/layouts/Layout.astro `

```astro
---
import '../styles/global.css';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';

interface Props {
	title: string;
}

const { title } = Astro.props;
---

<!doctype html>
<html lang="ru">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<meta name="generator" content={Astro.generator} />
		<title>{title}</title>
	</head>
	<body class="bg-[#f7f7f7] text-gray-900 font-sans flex flex-col min-h-screen">
		<Header />
		<main class="flex-grow max-w-4xl w-full mx-auto px-4 py-8">
			<slot />
		</main>
		<Footer />
	</body>
</html>
```


---

## ` src/pages/index.astro `

```astro
---
import Layout from '../layouts/Layout.astro';
import CategorySection from '../components/CategorySection.astro';
import TourRow from '../components/TourRow.astro';
import { getCollection } from 'astro:content';

const allExcursions = await getCollection('excursions');

const groupedExcursions = allExcursions.reduce((acc, tour) => {
  const category = tour.data.category;
  if (!acc[category]) {
    acc[category] = [];
  }
  acc[category].push(tour);
  return acc;
}, {} as Record<string, typeof allExcursions>);
---

<Layout title="Bounty Tours | Экскурсии на Пхукете">
  <div class="mb-10 text-center md:text-left border-b border-gray-200 pb-8">
    <h1 class="text-4xl md:text-5xl font-black uppercase tracking-wider mb-4 text-gray-900">
      Каталог <span class="text-blue-600">Bounty Tours</span>
    </h1>
    <p class="text-lg text-gray-600 max-w-2xl">
      Ваш надежный гид на Пхукете. Организуем морские прогулки, поездки по островам и приключения в джунглях. Бронирование без предоплаты.
    </p>
  </div>

  <div class="flex flex-col gap-10">
    {Object.entries(groupedExcursions).map(([category, tours]) => (
      <CategorySection title={category}>
        {tours.map((tour) => (
          <TourRow 
            id={tour.id} 
            title={tour.data.title} 
            priceAdult={tour.data.priceAdult} 
            badges={tour.data.badges} 
            cover={tour.data.cover}
          />
        ))}
      </CategorySection>
    ))}
  </div>
</Layout>
```


---

## ` src/pages/excursions/[id].astro `

```astro
---
import Layout from '../../layouts/Layout.astro';
import BookingForm from '../../components/BookingForm.astro';
import { getCollection, render } from 'astro:content';
import { Image } from 'astro:assets';

export async function getStaticPaths() {
  const excursions = await getCollection('excursions');
  return excursions.map(post => ({
    params: { id: post.id },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await render(post);
---

<Layout title={`${post.data.title} | Bounty Tours`}>
  <div class="mb-6">
    <a href="/" class="text-blue-600 text-sm font-bold hover:underline inline-flex items-center gap-1 transition">
      <span class="text-lg leading-none">←</span> Назад в каталог
    </a>
  </div>

  <!-- Баннер -->
  <div class="rounded-2xl overflow-hidden mb-8 h-64 md:h-96 w-full relative shadow-lg group">
    <Image 
      src={post.data.cover} 
      alt={post.data.title} 
      class="w-full h-full object-cover transition duration-700 group-hover:scale-105"
      width={1200}
      height={600}
      loading="eager"
    />
    <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"></div>
    <div class="absolute bottom-0 left-0 p-6 md:p-10 text-white w-full">
        {post.data.badges && post.data.badges.length > 0 && (
          <div class="flex flex-wrap gap-2 mb-3">
            {post.data.badges.map((badge) => (
              <span class="bg-blue-600 text-white text-[11px] font-bold px-3 py-1 rounded-full uppercase tracking-wider shadow-sm">
                {badge}
              </span>
            ))}
          </div>
        )}
        <h1 class="text-3xl md:text-5xl font-black uppercase tracking-wider drop-shadow-lg leading-tight">
            {post.data.title}
        </h1>
    </div>
  </div>

  <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 md:p-10 mb-10">
    <!-- Блок с ценой -->
    <div class="bg-blue-50/50 rounded-xl p-4 md:p-6 mb-8 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border border-blue-100">
      <div>
        <span class="block text-[11px] text-gray-500 uppercase tracking-wider font-bold mb-1">Стоимость (Взрослый)</span>
        <span class="text-4xl font-black text-gray-900">{post.data.priceAdult} ฿</span>
      </div>
      <a href="#booking-form" class="bg-blue-600 text-white px-8 py-4 rounded-xl font-bold hover:bg-blue-700 transition w-full md:w-auto text-center shadow-lg shadow-blue-200">
        Забронировать
      </a>
    </div>

    <!-- Текст из Markdown -->
    <div class="markdown-content text-gray-700 leading-relaxed text-lg">
      <Content />
    </div>
    
    <!-- Форма бронирования -->
    <div id="booking-form" class="mt-12 pt-10 border-t border-gray-100">
      <h2 class="text-2xl font-black uppercase tracking-wider mb-2 text-center md:text-left text-gray-900">Бронирование</h2>
      <p class="text-gray-500 mb-8 text-center md:text-left">
        Заполните форму ниже, и менеджер Bounty Tours свяжется с вами в Telegram.
      </p>
      
      <div class="bg-white p-6 md:p-10 rounded-2xl border border-gray-200 shadow-lg shadow-gray-100">
        <BookingForm tourTitle={post.data.title} />
      </div>
    </div>
  </div>
</Layout>

<style is:global>
  .markdown-content p { margin-bottom: 1.5rem; }
  .markdown-content h2 { font-size: 1.5rem; font-weight: 900; margin-top: 2.5rem; margin-bottom: 1rem; text-transform: uppercase; color: #111827; letter-spacing: 0.05em; }
  .markdown-content h3 { font-size: 1.25rem; font-weight: 800; margin-top: 2rem; margin-bottom: 0.75rem; color: #1f2937; }
  .markdown-content ul { list-style-type: none; padding-left: 0; margin-bottom: 1.5rem; }
  .markdown-content li { margin-bottom: 0.75rem; padding-left: 1.5rem; position: relative; }
  .markdown-content li::before { content: "•"; color: #2563eb; font-weight: bold; position: absolute; left: 0; font-size: 1.2em; line-height: 1; }
  .markdown-content strong { color: #111827; font-weight: 800; }
</style>
```
