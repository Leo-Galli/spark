import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('flags hype', () => {
  assert.deepEqual(solve(['local status', 'seamless sync']), ['seamless sync'])
})
