export type Command = "status" | "check" | "help"

export type ParsedArgs = {
  command: Command
  file?: string
}

export const parseArgs = (argv: string[]): ParsedArgs => {
  const args = argv.slice(2)
  if (args.length === 0 || args[0] === "help" || args[0] === "--help") {
    return { command: "help" }
  }
  const command = args[0]
  if (command !== "status" && command !== "check") {
    throw new Error(`unknown command: ${command}`)
  }
  const file = args[1]
  if (!file) {
    throw new Error(`${command} requires a Markdown file path`)
  }
  return { command, file }
}
