export const CATEGORIES = {
  'habits': { name: 'Habits', slug: 'habits', description: 'Daily habits for a longer life' },
  'nutrition': { name: 'Nutrition', slug: 'nutrition', description: 'Foods that extend your lifespan' },
  'exercise': { name: 'Exercise', slug: 'exercise', description: 'Move to live longer' },
  'sleep': { name: 'Sleep', slug: 'sleep', description: 'Sleep science for longevity' },
  'aging-science': { name: 'Aging Science', slug: 'aging-science', description: 'Cutting-edge aging research' }
} as const;

export type Category = keyof typeof CATEGORIES;

export function getCategoryName(cat: Category): string {
  return CATEGORIES[cat].name;
}

export function getCategoryBadgeClass(cat: Category): string {
  return `badge badge--${cat}`;
}
