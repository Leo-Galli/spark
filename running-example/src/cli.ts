#!/usr/bin/env node
import { parseArgs } from "./parse-args.js"
import { runStatus } from "./cmd-status.js"
import { runCheck } from "./cmd-check.js"
import { formatError } from "./format-errors.js"

const main = (): void => {
  try {
    const parsed = parseArgs(process.argv)
    if (parsed.command === "help") {
      console.log("Usage: tickdown <status|check> <file.md>")
      process.exit(0)
    }
    if (parsed.command === "status" && parsed.file) {
      console.log(runStatus(parsed.file))
      process.exit(0)
    }
    if (parsed.command === "check" && parsed.file) {
      const result = runCheck(parsed.file)
      console.log(result.text)
      process.exit(result.ok ? 0 : 1)
    }
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err)
    console.error(formatError(message))
    process.exit(2)
  }
}

main()
