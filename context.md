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
    schema: ({ image }) => z.object({
      title: z.string(),
      subtitle: z.string().optional(), // Подзаголовок (как "есть ранний выезд")
      category: z.string(),
      priceAdult: z.number(),
      priceChild: z.number().optional(), // Цена для ребенка
      childAge: z.string().optional(), // Возраст ребенка
      pricePrefix: z.string().optional(), // Префикс для цены (например, "от")
      badges: z.array(z.string()).optional(),
      cover: image().optional(), // Обложка теперь опциональна в каталоге
    })
  })
};
```


---

## ` src/content/excursions/elephants.md `

```md
---
title: "Као Лак + купание со слониками"
subtitle: "Лучшая экскурсия для детей"
category: "НАЗЕМНЫЕ"
priceAdult: 1600
priceChild: 1200
childAge: "4–9"
badges: ["НОВИНКА"]
cover: "../../assets/images/elephants.jpg"
---

Незабываемая прогулка и купание со слонами по настоящим джунглям Пхукета. Вы сможете покормить животных и сделать отличные фото.

Программа занимает около 45 минут. Трансфер включен.
```


---

## ` src/content/excursions/hanuman.md `

```md
---
title: "Шоу, парки и концерты"
subtitle: "Carnival, Siam Niramit, аквапарк, кабаре, экстрим и другие"
category: "НЕОБЫЧНЫЕ"
pricePrefix: "от"
priceAdult: 800
cover: "../../assets/images/hanuman.jpg"
---

Парки приключений в джунглях, Hanuman World. Полеты на тросах между деревьями, подвесные мосты и скоростные спуски.

Безопасность на высшем уровне. Подходит как для новичков, так и для любителей экстрима.
```


---

## ` src/content/excursions/james-bond.md `

```md
---
title: "4 Жемчужины Андамана"
subtitle: "Джеймс Бонд + Краби + Пхи Пхи с ночевкой"
category: "🔥 ХИТЫ 🔥"
pricePrefix: "от"
priceAdult: 5100
priceChild: 4300
childAge: "4–11"
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
title: "Острова Пхи Пхи"
subtitle: "Есть ранний выезд"
category: "🔥 ХИТЫ 🔥"
priceAdult: 2400
priceChild: 1950
childAge: "4–11"
cover: "../../assets/images/phiphi.jpg"
---

Кристально чистая вода, снорклинг, обезьяны и знаменитая бухта Майя Бэй, где снимали фильм "Пляж" с Леонардо Ди Каприо!
```


---

## ` src/content/excursions/similan.md `

```md
---
title: "Симиланские острова"
subtitle: "есть ранний выезд"
category: "МОРСКИЕ"
priceAdult: 2900
priceChild: 2300
childAge: "4–11"
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
<section class="mb-4">
  <div class="bg-[#f2fcfa] border-y border-[#d9f2ef] py-4 px-4 mb-0">
    <h2 class="text-xl font-black italic uppercase tracking-wider text-gray-800">{title}</h2>
  </div>
  <div class="flex flex-col">
    <slot />
  </div>
</section>
```


---

## ` src/components/Footer.astro `

```astro
---
---
<footer id="contacts" class="bg-[#0b172a] text-white mt-12 py-12">
  <div class="w-full max-w-[1200px] mx-auto px-4 md:px-8 flex flex-col md:flex-row justify-between items-center gap-6">
    <div class="text-center md:text-left">
      <h3 class="text-2xl font-black mb-2 uppercase tracking-wider">Bounty Tours</h3>
      <p class="text-slate-400 text-sm">Ваш надежный гид на Пхукете</p>
    </div>
    <div class="text-sm text-slate-300 text-center md:text-right">
      <p class="font-bold text-white mb-2 text-base">Контакты для связи:</p>
      <p class="mb-1">Telegram: <a href="https://t.me/+66952588444" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">+66 95 258 8444</a></p>
      <p>WhatsApp: <a href="https://wa.me/66952588444" target="_blank" rel="noopener noreferrer" class="hover:text-white transition">+66 95 258 8444</a></p>
    </div>
  </div>
</footer>
```


---

## ` src/components/Header.astro `

```astro
---
import { Image } from 'astro:assets';
import logo from '../assets/images/bounty-logo.svg';
---
<header class="bg-white shadow-sm sticky top-0 z-50">
  <div class="w-full max-w-[1200px] mx-auto px-4 md:px-8 py-4 flex justify-between items-center">
    <a href="/" class="block hover:opacity-80 transition">
      <Image src={logo} alt="Bounty Tours" class="h-10 md:h-12 w-auto object-contain" loading="eager" />
    </a>
    <a href="https://t.me/+66952588444" target="_blank" rel="noopener noreferrer" class="bg-[#00d0b5] text-white px-6 py-2.5 rounded-full text-sm font-bold hover:bg-teal-400 transition">
      Связаться
    </a>
  </div>
</header>
```


---

## ` src/components/TourRow.astro `

```astro
---
interface Props {
  id: string;
  title: string;
  subtitle?: string;
  priceAdult: number;
  priceChild?: number;
  childAge?: string;
  pricePrefix?: string;
  badges?: string[];
  isEven?: boolean;
}

const { id, title, subtitle, priceAdult, priceChild, childAge, pricePrefix = "", badges =[], isEven = false } = Astro.props;

// Чередование фона (белый и очень светло-серый)
const bgClass = isEven ? "bg-[#fafafa]" : "bg-white";
---
<!-- CSS Grid сетка, которая идеально выравнивается с шапкой в index.astro -->
<div class={`grid grid-cols-1 lg:grid-cols-[minmax(200px,_1fr)_auto_120px_120px_100px] gap-6 py-5 px-4 border-b border-gray-200 items-center transition-colors hover:bg-gray-50 ${bgClass}`}>
  
  <!-- 1. Название и подзаголовок -->
  <div class="flex flex-col">
    <h3 class="text-[17px] font-bold text-gray-700 leading-tight">{title}</h3>
    {subtitle && <p class="text-sm text-gray-500 mt-1">{subtitle}</p>}
  </div>

  <!-- 2. Кнопка -->
  <div class="w-full lg:w-[180px] mt-3 lg:mt-0">
    <a href={`/excursions/${id}`} class="block w-full text-center bg-[#00e5c9] text-white font-bold text-[13px] px-4 py-2.5 rounded hover:bg-[#00cbb2] transition-colors shadow-sm">
      Читать описание
    </a>
  </div>

  <!-- 3. Цена Взрослый (скрыто на мобильных, так как это табличный вид) -->
  <div class="hidden lg:block text-center font-bold text-gray-600">
    {pricePrefix} {priceAdult} бат
  </div>
  
  <!-- 4. Цена Ребенок -->
  <div class="hidden lg:block text-center font-bold text-gray-600">
    {priceChild ? `${pricePrefix} ${priceChild} бат` : ''}
  </div>

  <!-- 5. Возраст -->
  <div class="hidden lg:block text-center font-bold text-gray-600">
    {childAge || ''}
  </div>

  <!-- Мобильное отображение цен (только для смартфонов) -->
  <div class="grid grid-cols-3 gap-2 lg:hidden mt-4 text-xs text-center font-bold text-gray-600 bg-gray-100 p-2 rounded">
     <div>Взрослый:<br/><span class="text-gray-800 text-sm">{pricePrefix} {priceAdult} ฿</span></div>
     <div>Ребенок:<br/><span class="text-gray-800 text-sm">{priceChild ? `${pricePrefix} ${priceChild} ฿` : '-'}</span></div>
     <div>Возраст:<br/><span class="text-gray-800 text-sm">{childAge || '-'}</span></div>
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
		<!-- Главный контейнер: резиновый (w-full), макс. ширина 1200px, центрирование (mx-auto), адаптивные паддинги -->
		<main class="flex-grow w-full max-w-[1200px] mx-auto px-4 md:px-8 py-8 md:py-12">
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

const categoryOrder =[
  "🔥 ХИТЫ 🔥",
  "МОРСКИЕ",
  "НАЗЕМНЫЕ",
  "НЕОБЫЧНЫЕ"
];

const sortedCategories = Object.entries(groupedExcursions).sort(([categoryA], [categoryB]) => {
  const indexA = categoryOrder.indexOf(categoryA);
  const indexB = categoryOrder.indexOf(categoryB);
  return (indexA === -1 ? 999 : indexA) - (indexB === -1 ? 999 : indexB);
});
---

<Layout title="Bounty Tours | Экскурсии на Пхукете">
  <div class="mb-14 flex flex-col items-center text-center mt-4">
    <h1 class="text-5xl md:text-7xl font-black mb-8 text-black tracking-tight">
      Экскурсии на Пхукете
    </h1>

    <!-- Блок ссылок на мессенджеры -->
    <div class="flex flex-col md:flex-row items-center justify-center gap-4 md:gap-6 text-lg md:text-xl font-bold text-gray-900">
      <span>Бронируйте в Telegram или Whatsapp</span>
      
      <div class="flex items-center gap-3">
        <!-- Кнопка Telegram -->
        <a href="https://t.me/+66952588444" target="_blank" rel="noopener noreferrer" class="bg-[#0088cc] hover:bg-[#007ab8] text-white text-sm md:text-base py-2.5 px-5 rounded-full transition duration-300 shadow-sm flex items-center gap-2">
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.894 8.221l-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.446 1.394c-.14.18-.357.295-.6.295-.002 0-.003 0-.005 0l.213-3.054 5.56-5.022c.24-.213-.054-.334-.373-.121l-6.869 4.326-2.96-.924c-.64-.203-.658-.64.135-.954l11.566-4.458c.538-.196 1.006.128.832.94z"/></svg>
          Telegram
        </a>
        
        <!-- Кнопка WhatsApp -->
        <a href="https://wa.me/66952588444" target="_blank" rel="noopener noreferrer" class="bg-[#25D366] hover:bg-[#20bd5a] text-white text-sm md:text-base py-2.5 px-5 rounded-full transition duration-300 shadow-sm flex items-center gap-2">
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M11.996 0A12 12 0 0 0 0 12a11.968 11.968 0 0 0 1.611 6.002L0 24l6.155-1.614A11.966 11.966 0 0 0 11.996 24C18.621 24 24 18.62 24 12c0-6.621-5.379-12-12.004-12zm6.758 17.21c-.287.808-1.666 1.543-2.317 1.63-.538.071-1.22.146-3.82-1.026-3.328-1.493-5.467-4.93-5.632-5.155-.164-.225-1.344-1.787-1.344-3.411 0-1.624.84-2.42 1.139-2.736.298-.316.646-.395.861-.395.215 0 .43.002.616.012.203.01.472-.08.736.56.275.666.896 2.18.975 2.338.08.158.132.343.032.553-.1.21-.151.342-.298.513-.146.171-.314.368-.445.513-.146.158-.303.333-.122.65.18.315.803 1.328 1.716 2.146 1.18.10.6 2.158 2.502.43.145.556.342.731.25.908-.092 1.077.29 1.164.5.342.544.757 1.054.896 1.054.14 0 .341-.053.473-.25.132-.198.537-.633.684-.85.146-.217.292-.18.528-.093.236.086 1.494.704 1.751.81.258.106.43.158.494.246.064.088.064.513-.223 1.321z"/></svg>
          WhatsApp
        </a>
      </div>
    </div>

  </div>

  <!-- ШАПКА ТАБЛИЦЫ (скрыта на мобилках) -->

<div class="hidden lg:grid grid-cols-[minmax(200px,_1fr)_auto_120px_120px_100px] gap-6 pt-4 pb-2 border-t border-gray-800 mb-6 font-bold text-[13px] text-gray-800 items-end">
  <div class="pl-4">Название экскурсии</div>
  <div class="w-[180px]"></div> <!-- Пустое место над кнопкой -->
  <div class="text-center leading-tight">Стоимость<br>(взрослый)</div>
  <div class="text-center leading-tight">Стоимость<br>(ребенок)</div>
  <div class="text-center leading-tight">Возраст<br>ребенка</div>
</div>

  <!-- Выводим уже отсортированные категории -->
  <div class="flex flex-col gap-8">
    {sortedCategories.map(([category, tours]) => (
      <CategorySection title={category}>
        <div class="flex flex-col">
          {tours.map((tour, index) => (
            <TourRow 
              id={tour.id} 
              title={tour.data.title} 
              subtitle={tour.data.subtitle}
              priceAdult={tour.data.priceAdult} 
              priceChild={tour.data.priceChild}
              childAge={tour.data.childAge}
              pricePrefix={tour.data.pricePrefix}
              badges={tour.data.badges}
              isEven={index % 2 !== 0} 
            />
          ))}
        </div>
      </CategorySection>
    ))}
  </div>
</Layout>
```


---

## ` src/pages/excursions/[id].astro `

```astro
---
import Layout from "../../layouts/Layout.astro";
import { getCollection, render } from "astro:content";
import { Image } from "astro:assets";

export async function getStaticPaths() {
  const excursions = await getCollection("excursions");
  return excursions.map((post) => ({
    params: { id: post.id },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await render(post);
---

<Layout title={`${post.data.title} | Bounty Tours`}>
  <div class="mb-6">
    <a
      href="/"
      class="text-blue-600 text-sm font-bold hover:underline inline-flex items-center gap-1 transition"
    >
      <span class="text-lg leading-none">←</span> Назад в каталог
    </a>
  </div>

  <!-- Баннер -->
  <div
    class="rounded-2xl overflow-hidden mb-8 h-64 md:h-96 w-full relative shadow-lg group"
  >
    {
      post.data.cover && (
        <Image
          src={post.data.cover}
          alt={post.data.title}
          class="w-full h-full object-cover transition duration-700 group-hover:scale-105"
          width={1200}
          height={600}
          loading="eager"
        />
      )
    }
    <div
      class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent"
    >
    </div>
    <div class="absolute bottom-0 left-0 p-6 md:p-10 text-white w-full">
      {
        post.data.badges && post.data.badges.length > 0 && (
          <div class="flex flex-wrap gap-2 mb-3">
            {post.data.badges.map((badge) => (
              <span class="bg-blue-600 text-white text-[11px] font-bold px-3 py-1 rounded-full uppercase tracking-wider shadow-sm">
                {badge}
              </span>
            ))}
          </div>
        )
      }
      <h1
        class="text-3xl md:text-5xl font-black uppercase tracking-wider drop-shadow-lg leading-tight"
      >
        {post.data.title}
      </h1>
    </div>
  </div>

  <div
    class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 md:p-10 mb-10"
  >
    <!-- Блок с ценой -->
    <div
      class="bg-blue-50/50 rounded-xl p-4 md:p-6 mb-8 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border border-blue-100"
    >
      <div>
        <span
          class="block text-[11px] text-gray-500 uppercase tracking-wider font-bold mb-1"
          >Стоимость (Взрослый)</span
        >
        <span class="text-4xl font-black text-gray-900"
          >{post.data.pricePrefix || ""} {post.data.priceAdult} ฿</span
        >
      </div>
      <a
        href="#booking"
        class="bg-blue-600 text-white px-8 py-4 rounded-xl font-bold hover:bg-blue-700 transition w-full md:w-auto text-center shadow-lg shadow-blue-200"
      >
        Забронировать
      </a>
    </div>

    <!-- Текст из Markdown -->
    <div class="markdown-content text-gray-700 leading-relaxed text-lg">
      <Content />
    </div>

    <!-- Контакты для бронирования (ВМЕСТО ФОРМЫ) -->
    <div id="booking" class="mt-12 pt-10 border-t border-gray-100">
      <h2
        class="text-2xl font-black uppercase tracking-wider mb-2 text-center md:text-left text-gray-900"
      >
        Бронирование
      </h2>
      <p class="text-gray-500 mb-8 text-center md:text-left">
        Для бронирования экскурсии свяжитесь с нами в любом удобном мессенджере.
        Мы ответим в течение 5 минут.
      </p>

      <div class="flex flex-col sm:flex-row gap-4">
        <!-- Кнопка Telegram -->
        <a
          href="https://t.me/+66952588444"
          target="_blank"
          rel="noopener noreferrer"
          class="flex-1 bg-[#0088cc] hover:bg-[#007ab8] text-white text-center font-bold py-4 px-6 rounded-xl transition duration-300 shadow-md flex items-center justify-center gap-3"
        >
          <svg
            class="w-6 h-6 fill-current"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            ><path
              d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.894 8.221l-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.446 1.394c-.14.18-.357.295-.6.295-.002 0-.003 0-.005 0l.213-3.054 5.56-5.022c.24-.213-.054-.334-.373-.121l-6.869 4.326-2.96-.924c-.64-.203-.658-.64.135-.954l11.566-4.458c.538-.196 1.006.128.832.94z"
            ></path></svg
          >
          Написать в Telegram
        </a>

        <!-- Кнопка WhatsApp -->
        <a
          href="https://wa.me/66952588444"
          target="_blank"
          rel="noopener noreferrer"
          class="flex-1 bg-[#25D366] hover:bg-[#20bd5a] text-white text-center font-bold py-4 px-6 rounded-xl transition duration-300 shadow-md flex items-center justify-center gap-3"
        >
          <svg
            class="w-6 h-6 fill-current"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            ><path
              d="M11.996 0A12 12 0 0 0 0 12a11.968 11.968 0 0 0 1.611 6.002L0 24l6.155-1.614A11.966 11.966 0 0 0 11.996 24C18.621 24 24 18.62 24 12c0-6.621-5.379-12-12.004-12zm6.758 17.21c-.287.808-1.666 1.543-2.317 1.63-.538.071-1.22.146-3.82-1.026-3.328-1.493-5.467-4.93-5.632-5.155-.164-.225-1.344-1.787-1.344-3.411 0-1.624.84-2.42 1.139-2.736.298-.316.646-.395.861-.395.215 0 .43.002.616.012.203.01.472-.08.736.56.275.666.896 2.18.975 2.338.08.158.132.343.032.553-.1.21-.151.342-.298.513-.146.171-.314.368-.445.513-.146.158-.303.333-.122.65.18.315.803 1.328 1.716 2.146 1.18.10.6 2.158 2.502.43.145.556.342.731.25.908-.092 1.077.29 1.164.5.342.544.757 1.054.896 1.054.14 0 .341-.053.473-.25.132-.198.537-.633.684-.85.146-.217.292-.18.528-.093.236.086 1.494.704 1.751.81.258.106.43.158.494.246.064.088.064.513-.223 1.321z"
            ></path></svg
          >
          Написать в WhatsApp
        </a>
      </div>
    </div>
  </div>
</Layout>

<style is:global>
  .markdown-content p {
    margin-bottom: 1.5rem;
  }
  .markdown-content h2 {
    font-size: 1.5rem;
    font-weight: 900;
    margin-top: 2.5rem;
    margin-bottom: 1rem;
    text-transform: uppercase;
    color: #111827;
    letter-spacing: 0.05em;
  }
  .markdown-content h3 {
    font-size: 1.25rem;
    font-weight: 800;
    margin-top: 2rem;
    margin-bottom: 0.75rem;
    color: #1f2937;
  }
  .markdown-content ul {
    list-style-type: none;
    padding-left: 0;
    margin-bottom: 1.5rem;
  }
  .markdown-content li {
    margin-bottom: 0.75rem;
    padding-left: 1.5rem;
    position: relative;
  }
  .markdown-content li::before {
    content: "•";
    color: #2563eb;
    font-weight: bold;
    position: absolute;
    left: 0;
    font-size: 1.2em;
    line-height: 1;
  }
  .markdown-content strong {
    color: #111827;
    font-weight: 800;
  }
</style>

```
