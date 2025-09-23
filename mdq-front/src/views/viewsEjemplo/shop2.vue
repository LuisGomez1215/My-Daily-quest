<template>
  <IonPage>
    <IonContent
      class="gamertext ion-padding"
      :style="{ backgroundImage: `url(${backgroundImg})` }"
      fullscreen
    >
      <!-- Fondo decorativo -->
      <div class="container">
        <div class="d-flex justify-content-center align-items-center petscreen position-relative">
          <img class="h100 w100 img-fluid" :src="boxPetImg" />
        </div>
      </div>

      <!-- Buscador y filtro -->
      <div class="container py-4">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <IonSearchbar
            v-model="searchQuery"
            placeholder="Search items..."
            class="me-2"
          />
          <IonSelect v-model="selectedCategory" interface="popover" placeholder="All">
            <IonSelectOption value="All">All</IonSelectOption>
            <IonSelectOption value="Cosmetics">Cosmetics</IonSelectOption>
            <IonSelectOption value="Consumables">Consumables</IonSelectOption>
            <IonSelectOption value="Backgrounds">Backgrounds</IonSelectOption>
          </IonSelect>
        </div>

        <!-- Grid de ítems -->
        <IonGrid>
          <IonRow>
            <IonCol
              size="6"
              size-md="3"
              v-for="item in filteredItems"
              :key="item.id"
            >
              <IonCard
                class="inventory-slot d-flex justify-content-center align-items-center"
              >
                <img
                  :src="item.icon"
                  :alt="item.name"
                  class="inventory-image"
                />
              </IonCard>

              <IonCard class="small text-center mt-2">
                <template v-if="item.owned">
                  <p style="color: gray">{{ item.name }}</p>
                  <IonBadge color="success">✔ Owned</IonBadge>
                </template>
                <template v-else>
                  <a href="#" @click.prevent="confirmPurchase(item)">
                    <p class="text-wrap" style="color: black; overflow-wrap: break-word;">
                      {{ item.name }}
                    </p>
                  </a>
                  <p style="color: black" class="fw-light fst-italic">
                    ${{ item.price }}
                  </p>
                </template>
              </IonCard>
            </IonCol>
          </IonRow>
        </IonGrid>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import {
  IonPage,
  IonContent,
  IonSearchbar,
  IonSelect,
  IonSelectOption,
  IonGrid,
  IonRow,
  IonCol,
  IonBadge,
  IonCard,
} from "@ionic/vue";
import { ref, computed } from "vue";

// 🔹 Fondos
const backgroundImg = "/assets/backgrounds/background.png";
const boxPetImg = "/assets/backgrounds/boxpet.png";

// 🔹 Mock de items (API luego)
const items = ref([
  {
    id: 1,
    name: "Magic Hat",
    price: 120,
    owned: false,
    category: "Cosmetics",
    icon: "/assets/items/magic_hat.png",
  },
  {
    id: 2,
    name: "Health Potion",
    price: 50,
    owned: false,
    category: "Consumables",
    icon: "/assets/items/potion.png",
  },
  {
    id: 3,
    name: "Forest Background",
    price: 300,
    owned: true,
    category: "Backgrounds",
    icon: "/assets/items/forest_bg.png",
  },
]);

// 🔹 Buscador y filtro
const searchQuery = ref("");
const selectedCategory = ref("All");

const filteredItems = computed(() => {
  return items.value.filter((item) => {
    const matchesCategory =
      selectedCategory.value === "All" || item.category === selectedCategory.value;
    const matchesSearch = item.name
      .toLowerCase()
      .includes(searchQuery.value.toLowerCase());
    return matchesCategory && matchesSearch;
  });
});

// 🔹 Confirmar compra
function confirmPurchase(item) {
  if (confirm(`Do you want to buy "${item.name}" for $${item.price} credits?`)) {
    console.log("Purchased:", item);
    // TODO: integrar con backend API
  }
}
</script>

<style scoped>
.inventory-slot {
  background: #f0f0f0;
  border-radius: 12px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.inventory-image {
  max-width: 80%;
  max-height: 80%;
}

.fst-italic {
  font-style: italic;
}
</style>
