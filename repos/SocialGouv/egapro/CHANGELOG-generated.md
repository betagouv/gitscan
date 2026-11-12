## Changelog : egapro (30 derniers jours, au 11 novembre 2026)

### Résumé
Ce mois-ci, la plateforme a connu une avancée majeure sur l'accessibilité (RGAA) et l'expérience utilisateur, notamment pour les parcours de déclaration de rémunération et les avis du CSE. Les outils d'administration ont été enrichis pour offrir plus de contrôle sur les campagnes, tandis que la sécurité a été renforcée par l'introduction de nouvelles méthodes d'authentification. En parallèle, les fondations techniques ont été préparées pour supporter les futures évolutions de la base de données.

### Évolutions fonctionnelles

**Déclarations et parcours utilisateurs**
- Amélioration complète du parcours des avis CSE : nouveaux designs de pages de visualisation, récapitulatifs PDF et workflow de transmission optimisé [#4963](https://github.com/SocialGouv/egapro/issues/4963), [#4983](https://github.com/SocialGouv/egapro/issues/4983), [#5097](https://github.com/SocialGouv/egapro/issues/5097).
- Optimisation de la déclaration de rémunération : affichage du sens des écarts, nouvelles infobulles de lecture et récapitulatifs adaptés à la taille de l'entreprise [#4792](https://github.com/SocialGouv/egapro/issues/4792), [#4967](https://github.com/SocialGouv/egapro/issues/4967), [#5078](https://github.com/SocialGouv/egapro/issues/5078).
- Amélioration de la déclaration de représentation avec de nouveaux modèles de PDF et de pages de confirmation [#4916](https://github.com/SocialGouv/egapro/issues/4916), [#5081](https://github.com/SocialGouv/egapro/issues/5081).
- Meilleure gestion des verrous de déclaration avec information sur les délais de reprise possibles [#5085](https://github.com/SocialGouv/egapro/issues/5085).
- Mise à jour de l'Observatoire avec l'ajout de l'historique des SIREN pour les audits RGAA [#5079](https://github.com/SocialGouv/egapro/issues/5079).

**Espace Utilisateur (Mon Espace)**
- Amélioration de la visibilité des documents et des échéances des démarches [#5135](https://github.com/SocialGouv/egapro/issues/5135), [#5133](https://github.com/SocialGouv/egapro/issues/5133).
- Possibilité de déposer un rapport d'évaluation conjointe directement dans l'espace utilisateur en cas de mise en demeure [#4825](https://github.com/SocialGouv/egapro/issues/4825).

**Administration et Pilotage**
- Nouveaux outils de pilotage : paramétrage des dates limites de choix de parcours et statistiques de campagne affinées [#5151](https://github.com/SocialGouv/egapro/issues/5151), [#4812](https://github.com/SocialGouv/egapro/issues/4812).
- Export CSV des référents amélioré (libellés et colonnes réordonnées) [#5108](https://github.com/SocialGouv/egapro/issues/5108).

**Accessibilité et Design**
- Chantier massif d'accessibilité : mise en conformité RGAA sur l'ensemble des formulaires, tableaux, graphiques et documents PDF (norme PDF/UA-1) [#5017](https://github.com/SocialGouv/egapro/issues/5017), [#5018](https://github.com/SocialGouv/egapro/issues/5018), [#5023](https://github.com/SocialGouv/egapro/issues/5023).
- Refonte visuelle de la page d'accueil (hero, cartes, FAQ) et corrections de design sur l'ensemble de l'interface [#5103](https://github.com/SocialGouv/egapro/issues/5103), [#5092](https://github.com/SocialGouv/egapro/issues/5092).
- Harmonisation des libellés (wording) sur l'ensemble de la plateforme pour une meilleure clarté [#5152](https://github.com/SocialGouv/egapro/issues/5152), [#5136](https://github.com/SocialGouv/egapro/issues/5136).

**Sécurité et Légal**
- Renforcement de l'authentification : support de l'eidas2 pour l'administration et renforcement du MFA pour les déclarants [#5132](https://github.com/SocialGouv/egapro/issues/5132), [#4816](https://github.com/SocialGouv/egapro/issues/4816).
- Mise à jour des CGU et de la politique de confidentialité [#4828](https://github.com/SocialGouv/egapro/issues/4828).

### Évolutions techniques

**Infrastructure et Base de données**
- Préparation de la migration vers PostgreSQL 17 pour les environnements de développement et la V2 [#4871](https://github.com/SocialGouv/egapro/issues/4871), [#4870](https://github.com/SocialGouv/egapro/issues/4870).
- Optimisations de l'infrastructure (gestion des CronJobs, conteneurs et environnements de test) [#4827](https://github.com/SocialGouv/egapro/issues/4827), [#5106](https://github.com/SocialGouv/egapro/issues/5106), [#5006](https://github.com/SocialGouv/egapro/issues/5006).

**Sécurité et Observabilité**
- Amélioration de la traçabilité des audits (gestion des impersonations, traçage des pannes antivirus) [#4886](https://github.com/SocialGouv/egapro/issues/4886), [#4826](https://github.com/SocialGouv/egapro/issues/4826).
- Sécurisation des données : anonymisation des données personnelles envoyées à Sentry [#4902](https://github.com/SocialGouv/egapro/issues/4902).

**Qualité et CI/CD**
- Renforcement de la chaîne de tests : couverture E2E des verrous de déclaration et amélioration des tests ProConnect [#4911](https://github.com/SocialGouv/egapro/issues/4911), [#4869](https://github.com/SocialGouv/egapro/issues/4869).
- Intégration de contrôles d'accessibilité automatisés (ultra11y) dans les pipelines de CI [#5084](https://github.com/SocialGouv/egapro/issues/5084), [#4855](https://github.com/SocialGouv/egapro/issues/4855).
- Optimisation des outils de développement, incluant une configuration commune pour les outils d'IA [#5096](https://github.com/SocialGouv/egapro/issues/5096).
