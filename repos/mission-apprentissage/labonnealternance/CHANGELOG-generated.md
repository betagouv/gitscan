## Changelog : labonnealternance (30 derniers jours, au 2026-04-15)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la stabilité de la plateforme, notamment au niveau de la recherche d'offres et de la gestion des données. De nouvelles sources de données ont été intégrées (EDF, Enedis) et des optimisations ont été apportées pour gérer un volume de requêtes plus important. L'expérience utilisateur a également été améliorée avec des corrections SEO, l'ajout de fonctionnalités (formulaire Tally, bloc salaires, intégration portail alternance) et des corrections de bugs.

### Évolutions fonctionnelles
- Ajout de flux d'offres d'alternance provenant d'EDF et d'Enedis. [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819)
- Intégration d'un formulaire Tally sur la page de recherche pour recueillir des retours utilisateurs. [#2817](https://github.com/mission-apprentissage/labonnealternance/issues/2817)
- Ajout d'un bloc salaires sur les pages SEO métiers et redirection vers le simulateur de rémunération. [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785)
- Suppression de la carte dans la recherche pour simplifier l'interface. [#2790](https://github.com/mission-apprentissage/labonnealternance/issues/2790)
- Ajout de liens vers Mon Logement Étudiant. [#2793](https://github.com/mission-apprentissage/labonnealternance/issues/2793)
- Modification de l'article relatif au handicap. [#2816](https://github.com/mission-apprentissage/labonnealternance/issues/2816)
- Ajout de filtres par type de candidature (tags). [#2815](https://github.com/mission-apprentissage/labonnealternance/issues/2815)
- Mise à jour du plan du site. [#2838](https://github.com/mission-apprentissage/labonnealternance/issues/2838)
- Intégration du portail de l'alternance. [#2662](https://github.com/mission-apprentissage/labonnealternance/issues/2662)
- Amélioration du "smart apply" avec la gestion des tags. [#2787](https://github.com/mission-apprentissage/labonnealternance/issues/2787)
- Autorisation du passage en optionnel du `partner_job_id` pour l'API `/v3/job`. [#2783](https://github.com/mission-apprentissage/labonnealternance/issues/2783)

### Évolutions techniques
- Optimisation des lectures MongoDB en utilisant les secondaires pour la recherche, améliorant ainsi les performances. [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849)
- Stabilisation des healthchecks et réduction de la pression sur le stream processor. [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845)
- Correction des requêtes N+1 sur l'API `/api/traininglinks` pour améliorer la performance. [#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841)
- Mise en place d'un rate limiting proactif sur l'API job-étudiant pour gérer les pics de requêtes. [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831)
- Correction de bugs et amélioration des Core Web Vitals sur la page d'accueil. [#2794](https://github.com/mission-apprentissage/labonnealternance/issues/2794)
- Correction de vulnérabilités critiques dans les dépendances (handlebars, fast-xml-parser, basic-ftp). [#2810](https://github.com/mission-apprentissage/labonnealternance/issues/2810)
- Ajout d'un script pour analyser la blocklist des CFA. [#2822](https://github.com/mission-apprentissage/labonnealternance/issues/2822)
- Amélioration de l'import des offres d'Etudiant. [#2747](https://github.com/mission-apprentissage/labonnealternance/issues/2747)

### Autres changements
- Corrections SEO : ajout de canonical guides, configuration du robots.txt pour l'espace pro, et ajout de meta tags pour le simulateur. [#2851](https://github.com/mission-apprentissage/labonnealternance/issues/2851)
- Ajout d'une whitelist IP temporaire pour les tests de charge. [#2852](https://github.com/mission-apprentissage/labonnealternance/issues/2852)
- Correction du formatage de la description des offres Hellowork Buddi. [#2843](https://github.com/mission-apprentissage/labonnealternance/issues/2843)
- Mise à jour des notes des partenaires. [#2839](https://github.com/mission-apprentissage/labonnealternance/issues/2839)
- Correction du lien vers la région Grand Est. [#2835](https://github.com/mission-apprentissage/labonnealternance/issues/2835)
- Amélioration du look & feel du back-office pour les administrateurs LBA. [#2828](https://github.com/mission-apprentissage/labonnealternance/issues/2828)
- Correction de bugs et améliorations diverses de l'interface utilisateur (UI). [#2784](https://github.com/mission-apprentissage/labonnealternance/issues/2784)
- Mise à jour des astuces et du plan du site. [#2830](https://github.com/mission-apprentissage/labonnealternance/issues/2830)
- Correction de l'affichage des offres sur la page des CFA/entreprises partenaires. [#2784](https://github.com/mission-apprentissage/labonnealternance/issues/2784)
