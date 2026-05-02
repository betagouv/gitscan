# Synthèse d'activité : anct-cartographie-nationale (du 29/04/2024 au 30/04/2026)

## Résumé de l'activité
L'organisation a connu une période d'activité soutenue, axée sur l'amélioration des performances et de la sécurité de la plateforme cartographique. Des optimisations significatives ont été apportées au temps de chargement des pages, à la gestion du cache et à la protection contre les abus. Par ailleurs, des améliorations ont été apportées à l'outil en ligne de commande [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) pour une meilleure gestion des adresses et des lieux de médiation, notamment via l'optimisation de l'utilisation de l'API BAN et de l'API Cartographie Nationale.

## Sécurité
Des mesures de sécurité importantes ont été implémentées dans [cartographie](/repos/anct-cartographie-nationale/cartographie) :
- Ajout de limitations de débit pour se protéger contre les attaques et les abus.
- Blocage des bots malveillants sur les exports et configuration du pare-feu Nginx.
- Implémentation d'un pare-feu géographique pour restreindre l'accès en fonction de la localisation.
- Intégration de CrowdSec pour la détection collaborative des menaces.

## Autres changements notables
[cartographie](/repos/anct-cartographie-nationale/cartographie) a bénéficié de plusieurs évolutions techniques majeures :
- Optimisation significative des performances via la mise en cache, le chargement paresseux de MapLibre et l'extraction du contenu LCP vers des composants serveur.
- Réduction de la taille de l'image Docker de 42%.
- Amélioration de la configuration des ressources conteneur Scaleway et ajout d'un endpoint de vérification de l'état de santé.
- Refactorisation de la configuration Nginx et ajout de tests associés.
- Ajout de logs d'accès Nginx avec l'adresse IP du client et le statut du cache.

[mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a vu sa configuration CI/CD améliorée et l'URL de l'API Cartographie Nationale mise à jour pour utiliser CloudFront.

## Dépôts les plus actifs
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Améliorations majeures des performances, de la sécurité et de l'infrastructure de la plateforme cartographique.
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Optimisation de la gestion des adresses et des lieux de médiation, et amélioration du workflow CI/CD.
