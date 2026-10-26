import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('packet statuses', () => {
  assert.equal(solve('scoped'), true)
  assert.equal(solve('done'), false)
})
