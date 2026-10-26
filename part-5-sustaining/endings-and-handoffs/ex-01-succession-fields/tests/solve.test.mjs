import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('succession note fields', () => {
  assert.equal(solve({ status: 'seeking', contact: 'issues', artifacts: 'README+SECURITY' }).ok, true)
})
