import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('release first', () => {
  assert.deepEqual(solve({ release: true, showHn: true }), ['release', 'show-hn'])
})
