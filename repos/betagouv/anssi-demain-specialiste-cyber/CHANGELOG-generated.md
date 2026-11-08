## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 06/11/2026)

### Résumé
Cette période a été marquée par un enrichissement majeur de l'offre de découverte des métiers. La plateforme propose désormais une page dédiée aux métiers avec des parcours interactifs (exploration, témoignages de pros, suivi de parcours) et une meilleure intégration des données professionnelles. L'expérience utilisateur a également été affinée via des corrections de contenu et des améliorations visuelles.

### Évolutions fonctionnelles
- **Découverte des métiers** : Mise en ligne de la page "Les métiers" incluant des onglets interactifs ("J'explore", "J'écoute les Pros", "Je trace ma route") et des fiches détaillées par famille de métiers.
- **Contenu professionnel** : Ajout de vignettes de professionnels et de témoignages pour enrichir l'exploration des métiers.
- **Parcours de formation** : Implémentation de la page "Se former et s'entraîner" et ajout d'un test cyber sur la page d'accueil.
- **Expérience utilisateur (UX/UI)** : 
    - Amélioration de l'application du mode sombre.
    - Corrections de textes (wording) pour plus de clarté.
    - Ajustements de l'identité visuelle (retrait de certains éléments de branding ANSSI).

### Évolutions techniques
- **Architecture & API** : 
    - Création de nouveaux endpoints pour la gestion des familles de métiers et des fonctions.
    - Développement d'APIs dédiées aux parcours de sélection ("Je me mesure" et "Je m'entraîne").
    - Intégration de Grist comme source de données pour les métiers, fonctions et profils.
- **Infrastructure & CI/CD** : 
    - Migration de la stack vers Node.js 26 et Ubuntu 26.04.
    - Ajout du support Nix pour l'environnement de développement (shell Nix).
    - Mise à jour de la chaîne de tests avec le support de Vitest 5.
- **Qualité & Tooling** : 
    - Passage en ESM pour la configuration Vitest backend.
    - Automatisation du tri des imports.
    - Centralisation des instructions pour les agents d'IA.
    - Amélioration de la gestion des erreurs et de la persistance des résultats de tests.

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement.
- **Nettoyage** : Suppression des logs de debug d'authentification et optimisation du formatage du code.
