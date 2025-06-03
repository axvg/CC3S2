variable "nombre_entorno" {
  description = "Nombre base para el entorno generado."
  type        = string
  default     = "desarrollo"
}

variable "numero_instancias_app_simulada" {
  description = "Cuántas instancias de la app simulada crear."
  type        = number
  default     = 2
}

variable "mensaje_global" {
  description = "Un mensaje para incluir en varios archivos."
  type        = string
  default     = "Configuración gestionada por Terraform."
  sensitive   = true # Para demostrar
}

variable "connection_string" {
  type    = string
  default = ""
}

variable "deployment_id" {
  description = "global deployment Id"
  type        = string
  default     = "env_id"
}
