## Changelog : territoires-en-transitions (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant la gestion des référentiels, notamment en préparation de la bascule vers le référentiel "Territoires en Transitions" (TE). Des efforts considérables ont été déployés pour améliorer la sécurité, la robustesse et l'expérience utilisateur, en particulier dans les fonctionnalités d'audit et de labellisation. L'intégration d'IA pour l'import de plans est également en cours de développement.

### Évolutions fonctionnelles
- Ajout de la fusion des services, pilotes, explications et statuts CAE/ECI vers les mesures TE. [#16](https://github.com/incubateur-ademe/territoires-en-transitions/issues/16)
- Implémentation de la fusion des liens fiches CAE/ECI vers TE. [#16](https://github.com/incubateur-ademe/territoires-en-transitions/issues/16)
- Possibilité de filtrer les snapshots des référentiels archivés.
- Ajout de la gestion des dates de début et de fin pour les plans. (TET-7490)
- Amélioration de la sécurité : blocage de l'injection IDOR de relations cross-collectivité dans les plans et fichiers. (TET-7358, TET-7359, TET-7360)
- Ajout de la fonctionnalité d'import de plans via IA, incluant l'extraction, la création et le suivi de progression.
- Amélioration de l'interface d'audit et de labellisation avec une nouvelle checklist, la gestion des documents de candidature et un affichage plus clair des statuts.
- Ajout de la possibilité de télécharger les preuves d'un audit.
- Ajout d'un bandeau d'alerte pour les référentiels archivés ou en lecture seule.
- Amélioration de l'export Excel des indicateurs. (TET-7414)

### Évolutions techniques
- Refactorings importants dans la gestion des snapshots, avec migration vers le pattern `Result` pour une meilleure gestion des erreurs.
- Amélioration de la robustesse des tests E2E et parallélisation pour une exécution plus rapide.
- Mise à jour de TypeScript vers la version 6/7.
- Suppression de code obsolète et simplification de certaines structures de données.
- Migration de certains composants vers le nouveau layout.
- Mise à jour des dépendances (Next.js, swc, posthog-js).
- Amélioration de la sécurité avec la mise en place d'une Content Security Policy (CSP) globale.
- Refactor de la gestion des dates avec remplacement de Luxon par date-fns.
- Migration de certains modules vers le backend tRPC.

### Autres changements
- Documentation mise à jour pour les agents IA et le plan de migration des applications.
- Amélioration de la gestion des libellés et des messages d'erreur.
- Corrections de bugs mineurs et améliorations de la performance.
- Ajout de tests unitaires et E2E pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Mise à jour du schéma des préférences de la collectivité.
- Ajout de la gestion des thématiques SGPE dans le référentiel TE.
- Suppression de l'edge function `import_statut_emt`.
- Ajout d'un script d'import des statuts EMT.
- Amélioration de la gestion des erreurs et des logs.
- Optimisation de la configuration CI/CD.
