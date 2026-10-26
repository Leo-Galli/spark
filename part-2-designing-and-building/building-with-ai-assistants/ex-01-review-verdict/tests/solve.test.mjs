import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('accepts clean review', () => {
  assert.equal(solve({ diff: 'x', checks: { secrets: false, fenceBroken: false, testsPass: true } }), 'accept')
})

test('rejects secrets', () => {
  assert.equal(solve({ diff: 'x', checks: { secrets: true, fenceBroken: false, testsPass: true } }), 'reject')
})
