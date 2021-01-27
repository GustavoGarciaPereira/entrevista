
<template>

    <p>Cadastrar</p>
        <p>nome</p>
    <input v-model="nome" type="text" placeholder="nome">
        <p>Idade</p>
    <input v-model="idade" type="number" placeholder="idade">
        <p>Telefone</p>
    <input v-model="telefone" min="10" max="10" placeholder="telefone">
    <br>
    <br>
    <button @click="g()">Cadastrar</button>

      <div v-if="sucess">
        
        <p class="sucess">Salvou com sucesso</p>
        <a href="/listagem">Listagem de usuários</a>
        
      </div>
      <div v-if="error">
        <p class="error">Erro ao salvar {{ mensage_erro }}</p>
      </div>



</template>

<script>


export default {
  components: {


  },

  data(){
    return{
      nome:"",
      idade:"",
      telefone:"",
      sucess:false,
      error:false,
      mensage_erro:""
    }

  },

  methods:{

    
    async g(){
      if(
        this.nome !== "" ||
        this.idade !=="" ||
        this.telefone !==""
      ){
            const res = await this.axios.post('http://127.0.0.1:8000/usuario/lista-usario/', {
                  nome: `${this.nome}`,
                  idade: parseInt(this.idade),
                  telefone:`${this.telefone}`
                })
                .then(function (response) {
                  return response.status
                })
                .catch(function (error) {
                  
                  console.log(error);
                  //this.error = true
                });
                
                if(res === 200){
                  this.sucess = true
                }else{
                  this.error = true
                }
            }else{
              this.error = true
              this.mensage_erro = "alguns campos ficaram em branco"
            }
      }
      

  }

}
</script>


<style scoped>
.sucess{
  background-color: greenyellow;
}
.error{
  background-color:red;
}
</style>