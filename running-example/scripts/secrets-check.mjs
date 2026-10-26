import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const pattern = /(api[_-]?key|secret|token|password)\s*=\s*\S+/i
let bad = false
for (const dir of ['src', 'test', 'examples', 'scripts']) {
  const base = path.join(root, dir)
  if (!fs.existsSync(base)) continue
  for (const f of fs.readdirSync(base)) {
    const p = path.join(base, f)
    if (!fs.statSync(p).isFile()) continue
    const text = fs.readFileSync(p, 'utf8')
    if (pattern.test(text)) {
      console.error('possible secret assignment in', p)
      bad = true
    }
  }
}
if (bad) process.exit(1)
console.log('secrets:check ok')
