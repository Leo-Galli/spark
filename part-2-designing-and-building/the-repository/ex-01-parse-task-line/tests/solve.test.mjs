import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('parses open task', () => {
  assert.deepEqual(solve('- [ ] Write demo'), { done: false, text: 'Write demo' })
})

test('parses done task', () => {
  assert.deepEqual(solve('- [x] Ship'), { done: true, text: 'Ship' })
})

test('rejects non-task', () => {
  assert.equal(solve('hello'), null)
})
