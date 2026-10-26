import test from 'node:test'
import assert from 'node:assert/strict'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { runCheck } from '../dist/cmd-check.js'

const root = path.dirname(fileURLToPath(import.meta.url))

test('check ok on sprint', () => {
  const r = runCheck(path.join(root, '../examples/sprint.md'))
  assert.equal(r.ok, true)
})

test('check fails on duplicate markers', () => {
  const r = runCheck(path.join(root, '../examples/dup.md'))
  assert.equal(r.ok, false)
  assert.match(r.text, /duplicate id/)
})
