export const formatError = (message: string): string => `error: ${message}`

export const formatDuplicateIdError = (id: string): string =>
  `error: duplicate id "${id}" -- give each marker a unique {id:...} value`
