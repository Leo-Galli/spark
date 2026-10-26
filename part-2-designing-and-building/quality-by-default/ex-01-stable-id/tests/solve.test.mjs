import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('stable slug', () => {
  assert.equal(solve('Write Demo'), 'write-demo')
})

test('avoids collision', () => {
  assert.equal(solve('Write Demo', ['write-demo']), 'write-demo-2')
})
