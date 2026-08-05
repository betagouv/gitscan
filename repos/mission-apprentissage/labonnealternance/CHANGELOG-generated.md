## Changelog : labonnealternance (30 derniers jours, au 04 août 2026)

### Résumé
Ce mois a été marqué par une étape majeure avec le déploiement du nouveau moteur de recherche (v2) et un effort intensif sur le référencement naturel (SEO). La plateforme renforce également son engagement utilisateur grâce à l'automatisation de campagnes de relance par email et une amélioration globale de l'ergonomie et de l'accessibilité des contenus.

### Évolutions fonctionnelles
- **Recherche & Navigation** : Amélioration de l'expérience de recherche (tri des candidatures, optimisation du bouton de recherche mobile), ajout d'un fil d'ariane ([#5061](https://github.com/mission-apprentissage/labonnealternance/pull/5061)) et intégration d'enquêtes de satisfaction via Tally ([#5056](https://github.com/mission-apprentissage/labonnealternance/pull/5056)).
- **Engagement & Nurturing** : Mise en place de relances automatiques via Brevo pour les candidats inactifs et pour les entreprises dont les offres arrivent à échéance.
- **Administration & Gestion** : Création d'un nouvel écran d'administration dédié aux entreprises de type CFA ([#4974](https://github.com/mission-apprentissage/labonnealternance/pull/4974)) et mise à jour des mécanismes de gestion des listes de blocage.
- **Interface & UX** : Mise en conformité des articles avec les recommandations DSFR ([#4995](https://github.com/mission-apprentissage/labonnealternance/pull/4995)), refonte des pages d'erreur ([#4916](https://github.com/mission-apprentissage/labonnealternance/pull/4916)) et clarification des libellés pour le partage d'offres.

### Évolutions techniques
- **Moteur de recherche** : Migration et déploiement du nouveau moteur de recherche v2 basé sur MongoDB ([#4785](https://github.com/mission-apprentissage/labonnealternance/pull/4785)).
- **SEO & Visibilité** : Optimisation du référencement via des métadonnées dynamiques ([#5040](https://github.com/mission-apprentissage/labonnealternance/pull/5040)), un meilleur pilotage des robots via l'API Next.js ([#5044](https://github.com/mission-apprentissage/labonnealternance/pull/5044)) et optimisation de la page salaire.
- **Sécurité & Infrastructure** : Renforcement de la protection contre le scraping via le rate limiting Nginx ([#5075](https://github.com/mission-apprentissage/labonnealternance/pull/5075)), rotation des secrets SOPS ([#4939](https://github.com/mission-apprentissage/labonnealternance/pull/4939)) et correction de vulnérabilités critiques (CVE) sur les dépendances ([#5055](https://github.com/mission-apprentissage/labonnealternance/pull/5055)).
- **Données & Analytics** : Refactorisation des collections de données (Opcos, CFA, rôles) et amélioration du suivi analytique avec Matomo ([#4987](https://github.com/mission-apprentissage/labonnealternance/pull/4987)).

### Autres changements
- **Contenu** : Mise à jour des articles du guide alternant et des guides CFA.
- **Outils** : Maintenance et mise à jour de l'outil de BI Metabase ([#5031](https://github.com/mission-apprentissage/labonnealternance/pull/5031)).
