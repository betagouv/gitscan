## Changelog : labonnealternance (30 derniers jours, au 2026-09-18)

### Résumé
Ce mois a été marqué par un effort important sur le référencement naturel (SEO) et l'accessibilité de la plateforme. Les utilisateurs bénéficient désormais de meilleures capacités de recherche (par région et département) et d'une expérience mobile améliorée grâce au support des Progressive Web Apps (PWA). Plusieurs optimisations techniques ont été réalisées pour stabiliser l'indexation des offres et la fiabilité des flux de données.

### Évolutions fonctionnelles

**Recherche et Découverte**
- Amélioration de la recherche de lieux avec la possibilité de filtrer par département et région ([#5461](https://github.com/mission-apprentissage/labonnealternance/issues/5461)).
- Assouplissement des critères de recherche pour les liens de formation (trainingLinks) ([#5393](https://github.com/mission-apprentissage/labonnealternance/issues/5393)).
- Affichage du nom du CFA sur les offres déléguées dans les résultats de recherche ([#5343](https://github.com/mission-apprentissage/labonnealternance/issues/5359)).

**Expérience Utilisateur et Accessibilité**
- Mise en conformité RGAA pour l'accessibilité des images et des icônes ([#5396](https://github.com/mission-apprentissage/labonnealternance/issues/5396)).
- Transformation de l'application en PWA pour une utilisation optimale sur mobile ([#5221](https://github.com/mission-apprentissage/labonnealternance/issues/5221)).
- Optimisation de l'ergonomie de la recherche sur mobile (modale et suggestions clavier) ([#5219](https://github.com/mission-apprentissage/labonnealternance/issues/5219)).
- Correction de divers bugs d'interface : formulaires de candidature ([#5492](https://github.com/mission-apprentissage/labonnealternance/issues/5492), [#5464](https://github.com/mission-apprentissage/labonnealternance/issues/5464)), navigation et tabulation ([#5469](https://github.com/mission-apprentissage/labonnealternance/issues/5469)), et affichage des éléments de l'espace pro ([#5345](https://github.com/mission-apprentissage/labonnealternance/issues/5345)).

**Contenu et Recrutement**
- Création d'une page guide "Recruter un alternant" pour améliorer le conseil aux recruteurs ([#5128](https://github.com/mission-apprentissage/labonnealternance/issues/5128)).
- Collecte des engagements en faveur du handicap auprès des recruteurs ([#5222](https://github.com/mission-apprentissage/labonnealternance/issues/5222)).
- Ajout d'un compteur d'alternants recrutés sur les trois dernières années ([#5201](https://github.com/mission-apprentissage/labonnealternance/issues/5201)).

**Référencement (SEO)**
- Optimisation massive du SEO via l'ajout de données structurées (Schema.org), de balises canonical et de notifications automatiques aux moteurs de recherche (Google Indexing API, IndexNow) ([#5293](https://github.com/mission-apprentissage/labonnealternance/issues/5293), [#5280](https://github.com/mission-apprentissage/labonnealternance/issues/5280), [#5271](https://github.com/mission-apprentissage/labonnealternance/issues/5271), [#5270](https://github.com/mission-apprentissage/labonnealternance/issues/5270)).

### Évolutions techniques

**Performance et Fiabilité**
- Amélioration de la résilience face aux limites de requêtes (erreurs 429) sur les pages Notion ([#5485](https://github.com/mission-apprentissage/labonnealternance/issues/5485)).
- Optimisation de l'indexation des offres importées ([#5322](https://github.com/mission-apprentissage/labonnealternance/issues/5322)).
- Automatisation de la purge du cache du reverse proxy lors des déploiements ([#5366](https://github.com/mission-apprentissage/labonnealternance/issues/5367)).
- Migration du moteur de classification vers Mistral ([#5231](https://github.com/mission-apprentissage/labonnealternance/issues/5231)).

**Architecture et API**
- Suppression des anciens endpoints de l'API v1 (formations et métiers) ([#5261](https://github.com/mission-apprentissage/labonnealternance/issues/5261)).
- Bascule sur le nouveau flux de données Hellowork ([#5363](https://github.com/mission-apprentissage/labonnealternance/issues/5363)).
- Sécurisation des logs en empêchant la fuite de secrets vers Sentry ([#5301](https://github.com/mission-apprentissage/labonnealternance/issues/5301)).

### Autres changements
- Mise à jour de l'infrastructure : passage à Node 26, mise à jour des GitHub Actions et de l'image Docker Metabase ([#5335](https://github.com/mission-apprentissage/labonnealternance/issues/5335), [#5392](https://github.com/mission-apprentissage/labonnealternance/issues/5392)).
- Alignement des composants d'interface avec le design system ([#5470](https://github.com/mission-apprentissage/labonnealternance/issues/5470)).
