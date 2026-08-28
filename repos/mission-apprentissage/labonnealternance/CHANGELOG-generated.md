## Changelog : labonnealternance (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois a été marqué par un tournant majeur avec le déploiement du nouveau moteur de recherche comme outil principal. L'accent a été mis sur la visibilité du site (SEO) pour permettre aux utilisateurs de trouver plus facilement les offres sur Google, ainsi que sur l'amélioration de l'expérience mobile grâce à la possibilité d'installer l'application sur smartphone (PWA).

### Évolutions fonctionnelles
- **Nouveau moteur de recherche** : Bascule officielle du moteur de recherche "beta" vers le moteur principal ([#5139](https://github.com/mission-apprentissage/labonnealternance/issues/5139)).
- **Expérience Mobile** : L'application est désormais installable sur mobile via la technologie PWA ([#5221](https://github.com/mission-apprentissage/labonnealternance/issues/5221)) et la recherche mobile a été optimisée pour une meilleure ergonomie ([#5219](https://github.com/mission-apprentissage/labonnealternance/issues/5219)).
- **Nouvelles informations et contenus** : 
    - Ajout d'un compteur affichant les alternants recrutés sur les 3 dernières années ([#5201](https://github.com/mission-apprentissage/labonnealternance/issues/5201)).
    - Enrichissement du guide sur la rémunération pour répondre aux recherches sur les salaires en alternance ([#5035](https://github.com/mission-apprentissage/labonnealternance/issues/5035)).
    - Ajout de l'Apecita dans la section des partenaires ([#5161](https://github.com/mission-apprentissage/labonnealternance/issues/5161)).
- **Gestion administrative** : Mise en place d'un nouvel écran d'administration pour la gestion des offres partenaires ([#5135](https://github.com/mission-apprentissage/labonnealternance/issues/5135)).

### Évolutions techniques
- **Référencement et visibilité (SEO)** : 
    - Automatisation de l'indexation des offres via les API Google Indexing et IndexNow ([#5293](https://github.com/mission-apprentissage/labonnealternance/issues/5293), [#5271](https://github.com/mission-apprentissage/labonnealternance/issues/5271)).
    - Implémentation de données structurées (Schema.org) sur les fiches formations et organisations pour améliorer l'affichage dans les moteurs de recherche ([#5270](https://github.com/mission-apprentissage/labonnealternance/issues/5270), [#5129](https://github.com/mission-apprentissage/labonnealternance/issues/5129)).
    - Ajout de balises canonical et optimisation des métadonnées pour éviter le contenu dupliqué ([#5280](https://github.com/mission-apprentissage/labonnealternance/issues/5280)).
- **Performance et Rapidité** : 
    - Adoption des dernières fonctionnalités de Next.js (Partial Prefetching et Cache Components) pour rendre la navigation quasi instantanée ([#5120](https://github.com/mission-apprentissage/labonnealternance/issues/5120), [#5114](https://github.com/mission-apprentissage/labonnealternance/issues/5114)).
    - Optimisation des scores Lighthouse (LCP, polices, images) pour améliorer la vitesse de chargement mobile ([#5147](https://github.com/mission-apprentissage/labonnealternance/issues/5147)).
- **Intelligence Artificielle** : Migration de la classification des offres vers le modèle Mistral AI ([#5131](https://github.com/mission-apprentissage/labonnealternance/issues/5131)).
- **Sécurité et Infrastructure** : 
    - Mise en place de limites de requêtes (rate limiting) sur le front-end pour prévenir le scraping ([#5075](https://github.com/mission-apprentissage/labonnealternance/issues/5075)).
    - Renforcement de la sécurité des secrets (protection contre les fuites dans Sentry) ([#5294](https://github.com/mission-apprentissage/labonnealternance/issues/5294)).
    - Mise à jour majeure des dépendances technologiques : TypeScript 7, Next.js 16.3 et Zod v4 ([#5094](https://github.com/mission-apprentissage/labonnealternance/issues/5094), [#5096](https://github.com/mission-apprentissage/labonnealternance/issues/5096)).

### Autres changements
- **Standardisation du code** : Refactorisation massive du nommage des fichiers et dossiers pour adopter le format `kebab-case` sur l'ensemble du projet.
- **Documentation** : Nettoyage de la documentation obsolète et correction de liens périmés ([#5213](https://github.com/mission-apprentissage/labonnealternance/issues/5213)).
