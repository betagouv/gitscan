## Changelog : transfers (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, l'expérience utilisateur et la modernisation de l'application. Une nouvelle fonctionnalité de scan antivirus a été ajoutée pour protéger les fichiers stockés, et l'interface utilisateur a été améliorée avec des dates plus conviviales et une meilleure gestion des téléchargements. De plus, une migration technique vers Vite et Tanstack Router a été initiée pour optimiser le frontend.

### Évolutions fonctionnelles
- Ajout d'un scan antivirus pour les fichiers téléchargés afin d'empêcher le stockage de fichiers dangereux. [#9](https://github.com/suitenumerique/transfers/issues/9)
- Amélioration de l'affichage des dates : affichage relatif intelligent avec date complète au survol.
- Renforcement de la sécurité du flux de téléchargement et correction des points soulevés lors de la revue de code. [#11](https://github.com/suitenumerique/transfers/issues/11)
- Implémentation d'un flux de connexion ProConnect simplifié. [#13](https://github.com/suitenumerique/transfers/issues/13)
- Correction d'un problème empêchant les requêtes vers S3 dans le `connect-src` du CSP pour les uploads.

### Évolutions techniques
- Migration du frontend de Next.js vers Vite et Tanstack Router pour une meilleure performance et maintenabilité.
- Correction des remarques de CodeRabbit concernant la revue de code de la PR #10.
- Déplacement de Tanstack Router dans les dépendances de développement.
- Correction d'une anomalie identifiée par CodeRabbit.
- Amélioration de la robustesse du scan antivirus en cas de scanner indisponible.
- Correction des points soulevés lors de la revue de code concernant le flux de rescan.

### Autres changements
- Aucune information supplémentaire.
