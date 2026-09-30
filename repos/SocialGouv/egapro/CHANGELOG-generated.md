## Changelog : egapro (30 derniers jours, au 29 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la mise en conformité de l'accessibilité (RGAA), la fiabilisation du parcours de déclaration (rémunération et avis CSE) et l'enrichissement des outils de suivi. L'ouverture de l'observatoire public et l'amélioration de la gestion des données d'export (API SUIT) constituent les évolutions majeures de cette période.

### Évolutions fonctionnelles
- **Accessibilité (RGAA)** : Améliorations massives pour l'utilisation au clavier, la lecture par synthèse vocale des graphiques et tableaux, la gestion du zoom et la navigation structurée [#4616](https://github.com/SocialGouv/egapro/issues/4616).
- **Parcours de déclaration** : 
    - Optimisation de la déclaration de rémunération (gestion des saisies non numériques, clarification des libellés et suppression des dates bloquantes) [#4656](https://github.com/SocialGouv/egapro/issues/4656).
    - Fiabilisation du processus de consultation et de dépôt des avis CSE [#4437](https://github.com/SocialGouv/egapro/issues/4437).
    - Correction de bugs bloquant la soumission des dossiers [#4541](https://github.com/SocialGouv/egapro/issues/4541).
- **Espace Entreprise (Mon Espace)** : Mise à jour des informations de l'entreprise, gestion des entreprises étrangères (bandeau pays) et ajout de badges de suivi de statut (Clôturée/Incomplète) [#4442](https://github.com/SocialGouv/egapro/issues/4442).
- **Export et Données** : 
    - Amélioration de l'API SUIT avec l'exposition des effectifs par quartile et l'alignement des écarts G [#4536](https://github.com/SocialGouv/egapro/issues/4536).
    - Affichage de la taille des fichiers lors du téléchargement [#4499](https://github.com/SocialGouv/egapro/issues/4499).
- **Nouvelles fonctionnalités** : 
    - Lancement de l'observatoire public [#4360](https://github.com/SocialGouv/egapro/issues/4360).
    - Ajout de filtres par tranche d'effectif dans le tableau des déclarations pour les administrateurs [#4498](https://github.com/SocialGouv/egapro/issues/4498).
    - Mise en place d'un journal d'activité utilisateur anonymisé pour l'audit [#4526](https://github.com/SocialGouv/egapro/issues/4526).

### Évolutions techniques
- **Architecture & API** : 
    - Refactorisation des routes statiques et des schémas tRPC pour une meilleure typage et modularité.
    - Centralisation des contrôles de verrouillage (lock) et de la gestion des sessions.
- **Infrastructure & CI/CD** : 
    - Optimisation des tests E2E via l'utilisation de shards parallèles pour réduire le temps de validation [#4556](https://github.com/SocialGouv/egapro/issues/4556).
    - Amélioration de la gestion des images de stockage (MinIO) dans les environnements de test.
- **Sécurité** : Renforcement de la sécurité de l'espace administrateur par l'exigence de la double authentification [#4482](https://github.com/SocialGouv/egapro/issues/4482) et masquage des erreurs techniques dans les réponses API pour éviter les fuites d'informations.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique de l'API SUIT [#4527](https://github.com/SocialGouv/egapro/issues/4527).
- **Maintenance** : Uniformisation des scripts de projet en TypeScript et nettoyage de plusieurs composants et écrans obsolètes.
