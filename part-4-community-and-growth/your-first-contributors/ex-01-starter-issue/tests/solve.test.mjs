import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('starter issue fields', () => {
  assert.equal(solve({ title: 'Clearer error', path: 'src/format-errors.ts', acceptance: 'test fails then passes' }).ok, true)
})
