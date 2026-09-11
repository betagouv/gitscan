## Changelog : monitorenv (30 derniers jours, au 10 septembre 2026)

### Résumé
Cette période a été marquée par un renforcement des capacités d'administration, notamment avec la gestion des zones réglementaires et l'import d'utilisateurs, ainsi que par une amélioration de l'ergonomie de l'interface et de l'interactivité de la cartographie.

### Évolutions fonctionnelles
- **Administration & Backoffice** : 
    - Mise en place de la première version de la gestion des zones réglementaires.
    - Ajout du code FAO dans les tags du backoffice.
    - Création d'une fonctionnalité d'import d'utilisateurs via des fichiers CSV (format Cerbere).
- **Interface Utilisateur (UI/UX)** :
    - Amélioration de l'ergonomie avec l'ajout d'un en-tête fixe (sticky header).
    - Optimisation de l'interaction avec la carte : maintien de l'affichage des zones pendant le tracé et suppression des effets de survol perturbateurs.
    - Affichage plus précis des jours de début et de fin pour les fréquences hebdomadaires.
- **Corrections** :
    - Rectification du tri de la colonne de mise à jour sur le tableau de bord.
    - Correction de l'affichage des contacts des unités de contrôle dans l'API publique des missions.
    - Suppression de messages d'avertissement inutiles dans l'interface.

### Évolutions techniques
- **API & Flux de données** :
    - Ajout d'un endpoint de mise à jour (patch) pour les unités de ressources (incluant l'ID d'enregistrement et la radiofréquence).
    - Mise à jour du flux de données provenant de data.gouv pour les zones réglementaires.
    - Amélioration du traitement des données JSON pour les références réglementaires.
- **Performance & Architecture** :
    - Virtualisation de l'affichage du code FAO pour optimiser les performances.
    - Refactorisation des classes de données et de la structure des packages.
    - Mise à jour de la syntaxe des pipelines de données (migration Prefect).
- **Observabilité & Infrastructure** :
    - Renforcement du logging sur les flux de données ouvertes (open data).
    - Ajout de la clé API Carto pour les services cartographiques.

### Autres changements
- **Accessibilité** : Ajustement de la palette de couleurs pour améliorer l'accessibilité (A11Y).
- **Maintenance** : Nettoyage du code et mise à jour des fichiers de migration de base de données.
