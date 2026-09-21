## Changelog : monitorenv (30 derniers jours, au 16 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la gestion des zones réglementaires et des tags (notamment les codes FAO) via le backoffice. L'interface utilisateur a été affinée pour offrir une navigation plus fluide et une meilleure accessibilité, tandis que les processus d'importation de données et de gestion des utilisateurs ont été renforcés pour faciliter le travail des agents.

### Évolutions fonctionnelles
- **Gestion des zones et tags** : 
    - Déploiement de la version 1 du backoffice pour la gestion des zones réglementaires.
    - Ajout de la recherche et de la gestion des codes FAO dans le backoffice.
    - Amélioration de l'affichage des périodes de vigilance et des fréquences de répétition.
- **Expérience utilisateur (UI/UX)** :
    - Optimisation de l'interaction avec la carte (maintien de l'affichage des zones lors du tracé et suppression des effets de survol perturbateurs).
    - Amélioration de l'ergonomie globale : ajout d'un en-tête fixe (sticky header) et correction de l'affichage des tableaux de bord.
    - Mise en conformité de l'accessibilité (ajustement des contrastes de couleurs).
- **Administration et Missions** :
    - Nouvelle fonctionnalité d'importation d'utilisateurs via un fichier CSV (format Cerbere).
    - Inclusion des contacts des unités de contrôle dans les sorties de l'API publique des missions.
    - Ajout de nouveaux champs pour les unités de ressources (ID d'enregistrement et fréquence radio).

### Évolutions techniques
- **Flux de données** : Mise à jour et fiabilisation des flux de données provenant d'Open Data et de data.gouv (notamment pour les zones réglementaires).
- **Performances** : Implémentation de la virtualisation pour le composant de recherche des codes FAO afin d'optimiser l'affichage.
- **Backend & API** : 
    - Création de nouveaux points de terminaison (endpoints) pour la mise à jour des unités de ressources et l'import d'utilisateurs.
    - Corrections sur les flux de données en temps réel (SSE) et sur les filtres de requêtes de groupe.
- **Infrastructure** : 
    - Mise à jour de la syntaxe Prefect.
    - Intégration de la clé API Carto.
    - Ajout de logs pour le suivi des flux de données ouvertes.

### Autres changements
- **Maintenance** : Nettoyage du code (suppression de paramètres de log et de messages d'alerte obsolètes) et mise à jour des fichiers de migration de la base de données.
