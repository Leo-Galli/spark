import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('adapt requires rewrite', () => {
  assert.equal(solve({ seedProblem: 'A', problemOwnWords: 'B', usersOwnWords: 'C' }).ok, true)
  assert.equal(solve({ seedProblem: 'A', problemOwnWords: 'A', usersOwnWords: 'C' }).ok, false)
})
