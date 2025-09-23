<template>
  <IonPage>
    <IonContent class="ion-padding">
      <div class="ion-text-center ion-margin-top">
        <h2>Contraseña cambiada</h2>
      </div>

      <IonCard>
        <IonCardContent class="ion-text-center">
          <p>Has cambiado tu contraseña correctamente. Inicia sesión para continuar.</p>
          <IonButton
            expand="block"
            router-link="/login"
            class="ion-margin-top"
          >
            Iniciar sesión
          </IonButton>
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
  IonButton
} from "@ionic/vue";
</script>
