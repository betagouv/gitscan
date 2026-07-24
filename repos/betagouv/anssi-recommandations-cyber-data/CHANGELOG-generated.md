## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité du projet avec des mises à jour de nombreuses dépendances pour corriger des vulnérabilités. De nouvelles fonctionnalités ont été ajoutées pour la gestion des documents, notamment la suppression de documents et la possibilité de "jeopardyser" une collection entière. Des corrections ont également été apportées pour améliorer l'authentification et l'encodage des noms de fichiers.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer des documents.
- Ajout d'un formulaire permettant de traiter une collection de documents en bloc ("jeopardyser").
- Correction de l'enrôlement des utilisateurs en fournissant le bon nom d'utilisateur.
- Correction de l'encodage des noms de documents en UTF-8 pour éviter les problèmes de caractères spéciaux [#cece025](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/cece025).
- Redirection vers le TDB (Tooling Data Base) après authentification.
- Modification du prompt utilisé pour éviter les hallucinations dans les réponses.

### Évolutions techniques
- Mise en place de l'outil `zizmor` pour valider la configuration du projet et améliorer la sécurité [#685a93e](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/685a93e).
- Désactivation des identifiants `git` dans les dépôts clonés dans le CI pour renforcer la sécurité [#94041bd](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/94041bd).
- Intégration de Renovate pour la gestion automatisée des dépendances [#19f167b](https://github.com/betagouv/anssi-recommandations-cyber-data/commit/19f167b).
- Mises à jour de nombreuses dépendances pour corriger des vulnérabilités de sécurité (aiohttp, pyjwt, starlette, vitest, python-multipart, pandas, svelte, vite, etc.).

### Autres changements
- Nettoyage et simplification de la configuration du CI.
- Ajout de l'action Renovate pour la gestion des dépendances.
