<template>
  <IonPage>
    <IonContent
      class="d-flex justify-content-center align-items-center vh-100"
      :style="{ 
        backgroundImage: 'url(/assets/backgrounds/background.png)', 
        backgroundSize: 'cover', 
        backgroundPosition: 'center' 
      }"
    >
      <div class="container text-center">
        <h1 style="color:black; font-size: 3rem;">404!</h1>
        <p style="color:black;">Page not found</p>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { IonPage, IonContent } from "@ionic/vue";
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.8);
  padding: 2rem;
  border-radius: 12px;
}
</style>
