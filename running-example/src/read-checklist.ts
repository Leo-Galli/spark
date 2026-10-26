import fs from "node:fs"

export const readChecklist = (filePath: string): string => {
  if (!fs.existsSync(filePath)) {
    throw new Error(`file not found: ${filePath}`)
  }
  return fs.readFileSync(filePath, "utf8")
}
