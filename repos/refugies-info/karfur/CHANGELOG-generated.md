## Changelog : karfur (30 derniers jours, au 03 novembre 2026)

### Résumé
Ce mois-ci, l'effort principal a porté sur la mise en conformité du projet avec les normes d'accessibilité (RGAA), garantissant une meilleure utilisation pour les personnes en situation de handicap. Parallèlement, le système de notifications a été renforcé et une nouvelle gestion administrative des widgets a été mise en place.

### Évolutions fonctionnelles
- **Notifications** : 
    - Possibilité d'envoyer manuellement des notifications push pour les démarches et les dispositifs ([#4050](https://github.com/refugies-info/karfur/pull/4050)).
    - Amélioration de la fiabilité des notifications et du ciblage des utilisateurs actifs ([#4055](https://github.com/refugies-info/karfur/pull/4055)).
- **Recherche & Apprentissage** :
    - Optimisation de la fluidité de la recherche via l'implémentation de SWR ([#4019](https://github.com/refugies-info/karfur/pull/4019)).
    - Amélioration de l'expérience de recherche dans la section "Apprendre le français" (gestion des erreurs et débogage de la saisie).
- **Expérience Mobile** :
    - Corrections de bugs lors de l'enregistrement des données et de l'affichage des modales.
    - Nettoyage de l'interface (suppression de l'étiquette "Date dépassée" sur iOS/Android) ([#4047](https://github.com/refugies-info/karfur/pull/4047)).

### Évolutions techniques
- **Accessibilité (RGAA)** : Mise en conformité massive incluant :
    - Amélioration des contrastes de texte et des composants graphiques ([#4049](https://github.com/refugies-info/karfur/pull/4049)).
    - Optimisation de l'affichage pour le zoom à 200% et les écrans de petite taille (320px).
    - Amélioration de la navigation au clavier et de l'utilisation des lecteurs d'écran (gestion des titres, des rôles de recherche et des liens de saut).
- **Gestion des Widgets** :
    - Mise en place d'une API d'administration pour les widgets ([#4027](https://github.com/refugies-info/karfur/pull/4027)).
    - Ajout d'un système de webhooks pour la configuration et le contenu des widgets.
- **Sécurité & Infrastructure** :
    - Plusieurs campagnes de nettoyage de vulnérabilités (security sweeps) sur les dépendances.
    - Mise à jour de l'environnement Node.js pour les correctifs de sécurité.
    - Automatisation du versioning lors des déploiements en production.
    - Ajout de notifications Slack lors de la publication de nouvelles versions.

### Autres changements
- **Nettoyage** : Suppression de fonctionnalités obsolètes (anciens widgets) et de code mort.
- **Documentation** : Mise à jour du README concernant l'importance du versioning.
