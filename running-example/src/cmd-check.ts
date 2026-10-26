import { readChecklist } from "./read-checklist.js"
import { parseTasks } from "./parse-tasks.js"
import { findDuplicateMarkers } from "./ids.js"
import { formatDuplicateIdError } from "./format-errors.js"

export const runCheck = (file: string): { ok: boolean; text: string } => {
  const md = readChecklist(file)
  const tasks = parseTasks(md)
  const dups = findDuplicateMarkers(tasks)
  if (dups.length) {
    return { ok: false, text: dups.map(formatDuplicateIdError).join("\n") }
  }
  return { ok: true, text: `ok: ${tasks.length} tasks` }
}
