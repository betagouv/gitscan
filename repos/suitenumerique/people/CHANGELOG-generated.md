## Changelog : people (30 derniers jours, au 02/11/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité des données et la modernisation de l'infrastructure de développement. Les mises à jour ont permis de mieux protéger la confidentialité des configurations de domaines et d'optimiser les processus de déploiement et de test automatique.

### Évolutions fonctionnelles
- **Renforcement de la confidentialité** : la configuration des domaines est désormais masquée pour les utilisateurs disposant uniquement de droits de lecture sur ces domaines.
- **Sécurité des domaines** : l'appariement des domaines d'e-mail des organisations est désormais effectué de manière plus stricte pour garantir l'intégrité des comptes.

### Évolutions techniques
- **Infrastructure et CI/CD** : mise à jour majeure des outils de déploiement et de test (GitHub Actions, Playwright) et adoption du preset de configuration CI par défaut de la Suite Numérique.
- **Sécurité** : mise à jour de la bibliothèque `urllib3` pour corriger des vulnérabilités.
- **Qualité de code et Linting** : migration vers ESLint 9, transformation de la configuration ESLint en plugin et renommage de variables pour assurer la conformité aux standards Sonar.
- **Configuration** : mise à jour des fichiers de configuration applicative (interface, internationalisation et tests de bout en bout).
- **Nettoyage** : finalisation du nettoyage du package `oauth-provider`.

### Autres changements
- Mise à jour des chaînes de traduction (i18n).
