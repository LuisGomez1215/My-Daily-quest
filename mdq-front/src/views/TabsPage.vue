<script setup>
import { IonTabs, IonRouterOutlet, IonTabBar, IonTabButton, IonIcon, IonLabel } from '@ionic/vue'
import { home, person, settings } from 'ionicons/icons'
</script>

<template>
  <IonTabs>
    <IonRouterOutlet />

    <!-- Default Ionic Bottom Tabs -->
    <IonTabBar slot="bottom">
      <IonTabButton tab="tab1" href="/tabs/tab1">
        <IonIcon :icon="home" />
        <IonLabel>Home</IonLabel>
      </IonTabButton>

      <IonTabButton tab="tab2" href="/tabs/tab2">
        <IonIcon :icon="person" />
        <IonLabel>Profile</IonLabel>
      </IonTabButton>

      <IonTabButton tab="tab3" href="/tabs/tab3">
        <IonIcon :icon="settings" />
        <IonLabel>Settings</IonLabel>
      </IonTabButton>
    </IonTabBar>
  </IonTabs>
</template>
