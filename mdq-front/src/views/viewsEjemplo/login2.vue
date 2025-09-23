<template>
  <IonPage>
    <IonContent class="ion-padding gamertext" :style="backgroundStyle">
      <div class="flex flex-col justify-center items-center min-h-screen">
        <!-- Mensajes de error -->
        <div
          v-if="errorMessage"
          class="bg-red-500 text-white text-center px-4 py-2 rounded mb-4"
        >
          <strong>Error:</strong> {{ errorMessage }}
        </div>

        <!-- Formulario de login -->
        <div class="w-full max-w-md">
          <form @submit.prevent="handleLogin" class="bg-white shadow rounded p-6">
            <div class="mb-4">
              <label for="username" class="block text-gray-700 font-bold mb-2">
                Username
              </label>
              <IonInput
                id="username"
                v-model="username"
                type="text"
                required
                autofocus
                autocomplete="username"
              />
            </div>

            <div class="mb-4">
              <label for="password" class="block text-gray-700 font-bold mb-2">
                Password
              </label>
              <IonInput
                id="password"
                v-model="password"
                type="password"
                required
                autocomplete="current-password"
              />
            </div>

            <div class="text-center">
              <IonButton expand="block" type="submit">Log in!</IonButton>
              <div class="mt-3 text-sm text-gray-700">
                <a href="#">Olvidé mi contraseña</a> /
                <RouterLink to="/register">Registrarme</RouterLink>
              </div>
            </div>
          </form>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import {
  IonPage,
  IonContent,
  IonInput,
  IonButton
} from "@ionic/vue";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const username = ref("");
const password = ref("");
const errorMessage = ref("");

// Imagen de fondo
const backgroundStyle = {
  backgroundImage: "url('/assets/backgrounds/background.png')",
  backgroundSize: "cover",
  backgroundPosition: "center",
};

// Acción de login simulada
const handleLogin = () => {
  if (username.value === "test" && password.value === "1234") {
    router.push("/home");
  } else {
    errorMessage.value =
      "El nombre de usuario y/o contraseña no son correctos.";
  }
};
</script>
