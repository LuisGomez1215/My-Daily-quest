<script setup>
import {
  IonPage,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonCard,
  IonCardContent,
  IonItem,
  IonLabel,
  IonInput,
  IonButton,
  IonText
} from '@ionic/vue'

// reactive state placeholders (replace later with API calls)
import { ref } from 'vue'

const username = ref('')
const password = ref('')
const errorMessage = ref('') // stub: show error messages like Django version
</script>

<template>
  <IonPage>
    <IonHeader>
      <IonToolbar>
        <IonTitle>Iniciar sesión</IonTitle>
      </IonToolbar>
    </IonHeader>

    <IonContent class="ion-padding">

      <!-- Error Message -->
      <IonText v-if="errorMessage" color="danger" class="ion-text-center">
        <p><strong>Error:</strong> {{ errorMessage }}</p>
      </IonText>

      <!-- Login Form -->
      <IonCard>
        <IonCardContent>
          <form @submit.prevent="() => {}">

            <!-- Username -->
            <IonItem>
              <IonLabel position="floating">Nombre de usuario</IonLabel>
              <IonInput
                v-model="username"
                type="text"
                autocomplete="username"
                required
              />
            </IonItem>

            <!-- Password -->
            <IonItem>
              <IonLabel position="floating">Contraseña</IonLabel>
              <IonInput
                v-model="password"
                type="password"
                autocomplete="current-password"
                required
              />
            </IonItem>

            <!-- Submit Button -->
            <div class="ion-text-center ion-margin-top">
              <IonButton expand="block" type="submit">
                Iniciar sesión
              </IonButton>

              <IonText class="ion-margin-top">
                <p>
                  <a href="#">Olvidé mi contraseña</a> /
                  <a href="/register">Registrarme</a>
                </p>
              </IonText>
            </div>

          </form>
        </IonCardContent>
      </IonCard>
    </IonContent>
  </IonPage>
</template>
