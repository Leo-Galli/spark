import test from 'node:test'
import assert from 'node:assert/strict'
import { solve } from '../starter/solve.mjs'

test('MIT ok', () => { assert.equal(solve('MIT'), true) })

test('spaces fail', () => { assert.equal(solve('MIT OR Apache'), false) })
