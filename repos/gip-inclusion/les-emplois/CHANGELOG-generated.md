## Changelog : les-emplois (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec l'intégration complète de la gestion des orientations, permettant une synchronisation fluide avec les données externes (Dora). L'expérience utilisateur a été enrichie par une meilleure clarté des informations sur les profils et les candidatures, tandis que la sécurité a été renforcée par une gestion plus intuitive et robuste de la double authentification (MFA).

### Évolutions fonctionnelles
- **Gestion des orientations** : Mise en place d'une interface complète permettant de lister et de consulter les détails des orientations, avec des filtres avancés (expéditeur, structure, statut, bénéficiaire).
- **Expérience candidat** : Amélioration de la clarté des profils (explications sur les champs en lecture seule, alertes sur l'identité certifiée) et affichage systématique des coordonnées des conseillers.
- **Parcours de candidature** : Ajout d'aides contextuelles et d'informations sur les dates de contrat pour guider les utilisateurs lors de la saisie.
- **Sécurité (MFA)** : Amélioration de l'accompagnement à l'activation de la double authentification (exemples d'applications, liens de configuration simplifiés, messages clarifiés).
- **Services de diagnostic** : Priorisation des liens externes pour faciliter les orientations vers des services tiers.
- **Gestion des entreprises** : Automatisation du transfert des évaluations GEIQ lors du transfert d'une entreprise.

### Évolutions techniques
- **Synchronisation des données** : Automatisation de la synchronisation des statuts d'orientation depuis Dora et ajout de journaux de suivi (logs) pour tracer les changements de statut.
- **Sécurité et Authentification** : Renforcement des mécanismes de double authentification (MFA/OTP) et amélioration de la gestion des flux de connexion (FranceConnect, ProConnect).
- **Optimisation des performances** : Amélioration de la vitesse de chargement des listes de candidats et optimisation des requêtes à la base de données (réduction des requêtes N+1).
- **Architecture et Refactoring** : 
    - Refonte de la gestion des entreprises et renommage de composants pour plus de cohérence (passage de PoleEmploiConnect à ProConnect).
    - Mise en place de la suppression logique (soft-delete) pour les services et les structures.
- **Gestion de fichiers** : Optimisation du processus de nettoyage des fichiers inutilisés via un traitement par lots.

### Autres changements
- **Administration** : Amélioration de l'interface d'administration pour le suivi des dispositifs de sécurité et des utilisateurs.
- **Maintenance** : Nettoyage des modèles d'e-mails (suppression des mentions de sondages obsolètes) et mise à jour de la documentation technique.
