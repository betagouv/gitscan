## Changelog : csplab (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur, notamment avec l'ajout de composants réutilisables pour l'ATS (Applicant Tracking System) et la gestion des recrutements. Des efforts importants ont également été réalisés sur l'ingestion des données, avec une meilleure gestion des sources, des webhooks et des erreurs. Enfin, des bases solides sont posées pour l'authentification et la sécurité, ainsi que pour l'audit des actions.

### Évolutions fonctionnelles
- Ajout d'une interface pour les détails des recrutements [#856](https://github.com/betagouv/csplab/issues/856).
- Implémentation de la soumission de candidatures [#753](https://github.com/betagouv/csplab/issues/753).
- Ajout d'une interface pour la mise à jour des étapes de recrutement d'un organisme [#835](https://github.com/betagouv/csplab/issues/835).
- Possibilité de voir le métier associé à une offre dans la liste des offres [#747](https://github.com/betagouv/csplab/issues/747).
- Ajout d'une page pour consulter la documentation de l'API [#820](https://github.com/betagouv/csplab/issues/820).
- Ajout d'une authentification par email/mot de passe [#752](https://github.com/betagouv/csplab/issues/752) et authentification 2FA sur l'admin Django [#699](https://github.com/betagouv/csplab/issues/699).
- Ajout de la gestion des organismes et des étapes de recrutement [#798](https://github.com/betagouv/csplab/issues/798).
- Ajout d'un workflow pour les previews de branches Storybook sur demande [#867](https://github.com/betagouv/csplab/issues/867).

### Évolutions techniques
- Refactorisation de l'architecture pour séparer les couches domaine, présentation et infrastructure.
- Amélioration de la gestion des erreurs avec l'envoi des exceptions Celery à Sentry [#861](https://github.com/betagouv/csplab/issues/861).
- Découplage de l'application Celery pour éviter les dépendances cycliques [#862](https://github.com/betagouv/csplab/issues/862).
- Mise en place de releases Sentry lors des déploiements [#850](https://github.com/betagouv/csplab/issues/850).
- Utilisation de Docker et de conteneurs pour l'environnement de développement et de production.
- Migration vers un modèle utilisateur personnalisé Django.
- Amélioration de la gestion des dépendances et des workflows CI/CD.
- Ajout de tests Cypress et pytest pour assurer la qualité du code.
- Mise en place de tests plus lisibles avec le décorateur `patch` [#849](https://github.com/betagouv/csplab/issues/849).
- Utilisation de TypeScript et de React pour le frontend.
- Ajout de composants réutilisables pour l'interface utilisateur (table, pagination, badges, icônes, etc.).
- Amélioration des performances et de la scalabilité de l'application.
- Ajout d'un script pour mettre à jour les dépendances [#832](https://github.com/betagouv/csplab/issues/832).

### Autres changements
- Documentation améliorée pour l'API et les processus d'ingestion.
- Ajout de règles métier dans la couche domaine [#863](https://github.com/betagouv/csplab/issues/863).
- Nettoyage du code et refactorisation de certaines parties de l'application.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Mise à jour des dépendances et des outils de développement.
- Configuration améliorée pour l'environnement de production.
- Ajout d'un fichier `robots.txt` pour le SEO [#808](https://github.com/betagouv/csplab/issues/808).
- Ajout d'un fichier `security.txt` pour la sécurité [#695](https://github.com/betagouv/csplab/issues/695).
- Ajout d'un script de sauvegarde de la base de données [#833](https://github.com/betagouv/csplab/issues/833).
