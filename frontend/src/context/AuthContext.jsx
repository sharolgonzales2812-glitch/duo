import { createContext, useContext, useState, useEffect } from 'react'
import { loginApi, registroApi } from '../api/auth.js'

/**
 * AuthContext — Estado global de autenticación.
 * Provee: usuario, token, login(), logout(), registro(), cargando
 */
const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [usuario, setUsuario] = useState(null)
  const [token, setToken]     = useState(() => localStorage.getItem('access_token'))
  const [cargando, setCargando] = useState(false)

  // Persistir token en localStorage
  useEffect(() => {
    if (token) {
      localStorage.setItem('access_token', token)
    } else {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    }
  }, [token])

  const login = async (username, password) => {
    setCargando(true)
    try {
      const data = await loginApi(username, password)
      setToken(data.access)
      localStorage.setItem('refresh_token', data.refresh)
      setUsuario(data.usuario ?? null)
      return { ok: true }
    } catch (error) {
      return { ok: false, error: error.response?.data ?? 'Error de conexión' }
    } finally {
      setCargando(false)
    }
  }

  const logout = () => {
    setToken(null)
    setUsuario(null)
  }

  const registro = async (datos) => {
    setCargando(true)
    try {
      const data = await registroApi(datos)
      return { ok: true, data }
    } catch (error) {
      return { ok: false, error: error.response?.data ?? 'Error de conexión' }
    } finally {
      setCargando(false)
    }
  }

  return (
    <AuthContext.Provider value={{ usuario, token, cargando, login, logout, registro }}>
      {children}
    </AuthContext.Provider>
  )
}

// Hook de acceso rápido
export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth debe usarse dentro de AuthProvider')
  return ctx
}
