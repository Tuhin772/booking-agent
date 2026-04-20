import express from 'express'
import fetch from 'node-fetch'

const router = express.Router()

router.post('/', async (req, res) => {
  const { message, session_id } = req.body

  try {
    const response = await fetch('http://localhost:8000/agent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, session_id })
    })

    const data = await response.json()
    res.json(data)
  } catch (err) {
    res.status(500).json({ error: 'AI service unavailable' })
  }
})

export default router