<template>
  <IonPage>
    <IonContent
      class="ion-padding gamertext d-flex justify-content-center align-items-center min-vh-100"
      style="--background: url('/assets/backgrounds/background.png') no-repeat center center / cover;"
    >
      <!-- Alerta de errores -->
      <IonAlert
        :is-open="!!errorMessage"
        header="Error"
        :message="errorMessage"
        :buttons="['OK']"
        @didDismiss="errorMessage = null"
      />

      <IonText class="ion-text-center ion-margin-bottom">
        <h2>Registro</h2>
      </IonText>

      <IonCard class="ion-margin">
        <IonCardContent>
          <form @submit.prevent="submitForm">
            <IonItem>
              <IonLabel position="stacked">Nombre de usuario</IonLabel>
              <IonInput
                v-model="username"
                placeholder="Tu nombre de usuario"
                required
              />
            </IonItem>

            <IonItem>
              <IonLabel position="stacked">Correo electrónico</IonLabel>
              <IonInput
                type="email"
                v-model="email"
                placeholder="ejemplo@correo.com"
                required
              />
            </IonItem>

            <IonItem>
              <IonLabel position="stacked">Contraseña</IonLabel>
              <IonInput
                type="password"
                v-model="password"
                placeholder="Contraseña"
                required
              />
            </IonItem>

            <IonItem>
              <IonLabel position="stacked">Confirmar contraseña</IonLabel>
              <IonInput
                type="password"
                v-model="confirmPassword"
                placeholder="Repite la contraseña"
                required
              />
            </IonItem>

            <!-- Turnstile / Captcha si lo necesitas -->
            <!-- <TurnstileComponent v-model="captchaToken" /> -->

            <IonCard class="ion-text-center ion-margin-top">
              <IonButton expand="block" type="submit">
                Enviar
              </IonButton>
              <IonButton expand="block" @click="$router.push('/login')">
               Ir a Login
              </IonButton>
            </IonCard>
          </form>
        </IonCardContent>
      </IonCard>
    </IonContent>
  </IonPage>
</template>

<script setup>
import {
  IonPage,
  IonContent,
  IonCard,
  IonCardContent,
  IonItem,
  IonLabel,
  IonInput,
  IonButton,
  IonAlert,
  IonText,
} from "@ionic/vue";
import { ref } from "vue";

const username = ref("");
const email = ref("");
const password = ref("");
const confirmPassword = ref("");
const errorMessage = ref(null);

const submitForm = () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = "Las contraseñas no coinciden.";
    return;
  }

  // Aquí conectas con tu backend Django REST para registrar el usuario
  console.log("Registrando:", {
    username: username.value,
    email: email.value,
    password: password.value
  });
};
</script>

<style scoped>
.gamertext {
  font-family: "Press Start 2P", cursive; /* o la fuente gamer que uses */
}
</style>
