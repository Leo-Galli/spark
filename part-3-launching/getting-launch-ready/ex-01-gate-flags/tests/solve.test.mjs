import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('all flags required', () => {
  assert.equal(solve({ demoOk: true, ciGreen: true, changelogHonest: true, securityLive: true }), true)
  assert.equal(solve({ demoOk: true, ciGreen: true, changelogHonest: true, securityLive: false }), false)
})
