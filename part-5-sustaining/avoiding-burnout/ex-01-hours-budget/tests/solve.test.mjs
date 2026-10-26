import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('budget needs loser', () => {
  assert.equal(solve({ weeklyHours: 3, loserActivity: 'language class' }), true)
  assert.equal(solve({ weeklyHours: 3 }), false)
})
