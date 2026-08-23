# Restaurante App - Sistema Orientado a Objetos (Semana 10)

## Datos del Estudiante
- **Nombre:** Jhocelyn Del Pozo
- **Asignatura:** Programación Orientada a Objetos
- **Institución:** Universidad Estatal Amazonica (UEA)

---

## Descripción del Sistema
`restaurante_app` es una aplicación modular desarrollada en Python bajo los principios de la Programación Orientada a Objetos (POO). En esta décima semana, el proyecto evoluciona incorporando **persistencia de datos en formato JSON**, manejo estructurado de excepciones y la reconstrucción dinámica de objetos a partir de un almacenamiento externo.

---

## Estructura del Proyecto
El proyecto mantiene una arquitectura modular limpia, separando las entidades de dominio, la lógica del negocio, los servicios de archivos y la interfaz de consola:

```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md