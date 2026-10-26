import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('definition requires commercial use', () => {
  const r = solve({ use: true, study: true, modify: true, share: true, commercial: true })
  assert.equal(r.ok, true)
  assert.deepEqual(r.missing, [])
})

test('missing commercial fails', () => {
  const r = solve({ use: true, study: true, modify: true, share: true })
  assert.equal(r.ok, false)
  assert.ok(r.missing.includes('commercial'))
})
