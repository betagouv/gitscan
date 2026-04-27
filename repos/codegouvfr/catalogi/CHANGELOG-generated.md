## Changelog : catalogi (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion de la configuration, la correction de bugs liés à l'interface web et l'amélioration de la sécurité grâce à la configuration du Content Security Policy (CSP). Des ajustements ont également été apportés pour faciliter le développement local et le suivi des événements analytiques.

### Évolutions fonctionnelles
- Correction d'un bug sur l'interface web : ajout d'options manquantes pour les systèmes d'exploitation mobiles et amélioration de la sécurité des types de données. [#500](https://github.com/codegouvfr/catalogi/issues/500)
- Amélioration du suivi des événements analytiques : résolution d'un blocage lié au CSP et suivi des changements de route dans l'application monopage (SPA).
- Gestion de la configuration : introduction d'une nouvelle méthode de gestion de la configuration via des fichiers et propagation de cette configuration à travers l'application.

### Évolutions techniques
- Refactorisation de la gestion des fonctionnalités "gateway".
- Amélioration de la configuration locale du CSP pour permettre l'affichage des images.
- Ajout de `worker-src` au CSP par défaut pour les workers Sentry.
- Réorganisation des migrations de la base de données.

### Autres changements
- Documentation : amélioration de la documentation concernant la configuration locale du CSP.
- Mises à jour de version (build bumps).
