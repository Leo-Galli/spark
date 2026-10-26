export type Task = {
  done: boolean
  text: string
  markerId?: string
  line: number
}

const TASK_RE = /^(\s*)-\s*\[([ xX])\]\s+(?:\{id:([^}]+)\}\s*)?(.*)$/

export const parseTasks = (markdown: string): Task[] => {
  const tasks: Task[] = []
  const lines = markdown.split(/\r?\n/)
  lines.forEach((line, idx) => {
    const m = line.match(TASK_RE)
    if (!m) return
    tasks.push({
      done: m[2].toLowerCase() === "x",
      text: m[4].trim(),
      markerId: m[3]?.trim() || undefined,
      line: idx + 1,
    })
  })
  return tasks
}
