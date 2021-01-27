
<template>
    <p>Liatagem</p>
    <a href="/cadastro">Cadastrar novo usuário</a>
    Search <input name="query" v-model="searchQuery" />
  
      <!-- em interpolações de texto 
      <p>{{ $filters.capitalize("accountBalance") }}</p>

-->
        <table>
        <thead>
          <tr>
            <th v-for="key in columns" :key="key">
                {{ key }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr  v-for="item in filteredHeroes" :key="item.id">
            <td v-for="key in columns" :key="key">
                {{ item[key]}}
            </td>
          </tr>
        </tbody>
      </table>


    

</template>

<script>
export default {
  components: {

  },

  data(){
    return{
      lista_pessoas:[],
      columns:['created','nome','idade','telefone'],
      searchQuery: "",
      filteredHeroes:[]
    }

  },

  mounted(){
    this.listar()
    
  },

  methods:{

    async listar(){
        const pessoas = await this.axios.get('http://127.0.0.1:8000/usuario/lista-usario/').then((response) => {
          //console.log("fu",response.data)
        return response.data
      })
      this.filteredHeroes = pessoas
      return this.lista_pessoas = pessoas
    }
  },
  filters: {
      capitalize(value) {
        console.log(">>",value)
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      }
    }


}



</script>
<style scoped>
body {
  font-family: Helvetica Neue, Arial, sans-serif;
  font-size: 14px;
  color: #444;
}

table {
  border: 2px solid #42b983;
  border-radius: 3px;
  background-color: #fff;
}

th {
  background-color: #42b983;
  color: rgba(255, 255, 255, 0.66);
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

td {
  background-color: #f9f9f9;
}

th,
td {
  min-width: 120px;
  padding: 10px 20px;
}

th.active {
  color: #fff;
}

th.active .arrow {
  opacity: 1;
}

.arrow {
  display: inline-block;
  vertical-align: middle;
  width: 0;
  height: 0;
  margin-left: 5px;
  opacity: 0.66;
}

.arrow.asc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-bottom: 4px solid #fff;
}

.arrow.dsc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid #fff;
}
</style>