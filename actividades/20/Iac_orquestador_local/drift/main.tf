resource "null_resource" "local_server_1" {
  provisioner "local-exec" {
    command = "echo 'server 1!!!'"
  }
}

resource "null_resource" "local_server_3" {
  provisioner "local-exec" {
    command = "echo 'server 2!!!'"
  }
}

resource "null_resource" "load_balancer" {
  depends_on = [null_resource.local_server_1, null_resource.local_server_2]
  provisioner "local-exec" {
    command = "echo 'load balancer!!!!'"
  }
}
