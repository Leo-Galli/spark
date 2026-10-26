import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('idea card complete', () => {
  const r = solve({ id: 'IDEA-001', problem: 'leftover pain', users: 'small teams', mvp: 'status+check' })
  assert.equal(r.ok, true)
})

test('blank problem fails', () => {
  const r = solve({ id: 'IDEA-001', problem: '  ', users: 'x', mvp: 'y' })
  assert.equal(r.ok, false)
})
