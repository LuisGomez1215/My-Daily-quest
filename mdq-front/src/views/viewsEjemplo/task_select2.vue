<template>
  <IonPage>
    <IonContent
      class="gamertext d-flex justify-content-center align-items-center vh-100"
      :style="{ backgroundImage: 'url(/assets/backgrounds/background.png)', backgroundSize: 'cover' }"
    >
      <div class="container task-screen text-light py-3 col-10 col-md-6 col-lg-4 d-flex flex-column">
        <hr class="divider" />

        <!-- Título -->
        <div class="d-flex justify-content-between align-items-center mb-3 px-2">
          <span class="small" style="color:black;">🛒 Select goals to add!</span>
        </div>

        <!-- Lista de tareas -->
        <div class="task-list">
          <div
            v-for="task in tasks"
            :key="task.id"
            class="task-item d-flex align-items-center mb-2"
          >
            <!-- Icono -->
            <span class="task-icon me-2">
              {{ task.icon ? task.icon : "🎯" }}
            </span>

            <!-- Nombre -->
            <span class="task-text flex-grow-1">{{ task.name }}</span>

            <!-- Botón Add -->
            <IonButton
              size="small"
              color="success"
              class="ms-auto"
              @click="addTask(task.id)"
            >
              Add
            </IonButton>
          </div>

          <!-- Caso sin tareas -->
          <div
            v-if="tasks.length === 0"
            class="text-center small text-muted fst-italic"
          >
            <p style="color:black;">
              All default goals already added ✅
            </p>
          </div>
        </div>

        <!-- Crear nueva tarea -->
        <div class="add-goal-btn mt-4 text-center">
          <IonButton expand="block" color="primary" router-link="/create-task">
            ＋ CREATE GOAL!
          </IonButton>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { ref } from "vue";
import { IonPage, IonContent, IonButton } from "@ionic/vue";

// Lista de tareas (más adelante vendrá de la API/Django Rest)
const tasks = ref([
  { id: 1, name: "Go to the gym", icon: "💪" },
  { id: 2, name: "Read a book", icon: "📖" },
  { id: 3, name: "Meditate", icon: null },
]);

function addTask(taskId) {
  console.log("Task added:", taskId);
  // Aquí conectar con la API (POST a backend)
}
</script>

<style scoped>
.task-screen {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 12px;
  padding: 1rem;
}

.task-item {
  background: rgba(240, 240, 240, 0.9);
  border-radius: 8px;
  padding: 0.5rem;
}

.divider {
  border: 1px solid #000;
}
</style>
