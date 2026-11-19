## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 18 novembre 2026)

### Résumé
La plateforme a franchi une étape majeure avec le déploiement de nouvelles sections dédiées à l'exploration des métiers et à la formation. Les utilisateurs disposent désormais de parcours interactifs pour découvrir les métiers de la cybersécurité, écouter des témoignages de professionnels et tester leurs compétences. L'infrastructure a également été modernisée pour supporter ces nouvelles fonctionnalités.

### Évolutions fonctionnelles
- **Nouvelle expérience "Les métiers"** : Mise en place d'une page dédiée avec des onglets interactifs permettant de s'orienter ("Je me repère"), d'explorer les contenus, d'écouter des professionnels ("J'écoute les Pros") et de définir un parcours ("Je trace ma route").
- **Parcours de formation** : Création de la page "Se former et s'entraîner" pour accompagner l'apprentissage.
- **Exploration enrichie** : 
    - Affichage de fiches détaillées pour les familles de métiers.
    - Intégration de vignettes de professionnels pour humaniser les parcours.
    - Amélioration de la navigation grâce au tri et à l'affichage des numéros de familles de métiers.
- **Tests de niveau** : Intégration d'un test cyber et possibilité pour l'utilisateur d'enregistrer ses résultats.
- **Optimisations de l'interface (UI/UX)** : 
    - Amélioration du mode sombre.
    - Corrections de textes (wording) pour plus de clarté.
    - Mise à jour de l'en-tête (retrait des anciens logos et taglines).

### Évolutions techniques
- **Migration d'infrastructure** : Passage de la stack vers Node.js 26 et optimisation de la chaîne de déploiement (Nix, pnpm, CleverCloud).
- **Refonte de la gestion des données métiers** :
    - Intégration de Grist comme source de données pour les métiers, les fonctions et les familles.
    - Sécurisation de l'API en remplaçant l'exposition des identifiants techniques internes par des identifiants métiers.
    - Création de nouveaux points d'accès (endpoints) pour les familles de métiers et les fonctions associées.
- **Amélioration de la robustesse** : 
    - Renforcement de la validation des résultats de tests.
    - Optimisation du typage et de la gestion des ressources métier.

### Autres changements
- Mise à jour de l'UI Kit vers la version 1.64.0.
