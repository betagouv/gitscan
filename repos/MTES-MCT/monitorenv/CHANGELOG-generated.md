## Changelog : monitorenv (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois a été marqué par un enrichissement des outils d'administration et une amélioration notable de l'expérience utilisateur, tant sur les interfaces de gestion que sur la cartographie. Les performances de rendu spatial et la fiabilité des flux de données ont également été renforcées pour offrir une navigation plus fluide et des données plus précises.

### Évolutions fonctionnelles
- **Gestion du Backoffice** : Création d'une interface dédiée à la gestion des thèmes et déploiement d'une nouvelle version de l'outil de gestion des zones réglementaires.
- **Recherche et Filtrage** : 
    - Ajout de la recherche par code FAO et de nouveaux filtres (tri par date de modification, aide réglementaire).
    - Ajout d'une section pour les sous-thèmes dont la validité est expirée.
    - Amélioration de l'affichage des fréquences (affichage des jours de début et de fin pour les cycles hebdomadaires).
- **Améliorations de l'interface (UI/UX)** :
    - Optimisation de la navigation avec l'ajout d'un en-tête fixe (sticky header).
    - Amélioration de l'interactivité sur la carte (maintien de l'affichage des zones lors du dessin, suppression des effets de survol perturbants).
    - Corrections ergonomiques sur la gestion du focus et la clarté des composants de tags.
- **Données et API** : Enrichissement des sorties de l'API publique (inclusion des contacts des unités de contrôle) et ajout de paramètres de gestion pour les ressources (enregistrement et fréquence).

### Évolutions techniques
- **Optimisation Cartographique (SIG)** : Amélioration significative des performances de rendu des tuiles via l'utilisation de `ST_asMVT` et l'optimisation des requêtes de géométrie (système 3857).
- **Performances et Backend** :
    - Optimisation du temps de réponse en déportant certains tris complexes du backend (Kotlin) vers le frontend (TypeScript).
    - Mise en place de la virtualisation pour l'affichage des listes de codes FAO et gestion de l'invalidation du cache lors de la modification des utilisateurs.
- **Flux de données et Infrastructure** :
    - Mise à jour et fiabilisation des flux de données ouvertes (Open Data) avec l'ajout de logs de suivi.
    - Ajustements de l'environnement Docker (ajout de `curl`) et modification des ports de santé (healthcheck).
- **Sécurité et Authentification** : Renforcement de la gestion des accès (rejet des utilisateurs inconnus et redirection automatique vers l'inscription).

### Autres changements
- **Accessibilité** : Ajustement des contrastes de couleurs pour améliorer la lisibilité.
- **Base de données** : Mise à jour des fichiers de migration.
