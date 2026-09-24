## Changelog : labonnealternance (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois a été marqué par une amélioration majeure de l'accessibilité numérique (RGAA) et du référencement naturel (SEO) de la plateforme. Les outils pour les recruteurs ont été enrichis, notamment avec de nouvelles options de gestion d'offres et de suivi des engagements. Parallèlement, la gestion des données a été renforcée avec l'automatisation de la conservation et de la purge des CV, garantissant une meilleure conformité et fiabilité du système.

### Évolutions fonctionnelles
- **Recherche et navigation :**
  - Amélioration de la recherche de lieux avec la possibilité de filtrer par département et région ([#5248](https://github.com/mission-apprentissage/labonnealternance/issues/5248)).
  - Assouplissement des critères de recherche de formations pour les liens de formation ([#5393](https://github.com/mission-apprentissage/labonnealternance/issues/5393)).
  - Optimisation de la saisie du champ "métier" avec support de la saisie libre et raccourci clavier Entrée ([#5508](https://github.com/mission-apprentissage/labonnealternance/issues/5508)).
- **Outils Recruteurs :**
  - Ajout d'un motif de clôture d'offre : "J'ai reçu assez de candidatures" ([#5501](https://github.com/mission-apprentissage/labonnealternance/issues/5501)).
  - Mise en place d'un compteur d'alternants recrutés sur les trois dernières années ([#5201](https://github.com/mission-apprentissage/labonnealternance/issues/5201)).
  - Collecte des engagements en faveur du handicap auprès des recruteurs ([#5222](https://github.com/mission-apprentissage/labonnealternance/issues/5222)).
- **Contenu et SEO :**
  - Création d'une nouvelle page guide pour les recruteurs ("Recruter un alternant") ([#5128](https://github.com/mission-apprentissage/labonnealternance/issues/5128)).
  - Ajout de balises canonical ([#5280](https://github.com/mission-apprentissage/labonnealternance/issues/5280)) et de données structurées Schema.org ([#5270](https://github.com/mission-apprentissage/labonnealternance/issues/5270)) pour améliorer la visibilité des offres et formations.
- **Nouveautés :**
  - Intégration du flux LinkedIn ([#5482](https://github.com/mission-apprentissage/labonnealternance/issues/5482)).

### Évolutions techniques
- **Indexation et visibilité :**
  - Automatisation de la notification des offres (publication/retrait) via Google Indexing API ([#5293](https://github.com/mission-apprentissage/labonnealternance/issues/5293)) et IndexNow ([#5271](https://github.com/mission-apprentissage/labonnealternance/issues/5271)).
- **Gestion des données et conformité :**
  - Mise en place d'un système de conservation des CV pendant un an avec purge automatique ([#5495](https://github.com/mission-apprentissage/labonnealternance/issues/5495)).
  - Amélioration du processus d'anonymisation des candidatures ([#5516](https://github.com/mission-apprentissage/labonnealternance/issues/5516)).
- **Infrastructure et performance :**
  - Mise à jour de l'environnement technique (Node 26, images Docker Metabase) et des workflows GitHub Actions ([#5335](https://github.com/mission-apprentissage/labonnealternance/issues/5335)).
  - Optimisation de la résilience face aux limites de taux (rate limiting) de l'API Notion ([#5485](https://github.com/mission-apprentissage/labonnealternance/issues/5485)).
  - Amélioration de la gestion du cache du reverse proxy lors des déploiements ([#5366](https://github.com/mission-apprentissage/labonnealternance/issues/5366)).
- **Sécurité et fiabilité :**
  - Correction de fuites potentielles de secrets vers l'outil de monitoring Sentry ([#5294](https://github.com/mission-apprentissage/labonnealternance/issues/5294)).
  - Résolution de plusieurs boucles de redirection critiques sur les espaces professionnels ([#5383](https://github.com/mission-apprentissage/labonnealternance/issues/5383), [#5388](https://github.com/mission-apprentissage/labonnealternance/issues/5388)).

### Autres changements
- **Accessibilité (RGAA) :** Travail important de mise en conformité sur les images, les icônes et la structure des liens ([#5494](https://github.com/mission-apprentissage/labonnealternance/issues/5494), [#5483](https://github.com/mission-apprentissage/labonnealternance/issues/5483), [#5396](https://github.com/mission-apprentissage/labonnealternance/issues/5396)).
- **Expérience de développement :** Alignement des conventions de titres de Pull Requests et mise à jour des instructions pour les outils d'assistance IA (Claude/Copilot) ([#5522](https://github.com/mission-apprentissage/labonnealternance/issues/5522), [#5519](https://github.com/mission-apprentissage/labonnealternance/issues/5519)).
