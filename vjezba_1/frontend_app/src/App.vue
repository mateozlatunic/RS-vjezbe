<script setup>
import { ref, onMounted } from 'vue'

const API = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'
const items = ref([])
const name = ref('')
const error = ref('')
const podaci = ref(null)
const podaciError = ref('')

async function loadPodaci() {
  try {
    podaciError.value = ''
    const res = await fetch(`${import.meta.env.BASE_URL}podaci.json`)
    podaci.value = await res.json()
  } catch (e) {
    podaciError.value = 'Ne mogu učitati podaci.json.'
  }
}

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

onMounted(() => {
  load()
  loadPodaci()
})
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

        <section v-if="podaci">
      <h2>Jelovnik</h2>
      <ul>
        <li v-for="j in podaci.jelovnik" :key="j.id">
          {{ j.naziv }} — {{ j.cijena.toFixed(2) }} €
        </li>
      </ul>

      <h2>Recenzije</h2>
      <ul>
        <li v-for="r in podaci.recenzije" :key="r.gost">
          <strong>{{ r.gost }}</strong> ({{ r.ocjena }}/5): {{ r.komentar }}
        </li>
      </ul>

      <h2>Stolovi</h2>
      <ul>
        <li v-for="s in podaci.stolovi" :key="s.oznaka">
          {{ s.oznaka }}: {{ s.slobodna_mjesta }} slobodnih mjesta
        </li>
      </ul>
    </section>
    <p v-if="podaciError">{{ podaciError }}</p>

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