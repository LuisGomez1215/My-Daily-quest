<template>
  <IonPage>
    <IonContent class="ion-padding d-flex justify-content-center align-items-center">
      <div class="text-center">
        <h2 class="mb-3">Adventure Started! 🎉</h2>
        <p>Your journey has begun. Good luck, traveler!</p>

        <IonButton class="mt-4" expand="block" router-link="/adventure2">
          ← Back to Map
        </IonButton>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { IonPage, IonContent, IonButton } from "@ionic/vue";
</script>

<style scoped>
h2 {
  color: #28a745;
}
</style>
