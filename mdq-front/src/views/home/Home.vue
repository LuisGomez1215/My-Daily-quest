<!-- layouts/HomeLayout.vue - Con iconos temporales -->
<template>
  <ion-app>
    <!-- Top Navigation -->
    <div class="container">
      <nav id="nav" class="navbar fixed-top navbar-expand-sm d-flex" style="background-color: #f08897;">
        <router-link class="align-self-start" to="/settings">
          <!-- Icono temporal mientras no tengas la imagen -->
          <div class="icon temp-icon">☰</div>
          <!-- <img class="justify-content-start icon" src="/src/assets/icons/MENU.png" alt=""> -->
        </router-link>
        
        <div v-if="user.isAuthenticated" class="justify-content-end d-flex align-items-stretch">
          <!-- Icono temporal de moneda -->
          <div class="temp-icon coin-icon">💰</div>
          <!-- <img class="img-fluid align-self-start" src="/src/assets/icons/COIN.png" alt=""> -->
          <p class="icon align-self fs-5 text-sm-end navtext">{{ user.credits }}</p>
        </div>
      </nav>
    </div>

    <!-- Messages Section -->
    <div v-if="messages.length > 0" class="container mt-3" style="padding-top: 60px;">
      <div 
        v-for="message in messages" 
        :key="message.id"
        :class="`alert alert-${message.type} alert-dismissible`" 
        role="alert"
      >
        {{ message.text }}
        <button 
          type="button" 
          class="btn-close" 
          @click="dismissMessage(message.id)"
          aria-label="Close"
        ></button>
      </div>
    </div>

    <!-- Main Content Area -->
    <ion-content class="main-content">
      <router-view />
    </ion-content>

    <!-- Bottom Navigation -->
    <div class="container">
      <nav id="nav" class="navbar fixed-bottom navbar-expand-sm justify-content-center d-flex" style="background-color: #f08897;">
        <router-link to="/">
          <div class="icon temp-icon">🏠</div>
          <!-- <img class="icon" src="/src/assets/icons/HOME.png" alt=""> -->
        </router-link>
        
        <template v-if="user.isAuthenticated && user.hasPet">
          <router-link to="/">
            <div class="icon temp-icon">🐕</div>
            <!-- <img class="icon" src="/src/assets/icons/PET.png" alt=""> -->
          </router-link>
          <router-link to="/customize">
            <div class="icon temp-icon">📦</div>
            <!-- <img class="icon" src="/src/assets/icons/BOX.png" alt=""> -->
          </router-link>
          <router-link to="/tasks">
            <div class="icon temp-icon">✓</div>
            <!-- <img class="icon" src="/src/assets/icons/TASKS.png" alt=""> -->
          </router-link>
          <router-link to="/adventure">
            <div class="icon temp-icon">🗺️</div>
            <!-- <img class="icon" src="/src/assets/icons/MAP.png" alt=""> -->
          </router-link>
          <router-link to="/shop">
            <div class="icon temp-icon">🛒</div>
            <!-- <img class="icon" src="/src/assets/icons/SHOP.png" alt=""> -->
          </router-link>
        </template>
      </nav>
    </div>
  </ion-app>
</template>

<script setup>
import { ref, onMounted, provide } from 'vue';
import { IonApp, IonContent } from '@ionic/vue';

// Estado del usuario
const user = ref({
  isAuthenticated: true, // Cambiado a true para ver la navegación
  credits: 150,
  hasPet: true,
  username: 'Player1'
});

// Sistema de mensajes
const messages = ref([]);

// Función para mostrar mensajes
const showMessage = (text, type = 'info') => {
  const message = {
    id: Date.now(),
    text,
    type
  };
  messages.value.push(message);
  
  // Auto-remover después de 5 segundos
  setTimeout(() => {
    dismissMessage(message.id);
  }, 5000);
};

// Función para dismissar mensajes
const dismissMessage = (messageId) => {
  const index = messages.value.findIndex(m => m.id === messageId);
  if (index > -1) {
    messages.value.splice(index, 1);
  }
};

// Cargar datos del usuario al montar
onMounted(async () => {
  await loadUserData();
  // Simular detección de tema oscuro/claro
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  document.documentElement.setAttribute('data-bs-theme', prefersDark ? 'dark' : 'light');
  
  // Mensaje de bienvenida de prueba
  showMessage('¡Bienvenido a My Daily Quest!', 'success');
});

const loadUserData = async () => {
  try {
    // Simular datos de usuario - reemplaza con tu API
    const token = localStorage.getItem('token');
    if (token) {
      // Simulación de datos - reemplaza con llamada real a tu API
      user.value = {
        isAuthenticated: true,
        credits: 150,
        hasPet: true,
        username: 'Player1'
      };
    }
  } catch (error) {
    console.error('Error loading user data:', error);
  }
};

// Proveer funciones a componentes hijos
const layoutFunctions = {
  showMessage,
  loadUserData,
  user: user.value
};

provide('layout', layoutFunctions);
</script>

<style scoped>
/* Container styles */
.container {
  max-width: 100%;
  margin: 0 auto;
  padding: 0;
}

/* Main content padding to account for fixed navbars */
.main-content {
  --padding-top: 60px;
  --padding-bottom: 60px;
}

/* Navbar styles */
.navbar {
  min-height: 50px !important;
  height: 50px !important;
  max-height: 50px !important;
  padding: 0.5rem 1rem;
  z-index: 1030;
}

.fixed-top {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
}

.fixed-bottom {
  position: fixed;
  bottom: 0;
  right: 0;
  left: 0;
}

/* Icon styles */
.icon {
  padding-left: 10px;
  padding-right: 10px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Temporary icon styles */
.temp-icon {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  font-size: 20px;
  font-weight: bold;
  color: #333;
  transition: all 0.2s ease;
}

.temp-icon:hover {
  background-color: rgba(255, 255, 255, 1);
  transform: scale(1.1);
}

.coin-icon {
  font-size: 24px;
  background-color: transparent;
}

/* Navigation text */
.navtext {
  color: aliceblue;
  font-family: "Gamergirl", sans-serif;
  margin: 0;
  padding: 0 10px;
  font-size: 1.25rem;
}

/* Bootstrap utility classes */
.d-flex {
  display: flex !important;
}

.navbar-expand-sm {
  flex-wrap: nowrap;
  justify-content: flex-start;
}

.align-self-start {
  align-self: flex-start !important;
}

.align-items-stretch {
  align-items: stretch !important;
}

.justify-content-center {
  justify-content: center !important;
}

.justify-content-end {
  justify-content: flex-end !important;
}

.justify-content-start {
  justify-content: flex-start !important;
}

.img-fluid {
  max-width: 100%;
  height: auto;
}

.fs-5 {
  font-size: 1.25rem !important;
}

.text-sm-end {
  text-align: end !important;
}

.mt-3 {
  margin-top: 1rem !important;
}

/* Alert styles */
.alert {
  position: relative;
  padding: 0.75rem 1.25rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
  border-radius: 0.375rem;
}

.alert-dismissible {
  padding-right: 3rem;
}

.alert-info {
  color: #055160;
  background-color: #cff4fc;
  border-color: #b8daff;
}

.alert-success {
  color: #0f5132;
  background-color: #d1eddd;
  border-color: #badbcc;
}

.alert-warning {
  color: #664d03;
  background-color: #fff3cd;
  border-color: #ffecb5;
}

.alert-danger {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.btn-close {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  padding: 0.75rem 1.25rem;
  color: inherit;
  background: transparent url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='m.235.757 14.015 14.015a.5.5 0 0 1-.708.708L.236 1.465a.5.5 0 1 1 .708-.708z'/%3e%3cpath d='m14.25.757-14.015 14.015a.5.5 0 0 0 .708.708L14.957 1.465a.5.5 0 0 0-.708-.708z'/%3e%3c/svg%3e") center/1em auto no-repeat;
  border: 0;
  border-radius: 0.375rem;
  opacity: 0.5;
  cursor: pointer;
}

.btn-close:hover {
  opacity: 0.75;
}

/* Router link styles */
a {
  color: inherit;
  text-decoration: inherit;
}

a:hover .temp-icon {
  background-color: rgba(255, 255, 255, 1);
  transform: scale(1.1);
}

.router-link-active .temp-icon {
  background-color: rgba(255, 255, 255, 1);
  transform: scale(1.1);
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

/* Font import */
@font-face {
  font-family: "Gamergirl";
  src: url('../../assets/fonts/Gamergirl.ttf');
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .navbar {
    background-color: #2d1b2e !important;
  }
  
  .navtext {
    color: #f0f0f0;
  }
  
  .alert {
    filter: brightness(0.8);
  }
  
  .temp-icon {
    background-color: rgba(255, 255, 255, 0.8);
  }
}
</style>