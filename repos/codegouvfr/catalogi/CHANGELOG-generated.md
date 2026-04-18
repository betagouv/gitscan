## Changelog : catalogi (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Catalogi se concentrent sur l'amélioration de la configuration et de la gestion des environnements, ainsi que sur des optimisations techniques internes pour faciliter le développement et le déploiement. Des corrections ont également été apportées pour améliorer l'expérience utilisateur, notamment en ce qui concerne la compatibilité mobile et le blocage de contenu par la politique de sécurité du contenu (CSP).

### Évolutions fonctionnelles
- Amélioration de la gestion des configurations via des fichiers, permettant une plus grande flexibilité et une meilleure organisation. [#500](https://github.com/codegouvfr/catalogi/issues/500)
- Ajout d'options pour les systèmes d'exploitation mobiles dans l'interface web.
- Correction d'un problème bloquant l'affichage de certaines ressources (analytics, suivi des routes SPA) à cause de la politique de sécurité du contenu (CSP).
- Possibilité d'accéder à la base de données PostgreSQL localement via un tunnel SSH pour le débogage et l'administration.
- Ajout de champs personnalisables pour les logiciels via l'API.

### Évolutions techniques
- Migration de Yarn vers pnpm pour la gestion des dépendances, améliorant la performance et la cohérence.
- Utilisation de tsx pour le développement de l'API, permettant un rechargement à chaud plus rapide et une meilleure expérience de développement.
- Refactoring pour utiliser un modèle de packages internes pour le partage de types entre l'API et l'interface web.
- Mise à jour de Node.js vers la version 24 et de pnpm vers la version 10.32.1.
- Mise à jour des actions CI/CD (actions/checkout et actions/setup-node) vers la version 6.
- Amélioration de la configuration locale de la politique de sécurité du contenu (CSP) pour autoriser l'affichage des images.
- Ajout de `worker-src` à la politique de sécurité du contenu (CSP) pour permettre le fonctionnement des workers Sentry.

### Autres changements
- Documentation : Ajout d'un plan de migration pour passer de Yarn à pnpm, l'utilisation de tsx en développement et le nouveau modèle de packages internes.
- Correction de la configuration de l'analyseur IOC pour utiliser `pnpm-lock.yaml` au lieu de `yarn.lock`.
- Augmentation du numéro de version de l'application.
