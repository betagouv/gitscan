## Changelog : labonnealternance (30 derniers jours, au 16 août 2026)

### Résumé
Ce mois-ci a été marqué par un tournant majeur avec le déploiement du nouveau moteur de recherche et un effort massif pour améliorer la visibilité du site sur les moteurs de recherche (SEO). La plateforme est devenue plus rapide et plus robuste grâce à des optimisations de performance significatives et une mise à jour profonde des technologies de base.

### Évolutions fonctionnelles
- **Nouveau moteur de recherche** : Bascule du moteur de recherche beta en moteur principal, incluant des améliorations d'accessibilité (RGAA) ([#5146](https://github.com/mission-apprentissage/labonnealternance/issues/5146)) et l'intégration d'un système de feedback utilisateur ([#5056](https://github.com/mission-apprentissage/labonnealternance/issues/5056)).
- **Optimisation SEO & Visibilité** : Amélioration majeure du référencement Google via l'ajout de données structurées (Course, ItemList, JobPosting), de balises méta dynamiques et de maillages internes sur les pages de recherche, de métiers et de villes ([#5129](https://github.com/mission-apprentissage/labonnealternance/issues/5129), [#5141](https://github.com/mission-apprentissage/labonnealternance/issues/5141), [#5040](https://github.com/mission-apprentissage/labonnealternance/issues/5040), [#5050](https://github.com/mission-apprentissage/labonnealternance/issues/5050)).
- **Outils d'administration** : Mise en place de nouveaux écrans de gestion pour les offres partenaires ([#5135](https://github.com/mission-apprentissage/labonnealternance/issues/5135)) et pour les entreprises de type CFA ([#4974](https://github.com/mission-apprentissage/labonnealternance/issues/4974)).
- **Engagement et Nurturing** : Automatisation des relances par email pour les candidats inactifs et les entreprises via Brevo ([#4952](https://github.com/mission-apprentissage/labonnealternance/issues/4952), [#4980](https://github.com/mission-apprentissage/labonnealternance/issues/4980)).
- **Expérience Utilisateur** : Unification de la modale de clôture de recrutement ([#5046](https://github.com/mission-apprentissage/labonnealternance/issues/5046)) et corrections d'interface (menu header, boutons de recherche mobile) ([#5145](https://github.com/mission-apprentissage/labonnealternance/issues/5145), [#5057](https://github.com/mission-apprentissage/labonnealternance/issues/5057)).

### Évolutions techniques
- **Performance & Navigation** : Adoption du "Cache Components" et du "Partial Prefetching" pour permettre des navigations quasi instantanées entre les pages ([#5114](https://github.com/mission-apprentissage/labonnealternance/issues/5114), [#5120](https://github.com/mission-apprentissage/labonnealternance/issues/5120)).
- **Modernisation de la stack** : Mise à jour majeure des dépendances critiques incluant TypeScript 7, Next.js 16.3, Zod v4 et Node 26 ([#5094](https://github.com/mission-apprentissage/labonnealternance/issues/5094), [#5096](https://github.com/mission-apprentissage/labonnealternance/issues/5096)).
- **Sécurité & Fiabilité** : Implémentation du rate limiting Nginx pour prévenir le scraping ([#5075](https://github.com/mission-apprentissage/labonnealternance/issues/5075)), correction de vulnérabilités critiques (CVE) ([#5055](https://github.com/mission-apprentissage/labonnealternance/issues/5055)) et résolution d'erreurs critiques remontées par Sentry ([#5151](https://github.com/mission-apprentissage/labonnealternance/issues/5151)).
- **Intelligence Artificielle** : Migration de la classification des offres partenaires vers le modèle Mistral ([#5131](https://github.com/mission-apprentissage/labonnealternance/issues/5131)).

### Autres changements
- **Refactorisation du code** : Nettoyage massif de la structure des dossiers et fichiers pour appliquer la convention `kebab-case` sur l'ensemble du projet ([#5108](https://github.com/mission-apprentissage/labonnealternance/issues/5108)).
- **Documentation** : Mise à jour des principes d'architecture pour l'utilisation des agents IA ([#5125](https://github.com/mission-apprentissage/labonnealternance/issues/5125)).
