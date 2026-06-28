## Changelog : transfers (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, le service de transfert de fichiers a bénéficié d'améliorations significatives en termes de sécurité, d'expérience utilisateur et d'architecture. Une nouvelle fonctionnalité permet de générer des liens de téléchargement uniques et temporaires, renforçant la sécurité des partages. L'interface utilisateur a été modernisée avec une navigation plus intuitive et des informations de date plus claires. Enfin, une migration technique majeure vers Vite et Tanstack Router a été initiée pour améliorer la performance et la maintenabilité du frontend.

### Évolutions fonctionnelles
- **Sécurité des téléchargements:** Renforcement du flux de téléchargement et correction de failles de sécurité identifiées lors de la revue de code [#11](https://github.com/suitenumerique/transfers/issues/11).
- **Liens de téléchargement uniques:** Ajout de liens de téléchargement à usage unique qui s'auto-désactivent après le premier téléchargement complet [#5](https://github.com/suitenumerique/transfers/issues/5).
- **Authentification:** Implémentation d'un flux de connexion via ProConnect sans authentification préalable [#13](https://github.com/suitenumerique/transfers/issues/13).
- **Affichage des dates:** Amélioration de l'affichage des dates relatives (ex: "il y a 2 jours") avec un affichage complet de la date au survol et une meilleure accessibilité [#9](https://github.com/suitenumerique/transfers/issues/9).
- **Sécurité des uploads:** Ajout d'un scanner de fichiers pour empêcher le stockage de fichiers potentiellement dangereux [#9](https://github.com/suitenumerique/transfers/issues/9).
- **Compatibilité S3:** Autorisation de l'origine S3 dans la directive `connect-src` du CSP pour les uploads.

### Évolutions techniques
- **Migration Frontend:** Migration du frontend de Next.js vers Vite et Tanstack Router pour améliorer les performances et l'expérience de développement [#10](https://github.com/suitenumerique/transfers/issues/10).
- **Dépendances Frontend:** Déplacement de Tanstack Router vers les dépendances de développement.
- **Correction CodeRabbit:** Correction des remarques issues de l'analyse CodeRabbit.

### Autres changements
- **Documentation:** Ajout de documentation.
