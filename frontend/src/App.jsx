import { Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext.jsx'
import Home from './pages/Home.jsx'
import Login from './pages/Login.jsx'
import Registro from './pages/Registro.jsx'

/**
 * App.jsx — Enrutador principal de skincaremaysha.
 * Las rutas adicionales (Escaneo, Diagnóstico, Rutina, etc.)
 * se agregan en sus sprints correspondientes.
 */
function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/"         element={<Home />} />
        <Route path="/login"    element={<Login />} />
        <Route path="/registro" element={<Registro />} />
        {/* Ruta 404 → home */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </AuthProvider>
  )
}

export default App
