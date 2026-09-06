## Changelog : labonnealternance (30 derniers jours, au 04 septembre 2026)

### Résumé
Ce mois a été marqué par une étape majeure : le déploiement du nouveau moteur de recherche et l'optimisation profonde de la visibilité du site sur les moteurs de recherche (SEO). L'expérience utilisateur a été renforcée, notamment sur mobile grâce au support PWA, et les outils destinés aux recruteurs ont été enrichis pour mieux intégrer les enjeux de diversité (handicap) et faciliter la gestion des offres.

### Évolutions fonctionnelles
- **Recherche & Navigation** : Bascule vers le nouveau moteur de recherche, amélioration de la précision des résultats, restauration des contextes de recherche et unification de la navigation sur les fiches détaillées ([#5139](https://github.com/mission-apprentissage/labonnealternance/issues/5139), [#5194](https://github.com/mission-apprentissage/labonnealternance/issues/5194)).
- **Visibilité & SEO** : Optimisation massive du référencement via l'automatisation de l'indexation (Google Indexing API, IndexNow), ajout de données structurées (Schema.org) et intégration de balises canonical ([#5293](https://github.com/mission-apprentissage/labonnealternance/issues/5293), [#5271](https://github.com/mission-apprentissage/labonnealternance/issues/5271), [#5270](https://github.com/mission-apprentissage/labonnealternance/issues/5270)).
- **Expérience Recruteur** : Collecte des engagements handicap ([#5222](https://github.com/mission-apprentissage/labonnealternance/issues/5222)), mise en place d'un écran de gestion des offres partenaires ([#5135](https://github.com/mission-apprentissage/labonnealternance/issues/5135)) et simplification du processus de dépôt d'offres.
- **Mobile & Interface** : L'application est désormais installable en tant que PWA sur mobile ([#5221](https://github.com/mission-apprentissage/labonnealternance/issues/5221)), accompagnée d'une amélioration de l'interface mobile et de l'ajout de nouveaux indicateurs visuels (compteur d'alternants recrutés).

### Évolutions techniques
- **Architecture & Intelligence Artificielle** : Migration de la classification des offres vers l'IA Mistral ([#5131](https://github.com/mission-apprentissage/labonnealternance/issues/5131)) et transition complète vers le nouveau moteur de recherche.
- **Performance** : Optimisation des temps de chargement via l'adoption des *Cache Components* et du *Partial Prefetching* ([#5114](https://github.com/mission-apprentissage/labonnealternance/issues/5114), [#5120](https://github.com/mission-apprentissage/labonnealternance/issues/5120)), et amélioration des scores Lighthouse.
- **Stack Technique** : Mise à jour majeure de l'infrastructure logicielle vers Next.js 16.3, TypeScript 7 et Node 26 ([#5094](https://github.com/mission-apprentissage/labonnealternance/issues/5094)).
- **Maintenance & Refactoring** : Nettoyage massif du code (standardisation des fichiers et dossiers en kebab-case), amélioration de la fiabilité du monitoring Sentry et mise à jour des images Docker.

### Autres changements
- Mise à jour de la documentation technique et correction de nombreux liens obsolètes ([#5213](https://github.com/mission-apprentissage/labonnealternance/issues/5213)).
