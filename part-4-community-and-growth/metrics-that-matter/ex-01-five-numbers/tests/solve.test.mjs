import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('five numbers present', () => {
  assert.equal(solve({ openIssues: 3, medianFirstResponseDays: 2, returningContributors: 1, hoursSpent: 3, releases: 1 }), true)
})
