resource "local_file" "app_config" {
    filename = "./app/config"
    content = "production=true"
}

output "app_name" {
    value = "app012"
}