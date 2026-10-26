import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('valid statuses', () => {
  assert.equal(solve('accepted'), true)
  assert.equal(solve('maybe'), false)
})
