<template>
  <IonPage>
    <IonContent
      class="gamertext d-flex justify-content-center align-items-center vh-100"
      :style="{ backgroundImage: 'url(/assets/backgrounds/background.png)', backgroundSize: 'cover' }"
    >
      <div class="settings-container col-10 col-md-6 col-lg-4 d-flex flex-column container">
        <h2 class="settings-title ion-text-center">Settings</h2>

        <!-- Volume -->
        <div class="setting-item">
          <label for="volume">Volume</label>
          <div class="slider-container d-flex align-items-center gap-2">
            <span>🔈</span>
            <IonRange
              id="volume"
              min="0"
              max="100"
              step="1"
              v-model="volume"
              pin
            />
            <span>🔊</span>
          </div>
        </div>

        <!-- Palette -->
        <div class="setting-item">
          <label>Palette</label>
          <div class="d-flex gap-2">
            <div
              v-for="color in palette"
              :key="color"
              class="palette-option"
              :style="{ backgroundColor: color }"
              @click="selectColor(color)"
            >
          </div>
        </div>

        <!-- Export Data -->
        <div class="setting-item">
          <IonButton expand="block" color="primary" @click="exportData">
            Export Data
          </IonButton>
        </div>

        <!-- Logout -->
        <div class="setting-item">
          <IonButton expand="block" color="danger" @click="logout">
            Logout
          </IonButton>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { ref } from "vue";
import { IonPage, IonContent, IonRange, IonButton } from "@ionic/vue";

const volume = ref(50);
const palette = ["#753737ff", "#4b644bff", "#5c5c97ff", "#7c7c49ff"];

function selectColor(color) {
  console.log("Selected color:", color);
}

function exportData() {
  console.log("Exporting data...");
}

function logout() {
  console.log("Logging out...");
  // Aquí conectas con tu API de logout de Django Rest Framework
}
</script>

<style scoped>
.settings-title {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.setting-item {
  margin-bottom: 1.5rem;
}

.slider-container {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.palette-option {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  cursor: pointer;
  border: 2px solid #fff;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.3);
}
</style>
