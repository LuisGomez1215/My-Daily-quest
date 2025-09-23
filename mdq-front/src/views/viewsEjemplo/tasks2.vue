<template>
  <IonPage>
    <IonContent
      class="gamertext d-flex justify-content-center align-items-center vh-100"
      :style="{ backgroundImage: 'url(/assets/backgrounds/background.png)', backgroundSize: 'cover' }"
    >
      <div
        class="container task-screen text-light py-3 col-10 col-md-6 col-lg-4 d-flex flex-column overflow-auto"
      >
        <hr class="divider" />

        <!-- Contador de tareas -->
        <div class="d-flex justify-content-between align-items-center mb-3 px-2">
          <span class="small" style="color:black;">
            📅 {{ tasks.length }} goals left for today!
          </span>
        </div>

        <!-- Lista de tareas -->
        <div
          class="task-list flex-grow-1 overflow-auto px-1"
          style="max-height: 50vh;"
        >
          <div
            v-for="task in tasks"
            :key="task.id"
            class="task-item d-flex align-items-center p-2 border rounded mb-2"
            role="button"
            @click="completeTask(task.id)"
          >
            <!-- Icono -->
            <span class="task-icon me-2">
              {{ task.icon ? task.icon : "🎯" }}
            </span>

            <!-- Nombre -->
            <span class="task-text flex-grow-1">{{ task.name }}</span>

            <!-- Badge Custom -->
            <IonBadge v-if="task.custom" color="warning" class="ms-2 text-dark">
              Custom
            </IonBadge>
          </div>

          <!-- Caso vacío -->
          <div
            v-if="tasks.length === 0"
            class="text-center small"
            style="color:black;"
          >
            You don't have any tasks!
          </div>
        </div>

        <!-- Botón para añadir -->
        <div class="add-goal-btn mt-4 text-center">
          <IonButton expand="block" color="primary" router-link="/task-select">
            ＋ ADD A GOAL!
          </IonButton>
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { ref } from "vue";
import { IonPage, IonContent, IonButton, IonBadge } from "@ionic/vue";

// Lista simulada de tareas (esto luego se cargará desde API/backend)
const tasks = ref([
  { id: 1, name: "Go to the gym", icon: "💪", custom: true },
  { id: 2, name: "Read 20 pages", icon: "📖", custom: false },
  { id: 3, name: "Drink water", icon: null, custom: false },
]);

// Completar tarea
function completeTask(taskId) {
  console.log("Task completed:", taskId);
  // Aquí luego harás el POST al endpoint "task-complete"
}
</script>

<style scoped>
.task-screen {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 12px;
  padding: 1rem;
}

.task-item {
  background: rgba(250, 250, 250, 0.95);
  cursor: pointer;
  transition: background 0.2s ease-in-out;
}
.task-item:hover {
  background: rgba(220, 220, 220, 0.95);
}

.divider {
  border: 1px solid #000;
}
</style>
