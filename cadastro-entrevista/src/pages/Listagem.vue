
<template>
    <h1>Listagem</h1>
        
    <a href="" @click.prevent="home">home</a>
    <br>
    <a href="" @click.prevent="cadastro">cadastro</a>
  
    <br>
    <br>
    <p>Procurar pelo nome</p>
    <br>
    <input name="query" v-model="searchQuery" />

        <table>
        <thead>
          <tr>
            <th v-for="key in columns" :key="key">
                {{ key }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr  v-for="item in capitalize" :key="item.id">
            <td v-for="key in columns" :key="key">
                {{ item[key]}}
            </td>
          </tr>
        </tbody>
      </table>


    

</template>

<script>
import routes from '../routes'
export default {
  components: {
   
  },

  props: {
    href: {
      type:String,
      required: true
    }
  },

  data(){
    return{
      lista_pessoas:[],
      columns:['created','nome','idade','telefone'],
      searchQuery: "",
      filterUsuarios:[]
    }

  },

  mounted(){
    this.listar()
    
  },

  methods:{

    async listar(){
        const pessoas = await this.axios.get('https://cadastros-usuario.herokuapp.com/usuario/lista-usario/').then((response) => {
          //console.log("fu",response.data)
        return response.data
      })
      this.filterUsuarios = pessoas
      return this.lista_pessoas = pessoas
    },

    home () {
      this.$root.currentRoute = '/entrevista/'
      window.history.pushState(null, routes['/entrevista/'], '/entrevista/')
    },
    cadastro () {
      this.$root.currentRoute = '/entrevista/cadastro/'
      window.history.pushState(null, routes['/entrevista/cadastro/'], '/entrevista/cadastro/')
    }
  },
  computed: {
      capitalize() {
        let produtosEletronico = this.lista_pessoas.filter((value)=>{
            if (value.nome.trim() === this.searchQuery.trim())
              return value;
        });

        return produtosEletronico.length === 0 ? this.lista_pessoas : produtosEletronico

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