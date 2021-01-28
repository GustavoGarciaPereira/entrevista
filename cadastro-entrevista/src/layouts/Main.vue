<template>
  <ul>
    <li><v-link href="/entrevista/cadastro/">Cadastro</v-link></li>
    <li><v-link href="/entrevista/listagem/">Listagem</v-link></li>
  </ul>

  <slot></slot>
</template>

<script>
import VLink from '../components/VLink.vue'
export default {
  components: {
    VLink
  }
}
</script>