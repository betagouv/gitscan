# Synthèse d'activité : mission-apprentissage (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation "mission-apprentissage" s'est concentrée sur l'amélioration de la plateforme [labonnealternance](/repos/mission-apprentissage/labonnealternance) avec l'ajout de nouvelles fonctionnalités pour les utilisateurs, notamment des filtres de recherche plus précis, l'intégration de nouvelles offres d'emploi (EDF, Enedis) et un bloc salaires avec redirection vers un simulateur. Des corrections de sécurité ont également été apportées à l'infrastructure [infra](/repos/mission-apprentissage/infra) et à la plateforme [labonnealternance](/repos/mission-apprentissage/labonnealternance). La surveillance de la disponibilité des services continue d'être assurée par le projet [upptime](/repos/mission-apprentissage/upptime).

## Sécurité
- Correction de vulnérabilités critiques dans les dépendances de [labonnealternance](/repos/mission-apprentissage/labonnealternance) (handlebars, fast-xml-parser, basic-ftp).
- Correction concernant la gestion des adresses IP de confiance dans l'infrastructure [infra](/repos/mission-apprentissage/infra) pour garantir la sécurité et l'accessibilité des services.

## Autres changements notables
- Amélioration des lectures MongoDB sur les secondaires pour la recherche dans [labonnealternance](/repos/mission-apprentissage/labonnealternance) afin d'optimiser les performances.
- Gestion du rate limit 429 sur l'API job-étudiant avec retry et throttling proactif dans [labonnealternance](/repos/mission-apprentissage/labonnealternance) pour une meilleure robustesse.
- Mise à jour des habilitations du projet LBA dans l'infrastructure [infra](/repos/mission-apprentissage/infra) pour une gestion plus fine des permissions.
- Suppression des requêtes N+1 sur l'API /api/traininglinks dans [labonnealternance](/repos/mission-apprentissage/labonnealternance) pour améliorer l'efficacité.

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Ajout de fonctionnalités et corrections de bugs pour améliorer l'expérience utilisateur et la performance de la plateforme.
- [infra](/repos/mission-apprentissage/infra) : Améliorations de la sécurité et de la gestion des accès à l'infrastructure.
- [upptime](/repos/mission-apprentissage/upptime) : Surveillance continue de la disponibilité des services et mise à jour de l'état.
