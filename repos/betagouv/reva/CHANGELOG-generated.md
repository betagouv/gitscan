## Changelog : reva (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, l'écosystème REVA a franchi des étapes importantes avec la refonte du parcours de dépôt de dossier pour les candidats et l'enrichissement des fonctionnalités pour les structures collectives, notamment via une meilleure gestion des sous-comptes. La gestion administrative des certifications a été simplifiée et la structure technique a été renforcée pour améliorer la sécurité et la gestion des droits d'accès.

### Évolutions fonctionnelles
- **Parcours Candidat** : 
    - Mise en place d'un nouveau parcours de dépôt de dossier (DV) sur une page dédiée, incluant une gestion dynamique des dates et des blocs de ressources.
    - Amélioration de l'affichage des informations de faisabilité (badges et tuiles) et de l'historique des décisions.
    - Possibilité de choisir une certification spécifique lors d'une démarche de VAE collective multi-certifications.
- **VAE Collective** : 
    - Ajout d'une page de suivi des candidatures et d'un espace de gestion des paramètres pour les sous-comptes.
    - Amélioration de l'interface de gestion des sous-comptes (affichage de tags AAP, formulaires de création plus robustes et gestion des erreurs améliorée).
    - Meilleure visibilité des permissions sur les cartes de cohortes et les éléments de gestion.
- **Administration** : 
    - Création d'un tableau de bord dédié aux comptes locaux d'autorités de certification.
    - Simplification de la gestion des certifications grâce à l'ajout de fenêtres modales pour l'ajout et la suppression de certifications.
    - Amélioration de l'ergonomie des liens relatifs aux autorités de certification sur l'ensemble des interfaces.

### Évolutions techniques
- **Sécurité & Autorisation** : 
    - Refonte majeure du système de gestion des droits via la migration vers des politiques centralisées (`withPolicies`).
    - Introduction de nouveaux rôles et permissions spécifiques pour la gestion des sous-comptes (ex: rôle `SOUS_COMPTE_VAE_COLLECTIVE`).
- **Architecture & Données** : 
    - Introduction d'un nouvel objet métier `accompagnement` pour dissocier la notion de candidature de son mode d'accompagnement (autonome ou accompagné).
    - Ajout de la traçabilité de la dernière connexion (`lastLoginAt`) dans la table des comptes.
    - Mise en place de "feature flags" pour permettre un déploiement progressif des nouvelles pages de dépôt de dossier.
- **Fiabilité de l'API** : 
    - Amélioration de la robustesse lors de la création d'autorités de certification grâce à l'implémentation de mécanismes de rollback en cas d'échec.
    - Optimisation des requêtes GraphQL et de la gestion des permissions par cohorte.

### Autres changements
- **Infrastructure** : Modification de la configuration Traefik (désactivation de la réinitialisation de mot de passe Metabase).
- **Maintenance** : Nettoyage de code (suppression d'imports inutilisés) et renommage de contraintes de base de données pour une meilleure clarté.
