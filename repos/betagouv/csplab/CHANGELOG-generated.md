## Changelog : csplab (30 derniers jours, au 02 Juillet 2026)

### Résumé
Ce mois-ci, les évolutions de csplab se concentrent sur l'amélioration de l'ingestion des offres d'emploi, l'ajout de fonctionnalités pour les recruteurs (gestion des organismes et des étapes de recrutement), et la mise en place d'une infrastructure plus robuste (logs, sécurité, CI/CD). Des bases solides sont également posées pour l'interface utilisateur avec l'ajout de composants et la structuration du frontend.

### Évolutions fonctionnelles
- Ajout d'un modèle d'administration en lecture seule pour les instantanés de statistiques. [#894](https://github.com/betagouv/csplab/issues/894)
- Les configurations d'identifiants TalentSoft sont désormais dynamiques. [#892](https://github.com/betagouv/csplab/issues/892)
- Amélioration de l'interface pour la gestion des organismes, avec l'ajout d'étapes et la possibilité de les mettre à jour. [#883](https://github.com/betagouv/csplab/issues/883), [#893](https://github.com/betagouv/csplab/issues/893), [#886](https://github.com/betagouv/csplab/issues/886)
- Ajout de la soumission de candidatures. [#729](https://github.com/betagouv/csplab/issues/729)
- Ajout d'une interface pour afficher les détails d'un recrutement. [#856](https://github.com/betagouv/csplab/issues/856)
- Ajout d'une interface pour la gestion de mes recrutements. [#838](https://github.com/betagouv/csplab/issues/838)
- Affichage du métier dans la liste des offres pour les candidats. [#747](https://github.com/betagouv/csplab/issues/747)
- Ajout d'une page de connexion avec une interface utilisateur. [#752](https://github.com/betagouv/csplab/issues/752)
- Ajout d'une fonctionnalité permettant d'afficher le pipeline actif d'un organisme. [#821](https://github.com/betagouv/csplab/issues/821)

### Évolutions techniques
- Ajout de statistiques quotidiennes calculées et stockées. [#884](https://github.com/betagouv/csplab/issues/884)
- Séparation de la gestion des offres en base de données et de l'ingestion. [#887](https://github.com/betagouv/csplab/issues/887)
- Amélioration de la gestion des erreurs et ajout de timeouts pour les tâches Celery. [#797](https://github.com/betagouv/csplab/issues/797)
- Refactorisation de l'architecture pour séparer les responsabilités et améliorer la maintenabilité.
- Mise en place d'un système de logs API plus complet. [#720](https://github.com/betagouv/csplab/issues/720)
- Ajout de l'authentification à deux facteurs (2FA) sur l'administration Django. [#699](https://github.com/betagouv/csplab/issues/699)
- Amélioration de la gestion des dépendances et des déploiements (CI/CD).
- Ajout de tests unitaires et d'intégration pour améliorer la qualité du code.
- Amélioration de la lisibilité des tests avec l'utilisation de décorateurs. [#848](https://github.com/betagouv/csplab/issues/848)
- Ajout de releases Sentry lors des déploiements. [#850](https://github.com/betagouv/csplab/issues/850)
- Mise à jour des dépendances pour bénéficier des dernières corrections et améliorations de sécurité.

### Autres changements
- Documentation améliorée pour l'utilisation des webhooks Talentsoft. [#721](https://github.com/betagouv/csplab/issues/721)
- Ajout d'un fichier `security.txt` pour la divulgation responsable des vulnérabilités. [#695](https://github.com/betagouv/csplab/issues/695)
- Amélioration de la structure des tests. [#789](https://github.com/betagouv/csplab/issues/789), [#746](https://github.com/betagouv/csplab/issues/746)
- Refactorisation de composants Storybook. [#872](https://github.com/betagouv/csplab/issues/872), [#871](https://github.com/betagouv/csplab/issues/871), [#867](https://github.com/betagouv/csplab/issues/867)
- Ajout de composants UI de base pour le frontend (table, badges, avatars, etc.). [#852](https://github.com/betagouv/csplab/issues/852), [#812](https://github.com/betagouv/csplab/issues/812), [#853](https://github.com/betagouv/csplab/issues/853), [#817](https://github.com/betagouv/csplab/issues/817)
- Correction de bugs mineurs et améliorations de la performance.
