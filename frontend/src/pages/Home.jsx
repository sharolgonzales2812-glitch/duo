/**
 * Home.jsx — Página de inicio de skincaremaysha.
 * Muestra el hero de la plataforma y acceso a login/registro.
 */

import { Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext.jsx'

export default function Home() {
  const { token } = useAuth()

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-secundario px-4">
      <h1 className="font-titulo text-4xl text-texto mb-2">skincaremaysha</h1>
      <p className="text-texto-suave text-center max-w-md mb-8">
        Análisis facial inteligente con IA. Descubre tu tipo de piel,
        detecta problemas y recibe rutinas personalizadas.
      </p>

      {token ? (
        <Link
          to="/escaneo"
          className="bg-primario hover:bg-primario-dark text-white px-6 py-3 rounded-xl font-medium transition"
        >
          Iniciar escaneo facial
        </Link>
      ) : (
        <div className="flex gap-4">
          <Link
            to="/login"
            className="bg-primario hover:bg-primario-dark text-white px-6 py-3 rounded-xl font-medium transition"
          >
            Iniciar sesión
          </Link>
          <Link
            to="/registro"
            className="border border-primario text-primario hover:bg-primario hover:text-white px-6 py-3 rounded-xl font-medium transition"
          >
            Registrarse
          </Link>
        </div>
      )}
    </main>
  )
}
