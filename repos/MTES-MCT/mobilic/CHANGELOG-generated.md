## Changelog : mobilic (30 derniers jours, au 7 octobre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la fiabilité de l'interface d'administration et la précision du suivi réglementaire (seuils de repos). L'expérience utilisateur sur mobile (PWA) a été renforcée par un système d'alertes plus clair, et l'accessibilité du projet a été améliorée avec l'ajout de nouvelles pages d'information.

### Évolutions fonctionnelles
- **Accessibilité et information** : Ajout d'une page "Schéma pluriannuel" pour améliorer la transparence et l'accessibilité des données. [#955](https://github.com/MTES-MCT/mobilic/pull/955)
- **Système d'alertes (PWA)** : Amélioration de l'affichage des alertes pour les utilisateurs (bannières cumulables, fermables et mieux ancrées dans la page). [#961](https://github.com/MTES-MCT/mobilic/pull/961), [#964](https://github.com/MTES-MCT/mobilic/pull/964)
- **Conformité réglementaire** : Optimisation de la gestion des seuils de repos hebdomadaires et alignement des indicateurs sur les minima légaux. [#965](https://github.com/MTES-MCT/mobilic/pull/965), [#958](https://github.com/MTES-MCT/mobilic/pull/958)
- **Gestion administrative** : 
    - Amélioration du filtrage des employés (exclusion des utilisateurs n'ayant jamais utilisé la plateforme).
    - Meilleure visibilité des statuts de mission et des missions en cours.
    - Possibilité d'ajouter un type de déplacement lors de la saisie d'activités. [#941](https://github.com/MTES-MCT/mobilic/pull/941)
- **Formulaires** : Amélioration des formulaires de contrôle avec l'inclusion automatique du type de transport. [#928](https://github.com/MTES-MCT/mobilic/pull/928)

### Évolutions techniques
- **Optimisation des performances** : 
    - Amélioration de la fluidité de l'administration via une meilleure pagination et la réduction des appels API redondants. [#917](https://github.com/MTES-MCT/mobilic/pull/917), [#988](https://github.com/MTES-MCT/mobilic/pull/988), [#935](https://github.com/MTES-MCT/mobilic/pull/935)
    - Augmentation de la taille des pages de données (de 10 à 50 entrées) pour un affichage plus efficace.
- **Infrastructure et CI/CD** : 
    - Mise à jour de la configuration CircleCI vers la version 2.1. [#975](https://github.com/MTES-MCT/mobilic/pull/975)
    - Suppression des anciens processus de déploiement Scalingo. [#976](https://github.com/MTES-MCT/mobilic/pull/976)
- **Observabilité** : Mise en place du suivi du temps de chargement (login vers tableau de bord) via Sentry pour identifier les lenteurs. [#967](https://github.com/MTES-MCT/mobilic/pull/967)
- **Stabilité** : Restauration de fonctionnalités critiques (gestion des tokens API, mise en page PWA et calcul des statuts) suite à une erreur de fusion.
- **Résilience** : Amélioration de la robustesse des processus d'export de données. [#972](https://github.com/MTES-MCT/mobilic/pull/972)

### Autres changements
- **Nettoyage** : Suppression de code mort, de labels inutilisés et de guards de sécurité obsolètes.
- **Interface (UI)** : Ajustements cosmétiques sur les espacements, les polices de caractères et les indicateurs de navigation.
