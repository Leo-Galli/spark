import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('governance owner fields', () => {
  assert.equal(solve({ merger: 'Sam', stuckCall: 'public comment', revisitTriggers: ['second merger'] }).ok, true)
})
