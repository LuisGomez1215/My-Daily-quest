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
        <!-- Pantalla principal con caja -->
        <div class="d-flex justify-content-center align-items-center petscreen position-relative">
          <img class="h100 w100 img-fluid" src="/assets/backgrounds/boxpet.png" />

          <!-- Overlay -->
          <div class="pet-overlay position-absolute top-50 bottom-50 start-50 translate-middle">
            <!-- Si no hay mascota -->
            <template v-if="!petcheck">
              <router-link to="/petselect">
                <img class="h100 w100 img-fluid" src="/assets/icons/PETBOX.png" />
              </router-link>
            </template>

            <!-- Si ya hay mascota -->
            <template v-else>
              <div class="pet-wrapper position-relative d-inline-block">
                <img class="img-fluid spot-offset" src="/assets/icons/PETSPOT.png" />
                <img
                  class="pet img-fluid position-absolute top-50 start-50 translate-middle"
                  :src="pet.species.pet_avatar"
                  :alt="pet.name"
                />
              </div>
            </template>
          </div>
        </div>

        <!-- Stats -->
        <div v-if="petcheck" class="pet-stats text-center mt-3 border rounded p-3">
          <p class="mb-1">Lv {{ pet.level }}</p>

          <!-- Barra de progreso -->
          <div class="progress">
            <div
              id="exp-bar"
              class="progress-bar bg-primary"
              role="progressbar"
              :style="{ width: progressPercent + '%' }"
              :aria-valuenow="progressPercent"
              aria-valuemin="0"
              :aria-valuemax="nextLevelExp"
            ></div>
          </div>

          <p class="small mt-1">
            {{ currentExp.toFixed(0) }} / {{ nextLevelExp.toFixed(0) }} EXP
          </p>

          <p class="mt-2 mb-1">HP</p>
          <p class="mb-1">{{ pet.hp }}/{{ pet.hp }}</p>

          <p class="mt-2 mb-1">Stamina</p>
          <p class="mb-1">{{ pet.stamina }}/{{ pet.stamina }}</p>

          <p class="mt-2 mb-0">
            Mood: <strong>{{ pet.mood_status }}</strong>
          </p>

          <p class="mt-2 mb-1">Bond</p>
          <span
            v-for="i in 5"
            :key="i"
            :style="{ color: i <= pet.bond_meter ? 'red' : '#ddd' }"
          >
            ●
          </span>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { IonPage, IonContent } from "@ionic/vue";
import { ref, onMounted } from "vue";

// Ejemplo de datos que normalmente vendrían de la API
const petcheck = ref(true); // simula si hay mascota creada o no
const pet = ref({
  name: "Firu",
  level: 5,
  hp: 100,
  stamina: 80,
  mood_status: "Happy",
  bond_meter: 3,
  species: {
    pet_avatar: "/assets/icons/sample-pet.png"
  }
});

const currentExp = ref(40);
const nextLevelExp = ref(100);
const progressPercent = ref(0);

onMounted(() => {
  // animación progresiva de la barra de experiencia
  let current = 0;
  const target = Math.round((currentExp.value / nextLevelExp.value) * 100);
  const interval = setInterval(() => {
    if (current >= target) {
      clearInterval(interval);
    } else {
      current++;
      progressPercent.value = current;
    }
  }, 10);
});
</script>

<style scoped>
.petscreen {
  height: 300px;
}
.pet-overlay {
  width: 100%;
  height: 100%;
}
.pet {
  max-width: 120px;
}
.progress {
  height: 20px;
  background: #e0e0e0;
  border-radius: 10px;
}
.progress-bar {
  height: 100%;
  transition: width 0.2s ease-in-out;
}
</style>
