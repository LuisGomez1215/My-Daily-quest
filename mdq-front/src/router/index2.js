import { createRouter, createWebHistory } from 'vue-router'

// Páginas principales
import Home from '@/templates2/templates2/index2.vue'
import NotFound from '@/templates2/templates2/4042.vue'

// Registration
import Login from '@/templates2/templates2/registration/login2.vue'
import Register from '@/templates2/templates2/registration/register2.vue'
import PasswordReset from '@/templates2/templates2/registration/password-reset2.vue'
import PasswordResetDone from '@/templates2/templates2/registration/password-reset-done2.vue'
import PasswordResetChange from '@/templates2/templates2/registration/password-reset-change2.vue'
import PasswordResetComplete from '@/templates2/templates2/registration/password-reset-complete2.vue'
import Tos from '@/templates2/templates2/registration/tos2.vue'

// Adventure
import Adventure from '@/templates2/templates2/adventure/adventure2.vue'
import AdventureConfirmation from '@/templates2/templates2/adventure/adventure_confirmation2.vue'

// Tasks
import Tasks from '@/templates2/templates2/tasks/tasks2.vue'
import TaskSelect from '@/templates2/templates2/tasks/task_select2.vue'
import NewTask from '@/templates2/templates2/tasks/new_task2.vue'

// Pages
import PetSelect from '@/templates2/templates2/pages/pet_select2.vue'
import PetSelectForm from '@/templates2/templates2/pages/pet_select_form2.vue'
import Customize from '@/templates2/templates2/pages/customize2.vue'
import Shop from '@/templates2/templates2/pages/shop2.vue'

// Settings
import UserSettings from '@/templates2/templates2/settings/user_settings2.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/password-reset', component: PasswordReset },
  { path: '/password-reset-done', component: PasswordResetDone },
  { path: '/password-reset-change', component: PasswordResetChange },
  { path: '/password-reset-complete', component: PasswordResetComplete },
  { path: '/tos', component: Tos },
  { path: '/adventure', component: Adventure },
  { path: '/adventure-confirmation', component: AdventureConfirmation },
  { path: '/tasks', component: Tasks },
  { path: '/task-select', component: TaskSelect },
  { path: '/new-task', component: NewTask },
  { path: '/pet-select', component: PetSelect },
  { path: '/pet-select-form', component: PetSelectForm },
  { path: '/customize', component: Customize },
  { path: '/shop', component: Shop },
  { path: '/settings', component: UserSettings },
  { path: '/:pathMatch(.*)*', component: NotFound } // 404
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
