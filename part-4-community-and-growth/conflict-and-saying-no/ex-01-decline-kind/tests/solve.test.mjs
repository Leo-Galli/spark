import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('known decline kinds', () => {
  assert.equal(solve('out-of-scope'), true)
  assert.equal(solve('rude'), false)
})
