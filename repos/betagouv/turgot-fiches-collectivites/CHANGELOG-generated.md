## Changelog : turgot-fiches-collectivites (30 derniers jours, au 26 octobre 2026)

### Résumé
Le projet a connu une transformation majeure, marquée par un changement d'identité (passage de "Sully" à "Fico") et une refonte profonde de son architecture. L'accent a été mis sur la robustesse de la génération des fiches, l'élargissement des formats d'exportation (images, JSON, GeoJSON) et un alignement strict sur les standards de design de l'État (DSFR et Marianne).

### Évolutions fonctionnelles
- **Nouveaux formats d'exportation** : possibilité d'exporter les composants en formats PNG, SVG, JSON et GeoJSON.
- **Enrichissement des composants** :
    - Ajout des informations sur l'identité (maire/président).
    - Intégration de nouveaux graphiques (ex: financement par habitant).
    - Affichage de cartes spécifiques pour les EPCI.
    - Ajout d'un paramètre de date ("since") sur plusieurs composants.
- **Amélioration de l'affichage et de la donnée** :
    - Affichage des noms complets pour l'intercommunalité, le département et la région.
    - Filtrage des histogrammes (limités aux 5 dernières années et exclusion de l'année en cours).
    - Support de la recherche par code INSEE.
- **Nouvelle cible Web** : mise à disposition de Web Components permettant de consommer les données via JSON pour une intégration simplifiée.

### Évolutions techniques
- **Infrastructure et déploiement** : migration vers PostgreSQL et déploiement sur Dokku.
- **Refonte de l'architecture** :
    - Passage à un système de composants basé sur des décorateurs et des contrats de données typés.
    - Séparation claire entre le calcul des données (Python) et la mise en page (gabarits).
    - Optimisation des performances via la construction des fiches directement depuis la base de données (réduction des appels réseau).
- **Intégration et API** :
    - Connexion aux données de l'API Collectivités.
    - Amélioration de la gestion du CORS pour permettre l'intégration des composants sur des domaines tiers.
    - Refonte de l'API pour exposer des composants plus flexibles via des paramètres.
- **Design System** : alignement des composants et des rendus PDF sur le DSFR et les standards Marianne.

### Autres changements
- **Rebranding** : renommage global du projet de "Sully" vers "Fico".
- **Documentation** : simplification du fichier README.
- **Qualité du code** : nettoyage général, harmonisation de la nomenclature (anglais pour la technique, français pour le métier) et amélioration de la couverture de tests.
