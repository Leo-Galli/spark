import type { Task } from "./parse-tasks.js"

export const slugify = (text: string): string => {
  const base = text.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 24)
  return base || "task"
}

export const assignIds = (tasks: Task[]): Array<Task & { id: string }> => {
  const seen = new Set<string>()
  return tasks.map((t) => {
    let id = t.markerId || slugify(t.text)
    let n = 2
    while (seen.has(id)) {
      id = `${t.markerId || slugify(t.text)}-${n}`
      n += 1
    }
    seen.add(id)
    return { ...t, id }
  })
}

export const findDuplicateMarkers = (tasks: Task[]): string[] => {
  const counts = new Map<string, number>()
  for (const t of tasks) {
    if (!t.markerId) continue
    counts.set(t.markerId, (counts.get(t.markerId) || 0) + 1)
  }
  return [...counts.entries()].filter(([, n]) => n > 1).map(([id]) => id)
}
