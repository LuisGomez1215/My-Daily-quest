<template>
  <IonPage>
    <IonContent
      class="gamertext"
      :style="{ backgroundImage: `url(${backgroundImg})` }"
      fullscreen
    >
      <div class="container">
        <!-- PET SCREEN -->
        <div class="d-flex justify-content-center align-items-center petscreen position-relative">
          <img class="h100 w100 img-fluid" :src="boxPetImg" />

          <div class="pet-overlay position-absolute top-50 bottom-50 start-50 translate-middle">
            <div class="pet-wrapper position-relative d-inline-block">
              <img class="img-fluid spot-offset" :src="petSpotImg" />
              <img
                class="pet img-fluid position-absolute top-50 start-50 translate-middle"
                :src="pet.species.pet_avatar"
                :alt="pet.name"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- SEARCH + FILTER -->
      <div class="container py-4">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <IonInput
            v-model="search"
            placeholder="Search items..."
            class="me-2"
            style="max-width: 70%;"
          />
          <IonSelect v-model="filter" placeholder="All" style="max-width: 25%;">
            <IonSelectOption value="all">All</IonSelectOption>
            <IonSelectOption value="cosmetics">Cosmetics</IonSelectOption>
            <IonSelectOption value="consumables">Consumables</IonSelectOption>
            <IonSelectOption value="backgrounds">Backgrounds</IonSelectOption>
          </IonSelect>
        </div>

        <!-- INVENTORY GRID -->
        <div class="row g-3 text-center">
          <!-- COSMETICS -->
          <div
            class="col-3"
            v-for="clo in cosmetics"
            :key="clo.id"
            @click="equipItem(clo)"
          >
            <div
              class="inventory-slot d-flex flex-column justify-content-center align-items-center clickable-slot"
            >
              <img
                :src="clo.cosmetic.icon"
                :alt="clo.cosmetic.name"
                class="inventory-image"
              />
            </div>
            <p class="small mb-0 text-wrap" style="color:black;">
              {{ clo.cosmetic.name }}
            </p>
            <span
              v-if="clo.equipped"
              class="badge bg-success mt-1 small"
            >
              {{ clo.cosmetic.slot }}
            </span>
          </div>

          <!-- ITEMS -->
          <div class="col-3" v-for="inv in items" :key="inv.id">
            <div
              class="inventory-slot d-flex justify-content-center align-items-center text-wrap"
            >
              <img
                :src="inv.consumable.icon"
                :alt="inv.consumable.name"
                class="inventory-image"
              />
            </div>
            <div class="small">
              <p class="text-wrap" style="color:black;">
                {{ inv.consumable.name }}
              </p>
              <p style="color:black;">x{{ inv.quantity }}</p>
            </div>
          </div>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import {
  IonPage,
  IonContent,
  IonInput,
  IonSelect,
  IonSelectOption,
} from "@ionic/vue";
import { ref } from "vue";

// 🔹 Mock imágenes estáticas
const backgroundImg = "/assets/backgrounds/background.png";
const boxPetImg = "/assets/backgrounds/boxpet.png";
const petSpotImg = "/assets/icons/PETSPOT.png";

// 🔹 Mock mascota
const pet = ref({
  name: "Fluffy",
  species: {
    pet_avatar: "/assets/pets/sample_pet.png",
  },
});

// 🔹 Mock inventario
const cosmetics = ref([
  {
    id: 1,
    cosmetic: {
      name: "Red Hat",
      slot: "Head",
      icon: "/assets/cosmetics/red_hat.png",
    },
    equipped: true,
  },
  {
    id: 2,
    cosmetic: {
      name: "Blue Shirt",
      slot: "Body",
      icon: "/assets/cosmetics/blue_shirt.png",
    },
    equipped: false,
  },
]);

const items = ref([
  {
    id: 1,
    consumable: {
      name: "Health Potion",
      icon: "/assets/items/potion.png",
    },
    quantity: 3,
  },
  {
    id: 2,
    consumable: {
      name: "Energy Drink",
      icon: "/assets/items/energy.png",
    },
    quantity: 5,
  },
]);

// 🔹 Search y filtro
const search = ref("");
const filter = ref("all");

// 🔹 Simulación acción equipar
function equipItem(item) {
  console.log("Equip item:", item);
  // en backend se haría POST a "customize-equip"
}
</script>

<style scoped>
.h100 {
  height: 100%;
}
.w100 {
  width: 100%;
}
.inventory-slot {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 5px;
  background: white;
  cursor: pointer;
}
.inventory-image {
  max-width: 100%;
  height: auto;
}
</style>
