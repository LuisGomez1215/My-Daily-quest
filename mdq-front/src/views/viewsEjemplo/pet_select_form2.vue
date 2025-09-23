<template>
  <IonPage>
    <IonContent
      class="gamertext ion-padding"
      :style="{ backgroundImage: `url(${backgroundImg})` }"
      fullscreen
    >
      <div class="container d-flex justify-content-center align-items-center petscreen">
        <form class="w100 h100" @submit.prevent="submitForm">
          <IonCard class="w-100 h-100 text-center" style="background-color: #9b5862ff;">
            <!-- Imagen de la mascota -->
            <IonImg :src="species.pet_avatar" alt="pet" class="card-img-top w-100 circle" />

            <IonCardHeader>
              <IonCardTitle>{{ species.species }}</IonCardTitle>
            </IonCardHeader>

            <!-- Campos del formulario -->
            <IonCardContent style="background-color: #be6b77ff;">
              <IonItem>
                <IonLabel position="stacked">Pet Name</IonLabel>
                <IonInput v-model="form.petName" required />
              </IonItem>

              <IonItem>
                <IonLabel position="stacked">Color</IonLabel>
                <IonSelect v-model="form.color" placeholder="Select color">
                  <IonSelectOption value="brown">Brown</IonSelectOption>
                  <IonSelectOption value="black">Black</IonSelectOption>
                  <IonSelectOption value="white">White</IonSelectOption>
                </IonSelect>
              </IonItem>
            </IonCardContent>

            <!-- Botón -->
            <IonCardContent>
              <IonButton
                expand="block"
                type="submit"
                style="background-color: #bd4d5dff;"
              >
                welcome your new friend!
              </IonButton>
            </IonCardContent>
          </IonCard>
        </form>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import {
  IonPage,
  IonContent,
  IonCard,
  IonCardHeader,
  IonCardTitle,
  IonCardContent,
  IonImg,
  IonItem,
  IonLabel,
  IonInput,
  IonSelect,
  IonSelectOption,
  IonButton,
} from "@ionic/vue";
import { ref } from "vue";

// 🔹 Mock background + species
const backgroundImg = "/assets/backgrounds/background.png";

const species = ref({
  species: "Dragon",
  pet_avatar: "/assets/pets/sample_dragon.png",
});

// 🔹 Formulario simulado
const form = ref({
  petName: "",
  color: "",
});

// 🔹 Acción submit (a futuro → API POST)
function submitForm() {
  console.log("Pet selected:", form.value);
  alert(`Welcome your new friend, ${form.value.petName}!`);
}
</script>

<style scoped>
.w100 {
  width: 100%;
}
.h100 {
  height: 100%;
}
.circle {
  border-radius: 50%;
  max-width: 200px;
  margin: auto;
}
</style>
