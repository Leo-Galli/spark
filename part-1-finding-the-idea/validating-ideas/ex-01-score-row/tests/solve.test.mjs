import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('weighted score', () => {
  assert.equal(solve({ weights: { a: 2, b: 3 }, scores: { a: 4, b: 5 } }), 23)
})
