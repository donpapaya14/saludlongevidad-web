export const CATEGORIES = {
  'habitos': { name: 'Habitos', slug: 'habitos', description: 'Habitos diarios para vivir mas y mejor' },\n  'nutricion': { name: 'Nutricion', slug: 'nutricion', description: 'Alimentacion para la longevidad con ciencia' },\n  'ejercicio': { name: 'Ejercicio', slug: 'ejercicio', description: 'Movimiento minimo efectivo para longevidad' },\n  'sueno': { name: 'Sueno', slug: 'sueno', description: 'Optimizar el sueno para la salud' },\n  'ciencia': { name: 'Ciencia', slug: 'ciencia', description: 'Ultimos avances en investigacion del envejecimiento' },
} as const;

export type Category = keyof typeof CATEGORIES;

export function getCategoryName(cat: Category): string {
  return CATEGORIES[cat].name;
}

export function getCategoryBadgeClass(cat: Category): string {
  return `badge badge--${cat}`;
}
