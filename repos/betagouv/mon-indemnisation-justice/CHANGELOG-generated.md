## Changelog : mon-indemnisation-justice (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la refonte de l'application, notamment la migration vers Symfony 8 et Doctrine, ainsi que sur l'amélioration de l'expérience utilisateur avec la création d'un nouveau formulaire de dépôt de dossier plus intuitif et la gestion des brouillons. De nombreuses corrections de bugs et améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un système de brouillons pour les dossiers, permettant aux utilisateurs de sauvegarder leurs informations et de les compléter ultérieurement.
- Amélioration de l'affichage des pièces jointes et ajout d'une prévisualisation lors de l'ajout de fichiers.
- Ajout de la possibilité de saisir le SIRET de l'administration pour les agents.
- Intégration de nouveaux types d'attestations, incluant l'"Avis d'intervention".
- Amélioration de la gestion des erreurs et affichage de messages plus clairs aux utilisateurs.
- Correction de l'affichage de l'explication de la clôture sur la page "mes demandes".
- Amélioration de l'affichage du badge "Déclaration FDO".
- Ajout d'un message d'erreur plus clair en cas d'échec de l'inscription ou de la connexion via France Connect.
- Ajout d'un autocomplete sur le champ adresse.
- Mise à jour du courriel d'invitation à déposer sur décla FDO.
- Ajout de la possibilité de modifier les informations du dossier.

### Évolutions techniques
- Migration vers Symfony 8 et Doctrine pour bénéficier des dernières améliorations et corrections de sécurité.
- Refonte de l'architecture de l'application avec l'utilisation de Tanstack Router.
- Suppression de l'utilisation d'API Platform.
- Amélioration de la gestion des entités et des DTOs pour l'échange de données avec l'espace FIP6.
- Intégration de Sentry pour la surveillance des erreurs et la collecte d'informations de diagnostic.
- Mise à jour de l'image Docker pour retirer `APP_RUNTIME`.
- Correction de plusieurs erreurs et optimisations de performance liées à Doctrine.
- Normalisation des adresses en base de données et en entrée.
- Simplification de la gestion des erreurs.
- Suppression des classes de mapper.
- Utilisation du DossierManager pour la sauvegarde des données.

### Autres changements
- Documentation du schéma de base de données.
- Mise à jour des documents PN.
- Installation de Crisp pour le support client.
- Création d'un compte France Connect de bac à sable pour l'environnement de développement.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de tests unitaires et end-to-end pour garantir la qualité du code.
- Correction de plusieurs tests unitaires backend.
- Suppression de code obsolète.
- Amélioration de la gestion des permissions.
- Ajout de la transmission du contexte utilisateur à Sentry.
- Remontée de la mention "Référence à rappeler" dans l'email de confirmation de dépôt.
