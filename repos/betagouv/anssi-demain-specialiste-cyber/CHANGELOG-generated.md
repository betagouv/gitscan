## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 2026-11-10)

### Résumé
La plateforme s'enrichit de nouveaux contenus et parcours pour mieux guider les utilisateurs dans la découverte des métiers de la cybersécurité. L'ajout de la page "Les métiers" avec ses onglets interactifs, l'intégration de témoignages de professionnels et la mise en place d'un test cyber permettent une exploration plus immersive et personnalisée.

### Évolutions fonctionnelles
- **Nouvelle expérience "Les métiers"** : déploiement d'une page dédiée incluant des onglets interactifs pour explorer les parcours ("Je me repère", "J'explore", "J'écoute les Pros", "Je trace ma route").
- **Parcours de formation** : création de la section "Se former et s'entraîner en ligne".
- **Interactivité et tests** : ajout d'un test cyber avec possibilité d'enregistrer ses résultats.
- **Amélioration de la navigation métier** : 
    - Affichage et tri des familles de métiers par numéro.
    - Mise à jour visuelle (couleurs) des familles de métiers.
    - Intégration de vignettes présentant des témoignages de professionnels.
- **Ajustements de l'interface (UI)** : 
    - Amélioration de l'application du mode sombre.
    - Simplification de l'en-tête (retrait du logo et de la tagline ANSSI).
    - Corrections de textes (wording) pour une meilleure clarté.

### Évolutions techniques
- **Infrastructure et environnement** : 
    - Migration de la stack vers Node.js 26.
    - Mise à jour de l'environnement de CI vers Ubuntu 26.04.
    - Introduction du shell Nix pour le projet.
- **Développement de l'API** : 
    - Création de nouveaux endpoints pour les familles de métiers, les fonctions et les sélections de formation ("Je me mesure", "Je m'entraîne").
    - Refonte de l'exposition des données : masquage des identifiants techniques internes et utilisation d'identifiants métiers pour plus de sécurité.
    - Synchronisation des données (familles, fonctions, profils, ressources) via Grist.
- **Qualité et Toolchain** : 
    - Support de Vitest 5 pour les tests.
    - Automatisation du tri des imports.
    - Optimisation de la gestion des types et refactoring du constructeur de métier.
    - Ajustement des règles de linting (acceptation de lignes jusqu'à 120 caractères).

### Autres changements
- Réorganisation du guide de développement pour une meilleure accessibilité.
