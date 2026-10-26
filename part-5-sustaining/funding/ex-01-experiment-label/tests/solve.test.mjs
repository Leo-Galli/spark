import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('funding labels', () => {
  assert.equal(solve('sponsors'), true)
  assert.equal(solve('ads'), false)
})
