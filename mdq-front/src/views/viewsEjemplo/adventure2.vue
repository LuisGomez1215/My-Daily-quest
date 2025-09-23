<template>
  <IonPage>
    <IonContent
      class="gamertext d-flex justify-content-center align-items-center"
      :style="{ backgroundImage: `url(${backgroundImg})` }"
      fullscreen
    >
      <div class="container travel-screen text-light py-3 col-10 col-md-6 col-lg-4 d-flex flex-column align-items-center">
        <h2 class="text-center travel-title">Where will you travel?</h2>

        <!-- MAPA -->
        <div class="map-container my-2 justify-content-center border rounded">
          <img :src="mapImg" alt="Travel Map" class="map-image" />
        </div>

        <!-- SI ESTÁ VIAJANDO -->
        <div v-if="current" class="travel-info p-2 mt-2 text-center">
          <p>
            You are currently traveling to
            <span class="highlight">{{ current.destination.location_name }}</span>!
          </p>
          <p>
            ⏳ Time remaining:
            <span v-if="remaining > 0" id="countdown">{{ countdownText }}</span>
            <span v-else class="highlight">Completed!</span>
          </p>

          <!-- Barra de progreso -->
          <div v-if="remaining > 0" class="progress my-2" style="height: 20px;">
            <div
              class="progress-bar bg-success"
              role="progressbar"
              :style="{ width: progress + '%' }"
              :aria-valuenow="progress"
              aria-valuemin="0"
              aria-valuemax="100"
            >
              {{ progress }}%
            </div>
          </div>

          <!-- Botón reclamar -->
          <IonButton
            v-if="remaining <= 0"
            expand="block"
            class="btn-travel mt-2"
            router-link="/customize"
          >
            ✔ Claim Rewards
          </IonButton>

          <!-- Botón dev -->
          <IonButton expand="block" 
          class="btn-travel mt-2 mb-2 small"
          router-link="/customize"
          >
            ✔ Finish (Dev)
          </IonButton>
        </div>

        <!-- SI NO ESTÁ VIAJANDO -->
        <div v-else class="mb-3 text-center w-100">
          <IonSelect
            placeholder="Locations!"
            v-model="selectedLocation"
            @ionChange="showPreview"
          >
            <IonSelectOption v-for="loc in locations" :key="loc.id" :value="loc">
              {{ loc.location_name }}
            </IonSelectOption>
          </IonSelect>
        </div>

        <!-- Preview de viaje -->
        <div
          v-if="previewLocation"
          id="adventurePreview"
          class="travel-info p-2 mt-2"
        >
          <p class="mb-1">
            The location you selected will grant
            <span class="highlight">{{ previewLocation.exp_reward }}</span> EXP and
            <span class="highlight">{{ previewLocation.credit_reward }}</span> credits,
            travel will take
            <span class="highlight">{{ previewLocation.time }}</span> hours.
          </p>
          <p class="text-center mt-3 small" style="color:black;">
            Will you travel to <b>{{ previewLocation.location_name }}</b>?
          </p>
          <IonButton expand="block" class="btn-travel mt-2">LET'S GO!</IonButton>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import {
  IonPage,
  IonContent,
  IonButton,
  IonSelect,
  IonSelectOption,
} from "@ionic/vue";

// mock de imágenes
const backgroundImg = "/assets/backgrounds/background.png";
const mapImg = "/assets/backgrounds/map.png";

// mock de estado actual de viaje
const current = ref(null);


// lista mock de ubicaciones
const locations = ref([
  { id: 1, location_name: "Forest", exp_reward: 50, credit_reward: 20, time: 2 },
  { id: 2, location_name: "Mountain", exp_reward: 120, credit_reward: 60, time: 5 },
  { id: 3, location_name: "Castle", exp_reward: 200, credit_reward: 100, time: 8 },
]);

const selectedLocation = ref(null);
const previewLocation = ref(null);

function showPreview() {
  previewLocation.value = selectedLocation.value || null;
}

// countdown
const countdownText = ref("");
const progress = ref(0);
const remaining = ref(0);
let interval = null;

function updateCountdown() {
  if (!current.value) return;
  const endTime = current.value.created_at + current.value.duration * 1000;
  const now = Date.now();
  const diff = endTime - now;

  remaining.value = Math.max(0, diff);

  if (remaining.value <= 0) {
    countdownText.value = "✔ Completed!";
    progress.value = 100;
    clearInterval(interval);
    return;
  }

  const hours = Math.floor(diff / (1000 * 60 * 60));
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((diff % (1000 * 60)) / 1000);

  countdownText.value = `${hours}h ${minutes}m ${seconds}s`;

  progress.value = Math.min(
    100,
    ((now - current.value.created_at) / (current.value.duration * 1000)) * 100
  );
}

onMounted(() => {
  if (current.value) {
    updateCountdown();
    interval = setInterval(updateCountdown, 1000);
  }
});

onUnmounted(() => {
  if (interval) clearInterval(interval);
});
</script>

<style scoped>
.map-image {
  width: 100%;
}
.btn-travel {
  --background: #28a745;
  --color: white;
}
.highlight {
  font-weight: bold;
  color: yellow;
}
</style>
