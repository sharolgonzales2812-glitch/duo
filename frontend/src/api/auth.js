/**
 * api/auth.js — Llamadas a la API de autenticación.
 * Todas las funciones usan axios y apuntan al backend Django.
 */

import axios from 'axios'

const BASE_URL = '/api'

/** Obtiene tokens JWT (login). */
export async function loginApi(username, password) {
  const resp = await axios.post(`${BASE_URL}/auth/login/`, { username, password })
  return resp.data
}

/** Cierra sesión (blacklist del refresh token). */
export async function logoutApi(refreshToken) {
  return axios.post(`${BASE_URL}/auth/logout/`, { refresh: refreshToken })
}

/** Refresca el access token con el refresh token. */
export async function refreshTokenApi(refreshToken) {
  const resp = await axios.post(`${BASE_URL}/auth/refresh/`, { refresh: refreshToken })
  return resp.data
}

/** Registra un nuevo usuario. */
export async function registroApi(datos) {
  const resp = await axios.post(`${BASE_URL}/accounts/registro/`, datos)
  return resp.data
}

/** Obtiene el perfil del usuario autenticado. */
export async function getPerfilApi(token) {
  const resp = await axios.get(`${BASE_URL}/accounts/perfil/`, {
    headers: { Authorization: `Bearer ${token}` },
  })
  return resp.data
}
