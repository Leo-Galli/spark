import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('ranks by score desc', () => {
  assert.deepEqual(solve([{ id: 'a', score: 2 }, { id: 'b', score: 5 }]), ['b', 'a'])
})
