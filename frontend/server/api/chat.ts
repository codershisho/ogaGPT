export default defineEventHandler(async (event) => {
    const body = await readBody(event)
    const res = await $fetch('http://localhost:8000/chat', {
      method: 'POST',
      body,
    })
    return res
  })
  