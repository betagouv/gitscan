# Synthèse d'activité : gristgouv (du 08/06 au 16/07/2026)

## Résumé de l'activité
L'activité récente de l'organisation gristgouv s'est concentrée sur l'amélioration de la sécurité, de la qualité du code et de l'expérience utilisateur de la plateforme Grist. L'ajout de nouveaux widgets via [widgets-config](/repos/gristgouv/widgets-config) enrichit les capacités de visualisation des données, tandis que des améliorations apportées à [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) rendent l'affichage des informations plus clair et plus robuste. Le projet [grist-mooc](/repos/gristgouv/grist-mooc) a été mis à jour avec de nouveaux supports de formation, et l'image Docker [grist-docker-image](/repos/gristgouv/grist-docker-image) bénéficie d'une sécurité renforcée grâce à l'intégration d'un scanner de vulnérabilités.

## Sécurité
L'image Docker Grist ([grist-docker-image](/repos/gristgouv/grist-docker-image)) a bénéficié d'une amélioration significative de sa sécurité avec l'intégration de Trivy, un scanner de vulnérabilités, et une meilleure gestion de l'environnement de construction avec GVISOR. Cela permet de détecter et de corriger les failles de sécurité potentielles, renforçant ainsi la protection des données.

## Autres changements notables
- L'ajout d'un proxy pour le fleet Grist dans [grist-core](/repos/gristgouv/grist-core) améliore la communication entre les serveurs.
- L'intégration de tests automatisés dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) renforce la qualité et la stabilité du code.
- Le support de l'enregistrement dynamique des clients OAuth dans [grist-core](/repos/gristgouv/grist-core) offre une plus grande flexibilité pour l'intégration avec d'autres services.

## Dépôts les plus actifs
- [grist-docker-image](/repos/gristgouv/grist-docker-image) : Amélioration de la sécurité et de la robustesse de l'image Docker.
- [grist-core](/repos/gristgouv/grist-core) : Corrections de bugs et ajout de nouvelles fonctionnalités pour l'application principale Grist.
- [widgets-config](/repos/gristgouv/widgets-config) : Ajout de nouveaux widgets de visualisation de données.
- [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) : Amélioration de la lisibilité et de la robustesse des widgets existants.
