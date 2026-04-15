# Création d'un cluster Kubernetes dans OVH & installation de taiga

Dans un premier temps installer terraform sur votre machine : 

### Créé un token API si vous n'en avez pas
Vous obtiendrez votre l'`application key`, `application_secret`, `consumer_key` que vous pourrez préciser dans `terraform.tfvars`.

`service_name` est l'identifiant de votre projet/l'identifiant de souscription (pour OVH, en haut à gauche, sous le nom du projet).

## Installer et configurer Terraform 

Installer la [cli de Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

Remplacer par vos valeurs les variables d'environnement dans le fichier : terraform.tfvars

Taiga doit être accessible depuis l'ip de l'ingress