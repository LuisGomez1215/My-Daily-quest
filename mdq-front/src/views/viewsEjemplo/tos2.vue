<template>
  <IonPage>
    <IonContent class="ion-padding">
      <div class="container">
        <h2 class="ion-text-center">Términos y condiciones</h2>
        <IonItemDivider />

        <div>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris et est neque...
          </p>

          <h4><strong>Lorem et Ipsum</strong></h4>
          <p>
            Illyricum anean blandit lacus a lorem rhoncus feugiat. In sollicitudin urna...
          </p>

          <h4><strong>Viennensis et neam Baetica</strong></h4>
          <p>
            Nullam mollis tortor sed velit hendrerit fringilla. Nunc volutpat lorem in varius...
          </p>

          <h4><strong>Lugdunensis</strong></h4>
          <p>
            Nulla facilisi. Donec varius odio sed enim tempus, nec sagittis erat dictum...
          </p>

          <IonList>
            <IonItem>Publicar contenido ilegal o que no tenga relación con el objetivo fundamental de la aplicación.</IonItem>
            <IonItem>Publicar ventas u ofertas propias o de comercios no establecidos legalmente según las leyes chilenas vigentes.</IonItem>
            <IonItem>Publicaciones que tengan como objetivo la promoción de servicios de prostitución o pornografía.</IonItem>
            <IonItem>Publicaciones que busquen promover causas diferentes a la adquisición de un producto o servicio...</IonItem>
            <IonItem>Todo tipo de publicación que tenga por objetivo el engaño, fraude, robo de identidad, propagación de malware...</IonItem>
            <IonItem>Publicaciones de concursos sin la expresa autorización de Descuentos Rata.</IonItem>
            <IonItem>Publicaciones que aprovechen vulnerabilidades de sistemas computacionales de todo tipo...</IonItem>
            <IonItem>Cualquier promoción que contravenga las leyes chilenas o el criterio directo de Descuentos Rata.</IonItem>
            <IonItem>Cualquier publicación que tenga por objeto interferir con la seguridad de este sitio...</IonItem>
          </IonList>

          <p>
            Duis id scelerisque est. Quisque pharetra quam massa, at tincidunt lacus tristique...
          </p>

          <h4><strong>Alpes Cottiae</strong></h4>
          <p>
            Suspendisse auctor tempus ante. Duis ut maximus elit, quis porttitor ligula...
          </p>

          <h4><strong>Noricum Ripense</strong></h4>
          <p>
            Sed pretium quam et urna hendrerit, et tempus ligula vehicula. Mauris a maximus ante...
          </p>
        <IonButton expand="block" @click="$router.push('/registro')">
          Aceptar y continuar
        </IonButton>  
        </div>
      </div>
    </IonContent>
  </IonPage>
</template>

<script setup>
import { IonPage, IonContent, IonItemDivider, IonList, IonItem } from "@ionic/vue";
</script>
