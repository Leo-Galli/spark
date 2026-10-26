import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('detects token assignment', () => {
  assert.equal(solve('API_KEY=abc123'), true)
  assert.equal(solve('const x = 1'), false)
})
