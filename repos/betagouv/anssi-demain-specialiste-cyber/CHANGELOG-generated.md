## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 12 novembre 2026)

### Résumé
Cette période a été marquée par un enrichissement majeur de l'expérience utilisateur, notamment avec le déploiement de la nouvelle section "Les métiers" et de l'espace "Se former et s'entraîner". La plateforme propose désormais des parcours plus interactifs et des contenus dynamiques pour aider les utilisateurs à explorer les métiers de la cybersécurité. En parallèle, une refonte importante de l'infrastructure technique a été réalisée pour moderniser l'environnement de développement et de déploiement.

### Évolutions fonctionnelles
- **Nouvelle section "Les métiers"** : Mise en place d'une page dédiée incluant des onglets interactifs ("Je me repère", "J'explore", "J'écoute les Pros", "Je trace ma route") et l'intégration d'un test cyber.
- **Parcours de formation** : Création de la page "Se former et s'entraîner en ligne" avec des outils de mesure de niveau et d'entraînement.
- **Exploration des métiers** : 
    - Amélioration de la navigation avec des fiches détaillées par famille de métiers.
    - Ajout de vignettes de témoignages de professionnels.
    - Meilleure organisation des familles de métiers (tri par numéro et affichage des numéros).
- **Améliorations de l'interface (UI/UX)** :
    - Mise à jour de la charte graphique (couleurs des familles, gestion du mode sombre).
    - Corrections de textes (wording) pour plus de clarté et de cohérence.
    - Épuration de l'en-tête (retrait du logo ANSSI et de la tagline "Innovation ANSSI").

### Évolutions techniques
- **Modernisation de l'infrastructure** :
    - Migration de la stack vers Node.js 26.
    - Introduction d'un environnement de développement via Nix (shell Nix) pour une meilleure reproductibilité.
    - Mise à jour de la chaîne CI/CD (passage sur Ubuntu 26.04 et actualisation des GitHub Actions).
- **Refonte de l'API et de la gestion des données** :
    - Optimisation de l'API "Métiers" : passage de l'utilisation d'identifiants techniques à des identifiants métier, et création de nouveaux endpoints pour les familles et les fonctions.
    - Intégration de Grist pour la récupération dynamique des données (métiers, familles, fonctions).
    - Refactorisation du code pour mutualiser les types et améliorer la structure des ressources.
- **Qualité et tests** :
    - Amélioration du système de suivi des tests (enregistrement des résultats et consignation dans les journaux).
    - Mise à jour massive des dépendances de développement et de production.
    - Automatisation du tri des imports.

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement.
- **Maintenance** : Nettoyage des logs de debug d'authentification et centralisation des instructions pour les agents d'IA.
