## Changelog : drive-migrator (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, à l'expérience utilisateur et à la robustesse de l'outil. Les utilisateurs peuvent désormais télécharger des archives de migration de manière sécurisée, bénéficier d'une interface utilisateur améliorée et profiter de corrections de bugs pour une meilleure stabilité. Des fonctionnalités de gestion des comptes et de partage de fichiers ont également été ajoutées.

### Évolutions fonctionnelles
- Ajout d'une page de téléchargement sécurisée pour les archives de migration. [#145](https://github.com/suitenumerique/drive-migrator/issues/145)
- Implémentation d'un mode restreint avec validation administrative pour les nouveaux comptes utilisateurs.
- Affichage du nombre maximal de fichiers pouvant être migrés et de l'état de la migration partielle.
- Pré-remplissage et verrouillage du champ email Resana avec le compte Proconnect.
- Ajout d'une page "compte en attente" pour les comptes en mode restreint.
- Possibilité de limiter le nombre de fichiers migrés par espace de travail via un paramètre de configuration.
- Intégration de la liste des utilisateurs partagés dans l'export Drive.
- Prise en charge de l'authentification multifacteur (MFA) avec un code OTP pour la connexion à Resana via Keycloak.
- Ajout d'un attribut "label" aux backends source.
- Envoi d'un email de confirmation à la fin de l'export.
- Amélioration de l'interface utilisateur du tableau de bord et de la modale de partage.
- Ajout d'un favicon.

### Évolutions techniques
- Utilisation de runners GitHub-hosted pour l'exécution des workflows CI.
- Mise à jour de pytest en version 9 (correction de sécurité).
- Mise à jour de lodash et next dans le frontend.
- Mise à jour de la version de Python (3.14.6).
- Refactoring du code pour améliorer la clarté et la maintenabilité (renommage de variables, simplification de la logique).
- Application du formatteur de code Ruff aux backends source et drive.
- Correction de problèmes liés aux variables d'environnement dans les jobs CI.
- Suppression de clés obsolètes.
- Ajout de tests unitaires et corrections de bugs associés.
- Amélioration de la gestion des erreurs et des exceptions.
- Utilisation de `FRONTEND_THEME=dsfr` dans le build Docker du frontend.
- Ajout d'un script pour générer des données de démonstration pour le backend source filesystem.
- Ajout d'un target `frontend-lint` pour le linting du frontend.

### Autres changements
- Mise à jour de la documentation README avec la section "Getting Started".
- Ajout de tests de sécurité avec Zizmor.
- Correction de l'échappement des entités HTML dans les noms Resana.
- Correction d'un bug lié à l'actualisation du token d'accès Resana.
- Correction d'un problème avec l'hostname de l'endpoint OIDC pour une configuration Keycloak en mode standalone.
- Correction d'un bug dans le statut du job Resana.
- Correction de problèmes de style CSS bloquant le défilement de la page.
- Suppression de Crisp et retour à l'interface utilisateur précédente.
- Ajout d'un paramètre de configuration `DRIVE_SHARE_MEMBERS` pour contrôler le partage des membres dans Drive.
- Mise à jour des dépendances GitHub Actions.
- Ajout de commentaires et de documentation pour améliorer la compréhension du code.
