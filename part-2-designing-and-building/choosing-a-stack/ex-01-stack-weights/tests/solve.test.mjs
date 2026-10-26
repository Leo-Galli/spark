import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('stack weighted total', () => {
  assert.equal(solve({ weights: { familiarity: 25 }, scores: { familiarity: 5 } }), 125)
})
