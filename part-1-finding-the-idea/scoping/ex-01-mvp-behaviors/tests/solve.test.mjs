import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('mvp disjoint from out', () => {
  assert.equal(solve({ mvp: ['status'], outOfMvp: ['plugins'] }).ok, true)
})

test('overlap fails', () => {
  assert.equal(solve({ mvp: ['plugins'], outOfMvp: ['plugins'] }).ok, false)
})
