<template>
  <IonPage>
    <IonContent
      class="gamertext d-flex justify-content-center align-items-center vh-100"
      :style="{ backgroundImage: 'url(/assets/backgrounds/background.png)', backgroundSize: 'cover' }"
    >
      <div class="container task-screen text-light py-3 col-10 col-md-6 col-lg-4 d-flex flex-column">
        <hr class="divider" />

        <div class="d-flex justify-content-between align-items-center mb-3 px-2">
          <span class="small" style="color:black;">✏️ Create your own custom goal</span>
        </div>

        <!-- Form -->
        <div class="task-list">
          <form class="d-flex flex-column" @submit.prevent="saveTask">
            <!-- Task Name -->
            <div class="mb-3">
              <IonLabel for="taskName" class="form-label" style="color:black;">Task Name</IonLabel>
              <IonInput
                id="taskName"
                v-model="task.name"
                placeholder="Enter task name"
                fill="outline"
              />
            </div>

            <!-- Task Icon -->
            <div class="mb-3">
              <Ionlabel for="taskIcon" class="form-label" style="color:black;">Task Icon</Ionlabel>
              <input
                id="taskIcon"
                type="file"
                accept="image/*"
                @change="onFileChange"
                class="form-control"
              />
            </div>

            <!-- Save Button -->
            <IonButton expand="block" color="success" class="mt-3" type="submit">
              ✔ Save Goal
            </IonButton>
          </form>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { ref } from "vue";
import { IonPage, IonContent, IonInput, IonButton, IonLabel } from "@ionic/vue";

const task = ref({
  name: "",
  icon: null,
});

function onFileChange(event) {
  const file = event.target.files[0];
  if (file) {
    task.value.icon = file;
  }
}

function saveTask() {
  console.log("Saving task:", task.value);
  // Aquí más adelante conectamos con tu API (Django Rest Framework)
}
</script>

<style scoped>
.task-screen {
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 12px;
  padding: 1rem;
}

.divider {
  border: 1px solid #000;
}

.btn-add-goal {
  font-size: 1rem;
}
</style>
