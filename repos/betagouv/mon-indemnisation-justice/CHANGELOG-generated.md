## Changelog : mon-indemnisation-justice (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte de l'application, notamment la migration vers Symfony 8 et Doctrine, l'amélioration de l'expérience utilisateur avec l'introduction d'étapes de saisie plus claires et l'ajout de fonctionnalités pour la gestion des agents et des dossiers. Des corrections de bugs et des améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'affichage des pièces jointes et ajout d'une modale de prévisualisation.
- Ajout de la possibilité de télécharger des pièces jointes pendant la phase d'instruction du dossier.
- Amélioration de l'affichage de l'explication de la clôture d'un dossier sur la page "mes demandes".
- Ajout de la mention "Référence à rappeler" dans l'email de confirmation de dépôt.
- Inclusion du type "Avis d'intervention" dans la liste des types d'attestation.
- Correction de l'affichage du badge "Declaration FDO".
- Amélioration de la gestion des erreurs lors de l'inscription/connexion via France Connect, avec envoi d'informations à Sentry.
- Ajout de la gestion des permissions pour les points d'entrée API requérant.
- Correction de l'affichage des informations sur les personnes morales dans la vue dossier.
- Ajout d'un endpoint `/me` pour récupérer les informations du requérant.
- Amélioration de l'autocomplétion de l'adresse.
- Création d'une page d'erreur 404.
- Implémentation d'un système de brouillons pour les dossiers en cours de saisie.
- Création des entités `Personne` et `Brouillon`.
- Création des étapes de saisie du dossier (en cours de développement).

### Évolutions techniques
- Mise à jour de Symfony et Doctrine vers les versions 8.x.
- Refonte de la gestion des erreurs et simplification du code.
- Suppression de l'utilisation d'API Platform.
- Utilisation du router Tanstack pour l'espace requérant.
- Amélioration de la gestion des données et des entités.
- Suppression des classes de mapper.
- Normalisation des données d'adresses en minuscules.
- Transmission du contexte utilisateur à Sentry pour un meilleur suivi des erreurs.
- Mise à jour de l'image Docker pour supprimer `APP_RUNTIME`.
- Correction de bugs liés à Doctrine et aux tests unitaires backend.
- Correction d'une configuration obsolète pour Doctrine en production.
- Ajout de tests unitaires et end-to-end.
- Refactorisation de la route API de liste des communes par code postal.
- Ajout de DTOs pour l'échange de données de dossier avec l'espace FIP6.

### Autres changements
- Mise à jour de la documentation des PN (Points de Non-conformité).
- Installation de Crisp pour le support client.
- Documentation du schéma de base de données.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de données de test pour les agents et les administrations.
- Correction de liens morts et d'erreurs d'affichage.
- Suppression d'API Platform.
- Ajout de la gestion des bris de porte dans une table dédiée.
- Correction de la liaison déclaration <-> dossier et de la déconnexion utilisateur.
- Validation de la présence de tous les types de pièces jointes.
- Correction de la perte d'informations lors du changement d'étape.
- Ajout de la gestion des permissions pour les agents.
- Correction de l'inscription France Connect.
- Suppression des entités `bris_porte` et renommage de `requerants` en `usagers`.
- Correction de la normalisation des données côté FDO.
- Ajout de commentaires et d'explications dans le code.
- Correction de bugs remontés par Sentry (MON-INDEMNISATION-JUSTICE-9Q, MON-INDEMNISATION-JUSTICE-9P).
- Correction d'un bug lié à la gestion des personnes physiques et morales.
- Correction d'un bug lié à l'affichage de la liste des agents.
- Correction d'un bug lié à la gestion des rapports au logement.
- Correction d'un bug lié à la validation des dates.
- Ajout de messages d'erreur plus clairs pour l'utilisateur.
