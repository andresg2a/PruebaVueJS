<template>
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Validar Numero de Telefono</h1>
      <div class="mb-4">
        <input 
          v-model="phoneNumber" 
          type="text" 
          placeholder="Ingresa un numero de telefono" 
          class="border p-2 rounded w-full"
        />
        <button 
          @click="validatePhoneNumber" 
          class="mt-2 bg-blue-500 text-white py-2 p1x-4 rounded"
        >
          Validar
        </button>
      </div>
      <div v-if="validationResult" class="mt-4 p-4 border rounded">
        <h2 class="text-xl font-semibold">Resultado de la Validacion:</h2>
        <pre>{{ validationResult }}</pre>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        phoneNumber: '',
        validationResult: null,
      };
    },
    methods: {
      async validatePhoneNumber() {
        const apiKey = '7674209cabf01f75bc23883453bd571c'; 
        try {
          const response = await fetch(`http://apilayer.net/api/validate?access_key=${apiKey}&number=${this.phoneNumber}`);
          const data = await response.json();
          this.validationResult = data;
        } catch (error) {
          console.error('Error validating phone number:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>

  </style>
  