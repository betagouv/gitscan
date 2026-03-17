## Changelog : acces-cible (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à acces-cible au cours des 30 derniers jours. Les principales évolutions concernent l'amélioration de la robustesse de l'application, l'ajout de nouvelles fonctionnalités pour faciliter l'export de données et la gestion des sites, ainsi que des mises à jour techniques pour assurer la sécurité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout du nom du site aux exports CSV pour une meilleure identification des données exportées. [#476](https://github.com/betagouv/acces-cible/pull/476)
- Mise à jour du titre de l'application pour indiquer qu'il s'agit de la version bêta. [#475](https://github.com/betagouv/acces-cible/pull/475)
- Amélioration de la gestion des délais d'attente du réseau pour une meilleure stabilité. [#466](https://github.com/betagouv/acces-cible/pull/466)
- Ajout de limites de pagination configurables pour une meilleure gestion des listes de données. [#454](https://github.com/betagouv/acces-cible/pull/454)
- Amélioration de l'extraction du taux de conformité pour une plus grande précision. [#450](https://github.com/betagouv/acces-cible/pull/450)
- Amélioration de la suppression en masse pour une meilleure expérience utilisateur. [#449](https://github.com/betagouv/acces-cible/pull/449)
- Correction d'un problème de condition de course lors de la création de transitions. [#455](https://github.com/betagouv/acces-cible/pull/455)

### Évolutions techniques
- Mise à niveau de Ruby vers la version 4.0.1 pour bénéficier des dernières améliorations et correctifs de sécurité. [#478](https://github.com/betagouv/acces-cible/pull/478)
- Mise à niveau de plusieurs gems pour assurer la compatibilité et la sécurité de l'application. [#465](https://github.com/betagouv/acces-cible/pull/465), [#461](https://github.com/betagouv/acces-cible/pull/461), [#422](https://github.com/betagouv/acces-cible/pull/422)
- Suppression d'un helper DSFR obsolète et mise à jour des dépendances associées. [#460](https://github.com/betagouv/acces-cible/pull/460)
- Refactorisation du code pour utiliser une syntaxe plus moderne pour les sujets implicites.
- Correction d'un problème empêchant l'exécution des tests d'accessibilité sur les pages sans accessibilité. [#479](https://github.com/betagouv/acces-cible/pull/479)
- Amélioration de la robustesse des audits en évitant de modifier les sites.

### Autres changements
- Mise à jour de la documentation README. [#451](https://github.com/betagouv/acces-cible/pull/451)
- Suppression du helper `time_ago` et adaptation des formats de date dans les vues. [#452](https://github.com/betagouv/acces-cible/pull/452)
- Mise à jour du fichier `run_axe_on_homepage.html.md`. [#482](https://github.com/betagouv/acces-cible/pull/482)
