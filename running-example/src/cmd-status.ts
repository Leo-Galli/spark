import { readChecklist } from "./read-checklist.js"
import { parseTasks } from "./parse-tasks.js"
import { assignIds } from "./ids.js"
import { formatStatus } from "./format-report.js"

export const runStatus = (file: string): string => {
  const md = readChecklist(file)
  const tasks = assignIds(parseTasks(md))
  return formatStatus(tasks)
}
