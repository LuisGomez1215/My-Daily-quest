<!-- views/Auth/Login.vue -->
<template>
  <ion-page>
    <ion-content class="gamertext">
      <div class="login-background">
        <div class="container mt-3 py-3 col-10 d-flex flex-column">
          <!-- Error Alert -->
          <div v-if="errorMessage" class="alert alert-danger text-center" role="alert">
            <strong>Error:</strong>
            {{ errorMessage }}
          </div>

          <div class="row justify-content-center">
            <div class="col-sm-8">
              <form @submit.prevent="handleLogin" class="form card shadow">
                <div class="card-body">
                  <div class="mb-3">
                    <label for="username" class="form-label">Username</label>
                    <input 
                      type="text" 
                      v-model="loginForm.username"
                      name="username" 
                      autofocus 
                      autocapitalize="none"
                      autocomplete="username" 
                      maxlength="150" 
                      required 
                      id="username" 
                      class="form-control"
                    >
                  </div>
                  <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input 
                      type="password" 
                      v-model="loginForm.password"
                      name="password" 
                      autocomplete="current-password"
                      required 
                      id="password" 
                      class="form-control"
                    >
                  </div>
                  <div class="text-center">
                    <button class="btn btn-primary" type="submit" :disabled="loading">
                      {{ loading ? 'Iniciando sesión...' : 'Log in!' }}
                    </button>
                    <div class="mt-3">
                      <router-link to="/forgot-password">Olvidé mi contraseña</router-link> /
                      <router-link to="/register">Registrarme</router-link>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup>
import { ref } from 'vue';
import { IonPage, IonContent } from '@ionic/vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const loginForm = ref({
  username: '',
  password: ''
});

const errorMessage = ref('');
const loading = ref(false);

const handleLogin = async () => {
  loading.value = true;
  errorMessage.value = '';
  
  try {
    // Aquí irá tu lógica de autenticación
    // Por ejemplo, llamada a API
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(loginForm.value)
    });
    
    if (response.ok) {
      const data = await response.json();
      // Guardar token o datos de usuario
      localStorage.setItem('token', data.token);
      // Redirigir al home
      router.push('/');
    } else {
      errorMessage.value = 'El nombre de usuario y/o contraseña no son correctos.';
    }
  } catch (error) {
    errorMessage.value = 'Error de conexión. Intenta nuevamente.';
    console.error('Login error:', error);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.login-background {
  min-height: 100vh;
  background-image: url('/src/assets/backgrounds/background.png');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  max-width: 100%;
  padding: 1rem;
}

.gamertext {
  font-family: "Gamergirl", sans-serif;
}

.alert {
  border-radius: 0.375rem;
  padding: 0.75rem 1.25rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
}

.alert-danger {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.card {
  border: 1px solid rgba(0,0,0,.125);
  border-radius: 0.375rem;
  background-color: #fff;
}

.card-body {
  flex: 1 1 auto;
  padding: 1rem;
}

.shadow {
  box-shadow: 0 .125rem .25rem rgba(0,0,0,.075)!important;
}

.form-label {
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-control {
  display: block;
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ced4da;
  border-radius: 0.375rem;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

.form-control:focus {
  color: #212529;
  background-color: #fff;
  border-color: #86b7fe;
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgba(13,110,253,.25);
}

.btn {
  display: inline-block;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  text-align: center;
  text-decoration: none;
  vertical-align: middle;
  cursor: pointer;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  border-radius: 0.375rem;
  transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

.btn-primary {
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.btn-primary:hover {
  color: #fff;
  background-color: #0b5ed7;
  border-color: #0a58ca;
}

.btn:disabled {
  opacity: 0.65;
  cursor: not-allowed;
}

a {
  color: #0d6efd;
  text-decoration: underline;
}

a:hover {
  color: #0a58ca;
}

.mb-3 {
  margin-bottom: 1rem!important;
}

.mt-3 {
  margin-top: 1rem!important;
}

.py-3 {
  padding-top: 1rem!important;
  padding-bottom: 1rem!important;
}

.text-center {
  text-align: center!important;
}

.justify-content-center {
  justify-content: center!important;
}

.d-flex {
  display: flex!important;
}

.flex-column {
  flex-direction: column!important;
}

.col-10 {
  flex: 0 0 auto;
  width: 83.33333333%;
}

.col-sm-8 {
  flex: 0 0 auto;
  width: 66.66666667%;
}

@media (min-width: 576px) {
  .col-sm-8 {
    flex: 0 0 auto;
    width: 66.66666667%;
  }
}

.row {
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(-1 * 0);
  margin-right: calc(-0.5 * 1.5rem);
  margin-left: calc(-0.5 * 1.5rem);
}

.row > * {
  flex-shrink: 0;
  width: 100%;
  max-width: 100%;
  padding-right: calc(1.5rem * 0.5);
  padding-left: calc(1.5rem * 0.5);
  margin-top: 0;
}

/* Import de la fuente Gamergirl */
@font-face {
  font-family: "Gamergirl";
  src: url('../../../assets/fonts/Gamergirl.ttf');
}
</style>