## Changelog : mon-entreprise (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois-ci a été marqué par une refonte structurelle importante de la gestion des simulateurs et une modernisation de l'infrastructure de déploiement. Parallèlement, plusieurs corrections de calculs (notamment sur le SMIC et les retraites) et des améliorations visuelles ont été apportées pour garantir la précision des simulations et la qualité de l'expérience utilisateur.

### Évolutions fonctionnelles
- **Corrections de calculs** : Ajustement de la valeur du SMIC pour le calcul de la RGDU et mise à jour des taux 2026 pour les retraites complémentaires (CARMF et CARCDSF).
- **Améliorations visuelles** : Mise à jour des images de prévisualisation des simulateurs, ajout d'illustrations sur la page "demande de mobilité" et amélioration du style de certains textes.
- **Interface utilisateur** : Correction de coquilles dans le message de contact du footer, centrage du bouton de suggestion et ajustements de mise en page.

### Évolutions techniques
- **Infrastructure & CI/CD** : Automatisation des déploiements sur Clever Cloud et mise en place de "Review Apps", permettant de tester chaque Pull Request dans un environnement de prévisualisation dédié.
- **Architecture des simulateurs** : Refonte majeure de la gestion des simulateurs pour séparer les métadonnées (SEO, Open Graph, avertissements) de la configuration technique, rendant le système plus modulaire et facile à maintenir.
- **Performance** : Optimisation du temps de chargement via le chargement à la demande de certains composants (ex: `SeeAnswersButton`).
- **Qualité et outils** : Mise à jour de l'écosystème de développement (TypeScript, Vite, Vitest, Prettier) et renforcement des tests automatisés sur le routage, la navigation et l'API.
- **Optimisation API** : Amélioration de la gestion du cache et de la structure des endpoints.

### Autres changements
- **Documentation** : Mise à jour des guides techniques concernant l'infrastructure Clever Cloud, l'utilisation des métadonnées et les précisions sur les règles de calcul (RGDU).
- **Maintenance** : Nettoyage du code par la suppression de composants, de types et de commentaires obsolètes.
