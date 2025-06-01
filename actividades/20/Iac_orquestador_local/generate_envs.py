import os, json
from shutil import copyfile

# Parámetros de ejemplo para N entornos
ENVS = [
    {"name": f"app{i}", "network": f"net{i}"} for i in range(1, 11)
]

ENVS2 = [
    {"name": f"app{i}", "network": f"net{i}"} for i in range(1, 51)
]

MODULE_DIR = "modules/simulated_app"
OUT_DIR    = "environments"

def render_and_write(env):
    env_dir = os.path.join(OUT_DIR, env["name"])
    os.makedirs(env_dir, exist_ok=True)

    # 1) Copia la definición de variables (network.tf.json)
    copyfile(
        os.path.join(MODULE_DIR, "network.tf.json"),
        os.path.join(env_dir, "network.tf.json")
    )

    # 2) Genera main.tf.json SÓLO con recursos
    # fix para utilizar variables de cada app en network.tf.json
    config = {
        "resource": [
            {
                "null_resource": [
                    {
                        env["name"]: [
                            {
                                "triggers": {
                                    "name":    "${var.name}",
                                    "network": "${var.network}"
                                },
                                "provisioner": [
                                    {
                                        "local-exec": {
                                            "command": (
                                                f"echo 'Arrancando servidor "
                                                f"{env['name']} en red {env['network']}'"
                                            )
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    with open(os.path.join(env_dir, "main.tf.json"), "w") as fp:
        json.dump(config, fp, sort_keys=True, indent=4)

def render_and_write_2(env):
    env_dir = os.path.join(OUT_DIR, env["name"])
    dev_dir = os.path.join(env_dir, "dev")
    prod_dir = os.path.join(env_dir, "prod")

    os.makedirs(env_dir, exist_ok=True)
    os.makedirs(dev_dir, exist_ok=True)
    os.makedirs(prod_dir, exist_ok=True)

    # 1) Copia la definición de variables (network.tf.json)
    copyfile(
        os.path.join(MODULE_DIR, "network.tf.json"),
        os.path.join(dev_dir, "network.tf.json")
    )

    copyfile(
        os.path.join(MODULE_DIR, "network.tf.json"),
        os.path.join(prod_dir, "network.tf.json")
    )

    # 2) Genera main.tf.json SÓLO con recursos
    # fix para utilizar variables de cada app en network.tf.json
    config = {
        "resource": [
            {
                "null_resource": [
                    {
                        env["name"]: [
                            {
                                "triggers": {
                                    "name":    "${var.name}",
                                    "network": "${var.network}"
                                },
                                "provisioner": [
                                    {
                                        "local-exec": {
                                            "command": (
                                                f"echo 'Arrancando servidor "
                                                f"{env['name']} en red {env['network']}'"
                                            )
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    with open(os.path.join(dev_dir, "main.tf.json"), "w") as fp:
        json.dump(config, fp, sort_keys=True, indent=4)

    with open(os.path.join(prod_dir, "main.tf.json"), "w") as fp:
        json.dump(config, fp, sort_keys=True, indent=4)

def render_and_write_args():
    parser = argparse.ArgumentParser(description="Crear apps")
    parser.add_argument("--count", required=True, help="Numero de apps a crear")
    parser.add_argument("--prefix", required=True, help="Prefijo de las app")
    parser.add_argument("--port", required=True, help="Puerto de las redes de servidores en todas las apps")

    args = parser.parse_args()

    # print(args.count, type(args.count))
    # return
    count = args.count
    prefix_app = f"{args.prefix}-app"

    for i in range(int(count)):
        env_dir = os.path.join(OUT_DIR, f"{prefix_app}-{i}")
        os.makedirs(env_dir, exist_ok=True)

        # 1) Copia la definición de variables (network.tf.json)
        copyfile(
            os.path.join(MODULE_DIR, "network.tf.json"),
            os.path.join(env_dir, "network.tf.json")
        )

        # 2) Genera main.tf.json SÓLO con recursos
        # fix para utilizar variables de cada app en network.tf.json
        config = {
            "resource": [
                {
                    "null_resource": [
                        {
                            f"{prefix_app}": [
                                {
                                    "triggers": {
                                        "name":    "${var.name}",
                                        "network": "${var.network}"
                                    },
                                    "provisioner": [
                                        {
                                            "local-exec": {
                                                "command": (
                                                    f"echo 'Arrancando servidor "
                                                    "${var.name} en red ${var.network}'"
                                                )
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        with open(os.path.join(env_dir, "main.tf.json"), "w") as fp:
            json.dump(config, fp, sort_keys=True, indent=4)


if __name__ == "__main__":
    # Limpia entornos viejos (si quieres)
    # to verify state changes don't delete directories
    # if os.path.isdir(OUT_DIR):
    #     import shutil
    #     shutil.rmtree(OUT_DIR)

    for env in ENVS:
        render_and_write(env)
    print(f"Generados {len(ENVS)} entornos en '{OUT_DIR}/'")

    # use it with flags: --count, --port and --prefix (all required)
    # render_and_write_args()
