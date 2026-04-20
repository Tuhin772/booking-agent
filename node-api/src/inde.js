import express from 'express'
import cors from 'cors'
import chatRoutes from './routes/chat.js'
import bookingRoutes from './routes/bookings.js'
import slotRoutes from './routes/slots.js'

const app = express()
app.use(cors())
app.use(express.json())

app.use('/api/chat', chatRoutes)
app.use('/api/bookings', bookingRoutes)
app.use('/api/slots', slotRoutes)

app.listen(3000, () => console.log('Node API running on :3000'))