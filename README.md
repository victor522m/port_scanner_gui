# 🔍 **Port_Scaner**

**Port_Scaner** es una herramienta de escaneo de puertos con interfaz gráfica (GUI) creada en Python. Permite a los usuarios detectar puertos abiertos en una dirección IP específica, ya sea escaneando un rango definido o revisando una lista de puertos comunes. La aplicación utiliza un diseño amigable con `Tkinter` y un enfoque eficiente basado en hilos para realizar escaneos rápidos y efectivos.

---

## 🚀 **Características**

- **Escaneo de puertos en tiempo real**:
  - Introduce un rango de puertos para escanear o utiliza la lista de puertos comunes.
  - Identifica servicios asociados a los puertos abiertos.

- **Interfaz gráfica intuitiva**:
  - Entradas para dirección IP y rango de puertos.
  - Botones para iniciar el escaneo.
  - Barra de progreso para visualizar el avance.
  - Área de salida para mostrar resultados en tiempo real.

- **Colores personalizados**:
  - Resultados destacados en verde.
  - Mensajes informativos en azul.
  - Barra de progreso en rojo.

- **Validación de entrada**:
  - Verifica que la dirección IP y el rango de puertos sean válidos.

---

## 🖥️ **Captura de pantalla**

```
[+] Puerto 80 ABIERTO - Servicio: http
[+] Puerto 443 ABIERTO - Servicio: https
Escaneo completado.
```

---

## 📦 **Instalación**

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/port_scaner.git
   cd port_scaner
   ```

2. **Asegúrate de tener Python instalado**:
   - Este proyecto requiere **Python 3.7 o superior**. Verifica tu versión con:
     ```bash
     python --version
     ```

3. **Ejecuta el programa**:
   No se necesitan dependencias adicionales. Simplemente ejecuta:
   ```bash
   python port_scaner.py
   ```

---

## 🛠️ **Cómo usar**

1. **Inicia el programa**:
   ```bash
   python port_scaner.py
   ```

2. **Introduce los datos**:
   - Escribe la dirección IP que deseas escanear.
   - Especifica un rango de puertos o utiliza el botón de **puertos comunes**.

3. **Inicia el escaneo**:
   - Haz clic en "Escanear Rango" o "Escanear Puertos Comunes".
   - Observa los resultados en el área de salida y el progreso en la barra.

4. **Resultados**:
   - Los puertos abiertos se muestran en verde con su servicio correspondiente.

---

## 📋 **Estructura del proyecto**

```
port_scaner/
│
├── port_scaner.py   # Código principal del programa
├── README.md        # Este archivo
```

---

## 🔧 **Mejoras futuras**

- **Detección avanzada de servicios**:
  - Implementar técnicas como el banner grabbing para identificar servicios con mayor precisión.

- **Soporte para IPv6**:
  - Ampliar la funcionalidad para incluir direcciones IPv6.

- **Cancelación de escaneos**:
  - Agregar un botón para detener el escaneo en curso.

- **Exportación de resultados**:
  - Permitir guardar los resultados en archivos de texto o CSV.

- **Mejoras en la interfaz**:
  - Hacer la GUI más responsiva y visualmente atractiva.

---

## 🛡️ **Notas de seguridad**

- **Port_Scaner** debe usarse únicamente con fines educativos o éticos.
- **No escanees redes o dispositivos sin permiso explícito**. El uso indebido de esta herramienta puede ser ilegal.

---

## 🧑‍💻 **Contribuciones**

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar **Port_Scaner**, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama:
   ```bash
   git checkout -b mi-mejora
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Mejora: Descripción de la mejora"
   ```
4. Envía un pull request.

---

## 📧 **Contacto**

Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio o contactarme en [tu-email@example.com](mailto:victor522m@gmail.com).

---

¡Gracias por usar **Port_Scaner**! 😊
