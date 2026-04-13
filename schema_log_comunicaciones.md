# Schema: `reportes.log_comunicaciones`
**Colección MongoDB** — Filtro de extracción: `{ cola_id: 43 }`

---

## Campos Raíz

| Campo | Tipo BSON | Requerido | Descripción |
|-------|-----------|-----------|-------------|
| `_id` | objectId | SI | Identificador único del documento |
| `agente_id` | int | no | ID del agente |
| `agente_nombre` | string | no | Nombre del agente |
| `alias_contacto` | string | no | Alias del contacto |
| `anio_fin_atencion` | int | no | Año de fin de atención |
| `anio_ingreso` | int | SI | Año de ingreso |
| `anio_inicio_atencion` | int | no | Año de inicio de atención |
| `arranque_id` | int | no | ID de arranque |
| `callid` | string | no | ID de llamada |
| `campana_id` | int | no | ID de campaña |
| `campana_nombre` | string | no | Nombre de campaña |
| `chan_id` | string | no | ID de canal |
| `codigo_atencion` | string | no | Código de atención |
| `cola_id` | int | no | ID de cola (**filtro: 43**) |
| `cola_nombre` | string | no | Nombre de la cola |
| `comunicacion_id` | string | no | ID de comunicación |
| `correlativo` | string | SI | Correlativo del registro |
| `dia_semana_fin_atencion_id` | int | no | ID día de semana fin atención |
| `dia_semana_fin_atencion_nombre` | string | no | Nombre día de semana fin atención |
| `dia_semana_ingreso_id` | int | SI | ID día de semana de ingreso |
| `dia_semana_ingreso_nombre` | string | SI | Nombre día de semana de ingreso |
| `dia_semana_inicio_atencion_id` | int | no | ID día de semana inicio atención |
| `dia_semana_inicio_atencion_nombre` | string | no | Nombre día de semana inicio atención |
| `estado_atencion` | int | no | Estado de la atención |
| `etiqueta_id` | string | no | ID de etiqueta |
| `etiqueta_nombre` | string | no | Nombre de etiqueta |
| `extension` | string | no | Extensión telefónica |
| `fecha_fin` | date | no | Fecha de fin |
| `fecha_fin_atencion` | date | no | Fecha de fin de atención |
| `fecha_fin_atencion_index` | date | no | Fecha fin atención (índice) |
| `fecha_fin_comunicacion` | date | no | Fecha fin de comunicación |
| `fecha_ingreso_cola` | date | no | Fecha de ingreso a la cola |
| `fecha_ingreso_cola_index` | date | no | Fecha ingreso cola (índice) |
| `fecha_inicio` | date | no | Fecha de inicio |
| `fecha_inicio_atencion` | date | no | Fecha de inicio de atención |
| `fecha_inicio_atencion_data_comparacion` | string | no | Fecha inicio atención para comparación |
| `fecha_inicio_atencion_index` | date | no | Fecha inicio atención (índice) |
| `fecha_inicio_comunicacion` | date | no | Fecha inicio de comunicación |
| `fecha_inicio_comunicacion_index` | date | no | Fecha inicio comunicación (índice) |
| `fecha_primer_registro` | date | no | Fecha del primer registro |
| `fecha_primera_respuesta_agente` | date | no | Fecha primera respuesta del agente |
| `fin_timbrado_marcador` | date | no | Fin de timbrado del marcador |
| `finalizada_por` | string | no | Quién finalizó la comunicación |
| `gestion_unica` | bool | no | Indica si es gestión única |
| `hora_fin_atencion_index` | int | no | Hora fin atención (índice) |
| `hora_ingreso_cola_index` | int | no | Hora ingreso cola (índice) |
| `hora_inicio_atencion_index` | int | no | Hora inicio atención (índice) |
| `hora_inicio_comunicacion_index` | int | no | Hora inicio comunicación (índice) |
| `identificacion` | string | no | Identificación del contacto |
| `inicio_timbrado_marcador` | date | no | Inicio de timbrado del marcador |
| `instancia` | string | no | Instancia del sistema |
| `isMarcador` | bool | no | Indica si es marcador |
| `lote_id` | long | no | ID de lote |
| `lote_nombre` | string | no | Nombre de lote |
| `mes_fin_atencion` | int | no | Mes de fin de atención |
| `mes_ingreso` | int | SI | Mes de ingreso |
| `mes_inicio_atencion` | int | no | Mes de inicio de atención |
| `nodo_id` | int | no | ID de nodo |
| `nodo_nombre` | string | no | Nombre del nodo |
| `nombre_sub_resultado` | string | no | Nombre del sub-resultado |
| `origen` | string | no | Origen de la comunicación |
| `proveedor_id` | long | no | ID del proveedor |
| `proveedor_nombre` | string / null | no | Nombre del proveedor |
| `publicidad_id` | long | no | ID de publicidad |
| `publicidad_identificador` | string | no | Identificador de publicidad |
| `publicidad_nombre` | string | no | Nombre de publicidad |
| `realizado_tipificacion_obligatoria` | long | no | Indica si se realizó tipificación obligatoria |
| `resultado_id` | int | no | ID del resultado |
| `resultado_marcador_id` | int | no | ID del resultado del marcador |
| `resultado_marcador_nombre` | string | no | Nombre del resultado del marcador |
| `servicio_id` | int | SI | ID del servicio |
| `servicio_secundario` | bool | no | Indica si es servicio secundario |
| `sip_code` | string / null | no | Código SIP |
| `sub_resultado_id` | long | no | ID del sub-resultado |
| `sub_tipo_marcador_id` | long | no | ID del sub-tipo de marcador |
| `sub_tipo_marcador_nombre` | string | no | Nombre del sub-tipo de marcador |
| `supera_umbral` | bool | no | Indica si supera el umbral |
| `tiempo` | int | no | Tiempo total |
| `tiempo_atencion` | int | no | Tiempo de atención |
| `tiempo_cola` | int | no | Tiempo en cola |
| `tiempo_conversacion` | int | no | Tiempo de conversación |
| `tiempo_gestion` | int | no | Tiempo de gestión |
| `tiempo_ring` | int | no | Tiempo de ring |
| `tiempo_ring_acumulado` | long | no | Tiempo ring acumulado |
| `tiempo_ring_agente` | long | no | Tiempo ring del agente |
| `tiempo_timbrado_marcador` | int | no | Tiempo de timbrado del marcador |
| `tipo_comunicacion_id` | int | SI | ID del tipo de comunicación |
| `tipo_marcador_id` | long | no | ID del tipo de marcador |
| `tipo_marcador_nombre` | string | no | Nombre del tipo de marcador |
| `tipo_telefono_marcador` | string | no | Tipo de teléfono del marcador |
| `whatsapp_id` | string | no | ID de WhatsApp |
| `workflow_nombre` | string | no | Nombre del workflow |
| `workflow_numero` | string | no | Número del workflow |
| `field-1` | string | no | Campo adicional 1 |
| `field-2` | string | no | Campo adicional 2 |

---

## Objeto Anidado: `contacto`

| Campo | Tipo BSON | Requerido | Descripción |
|-------|-----------|-----------|-------------|
| `contacto._id.date` | string | SI | Fecha del ID del contacto |
| `contacto._id.timestamp` | long | SI | Timestamp del ID del contacto |
| `contacto.campana` | long | no | ID de campaña del contacto |
| `contacto.carga_id` | string | no | ID de carga |
| `contacto.chan_id` | string | no | ID de canal del contacto |
| `contacto.contacto_id` | long | no | ID interno del contacto |
| `contacto.contacto_nombre` | string | no | Nombre del contacto |
| `contacto.contacto_validado` | long | no | Indica si el contacto fue validado |
| `contacto.correos` | string / array | SI | Correos electrónicos |
| `contacto.departamento` | string | SI | Departamento |
| `contacto.dirección` | string | SI | Dirección |
| `contacto.distrito` | string | SI | Distrito |
| `contacto.facebooks` | array | no | Perfiles de Facebook |
| `contacto.fecha_creacion` | string | no | Fecha de creación del contacto |
| `contacto.fecha_modificacion` | string | no | Fecha de modificación del contacto |
| `contacto.from_marcador` | bool | no | Indica si proviene del marcador |
| `contacto.id_campana` | string | no | ID de campaña (string) |
| `contacto.id_contacto` | long | SI | ID del contacto |
| `contacto.isDirty` | bool | no | Indica si el contacto fue modificado |
| `contacto.lote_id` | string | no | ID de lote del contacto |
| `contacto.nombre` | string | SI | Nombre del contacto |
| `contacto.nombre_base` | string | SI | Nombre en base de datos |
| `contacto.nro_de_documento` | string | SI | Número de documento |
| `contacto.numeros` | string | no | Números adicionales |
| `contacto.otros_distritos` | string | no | Otros distritos |
| `contacto.provincia` | string | SI | Provincia |
| `contacto.telefonos` | array[string] | SI | Lista de teléfonos |
| `contacto.tipo_campaña` | string | no | Tipo de campaña |
| `contacto.tipo_de_campaña` | string | no | Tipo de campaña (alternativo) |
| `contacto.twitters` | array | no | Perfiles de Twitter |

---

## Array Anidado: `detalle[]`

Cada elemento del array `detalle` contiene:

| Campo | Tipo BSON | Requerido | Descripción |
|-------|-----------|-----------|-------------|
| `comunicacion_id` | string | SI | ID de la comunicación |
| `fecha_fin` | string | SI | Fecha de fin del nodo |
| `fecha_inicio` | string | SI | Fecha de inicio del nodo |
| `mensaje_entrante` | string | SI | Mensaje entrante |
| `nodo_id` | long | SI | ID del nodo |
| `nodo_nombre` | string | SI | Nombre del nodo |
| `respuesta_id` | string | SI | ID de la respuesta |
| `respuesta_nombre` | string | SI | Nombre de la respuesta |
| `tiempo` | long | SI | Tiempo en el nodo |
| `tipo_nodo` | long | SI | Tipo de nodo |

---

## Array Anidado: `gestiones[]`

Cada elemento del array `gestiones` contiene:

| Campo | Tipo BSON | Requerido | Descripción |
|-------|-----------|-----------|-------------|
| `comentario` | string | SI | Comentario de la gestión |
| `fecha_index` | date / string | SI | Fecha (índice) |
| `fecha_registro` | date / string | SI | Fecha de registro |
| `fecha_string` | string | no | Fecha en formato string |
| `hora_index` | int / long | SI | Hora (índice) |
| `nivel1` | long / int | SI | ID nivel 1 de tipificación |
| `nivel1_nombre` | string | SI | Nombre nivel 1 |
| `nivel2` | long / int | SI | ID nivel 2 de tipificación |
| `nivel2_nombre` | string | SI | Nombre nivel 2 |
| `nivel3` | long / int | SI | ID nivel 3 de tipificación |
| `nivel3_nombre` | string | SI | Nombre nivel 3 |
| `nivel4` | long / int | SI | ID nivel 4 de tipificación |
| `nivel4_nombre` | string | SI | Nombre nivel 4 |
| `resultado_id` | long | SI | ID del resultado |
| `resultado_nombre` | string | SI | Nombre del resultado |
| `tema_id` | long | SI | ID del tema |
| `tema_nombre` | string | SI | Nombre del tema |

---

## Array Anidado: `gestiones_old[]`

Cada elemento del array `gestiones_old` contiene (versión legacy):

| Campo | Tipo BSON | Requerido | Descripción |
|-------|-----------|-----------|-------------|
| `comentario` | string | SI | Comentario de la gestión |
| `fecha_index` | date | SI | Fecha (índice) |
| `fecha_registro` | date | SI | Fecha de registro |
| `fecha_string` | string | SI | Fecha en formato string |
| `hora_index` | int | SI | Hora (índice) |
| `nivel1` | long | SI | ID nivel 1 |
| `nivel1_nombre` | string | SI | Nombre nivel 1 |
| `nivel2` | long / int | SI | ID nivel 2 |
| `nivel2_nombre` | string | SI | Nombre nivel 2 |
| `nivel3` | long | SI | ID nivel 3 |
| `nivel3_nombre` | string | SI | Nombre nivel 3 |
| `nivel4` | long | SI | ID nivel 4 |
| `nivel4_nombre` | string | SI | Nombre nivel 4 |
| `resultado_id` | long | SI | ID del resultado |
| `resultado_nombre` | string | SI | Nombre del resultado |
| `tema_id` | long | SI | ID del tema |
| `tema_nombre` | string | SI | Nombre del tema |

---

## Objeto Anidado: `marcador_info`

| Campo | Tipo BSON | Requerido | Descripción |
|-------|-----------|-----------|-------------|
| `arranque_id` | long / string | SI | ID de arranque |
| `chan_id` | string | SI | ID de canal |
| `code` | string | SI | Código del marcador |
| `dato1` … `dato20` | string | SI | Datos del marcador (1 al 20) |
| `lote_id` | long / string | SI | ID de lote |
| `lote_nombre` | string | SI | Nombre del lote |
| `nombre` | string | SI | Nombre del contacto en marcador |
| `numero` | string | SI | Número marcado |
| `register_id` | long / string | SI | ID de registro |
| `resultado_id` | long | no | ID del resultado del marcador |
| `sub_tipo_marcador_id` | long / string | SI | ID sub-tipo de marcador |
| `sub_tipo_marcador_nombre` | string | SI | Nombre sub-tipo de marcador |
| `tipo_marcador_id` | long / string | SI | ID tipo de marcador |
| `tipo_marcador_nombre` | string | SI | Nombre tipo de marcador |
| `tipo_numero` | string | SI | Tipo de número marcado |
| `field-1` | string | no | Campo adicional |

---

## Query de extracción MongoDB

```js
db.getCollection("reportes.log_comunicaciones").find({ cola_id: 43 })
```

### Proyección sugerida (campos principales)

```js
db.getCollection("reportes.log_comunicaciones").find(
  { cola_id: 43 },
  {
    _id: 1,
    cola_id: 1,
    cola_nombre: 1,
    agente_id: 1,
    agente_nombre: 1,
    campana_id: 1,
    campana_nombre: 1,
    fecha_ingreso_cola: 1,
    fecha_inicio_atencion: 1,
    fecha_fin_atencion: 1,
    tiempo_cola: 1,
    tiempo_atencion: 1,
    tiempo_conversacion: 1,
    estado_atencion: 1,
    resultado_id: 1,
    tipo_comunicacion_id: 1,
    "contacto.nombre": 1,
    "contacto.nro_de_documento": 1,
    "contacto.telefonos": 1,
    "gestiones": 1
  }
)
```
