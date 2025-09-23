<!-- App.vue - Versión con Header Global -->
<script setup>
import { IonApp, IonHeader, IonToolbar, IonTitle, IonContent, IonRouterOutlet } from '@ionic/vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <IonApp>

    <IonContent>
      <!-- IMPORTANTE: Usar RouterView en lugar de IonRouterOutlet cuando tienes header global -->
      <RouterView />
    </IonContent>
  </IonApp>
</template>

<style>
/* Mismo CSS que la opción anterior */
@import '@ionic/vue/css/core.css';
@import '@ionic/vue/css/normalize.css';
@import '@ionic/vue/css/structure.css';
@import '@ionic/vue/css/typography.css';
@import '@ionic/vue/css/padding.css';
@import '@ionic/vue/css/float-elements.css';
@import '@ionic/vue/css/text-alignment.css';
@import '@ionic/vue/css/flex-utils.css';
@import '@ionic/vue/css/display.css';

@font-face {
  font-family: "Gamergirl";
  src: url('./assets/fonts/Gamergirl.ttf');
}

.gamertext {
  font-family: "Gamergirl";
}

/* Resto de estilos... */
</style>