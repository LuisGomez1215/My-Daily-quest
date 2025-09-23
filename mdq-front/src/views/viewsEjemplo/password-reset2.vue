<template>
  <IonPage>
    <IonContent class="ion-padding">
      <!-- Mensaje de error -->
      <IonAlert
        :is-open="!!errorMessage"
        header="Error"
        :message="errorMessage"
        :buttons="['OK']"
        @didDismiss="errorMessage = null"
      />

      <IonCardHeader class="ion-text-center ion-margin-top">
        <IonCardTitle>Contraseña olvidada</IonCardTitle>
      </IonCardHeader>

      <IonCard>
        <IonCardContent>
          <p>
            Escribe tu correo a continuación, y de ser correcto,
            recibirás instrucciones para poder reestablecer tu contraseña.
          </p>

          <!-- Formulario -->
          <form @submit.prevent="submitForm">
            <IonItem>
              <IonLabel position="stacked">Correo electrónico</IonLabel>
              <IonInput
                type="email"
                v-model="email"
                placeholder="ejemplo@correo.com"
                required
              />
            </IonItem>

            <!-- Si necesitas un captcha/turnstile, va aquí como un componente -->
            <!-- <TurnstileComponent v-model="captchaToken" /> -->

            <div class="ion-text-center ion-margin-top">
              <IonButton expand="block" type="submit">
                Restablecer contraseña
              </IonButton>
              <IonButton
                expand="block"
                color="medium"
                router-link="/login">
              <ion-icon slot="start" name="chevron-back-outline">
              </ion-icon>  
                ← Volver
              </IonButton>
            </div>
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
  IonCardHeader,
  IonCardTitle
} from "@ionic/vue";
import { ref } from "vue";

const email = ref("");
const errorMessage = ref(null);

const submitForm = () => {
  if (!email.value.includes("@")) {
    errorMessage.value = "Por favor ingresa un correo válido.";
    return;
  }

  // Aquí llamas a la API de Django REST (endpoint de password reset)
  console.log("Correo ingresado:", email.value);
};
</script>
