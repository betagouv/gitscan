## Changelog : domifa (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois a été marqué par un effort majeur de mise en conformité avec les normes d'accessibilité (RGAA) sur le portail usagers. La sécurité a été renforcée par l'intégration systématique de scans antivirus sur les fichiers importés, et la gestion administrative des comptes régionaux (DREETS/DDETS) a été simplifiée pour offrir plus d'autonomie aux gestionnaires.

### Évolutions fonctionnelles
- **Accessibilité (RGAA) :** Améliorations massives de l'expérience utilisateur pour respecter les normes d'accessibilité (clarté des liens, visibilité du focus, étiquettes de formulaires et gestion des messages d'erreur).
- **Gestion des comptes :**
    - Possibilité pour la DGCS de gérer les comptes DREETS et DDETS de chaque région.
    - Extension des capacités de gestion pour les DREETS, incluant la suppression de comptes régionaux via la [PR #4346](https://github.com/SocialGouv/domifa/pull/4346).
    - Support de nouveaux domaines de messagerie institutionnels (ex: guyane.gouv.fr).
- **Mode Support :** Mise en place d'un mode support permettant d'assister les utilisateurs tout en restreignant certaines actions sensibles comme l'export de données ou la modification de paramètres ([#4334](https://github.com/SocialGouv/domifa/pull/4334), [#4339](https://github.com/SocialGouv/domifa/pull/4339), [#4323](https://github.com/SocialGouv/domifa/pull/4323)).
- **Expérience Utilisateur :**
    - Ajout d'un menu déroulant de sélection du portail sur les pages de connexion ([#4335](https://github.com/SocialGouv/domifa/pull/4335)).
    - Mise en place d'un système d'avis de maintenance pour informer les utilisateurs.
    - Amélioration de la synchronisation et de l'affichage de la liste des usagers.

### Évolutions techniques
- **Sécurité & Antivirus :**
    - Intégration de ClamAV pour scanner systématiquement les fichiers lors des imports (usagers, documents de structure, formulaires de contact).
    - Amélioration de la gestion des erreurs d'antivirus et de la validation des types de fichiers pour éviter les plantages.
- **Backend & API :**
    - Renforcement de la sécurité des points de terminaison (endpoints) des usagers.
    - Optimisation de la logique de synchronisation des données (`lastSync`) pour garantir la cohérence des listes.
    - Augmentation de la limite de référence pour les usagers.
    - Activation de l'envoi d'emails transactionnels Brevo en environnement de préproduction.
- **Architecture :** Optimisation de la configuration DSFR (déplacement en script groupé) pour une meilleure conformité aux politiques de sécurité de contenu (CSP).

### Autres changements
- **Documentation :** Mise à jour des déclarations d'accessibilité suite aux audits RGAA.
- **Maintenance :** Nettoyage des anciens articles de news et suppression de classes CSS inutilisées.
