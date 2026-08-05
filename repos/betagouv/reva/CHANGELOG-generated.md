## Changelog : reva (30 derniers jours, au 04/08/2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes majeures avec le déploiement du parcours de faisabilité dématérialisée autonome et une refonte de la gestion des organismes certificateurs. Ces évolutions permettent un parcours candidat plus fluide et une gestion administrative plus précise, tout en renforçant la sécurité des accès via un nouveau moteur de permissions.

### Évolutions fonctionnelles
- **Dématérialisation de la faisabilité :** Mise en place du parcours "autonome" avec de nouvelles étapes dédiées (prérequis, blocs de compétences, certification, déclaration sur l'honneur et pièces jointes).
- **Gestion des organismes certificateurs :** 
    - Possibilité de sélectionner plusieurs organismes certificateurs.
    - Ajout de pages d'avertissement et de détails sur les contacts des organismes.
    - Amélioration de l'affichage des informations de contact sur le tableau de bord candidat.
- **Expérience utilisateur (UX) :**
    - Amélioration des filtres de recherche pour les administrateurs (notamment pour les AAP).
    - Optimisation des formulaires de saisie (adresse, code postal, département) pour garantir la complétude des données.
    - Amélioration de la recherche d'organismes (débit de recherche optimisé).
- **Collectifs VAE :** Introduction de nouveaux rôles et de permissions plus fines pour les porteurs de projet.

### Évolutions techniques
- **Sécurité et Autorisation :**
    - Migration massive de l'API vers un nouveau moteur d'autorisation (`withPolicies`) pour sécuriser les accès aux ressources (candidatures, rendez-vous, référentiels, etc.).
    - Implémentation d'un mapping précis entre les rôles Keycloak et les permissions spécifiques des collectifs VAE.
- **Automatisation des données :** Mise en place d'un mécanisme de synchronisation automatique des organismes certificateurs en fonction du département du candidat ou des changements de cartographie.
- **Qualité logicielle :**
    - Augmentation significative de la couverture de tests (tests unitaires et d'intégration sur l'API, l'administration, le parcours candidat et l'interopérabilité).
    - Centralisation et traduction en français des messages d'erreur de l'API.
- **Architecture :** Utilisation de "feature flags" pour le pilotage du déploiement des nouvelles fonctionnalités (notamment pour la faisabilité dématérialisée).

### Autres changements
- **Nettoyage :** Suppression de tables de base de données, de types et de code obsolètes (notamment sur les événements d'audit et certains types de candidatures).
- **Maintenance :** Optimisation des scripts de rappel de paiement et de gestion des comptes locaux.
