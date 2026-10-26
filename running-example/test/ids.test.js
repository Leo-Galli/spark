import test from 'node:test'
import assert from 'node:assert/strict'
import { slugify, assignIds } from '../dist/ids.js'

test('slugify', () => {
  assert.equal(slugify('Write Demo'), 'write-demo')
})

test('assignIds avoids collisions', () => {
  const out = assignIds([
    { done: false, text: 'Write Demo', line: 1 },
    { done: false, text: 'Write Demo', line: 2 },
  ])
  assert.equal(out[0].id, 'write-demo')
  assert.equal(out[1].id, 'write-demo-2')
})
