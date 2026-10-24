<script setup>
import { ref, onMounted } from 'vue'

const API = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'
const items = ref([])
const name = ref('')
const error = ref('')

async function load() {
  try {
    error.value = ''
    const res = await fetch(`${API}/items`)
    items.value = await res.json()
  } catch (e) {
    error.value = 'Ne mogu se spojiti na backend. Ako je na Renderu, pričekaj do minutu da se probudi.'
  }
}

async function add() {
  if (!name.value.trim()) return
  await fetch(`${API}/items`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: name.value }),
  })
  name.value = ''
  load()
}

async function remove(id) {
  await fetch(`${API}/items/${id}`, { method: 'DELETE' })
  load()
}

onMounted(load)
</script>

<template>
  <main>
    <h1>Stavke</h1>

    <form @submit.prevent="add">
      <input v-model="name" placeholder="Nova stavka" />
      <button type="submit">Dodaj</button>
    </form>

    <p v-if="error">{{ error }}</p>

    <ul>
      <li v-for="i in items" :key="i.id">
        {{ i.name }}
        <button @click="remove(i.id)">Obriši</button>
      </li>
    </ul>
  </main>
</template>

<style scoped>
main {
  max-width: 500px;
  margin: 2rem auto;
  padding: 0 1rem;
}
li {
  margin: 0.5rem 0;
}
</style>