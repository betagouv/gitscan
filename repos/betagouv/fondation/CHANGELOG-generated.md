## Changelog : fondation (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur (navigation plus fluide, nouveaux tableaux de données) et la fiabilisation de la gestion des sessions et des documents. La sécurité de l'accès a été renforcée et les alertes ont été basculées vers Tchap pour une meilleure intégration avec les outils de l'État.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Accès aux sessions archivées pour les membres, avec détails sur le type et la date d'archivage ([#728](https://github.com/betagouv/fondation/issues/728)).
    - Recherche de magistrats par nom directement depuis la navigation ([#719](https://github.com/betagouv/fondation/issues/719)).
    - Mise en place d'un système de sondage de satisfaction global avec historique des réponses ([#686](https://github.com/betagouv/fondation/issues/686)).
    - Nouveaux outils pour le secrétariat : publication de la table des auditions ([#687](https://github.com/betagouv/fondation/issues/687)) et pré-remplissage des avis via les commentaires de session ([#662](https://github.com/betagouv/fondation/issues/662)).
    - Affichage de la composition des sessions via des badges visuels ([#697](https://github.com/betagouv/fondation/issues/697)).
- **Améliorations de l'interface et de l'expérience utilisateur (UX)** :
    - Unification des écrans de secrétariat et d'administration via l'utilisation de DataTables ([#726](https://github.com/betagouv/fondation/issues/726)).
    - Migration des alertes de Mattermost vers Tchap ([#689](https://github.com/betagouv/fondation/issues/689)).
    - Amélioration de la lisibilité des noms (affichage du nom de jeune fille et du prénom) ([#691](https://github.com/betagouv/fondation/issues/691)).
    - Optimisation de la barre de session et de l'en-tête lors du défilement ([#651](https://github.com/betagouv/fondation/issues/651)).
    - Clarification des libellés (ex: "Voir mon rapport" pour les rapports de rapporteur) ([#717](https://github.com/betagouv/fondation/issues/717)).
- **Corrections** :
    - Fiabilisation de la gestion des rapports officiels et de leur lien avec les ordres du jour ([#725](https://github.com/betagouv/fondation/issues/725), [#670](https://github.com/betagouv/fondation/issues/670), [#658](https://github.com/betagouv/fondation/issues/658)).
    - Amélioration du cycle de vie des documents (maintien en mode brouillon jusqu'à validation, suivi correct du statut du fichier) ([#657](https://github.com/betagouv/fondation/issues/657), [#696](https://github.com/betagouv/fondation/issues/696)).
    - Corrections diverses sur l'affichage des informations (restitution des temps, commentaires, et gestion des doublons de recherche) ([#711](https://github.com/betagouv/fondation/issues/711), [#710](https://github.com/betagouv/fondation/issues/710), [#694](https://github.com/betagouv/fondation/issues/694)).

### Évolutions techniques
- **Sécurité** : Renforcement de la robustesse de la connexion par mot de passe contre les tentatives de devinettes et les caractères spéciaux ([#732](https://github.com/betagouv/fondation/issues/732)).
- **Gestion des données et stockage** :
    - Optimisation du nettoyage des fichiers orphelins sur le stockage S3 ([#733](https://github.com/betagouv/fondation/issues/733), [#659](https://github.com/betagouv/fondation/issues/659)).
    - Amélioration de la gestion des métadonnées et de l'encodage des noms de fichiers ([#712](https://github.com/betagouv/fondation/issues/712)).
    - Correction des erreurs de lecture lorsque des fichiers sont manquants dans le stockage ([#729](https://github.com/betagouv/fondation/issues/729)).
    - Rattrapage (backfill) de la taille des pièces jointes pour les fichiers anciens ([#731](https://github.com/betagouv/fondation/issues/731)).
- **Architecture et Refactoring** :
    - Refactorisation des modules pour favoriser l'utilisation de services et supprimer les cycles d'importation ([#692](https://github.com/betagouv/fondation/issues/692), [#695](https://github.com/betagouv/fondation/issues/695)).
    - Amélioration de la gestion des migrations de base de données ([#708](https://github.com/betagouv/fondation/issues/708), [#705](https://github.com/betagouv/fondation/issues/705)).
- **Infrastructure et CI/CD** :
    - Alignement des versions de PostgreSQL (local, CI et production) ([#727](https://github.com/betagouv/fondation/issues/727)).
    - Automatisation des notifications de déploiement et d'échec de release vers Tchap ([#709](https://github.com/betagouv/fondation/issues/709)).
    - Ajout d'un script de déploiement pour l'environnement de staging ([#701](https://github.com/betagouv/fondation/issues/701)).
    - Synchronisation des clients OpenAPI générés ([#730](https://github.com/betagouv/fondation/issues/730)).

### Autres changements
- Mise à jour de la documentation concernant l'importation des données LOLFI ([#684](https://github.com/betagouv/fondation/issues/684)).
