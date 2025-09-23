<template>
  <IonPage>
    <IonContent class="ion-padding">
      <IonCardHearder class="ion-text-center ion-margin-top">
        <IonCardTitle>Instrucciones para reiniciar contraseña enviadas</IonCardTitle>
      </IonCardHearder>

      <IonCard>
        <IonCardContent>
          <p>
            Si el correo que ingresaste es correcto, te enviaremos instrucciones para cambiar tu contraseña.
          </p>
          <p>
            Si no has recibido el email, asegúrate de haber ingresado el correo con el que te registraste, y revisa la carpeta de spam.
          </p>
          <IonButton expand="block" 
          routerLink="/login">Volver al inicio de sesión</IonButton>
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
  IonCardHearder,
  IonCardTitle,
} from "@ionic/vue";
</script>
