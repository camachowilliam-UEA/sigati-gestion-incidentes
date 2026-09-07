# Sistema de Gestión e Inventario de Activos de TI y Control de Incidentes (SIGA-TI)

**Unidad 3: Implementación de Módulo Nuclear y Aseguramiento de Calidad (CI/CD)**  
**Carrera:** Tecnologías de la Información — Universidad Estatal Amazónica (UEA)  
**Asignatura:** Ingeniería de Software  
**Integrantes:**
- William Alexander Camacho Sánchez (Líder de análisis / Documentador ágil)
- Brayan Jacinto Camacho Tapia (Analista de procesos)

---

## 1. Módulo Implementado
Implementación del núcleo de validación de reglas de negocio para el registro de tickets técnicos de soporte informático (**RF-004** y **RF-007**).

## 2. Estrategia de Ramas (GitHub Flow)
- `main`: Rama de producción. Contiene código testeado, estable y validado por la integración continua.
- `feature/*`: Ramas de características temporales (ej: `feature/validacion-incidentes`). Todo cambio se consolida exclusivamente a través de Pull Requests.

## 3. Integración Continua (CI)
Pipeline configurado en GitHub Actions que compila el entorno Python 3.11 y ejecuta la suite de pruebas unitarias con `pytest` en cada evento de `push` o `pull_request`.