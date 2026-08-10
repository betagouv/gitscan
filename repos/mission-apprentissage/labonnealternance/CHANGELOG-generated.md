## Changelog : labonnealternance (30 derniers jours, au 9 août 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'expérience de recherche avec le lancement du moteur de recherche v2 et une optimisation profonde du référencement (SEO). Nous avons également automatisé les processus de relance par email pour dynamiser l'engagement des candidats et des entreprises, tout en améliorant la rapidité de navigation grâce à l'introduction d'un système de mise en cache avancé.

### Évolutions fonctionnelles
- **Recherche & Découverte :** Déploiement du nouveau moteur de recherche v2 ([#4785](https://github.com/mission-apprentissage/labonnealternance/pull/4785)), intégration d'une enquête Tally pour recueillir les retours ([#5056](https://github.com/mission-apprentissage/labonnealternance/pull/5056)) et amélioration de la pertinence du tri des candidatures.
- **SEO & Visibilité :** Optimisation massive du référencement via des métadonnées dynamiques, l'ajout de fils d'Ariane, un maillage interne renforcé et une optimisation de la page dédiée aux salaires ([#5040](https://github.com/mission-apprentissage/labonnealternance/pull/5040), [#5061](https://github.com/mission-apprentissage/labonnealternance/pull/5061), [#5050](https://github.com/mission-apprentissage/labonnealternance/pull/5050)).
- **Engagement & Nurturing :** Mise en place de campagnes de relance automatisées via Brevo pour les candidats inactifs et les entreprises ([#4952](https://github.com/mission-apprentissage/labonnealternance/pull/4952), [#4980](https://github.com/mission-apprentissage/labonnealternance/pull/4980)).
- **Interface Utilisateur :** Unification de la modale de clôture de recrutement ([#5046](https://github.com/mission-apprentissage/labonnealternance/pull/5046)), correction de l'ergonomie de recherche sur mobile ([#5057](https://github.com/mission-apprentissage/labonnealternance/pull/5057)) et amélioration des notifications Slack ([#4967](https://github.com/mission-apprentissage/labonnealternance/pull/4967)).
- **Administration :** Création d'un nouvel écran de gestion dédié aux entreprises de type CFA ([#4974](https://github.com/mission-apprentissage/labonnealternance/pull/4974)).

### Évolutions techniques
- **Performance :** Implémentation des "Cache Components" permettant une navigation quasi instantanée sur l'ensemble des routes de la plateforme ([#5114](https://github.com/mission-apprentissage/labonnealternance/pull/5114), [#5118](https://github.com/mission-apprentissage/labonnealternance/pull/5118)).
- **Mise à jour de la Stack :** Migration vers TypeScript 7, Next.js 16.3 et Biome 2.5.7 ([#5094](https://github.com/mission-apprentissage/labonnealternance/pull/5094)) et passage à Zod v4 ([#5096](https://github.com/mission-apprentissage/labonnealternance/pull/5096)).
- **Sécurité & Résilience :** Mise en place de limites de débit (rate limiting) sur Nginx pour prévenir le scraping ([#5075](https://github.com/mission-apprentissage/labonnealternance/pull/5075)), correction de vulnérabilités critiques (CVE) ([#5055](https://github.com/mission-apprentissage/labonnealternance/pull/5055)) et amélioration de la gestion des erreurs d'API ([#5007](https://github.com/mission-apprentissage/labonnealternance/pull/5007)).
- **Refactoring :** Extraction de modules pour les emails transactionnels et les données du baromètre, et optimisation des requêtes de recherche MongoDB.

### Autres changements
- **Nettoyage :** Renommage massif des fichiers et dossiers en `kebab-case` pour harmoniser la structure du projet.
- **Infrastructure :** Mise à jour de l'image Docker de Metabase ([#5093](https://github.com/mission-apprentissage/labonnealternance/pull/5093)) et ajustements de la configuration de l'environnement de preview ([#5113](https://github.com/mission-apprentissage/labonnealternance/pull/5113)).
