import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('rejects costume folders', () => {
  assert.equal(solve(['cli', 'parse-tasks']).ok, true)
  assert.equal(solve(['plugins']).ok, false)
})
