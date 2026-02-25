## Changelog : infomedicament (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la page des médicaments avec l'ajout d'informations détaillées (excipients, AIPS, etc.) et l'amélioration de la recherche. Des corrections ont été apportées pour stabiliser le service, notamment au niveau des scripts de mise à jour de la base de données et de la gestion des erreurs. Des mesures de sécurité ont également été implémentées pour protéger l'application contre les abus.

### Évolutions fonctionnelles
- Ajout d'informations sur les excipients des médicaments (#182).
- Amélioration de la page des médicaments avec l'ajout d'informations sur les AIPS (Autorisations d'Innovation et de Promotion de l'Utilisation Rationnelle des Médicaments), les statuts de commercialisation, les alertes de sécurité et la surveillance renforcée (#164).
- Affichage des informations princeps et génériques (#187).
- La recherche permet maintenant de filtrer sur les codes ATC5 (#191).
- Amélioration de l'autocomplétion de la recherche avec les noms de spécialités (#191).
- Limitation des résultats de recherche à 100 médicaments (#191).
- Ajout de badges d'explicabilité à la recherche (#183).
- Possibilité de cliquer sur une spécialité dans les résultats de recherche pour accéder à sa page (#183).
- Affichage des informations sur les AIPS dans les résultats de recherche et les résumés (#187).
- Amélioration de l'affichage des indications (#175).
- Correction de l'affichage des tags princeps et génériques (#175).

### Évolutions techniques
- Refactorisation de la recherche pour simplifier l'UI et le code (#183).
- Migration de la base de données pour améliorer la recherche (#183).
- Utilisation de la base de données pour les données ATC au lieu de fichiers statiques (#191).
- Amélioration de la gestion des erreurs et de la robustesse des scripts de mise à jour de la base de données (PDBM) (#191, #188).
- Mise à jour des dépendances : Next.js (15.5.10), Vitest (3.0.5) (#182).
- Ajout de tests d'intégration pour les scripts de mise à jour (#191).
- Ajout de tests unitaires et d'UI (#191, #174).
- Amélioration de la gestion des requêtes vers la base de données (caching, optimisation des requêtes) (#191).

### Autres changements
- Documentation de la procédure de déploiement et du workflow Git (#191).
- Ajout de mesures de sécurité : limitation du taux de requêtes, ajout d'en-têtes CSP (Content Security Policy) et protection des routes de débogage (#182).
- Nettoyage du code et suppression de fichiers inutilisés (#191).
- Amélioration de la configuration de la base de données PostgreSQL (keepAlive, timeouts) (#191).
- Correction de bugs mineurs et améliorations de la qualité du code (#188, #175).
- Ajout de commentaires et documentation dans le code (#175).
