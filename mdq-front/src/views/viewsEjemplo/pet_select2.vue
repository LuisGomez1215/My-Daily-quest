<template>
  <IonPage>
    <IonContent
      class="gamertext ion-padding"
      :style="{ backgroundImage: `url(${backgroundImg})` }"
      fullscreen
    >
      <div class="container d-flex flex-column justify-content-center align-items-center min-vh-100">
        <!-- Lista de mascotas -->
        <div
          v-for="pet in pets"
          :key="pet.id"
          class="d-flex align-items-center justify-content-start custom-card"
        >
          <!-- Avatar circular -->
          <div class="circle-wrapper d-flex align-items-center justify-content-center">
            <img :src="pet.pet_avatar" :alt="pet.species" class="circle-img" />
          </div>

          <!-- Texto -->
          <div class="text-box flex-grow-1">
            <RouterLink
              class="w-100 h-100 biggertext"
              :to="`/pet-select-form/${pet.id}`"
            >
              <div class="biggertext">{{ pet.species }}</div>
            </RouterLink>
            <hr class="divider" />
            <div class="smallertext">{{ pet.desc }}</div>
          </div>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { IonPage, IonContent } from "@ionic/vue";
import { RouterLink } from "vue-router";
import { ref } from "vue";

// 🔹 Fondo
const backgroundImg = "/assets/backgrounds/background.png";

// 🔹 Mock de mascotas (se reemplaza con API a futuro)
const pets = ref([
  {
    id: 1,
    species: "Dragon",
    pet_avatar: "/assets/pets/sample_dragon.png",
    desc: "A fierce but loyal companion.",
  },
  {
    id: 2,
    species: "Cat",
    pet_avatar: "/assets/pets/sample_cat.png",
    desc: "Playful and curious friend.",
  },
  {
    id: 3,
    species: "Fox",
    pet_avatar: "/assets/pets/sample_fox.png",
    desc: "Clever and quick adventurer.",
  },
]);
</script>

<style scoped>
.custom-card {
  background-color: #ffffffaa;
  border-radius: 12px;
  padding: 1rem;
  margin: 1rem 0;
  width: 100%;
  max-width: 600px;
}

.circle-wrapper {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: #eee;
  overflow: hidden;
  margin-right: 1rem;
}

.circle-img {
  width: 100%;
  height: auto;
  object-fit: cover;
}

.biggertext {
  font-size: 1.3rem;
  font-weight: bold;
  color: #000;
}

.smallertext {
  font-size: 0.9rem;
  color: #333;
}

.divider {
  border-top: 1px solid #ccc;
  margin: 0.5rem 0;
}
</style>
