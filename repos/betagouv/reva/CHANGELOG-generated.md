## Changelog : reva (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par une amélioration significative de l'intégration de France Connect, avec l'ajout de la gestion de champs supplémentaires et une simplification du processus de création de candidatures. Des améliorations ont également été apportées à l'interface utilisateur, notamment sur les pages de statut et de confirmation d'inscription, ainsi qu'à la gestion des cohortes VAE collectives. Plusieurs corrections de bugs et optimisations techniques ont été réalisées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'intégration de France Connect : ajout de la gestion de la nationalité, du code postal, de la localité, du numéro de téléphone et simplification du processus de création de candidatures (#2026-02-18T17:51:22, #2026-02-17T10:45:13, #2026-02-17T10:45:13, #2026-02-02T21:08:49).
- Nouvelle page de confirmation d'inscription après la création d'un compte (#2026-01-26T21:44:19).
- Amélioration des tuiles du tableau de bord candidat avec des états en lecture seule et un rendu conditionnel amélioré (#2026-01-23T13:44:13).
- Ajout d'une confirmation modale lors de la déclaration de complétude d'un DF par une autorité de certification (#2026-02-16T16:48:24).
- Amélioration de la gestion des blocs de compétences dans la génération du PDF DF dématérialisé (#2026-01-23T16:51:20).
- Ajout de la possibilité de sélectionner plusieurs certifications pour les cohortes VAE collectives (#2026-01-26T15:12:33).
- Ajout d'un indicateur de chargement sur la page d'inscription (#2026-02-19T14:35:49).
- Amélioration de l'affichage des résultats de jury dans l'interface d'administration (#2026-02-17T12:10:11).
- Correction de l'adresse e-mail d'envoi des décisions de faisabilité (#2026-02-19T17:45:41).
- Correction de l'espacement réactif sur la FAQ du site web (#2026-02-17T14:23:47).

### Évolutions techniques
- Refactorisation de la gestion des variables d'environnement pour améliorer la sécurité et la flexibilité (#2026-02-27T12:37:23, #2026-02-27T12:25:26).
- Mise en place de plugins Fastify pour la gestion des cookies et la limitation du taux de requêtes (#2026-02-27T12:25:26).
- Utilisation de JWT pour la gestion de l'état dans les cookies (#2026-02-06T17:10:34).
- Refactorisation du code pour utiliser des URL construites de manière plus propre (#2026-02-06T17:10:35).
- Mise à jour des dépendances (Next.js, React, etc.) dans plusieurs packages (#2026-01-30T10:37:44, #2026-01-30T10:19:59, #2026-01-30T10:17:43).
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et les corrections de bugs.
- Amélioration de la gestion des erreurs et des messages d'erreur pour France Connect (#2026-02-13T14:47:35).
- Refactorisation de la gestion des layouts et des composants dans l'application candidat (#2026-02-10T21:12:40).

### Autres changements
- Ajout d'une configuration pour un nouveau tableau de bord Metabase pour le CPNEFP de la Métallurgie (#2026-02-16T15:08:48).
- Mise à jour de la documentation et des commentaires dans le code.
- Ajout de fichiers de configuration pour Claude dans le fichier .gitignore (#2026-02-13T14:47:34).
- Correction de la valeur par défaut de `juryEstimatedCost` dans l'interface d'administration (#2026-02-12T12:09:41, #2026-02-11T12:18:57).
- Suppression du rateLimit dans l'API (#2026-02-09T15:24:06).
- Ajout d'un flag de fonctionnalité pour activer la sélection multiple de certifications dans les cohortes VAE collectives (#2026-01-28T09:50:56).
