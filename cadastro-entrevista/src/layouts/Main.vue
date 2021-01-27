<template>
  <ul>
    <li><v-link href="/">Home</v-link></li>
    <li><v-link href="/cadastro">Cadastro</v-link></li>
    <li><v-link href="/listagem">Listagem</v-link></li>
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
<!-- Add "scoped" attribute to limit CSS to this component only -->
