## Changelog : gestion-des-subventions-locales (30 derniers jours, au 2026-06-16)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et la performance de l'application, notamment au niveau de la synchronisation avec les sources de données (DS), de la gestion des documents et de l'expérience utilisateur. Des optimisations ont été apportées pour gérer les erreurs et améliorer la réactivité de l'interface, ainsi que des corrections de bugs et des refactorings pour une meilleure maintenabilité du code.

### Évolutions fonctionnelles
- Possibilité de masquer la colonne d'actions dans le tableau des enveloppes sur les pages de programmation et de simulation. [#752](https://github.com/betagouv/gestion-des-subventions-locales/issues/752)
- Ajout d'une entrée de menu dédiée pour les modèles de publipostage. [#750](https://github.com/betagouv/gestion-des-subventions-locales/issues/750)
- Importation des dossiers depuis tous les territoires gérés. [#749](https://github.com/betagouv/gestion-des-subventions-locales/issues/749)
- Affichage du périmètre, des dates Turgot et du statut du report dans l'interface d'administration. [#748](https://github.com/betagouv/gestion-des-subventions-locales/issues/748)
- Possibilité de changer le statut de plusieurs projets en "refusé" ou "classé sans suite" en lot. [#726](https://github.com/betagouv/gestion-des-subventions-locales/issues/726)
- Recherche de dossiers par sous-chaîne du numéro de dossier. [#728](https://github.com/betagouv/gestion-des-subventions-locales/issues/728)
- Découplage de la notification de refus/classement du changement de statut. [#719](https://github.com/betagouv/gestion-des-subventions-locales/issues/719)
- Possibilité de rendre le QR code de suivi optionnel sur les documents générés. [#720](https://github.com/betagouv/gestion-des-subventions-locales/issues/720)
- Gestion des tableaux dans l'éditeur TipTap. [#733](https://github.com/betagouv/gestion-des-subventions-locales/issues/733)

### Évolutions techniques
- Amélioration de la performance en activant la compression WhiteNoise (gzip + Brotli) des fichiers statiques. [#757](https://github.com/betagouv/gestion-des-subventions-locales/issues/757)
- Priorisation des tâches Celery en fonction du contexte d'appel. [#751](https://github.com/betagouv/gestion-des-subventions-locales/issues/751)
- Refactorisation de plusieurs composants pour utiliser des Class-Based Views (CBV) au lieu de Function-Based Views (FBV), améliorant ainsi la structure du code et sa maintenabilité. (Plusieurs commits)
- Refactorisation de la gestion des événements DS pour les enregistrer dans l'historique des projets. [#755](https://github.com/betagouv/gestion-des-subventions-locales/issues/755)
- Ajout d'un mécanisme de verrouillage avec Redis pour éviter les synchronisations concurrentes des dossiers DS. [#740](https://github.com/betagouv/gestion-des-subventions-locales/issues/740)
- Amélioration de la gestion des erreurs lors de la sauvegarde des curseurs de synchronisation DS. [#724](https://github.com/betagouv/gestion-des-subventions-locales/issues/724)
- Refactorisation du code GraphQL pour une meilleure organisation. [#721](https://github.com/betagouv/gestion-des-subventions-locales/issues/721)
- Ajout de logs structurés et d'un identifiant de requête sur le proxy DS. [#731](https://github.com/betagouv/gestion-des-subventions-locales/issues/731)
- Augmentation du timeout Gunicorn pour la génération de documents. [#763](https://github.com/betagouv/gestion-des-subventions-locales/issues/763)

### Autres changements
- Documentation : ajout d'un fichier `AGENTS.md` pour guider les agents. [#722](https://github.com/betagouv/gestion-des-subventions-locales/issues/722)
- Documentation : ajout d'informations sur l'utilisation des branches hotfix pour le déploiement par tag.
- Corrections de tests et de bugs mineurs.
- Amélioration de la gestion des erreurs et des validations.
- Nettoyage et refactoring du code.
