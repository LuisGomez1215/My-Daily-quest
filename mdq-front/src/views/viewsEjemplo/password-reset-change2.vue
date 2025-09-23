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

      <div class="ion-text-center ion-margin-top">
        <h2>Reestablecer contraseña</h2>
      </div>

      <IonCard>
        <IonCardContent>
          <!-- Si el link es válido -->
          <div v-if="validLink">
            <p class="ion-text-center">
              Ingresa tu nueva contraseña y repítela para confirmar.
            </p>

            <IonItem>
              <IonLabel position="stacked">Nueva contraseña</IonLabel>
              <IonInput
                type="password"
                v-model="password"
                placeholder="Ingresa nueva contraseña"
              />
            </IonItem>

            <IonItem>
              <IonLabel position="stacked">Confirmar contraseña</IonLabel>
              <IonInput
                type="password"
                v-model="confirmPassword"
                placeholder="Repite la contraseña"
              />
            </IonItem>

            <div class="ion-text-center ion-margin-top">
              <IonButton expand="block" @click="submitForm">
                Cambiar contraseña
              </IonButton>
              <IonButton
                expand="block"
                color="medium"
                router-link="/login"
              >
                ← Cancelar
              </IonButton>
            </div>
          </div>

          <!-- Si el link no es válido -->
          <div v-else>
            <p>
              El enlace para reestablecer contraseña no es válido, probablemente porque ya fue utilizado.
              Por favor solicita un nuevo enlace.
            </p>
          </div>
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
  IonAlert
} from "@ionic/vue";
import { ref } from "vue";

const password = ref("");
const confirmPassword = ref("");
const errorMessage = ref(null);
const validLink = ref(true); // Esto vendría de la API de Django REST

const submitForm = () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = "Las contraseñas no coinciden.";
    return;
  }

  // Aquí llamas a la API de Django REST con Axios o Fetch
  console.log("Nueva contraseña:", password.value);
};
</script>
