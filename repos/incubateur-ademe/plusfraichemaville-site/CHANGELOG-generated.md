## Changelog : plusfraichemaville-site (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, le site a connu des améliorations significatives en termes de contenu et de fonctionnalités, notamment l'ajout de nouvelles pages dédiées à la santé et aux canicules, ainsi que des optimisations pour le référencement (SEO) et l'expérience utilisateur. Des corrections et des ajustements ont également été apportés suite aux retours d'utilisateurs.

### Évolutions fonctionnelles

- Ajout d'une page dédiée aux urgences canicule ([#514](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/514)).
- Ajout d'une page permettant de demander de l'aide pour un projet ([#513](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/513)).
- Création d'une page dédiée à la surchauffe urbaine et à la santé ([#509](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/509)).
- Ajout d'un bloc "santé" dans la page "timing" de la surchauffe urbaine ([#512](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/512)).
- Ajout du budget 2025 ([#518](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/518)).
- Suppression des aides régionales et du lien "Aides Territoires" sur les fiches solution ([#519](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/519)).
- Tri des fiches solutions par type dans la page santé.

### Évolutions techniques

- Intégration d'une API pour permettre à pfat d'utiliser les données climadiag ([#520](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/520)).
- Amélioration de la gestion des données climadiag : possibilité de mise à jour sans effacement des données LCZ.
- Ajout d'attributs MetaData pour le SEO des pages REX ([#516](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/516)).
- Ajout de liens canonical pour améliorer le SEO ([#516](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/516)).
- Ajout de tags Matomo pour le suivi des nouvelles fonctionnalités.
- Suppression des balises HTML de la méta description.
- Chargement asynchrone des fiches solutions santé.
- Ajout de descriptions pour les lecteurs d'écran pour les infographies.

### Autres changements

- Corrections diverses suite aux retours métier (plusieurs commits).
- Correction d'un problème lié à l'envoi de chaînes vides.
- Correction d'un problème lié au consentement Matomo.
- Correction d'un dernier retour sur la page urgence santé.
- Correction de problèmes de configuration de PostHog.
