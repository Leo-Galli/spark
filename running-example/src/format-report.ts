import type { Task } from "./parse-tasks.js"

export const formatStatus = (tasks: Array<Task & { id: string }>): string => {
  const open = tasks.filter((t) => !t.done)
  const done = tasks.filter((t) => t.done)
  const lines = [
    `open: ${open.length}`,
    `done: ${done.length}`,
    ...open.map((t) => `- [ ] ${t.id} ${t.text}`),
  ]
  return lines.join("\n")
}
