provider "local" {
    # to test in local
}

module "network" {
    source = "./modules/network"
}

module "database" {
    source = "./modules/database"
}

module "application" {
    source = "./modules/application"
}

output "network_output" {
    value = module.network.network_name
}

output "database_output" {
    value = module.database.database_name
}

output "application_output" {
    value = module.application.app_name
}

# output "app_file" {
#    value = local_file.app_config.filename
# }