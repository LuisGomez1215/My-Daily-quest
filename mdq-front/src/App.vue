<script setup>
import { IonApp, IonHeader, IonToolbar, IonTitle, IonContent, IonRouterOutlet, IonFooter } from '@ionic/vue'
</script>

<template>
  <ion-router-outlet />
  <IonApp>
    <!-- Top Navbar -->
    <IonHeader>
      <IonToolbar style="--background: #f08897;">
        <IonTitle>home</IonTitle>
      </IonToolbar>
    </IonHeader>

    <!-- Page Content -->
    <IonContent fullscreen>
      <!-- Messages (placeholder) -->
      <div id="messages" class="ion-padding">
        <!-- Replace with a Vue messages component later -->
      </div>

      <!-- Page Outlet (like {% block content %}) -->
      <IonRouterOutlet />
    </IonContent>

    <!-- Bottom Navbar -->
    <IonFooter>
      <IonToolbar style="--background: #f08897;">
        <IonTitle>Footer Nav</IonTitle>
      </IonToolbar>
    </IonFooter>
  </IonApp>
</template>

<style>
/* Optional: bring over styles from /public/css/main.css if needed */
</style>