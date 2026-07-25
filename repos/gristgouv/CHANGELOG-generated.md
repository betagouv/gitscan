# Synthèse d'activité : gristgouv (du 13 juin au 16 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation gristgouv s'est concentrée sur l'amélioration de la sécurité, la qualité du code et l'enrichissement des fonctionnalités de la plateforme Grist. Des nouveaux widgets de visualisation de données ont été intégrés, et des améliorations ont été apportées à la gestion des erreurs et à la compatibilité des widgets existants. L'image Docker a été renforcée avec un scanner de vulnérabilités et une meilleure isolation grâce à GVISOR. Des efforts importants ont également été consacrés à l'amélioration de l'expérience d'apprentissage via le mooc Grist et à l'ajout de tests automatisés pour le formulaire intra. Enfin, des corrections de bugs et des améliorations de l'authentification OAuth ont été implémentées dans le cœur de Grist.

## Sécurité
L'image Docker Grist a bénéficié d'améliorations significatives en matière de sécurité grâce à l'intégration de Trivy, un scanner de vulnérabilités, et à l'utilisation de GVISOR pour une meilleure isolation de l'environnement de construction [grist-docker-image](/repos/gristgouv/grist-docker-image).

## Autres changements notables
- Ajout d'un proxy pour le fleet Grist dans [grist-core](/repos/gristgouv/grist-core) pour faciliter la communication entre serveurs.
- Support de l'enregistrement dynamique des clients OAuth (RFC 7591) dans [grist-core](/repos/gristgouv/grist-core).
- Ajout d'une suite de tests automatisés (smoke tests) avec Vitest pour le formulaire intra [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).

## Dépôts les plus actifs
- [widgets-config](/repos/gristgouv/widgets-config) : Ajout de nouveaux widgets D3.js pour enrichir les visualisations disponibles.
- [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) : Amélioration de la lisibilité et de la robustesse des widgets, notamment en gérant mieux l'affichage des erreurs.
- [grist-docker-image](/repos/gristgouv/grist-docker-image) : Renforcement de la sécurité de l'image Docker avec Trivy et GVISOR.
- [grist-core](/repos/gristgouv/grist-core) : Corrections de bugs, améliorations de l'authentification OAuth et ajout de nouvelles fonctionnalités comme le masquage des numéros de ligne.
