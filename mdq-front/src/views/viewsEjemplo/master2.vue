<template>
  <IonPage>
    <!-- NAV SUPERIOR -->
    <IonHeader>
      <IonToolbar style="background-color: #f08897;">
        <IonButtons slot="start">
          <IonButton router-link="/settings">
            <IonIcon class="icon" src="/assets/icons/MENU.png" alt="menu" />
          </IonButton>
        </IonButtons>

        <!-- Créditos usuario -->
        <IonButtons slot="end" v-if="isAuthenticated">
          <div class="d-flex align-items-center">
            <IonIcon class="icon" src="/assets/icons/COIN.png" alt="coins" />
            <p class="fs-5 mb-0 ms-1">{{ wallet.credits }}</p>
          </div>
        </IonButtons>
      </IonToolbar>
    </IonHeader>

    <!-- CONTENIDO DE LA PÁGINA HIJA -->
    <IonContent>
      <slot />
    </IonContent>

    <!-- NAV INFERIOR -->
    <IonFooter>
      <IonToolbar style="background-color: #f08897;">
        <div class="d-flex justify-content-center w-100 gap-3">
          <IonButton fill="clear" router-link="/home">
            <IonIcon class="icon" src="/assets/icons/HOME.png" alt="home" />
          </IonButton>

          <template v-if="isAuthenticated && hasPet">
            <IonButton fill="clear" router-link="/pet">
              <IonIcon class="icon" src="/assets/icons/PET.png" alt="pet" />
            </IonButton>
            <IonButton fill="clear" router-link="/customize">
              <IonIcon class="icon" src="/assets/icons/BOX.png" alt="customize" />
            </IonButton>
            <IonButton fill="clear" router-link="/tasks">
              <IonIcon class="icon" src="/assets/icons/TASKS.png" alt="tasks" />
            </IonButton>
            <IonButton fill="clear" router-link="/travel">
              <IonIcon class="icon" src="/assets/icons/MAP.png" alt="adventure" />
            </IonButton>
            <IonButton fill="clear" router-link="/shop">
              <IonIcon class="icon" src="/assets/icons/SHOP.png" alt="shop" />
            </IonButton>
          </template>
        </div>
      </IonToolbar>
    </IonFooter>
  </IonPage>
</template>

<script setup>
import {
  IonPage,
  IonHeader,
  IonFooter,
  IonToolbar,
  IonContent,
  IonButton,
  IonButtons,
  IonIcon,
} from "@ionic/vue";
import { ref } from "vue";

// 🔹 Simulación del usuario (mock por ahora)
const isAuthenticated = ref(true);
const hasPet = ref(true);
const wallet = ref({
  credits: 120,
});
</script>

<style scoped>
.icon {
  width: 30px;
  height: 30px;
}
</style>
