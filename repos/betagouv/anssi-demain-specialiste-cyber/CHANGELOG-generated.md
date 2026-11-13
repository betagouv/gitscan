## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 12/11/2026)

### Résumé
Ce mois a été marqué par un développement majeur de l'expérience utilisateur, notamment avec l'arrivée de la nouvelle page "Les métiers". Cette section propose désormais un parcours interactif pour découvrir les professions de la cybersécurité via des onglets thématiques, des témoignages de professionnels et un test cyber. Parallèlement, la plateforme a bénéficié d'une modernisation technique importante pour stabiliser l'environnement de développement et l'infrastructure.

### Évolutions fonctionnelles
- **Nouvelle expérience "Les métiers"** :
    - Mise en place d'une page dédiée avec des onglets dynamiques : "Je me repère", "J'explore", "J'écoute les Pros" et "Je trace ma route".
    - Intégration de vignettes de professionnels et de contenus dynamiques pour enrichir la découverte.
    - Ajout d'un test cyber interactif.
- **Parcours de formation** : Création de la page "Se former et s'entraîner" pour guider les utilisateurs dans leur apprentissage.
- **Améliorations de l'interface et du contenu** :
    - Meilleure organisation des métiers : tri par numéro et affichage des numéros de famille pour faciliter la navigation.
    - Optimisation de l'affichage du mode sombre.
    - Mise à jour de l'identité visuelle (retrait du logo ANSSI et de la tagline) et corrections de plusieurs textes (wording) pour plus de clarté.
    - Mise à jour des couleurs pour certaines familles de métiers (ex: "Conception").

### Évolutions techniques
- **Modernisation de l'infrastructure et du tooling** :
    - Migration de la stack vers Node.js 26.
    - Introduction d'un shell Nix pour standardiser l'environnement de développement.
    - Optimisation de la CI/CD avec le passage sur Ubuntu 26.04 et mise à jour des GitHub Actions.
    - Amélioration de la configuration de déploiement sur CleverCloud.
- **Refonte de l'API et gestion des données** :
    - Connexion des données métiers (familles, fonctions, profils) avec Grist.
    - Création de nouveaux endpoints API pour les familles de métiers et les fonctions.
    - Sécurisation et simplification de l'API : passage d'identifiants techniques à des identifiants métiers et masquage des IDs internes.
    - Implémentation de la gestion et de la validation des résultats de tests dans le journal.
- **Qualité du code et architecture** :
    - Mutualisation des types autour des métiers et extraction de composants logiques (recherche d'entités, constructeurs).
    - Nettoyage massif des surcharges inutiles et des logs de debug.
    - Renforcement de la robustesse des tests unitaires.

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement.
- **Productivité** : Mise en place du tri automatique des imports.
