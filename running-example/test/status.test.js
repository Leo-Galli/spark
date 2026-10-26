import test from 'node:test'
import assert from 'node:assert/strict'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { runStatus } from '../dist/cmd-status.js'

const root = path.dirname(fileURLToPath(import.meta.url))
const sample = path.join(root, '../examples/sprint.md')

test('status counts open and done', () => {
  const out = runStatus(sample)
  assert.match(out, /open: 2/)
  assert.match(out, /done: 1/)
})
