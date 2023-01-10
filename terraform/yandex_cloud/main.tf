terraform {
  required_version = ">= 0.13"

  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.73.0"
    }
    local = {
      source  = "terraform-registry.storage.yandexcloud.net/hashicorp/local"
      version = "2.2.2"
    }
  }
}

provider "yandex" {
  token     = var.yc_token
  cloud_id  = var.yc_cloud_id
  folder_id = var.yc_folder_id
  zone      = var.yc_zone
}


resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd8jekrp7jglcetucr2a"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = file("users.txt")
  }
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = var.yc_zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_vpc_security_group" "group-1" {
  name = "Security group"
  description = "Security group allowing incoming 8080 and 22 and any outgoing"
  network_id  = yandex_vpc_network.network-1.id

  labels = {
    my-label = "default-sg"
  }

  ingress {
    protocol       = "TCP"
    description    = "User service port"
    v4_cidr_blocks = ["0.0.0.0/0", ]
    port           = 5000
  }

  ingress {
    protocol       = "TCP"
    description    = "SSH service port"
    v4_cidr_blocks = ["0.0.0.0/0", ]
    port           = 22
  }

  egress {
    protocol       = "ANY"
    description    = "Any outgoing connections"
    v4_cidr_blocks = ["0.0.0.0/0", ]
    from_port      = 0
    to_port        = 0
  }
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}